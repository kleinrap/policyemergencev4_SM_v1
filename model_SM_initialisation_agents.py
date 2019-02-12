import random
import copy

from model_SM_active_agents import ActiveAgent

def init_active_agents(self):

	# belief tree properties
	len_S = 7
	len_PC = 3
	len_DC = 1

	# policy maker 1
	x = 0
	y = 0
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy maker 2
	x = 0
	y = 1
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy maker 3
	x = 0
	y = 2
	agent_type = 'policymaker'
	resources = 75
	affiliation = 1
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 1
	x = 1
	y = 0
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 0
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 2
	x = 1
	y = 1
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 0
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 3
	x = 1
	y = 2
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 4
	x = 1
	y = 3
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 5
	x = 1
	y = 4
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# external party 1
	x = 2
	y = 0
	agent_type = 'externalparty'
	resources = 75
	affiliation = 0
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# external party 2
	x = 2
	y = 1
	agent_type = 'externalparty'
	resources = 75
	affiliation = 1
	agent = ActiveAgent((x, y), self, agent_type, resources, affiliation)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)