from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

'''
Need addition model - For coupling:
- Migration
    - The net amount of agent change per step needs to be zero.
    - Random agents are removed? Or unhappy agents? It should be unhappy ones - that makes more sense at least.
    - Type 0 agents leaving must be replaced by type 1 agents.
    - Type 1 agents leaving must be replaced by type 0 agents.
    - Where are new agents incoming placed onto the map? Random locations
    - Is there a constant turnover? Or is it a one time thing? Dor policy instruments, it makes more sense to have a continuous turnover of a certain percentage


KPIs:
What needs to be recorded (KPIs):
Empty cells -- Implemented
Green cells (type 0) -- Implemented
Blue cells (type 1) -- Implemented
Vision - Global - Implemented
Movement - Global - Implemented
Green homophily - Implemented
Blue homophily - Implemented
'''

class SchellingAgent(Agent):
    '''
    Schelling segregation agent
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

    def step(self):

        # Checking if the agent is happy
        happyBool = self.happy_check()

        # If unhappy, move - considering the movement quota and whether the agent is type0 or type1:
        if happyBool == False:
            if self.model.movementQuotaCount <= self.model.movementQuota*self.model.schedule.get_agent_count():
                self.model.grid.move_to_empty(self)
                self.model.movementQuotaCount += 1

    def happy_check(self):

        '''
        Function used to check if the agent is happy in its current position. Use for checking if there is a need to move and to check if the location it is moving to is appropriate.
        '''
        # Initialisation of patameters
        similar = 0
        happyBool = bool()

        # Finding the neighbors
        neighborList = self.model.grid.get_neighbors(self.pos, True, False, self.model.happyCheckRadius)

        # Iterating through the neighbors to find whether they are similar:
        for neighbor in neighborList:
            if neighbor.type == self.type:
                similar += 1

        # Converting similarity value into a percentage
        similar = similar/len(neighborList)

        if (self.type == 0 and similar > self.model.homophilyType0) or (self.type == 1 and similar > self.model.homophilyType1):
            happyBool = True
            self.model.happy += 1

        return happyBool


class Schelling(Model):
    '''
    Model class for the Schelling segregation model.
    This class has been modified from the original model of mesa. Complexity has been added such that the model be used with a model of the policy making process.
    '''

    def __init__(self, height=20, width=20, density=0.8, minority_pc=0.2, homophilyType0=0.3, homophilyType1=0.3, movementQuota=0.30, happyCheckRadius=5, moveCheckRadius=5):
        '''
        '''

        self.height = height
        self.width = width
        self.density = density
        self.minority_pc = minority_pc
        self.homophilyType0 = homophilyType0
        self.homophilyType1 = homophilyType1
        self.movementQuota = movementQuota
        self.happyCheckRadius = happyCheckRadius
        self.moveCheckRadius = moveCheckRadius

        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(height, width, torus=True)

        self.happy = 0
        self.empty = 0
        self.type0agents = 0
        self.type1agents = 0
        self.movementQuotaCount = 0
        self.datacollector = DataCollector(
            # Model-level count of happy agents
            {"happy": "happy", "empty": "empty"},
             # Model-level count of empty cells
            # For testing purposes, agent's individual x and y
            {"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]})

        # Set up agents
        # We use a grid iterator that returns
        # the coordinates of a cell as well as
        # its contents. (coord_iter)
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                if self.random.random() < self.minority_pc:
                    agent_type = 1
                else:
                    agent_type = 0

                agent = SchellingAgent((x, y), self, agent_type)
                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)
        print("Schedule", len(self.schedule.agents))

        self.running = True
        self.datacollector.collect(self)


    def step(self):
        '''
        Run one step of the model. If All agents are happy, halt the model.
        '''
        self.happy = 0  # Reset counter of happy agents
        self.empty = 0  # Reset counter of empty cells
        self.type0agents = 0  # Reset count of type 0 agents
        self.type1agents = 0  # Reset count of type 1 agents
        self.movementQuotaCount = 0

        # run the step for the agents

        self.schedule.step()
        print(self.movementQuotaCount, " agents moved.")
        print(round(self.happy/self.schedule.get_agent_count() * 100,2), " are happy agents.")

        # Calculating empty counter
        self.empty = (self.height*self.width) - self.schedule.get_agent_count()
        # Calculating type 0 and type 1 agent numbers
        for agent in self.schedule.agent_buffer(shuffled=True):
            if agent.type == 0:
                self.type0agents += 1
            if agent.type == 1:
                self.type1agents += 1


        # collect data
        self.datacollector.collect(self)

        if self.happy == self.schedule.get_agent_count():
            self.running = False
            print("All agents are happy, the simulation ends!")