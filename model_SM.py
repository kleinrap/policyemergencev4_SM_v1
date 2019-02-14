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

		# Set up agents (manually for now)
		init_active_agents(self)

		print("Schedule has : ", len(self.schedule.agents), " agents.")
		print(self.schedule.agents)

		for agent in self.schedule.agent_buffer(shuffled=False):
			print(agent.ID, " ", agent.pos, " ", agent.agent_type, " ", agent.resources, " ", agent.affiliation, " ", agent.issuetree[0][0], " ", agent.policytree[0][2])

		self.running = True
		self.numberOfAgents = self.schedule.get_agent_count()
		self.datacollector.collect(self)