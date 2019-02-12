from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector


class PolicyMakerAgent(Agent):
    '''
    Policy maker agent.
    '''
    def __init__(self, pos, model):
        '''
         Create a new Schelling agent.
         Args:
            unique_id: Unique identifier for the agent.
            x, y: Agent initial location.
            agent_type: Indicator for the agent's type (minority=1, majority=0)
        '''
        super().__init__(pos, model)
        self.pos = pos

class PolicyEntrepreneurAgent(Agent):
    '''
    Policy entrepreneur agent.
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

class ExternalPartyAgent(Agent):
    '''
    External party agent.
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

	def __init__(self, height=20, width=20, density=0.8):

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

		# Set up agents
		# We use a grid iterator that returns
		# the coordinates of a cell as well as
		# its contents. (coord_iter)
		for cell in self.grid.coord_iter():
			x = cell[1]
			y = cell[2]
			agentPM = PolicyMakerAgent((x, y), self)
			self.grid.position_agent(agentPM, (x, y))
			self.schedule.add(agentPM)
		print("Schedule: ", len(self.schedule.agents))

		self.running = True
		self.numberOfAgents = self.schedule.get_agent_count()
		self.datacollector.collect(self)