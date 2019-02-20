from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from collections import defaultdict

from model_SM_initialisation_agents import init_active_agents, init_electorate_agents, init_truth_agent
from model_SM_agents import ActiveAgent, ElectorateAgent, TruthAgent
from model_module_interface import policy_instrument_input, issue_tree_input


class PolicyEmergenceSM(Model):

	'''
	Simplest Model for the policy emergence model.
	'''

	def __init__(self, height=20, width=20, PMnumber=3, PEnumber=5, EPnumber=2):

		self.height = height
		self.width = width

		self.stepCount = 0
		self.agenda_PC = None
		self.agenda_PF = None
		self.policy_implemented = None

		self.schedule = RandomActivation(self)
		self.grid = SingleGrid(height, width, torus=True)

		self.datacollector = DataCollector(
			# Model-level count of happy agents
			{"step": "stepCount"},
			# For testing purposes, agent's individual x and y
			{"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]})

		# belief tree properties
		self.len_S, self.len_PC, self.len_DC, self.len_CR = issue_tree_input(self)
		# print(self.len_S, self.len_PC, self.len_DC, self.len_CR)

		# issue tree properties
		self.policy_instruments, self.len_ins_1, self.len_ins_2 = policy_instrument_input(self, self.len_PC)

		

		# Set up active agents (manually for now)
		init_active_agents(self, self.len_S, self.len_PC, self.len_DC, self.len_CR, self.len_PC, self.len_ins_1, self.len_ins_2)

		# Set up passive agents (manually for now)
		init_electorate_agents(self, self.len_S, self.len_PC, self.len_DC)

		# Set up truth agent
		init_truth_agent(self, self.len_S, self.len_PC, self.len_DC, self.len_ins_1, self.len_ins_2)
		# the issue tree will need to be updated at a later stage witht he values from the system/policy context

		print("Schedule has : ", len(self.schedule.agents), " agents.")
		print(self.schedule.agents)
		print(" ")

		for agent in self.schedule.agent_buffer(shuffled=False):
			print(' ')
			print(agent)
			print(type(agent))
			# if isinstance(agent, ActiveAgent):
			# 	print(agent.unique_id, " ", agent.pos, " ", agent.agent_type, " ", agent.resources, " ", agent.affiliation, " ", agent.issuetree[agent.unique_id], " ", agent.policytree[agent.unique_id][0])
			# if isinstance(agent, ElectorateAgent):
			# 	print(agent.unique_id, " ", agent.pos, " ", agent.affiliation, " ", agent.issuetree)
			# if isinstance(agent, TruthAgent):
			# 	print(agent.pos, " ", agent.issuetree)

		self.running = True
		self.numberOfAgents = self.schedule.get_agent_count()
		self.datacollector.collect(self)

	def step(self):
		print(" ")
		print("step me")

		'''
		Main steps of the Simplest Model for policy emergence:
		0. Module interface - Input
			Obtention of the beliefs from the system/policy context
			!! This is to be implemented at a later stage
		1. Agenda setting step
		2. Policy formulation step
		3. Module interface - Output
			Implementation of the policy instrument selected
		'''

		# 0.
		self.module_interface_input()

		# 1.
		self.agenda_setting()

		# 2.
		self.policy_formulation()

		# 3.
		self.module_interface_output()


		# end of step actions:
		# iterate the steps counter
		self.stepCount += 1

		# collect data
		self.datacollector.collect(self)

	def module_interface_input(self):

		'''
		The module interface input step consists of actions related to the module interface and 
		'''

		print("Module interface output not introduced yet")

	def agenda_setting(self):

		'''
		The agenda setting step is the first step in the policy process conceptualised in this model. The steps are given as follows:
		1. Active agents policy core issue selection
		2. Active agents policy family selection
		3. Active agents actions [to be detailed later]
		4. Active agents policy core issue selection update
		5. Active agents policy family selection update
		6. Agenda selection
		'''

		print("Agent setting step is incomplete for now")

		# 1. & 2.
		for agent in self.schedule.agent_buffer(shuffled=False):
			if isinstance(agent, ActiveAgent):  # considering only active agents
				agent.selection_PC()
				agent.selection_PF()

		# 3.

		# 4. & 5.
		for agent in self.schedule.agent_buffer(shuffled=False):
			if isinstance(agent, ActiveAgent):  # considering only active agents
				agent.selection_PC()
				agent.selection_PF()

		# 6. 
		# Note that the agenda is made ONLY with the policy makers here 
		selected_PC_list = []
		selected_PF_list = []
		for agent in self.schedule.agent_buffer(shuffled=False):
			if isinstance(agent, ActiveAgent) and agent.agent_type == 'policymaker':  # considering only policy makers
				selected_PC_list.append(agent.selected_PC)
				selected_PF_list.append(agent.selected_PF)

		# finding the most common policy core issue
		self.agenda_PC = max(set(selected_PC_list), key=selected_PC_list.count)

		self.agenda_PF = None



	def policy_formulation(self):

		'''
		The policy formulation step is the second step in the policy process conceptualised in this model. The steps are given as follows:
		1. Active agents policy core issue selection
		2. Active agents policy family selection
		3. Active agents actions [to be detailed later]
		4. Active agents policy core issue selection update
		5. Active agents policy family selection update
		6. Agenda selection
		'''

		print("Policy formulation not introduced yet")

	def module_interface_output(self):

		print("Module interface output not introduced yet")


	def preference_udapte(self, agent, who):

		"""
		The preference update function
		===========================

		This function is used to update the preferences of the agents in their
		respective belief trees.

		agent - this is the owner of the belief tree
		who - this is the part of the belieftree that is considered - agent.unique_id should be used for this - this is done to also include partial knowledge preference calculation

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

