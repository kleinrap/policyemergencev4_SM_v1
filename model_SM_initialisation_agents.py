import random
import copy

from model_SM_active_agents import ActiveAgent

def init_active_agents(self):

	# Policy maker 1
	x = 0
	y = 0
	agent_type = 'policymaker'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy maker 2
	x = 0
	y = 1
	agent_type = 'policymaker'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy maker 3
	x = 0
	y = 2
	agent_type = 'policymaker'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy entrepreneur 1
	x = 1
	y = 0
	agent_type = 'policyentrepreneur'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy entrepreneur 2
	x = 1
	y = 1
	agent_type = 'policyentrepreneur'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy entrepreneur 3
	x = 1
	y = 2
	agent_type = 'policyentrepreneur'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy entrepreneur 4
	x = 1
	y = 3
	agent_type = 'policyentrepreneur'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# Policy entrepreneur 5
	x = 1
	y = 4
	agent_type = 'policyentrepreneur'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# External party 1
	x = 2
	y = 0
	agent_type = 'externalparty'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# External party 2
	x = 1
	y = 1
	agent_type = 'externalparty'
	agent = ActiveAgent((x, y), self, agent_type)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	print("Hello agents")