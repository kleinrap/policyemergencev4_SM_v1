from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from model_SM_initialisation_agents import init_active_agents
from model_SM_active_agents import ActiveAgent




class TruthAgent(Agent):
    '''
    Truth agent used for the purpose of the simulation only.
    '''
    def __init__(self, pos, model, agent_type):
        '''
         Create a new Schelling agent.
         Args:
            unique_id: Unique identifier for the agent.
            x, y: Agent initial location.
            agent_type: Indicator for the agent's type (minority=1, majority=0)
        '''
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type

class PolicyEmergenceSM(Model):

	'''
	Simplest Model for the policy emergence model.
	'''

	def __init__(self, height=20, width=20, PMnumber=3, PEnumber=5, EPnumber=2):

		self.height = height
		self.width = width

		self.stepCount = 0

		self.schedule = RandomActivation(self)
		self.grid = SingleGrid(height, width, torus=True)

		self.datacollector = DataCollector(
			# Model-level count of happy agents
			{"step": "stepCount"},
			# For testing purposes, agent's individual x and y
			{"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]})

		# belief tree properties
		self.len_S_names = ["vision", "movement", "last_movement", "type0preferences", "type1preferences"]
		self.len_S = len(self.len_S_names)
		self.len_PC_names = ["freedom", "happiness"]
		self.len_PC = len(self.len_PC_names)
		self.len_DC_names = ["evenness"]
		self.len_DC = len(self.len_DC_names)
		self.number_causalrelation = self.len_DC*self.len_PC + self.len_PC*self.len_S

		# issue tree properties
		self.len_PF = self.len_PC
		self.len_PF_names = self.len_PC_names
		self.len_ins_1 = 4
		self.len_ins_1_names = ["TBD", "TBD", "TBD", "TBD"]
		self.len_ins_2 = 6
		self.len_ins_2_names = ["TBD", "TBD", "TBD", "TBD", "TBD", "TBD"]

		# agent global properties
		self.number_activeagents = 10

		# Set up active agents (manually for now)
		init_active_agents(self, self.len_S, self.len_PC, self.len_DC, self.number_causalrelation, self.len_PF, self.len_ins_1, self.len_ins_2, self.number_activeagents)

		# Set up passive agents (manually for now)
		init_electorate_agents(self, self.len_S, self.len_PC, self.len_DC)

		print("Schedule has : ", len(self.schedule.agents), " agents.")
		print(self.schedule.agents)

		for agent in self.schedule.agent_buffer(shuffled=False):
			print(agent.ID, " ", agent.pos, " ", agent.agent_type, " ", agent.resources, " ", agent.affiliation, " ", agent.issuetree[agent.ID], " ", agent.policytree[agent.ID][0])

		self.running = True
		self.numberOfAgents = self.schedule.get_agent_count()
		self.datacollector.collect(self)

	def preference_udapte(self, agent, who):

		"""
		The preference update function
		===========================

		This function is used to update the preferences of the agents in their
		respective belief trees.

		agent - this is the owner of the belief tree
		who - this is the part of the belieftree that is considered - agent.ID should be used for this - this is done to also include partial knowledge preference calculation

		"""	

		len_DC = self.len_DC
		len_PC = self.len_PC
		len_S = self.len_S

		#####
		# 1.5.1. Preference calculation for the deep core issues

		# 1.5.1.1. Calculation of the denominator
		PC_denominator = 0
		for h in range(len_DC):
			if agent.issuetree[who][h][1] == None or agent.issuetree[who][h][0] == None:
				PC_denominator = 0
			else:
				PC_denominator = PC_denominator + abs(agent.issuetree[who][h][1] - agent.issuetree[who][h][0])
		# print('The denominator is given by: ' + str(PC_denominator))

		# 1.5.1.2. Selection of the numerator and calculation of the preference
		for i in range(len_DC):
			# There are rare occasions where the denominator could be 0
			if PC_denominator != 0:
				agent.issuetree[who][i][2] = abs(agent.issuetree[who][i][1] - agent.issuetree[who][i][0]) / PC_denominator
			else:
				agent.issuetree[who][i][2] = 0

		#####	
		# 1.5.2 Preference calculation for the policy core issues
		ML_denominator = 0
		# 1.5.2.1. Calculation of the denominator
		for j in range(len_PC):
			ML_denominator = 0
			# print('Selection PC' + str(j+1))
			# print('State of the PC' + str(j+1) + ': ' + str(agent.issuetree[0][len_DC + j][0])) # the state printed
			# Selecting the causal relations starting from PC
			for k in range(len_DC):
				# Contingency for partial knowledge issues
				

				print(agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)-1][0])
				if agent.issuetree[who][k][1] == None or agent.issuetree[who][k][0] == None or agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0] == None:
					ML_denominator = 0
				else:
					# print('Causal Relation PC' + str(j+1) + ' - PC' + str(k+1) + ': ' + str(agent.issuetree[0][len_DC+len_PC+len_S+j+(k*len_PC)][1]))
					# print('Gap of PC' + str(k+1) + ': ' + str((agent.issuetree[0][k][1] - agent.issuetree[0][k][0])))
					# Check if causal relation and gap are both positive of both negative
					# print('agent.issuetree[' + str(who) + '][' + str(len_DC+len_PC+len_S+j+(k*len_PC)) + '][0]: ' + str(agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0]))
					if (agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0] < 0 and (agent.issuetree[who][k][1] - agent.issuetree[who][k][0]) < 0) \
					  or (agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0] > 0 and (agent.issuetree[who][k][1] - agent.issuetree[who][k][0]) > 0):
						ML_denominator = ML_denominator + abs(agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0]*\
						  (agent.issuetree[who][k][1] - agent.issuetree[who][k][0]))
						# print('This is the PC numerator: ' + str(ML_denominator))
					else:
						ML_denominator = ML_denominator	

		# 1.5.2.2. Addition of the gaps of the associated mid-level issues
		for i in range(len_PC):
			# Contingency for partial knowledge issues
			if agent.issuetree[who][len_DC + i][1] == None or agent.issuetree[who][len_DC + i][0] == None:
				ML_denominator = ML_denominator
			else:
				# print('This is the gap for the ML' + str(i+1) + ': ' + str(agent.issuetree[0][len_DC + i][1] - agent.issuetree[0][len_DC + i][0]))
				ML_denominator = ML_denominator + abs(agent.issuetree[who][len_DC + i][1] - agent.issuetree[who][len_DC + i][0])
		# print('This is the ML denominator: ' + str(ML_denominator))
		
		# 1.5.2.3 Calculation the numerator and the preference
		# Select one by one the Pr
		for j in range(len_PC):

			# 1.5.2.3.1. Calculation of the right side of the numerator
			ML_numerator = 0
			# print('Selection ML' + str(j+1))
			# print('State of the ML' + str(j+1) + ': ' + str(agent.issuetree[0][len_DC + j][0])) # the state printed
			# Selecting the causal relations starting from Pr
			for k in range(len_DC):
				# Contingency for partial knowledge issues
				if agent.issuetree[who][k][1] == None or agent.issuetree[who][k][0] == None or agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0] == None:
					ML_numerator = 0
				else:
					# print('Causal Relation ML' + str(j+1) + ' - Pr' + str(k+1) + ': ' + str(agent.issuetree[0][len_DC+len_PC+len_S+j+(k*len_PC)][1]))
					# print('Gap of Pr' + str(k+1) + ': ' + str((agent.issuetree[0][k][1] - agent.issuetree[0][k][0])))
					# Check if causal relation and gap are both positive of both negative
					if (agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0] < 0 and (agent.issuetree[who][k][1] - agent.issuetree[who][k][0]) < 0) \
					  or (agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0] > 0 and (agent.issuetree[who][k][1] - agent.issuetree[who][k][0]) > 0):
						ML_numerator = ML_numerator + abs(agent.issuetree[who][len_DC+len_PC+len_S+j+(k*len_PC)][0]*\
						  (agent.issuetree[who][k][1] - agent.issuetree[who][k][0]))
						# print('This is the ML numerator: ' + str(ML_numerator))
					else:
						ML_numerator = ML_numerator	

			# 1.5.2.3.2. Addition of the gap to the numerator
			# Contingency for partial knowledge issues
			if agent.issuetree[who][len_DC + j][1] == None or agent.issuetree[who][len_DC + j][0] == None:
				ML_numerator = 0
			else:
				# print('This is the gap for the ML' + str(j+1) + ': ' + str(agent.issuetree[0][len_DC + j][1] - agent.issuetree[0][len_DC + j][0]))
				ML_numerator = ML_numerator + abs(agent.issuetree[who][len_DC + j][1] - agent.issuetree[who][len_DC + j][0])
			# print('The numerator is equal to: ' + str(ML_numerator))
			# print('The denominator is equal to: ' + str(ML_denominator))

			# 1.5.2.3.3. Calculation of the preference
			if ML_denominator != 0:
				agent.issuetree[who][len_DC+j][2] = ML_numerator/ML_denominator 
			# print('The new preference of the policy core ML' + str(j+1) + ' is: ' + str(agent.issuetree[0][len_DC+j][2]))
			else:
				agent.issuetree[who][len_DC+j][2] = 0

			#####
			# 1.6.3. Preference calculation for the secondary issues
			# Currently not implemented as it is not useful within the policy process. Preferences are only used at the secondary level to help define what will be on the agenda.
			# This is something that could be implemented in the future by copying and modifying the calculation for the policy core preferences.

