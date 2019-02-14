import random
import copy

from model_SM_active_agents import ActiveAgent

def init_active_agents(self):

	# belief tree properties
	len_S = 4
	len_S_names = ["vision", "movement", "type0preferences", "type1preferences"]
	len_PC = 2
	len_PC_names = ["freedom", "preferences"]
	len_DC = 1 
	len_DC_names = ["evenness"]
	number_causalrelation = len_DC*len_PC + len_PC*len_S

	# issue tree properties
	len_PF = len_PC
	len_PF_names = len_PC_names
	len_ins_1 = 4
	len_ins_1_names = ["TBD", "TBD", "TBD", "TBD"]
	len_ins_2 = 6
	len_ins_2_names = ["TBD", "TBD", "TBD", "TBD", "TBD", "TBD"]

	# agent global properties
	number_activeagents = 10

	# model issue tree structure
	issuetree0 = [None]
	# the format for the whole issue tree is then given as - this issue tree is filled with the perception of other agent's issues beliefs, goals and preferences.
	# [issuetree] = [[issuetree_owner],[issuetree_agent1],...[issuetree_agentn]]
	# the format of the issue tree of one agent is:
	# [issuetree_owner] = [[issues], [causal relations]]
	# [issues] = [[DC1], ...,[DCn],[PC1],..,[PCn],[S1],...,[Sn]]
	# [causal relations] = [[DC1-PC1],...,[DC1-PCn],...,[DCn-PCn],[PC1-S1],...,[PC1-Sn],...,[PCn-Sn],]
	# the format of the issue is: [X] = [0, 0, 0] = [beliefs, goals, preferences]
	issuetree_empty_issues = [[0, 0, 0] for f in range(len_DC + len_PC + len_S)]
	issuetree_full = issuetree_empty_issues
	for p in range(number_causalrelation):
		issuetree_full.append([0])
	issuetree0[0] = issuetree_full
	for r in range(number_activeagents):
		issuetree_empty_agents = [[None, None, None] for p in range(len_DC + len_PC + len_S)]
		for f in range(number_causalrelation):
			issuetree_empty_agents.append([None])
		issuetree0.append(issuetree_empty_agents)

	# model policy tree structure
	# The format for the whole tree is given as - this policy tree is filled with the perception of other agent's policy impacts:
	# [policytree] = [[policytree_owner],[policytree_agent1],...,[policytree_agentn]]
	# [policytree_owner] = [[PF1],...,[PFn],[PI1.1],...,[PI1.n],...,[PIn.1],...,[PIn.n]]
	# [PF1] = [PC1,...,PCn]
	# [PI1.1] = [S1,...,Sn]
	policytree0 = [None]
	policytree0[0] = [[0] for f in range(len_PF + len_ins_1 + len_ins_2)]
	for n in range(len_PC):
		policytree0[0][n] = [0 for f in range(len_PC)]
	for m in range(len_ins_1+len_ins_2):
		policytree0[0][len_PC+m] = [0 for f in range(len_S)]
	for r in range(number_activeagents):
		policytree_empty_agents = [[None] for f in range(len_PF + len_ins_1 + len_ins_2)]
		for n in range(len_PC):
			policytree_empty_agents[n] = [None for f in range(len_PC)]
		for m in range(len_ins_1+len_ins_2):
			policytree_empty_agents[len_PC+m] = [None for f in range(len_S)]
		policytree0.append(policytree_empty_agents)

	# policy maker 1
	x = 0
	y = 0
	ID = 0
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy maker 2
	x = 0
	y = 1
	ID = 1
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy maker 3
	x = 0
	y = 2
	ID = 2
	agent_type = 'policymaker'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 1
	x = 1
	y = 0
	ID = 3
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 2
	x = 1
	y = 1
	ID = 4
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 3
	x = 1
	y = 2
	ID = 5
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 4
	x = 1
	y = 3
	ID = 6
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 5
	x = 1
	y = 4
	ID = 7
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# external party 1
	x = 2
	y = 0
	ID = 8
	agent_type = 'externalparty'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# external party 2
	x = 2
	y = 1
	ID = 9
	agent_type = 'externalparty'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)