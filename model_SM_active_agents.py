from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

class ActiveAgent(Agent):
    '''
    Active agents, including policy makers, policy entrepreneurs and external parties.
    '''
    def __init__(self, pos, model, agent_type, resources, affiliation):
        '''
         Create a new Schelling agent.
         Args:
            unique_id: Unique identifier for the agent.
            x, y: Agent initial location.
            agent_type: Indicator for the agent's type (minority=1, majority=0)
        '''
        super().__init__(pos, model)
        self.pos = pos  # defines the position of the agent on the grid
        self.agent_type = agent_type  # defines the type of agents from policymaker, policyentrepreneur and externalparty
        self.resources = resources  # resources used for agents to perform actions
        self.affiliation = affiliation  # political affiliation affecting agent interactions