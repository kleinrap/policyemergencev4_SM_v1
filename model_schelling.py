from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

'''
Need addition model - For coupling:
- Migration
- Homophily differences between colours
- Change in the happiness check
- Movement quota parameter
- Introduction of the algorithm for moving
- Additions of the other KPIs
- 
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

        # Happiness check:
        similar = 0
        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move (only within the quota):
        if similar < self.model.homophily:
            # print(self.model.movementQuotaCount, self.model.movementQuota*self.model.schedule.get_agent_count())
            if self.model.movementQuotaCount <= self.model.movementQuota*self.model.schedule.get_agent_count():
                self.model.grid.move_to_empty(self)
                self.model.movementQuotaCount += 1
        else:
            self.model.happy += 1



class Schelling(Model):
    '''
    Model class for the Schelling segregation model.
    '''

    def __init__(self, height=20, width=20, density=0.8, minority_pc=0.2, homophily=3, movementQuota=0.30):
        '''
        '''

        self.height = height
        self.width = width
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily
        self.movementQuota = movementQuota

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
        print(self.happy, " are happy agents.")

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

        # print('self.schedule.get_agent_count(): ', self.schedule.get_agent_count())
        # print('self.happy: ', self.happy)

        if self.happy == self.schedule.get_agent_count():
            self.running = False


    # What needs to be recorded (KPIs):
    # Empty cells -- Total cells - agents number
    # Green cells (type 0) -- 
    # Blue cells (type 1) --
    # Vision - Global - Not implemented yet
    # Movement - Global - Not implemented yet
    # Green homophily - Not implemented yet
    # Blue homophily - Not implemented yet

