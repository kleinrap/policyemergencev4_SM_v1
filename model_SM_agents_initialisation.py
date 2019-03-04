import random
import copy

from model_SM_agents import ActiveAgent, ElectorateAgent, TruthAgent

def init_active_agents(self, len_S, len_PC, len_DC, len_CR, len_PF, len_ins_1, len_ins_2, len_ins_all):

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
	issuetree_empty_issues = [[None, None, None] for f in range(len_DC + len_PC + len_S)]
	issuetree_full = issuetree_empty_issues
	for p in range(len_CR):
		issuetree_full.append([None])
	issuetree0[0] = issuetree_full
	for r in range(number_activeagents):
		issuetree_empty_agents = [[None, None, None] for p in range(len_DC + len_PC + len_S)]
		for f in range(len_CR):
			issuetree_empty_agents.append([None])
		issuetree0.append(issuetree_empty_agents)

	# model policy tree structure
	# The format for the whole tree is given as - this policy tree is filled with the perception of other agent's policy impacts:
	# [policytree] = [[policytree_owner],[policytree_agent1],...,[policytree_agentn]]
	# [policytree_owner] = [[PF1],...,[PFn],[PI1.1],...,[PI1.n],...,[PIn.1],...,[PIn.n]]
	# [PF1] = [PC1,...,PCn, Preference]
	# [PI1.1] = [S1,...,Sn, Preference]
	policytree0 = [None]
	policytree0[0] = [[None] for f in range(len_PF + len_ins_1 + len_ins_2 + len_ins_all)]
	for n in range(len_PC):
		policytree0[0][n] = [None for f in range(len_PC + 1)] # +1 is placed for the inclusion of preferences
	for m in range(len_ins_1 + len_ins_2 + len_ins_all):
		policytree0[0][len_PF+m] = [None for f in range(len_S+1)]  # +1 is placed for the inclusion of preferences
	for r in range(number_activeagents):
		policytree_empty_agents = [[None] for f in range(len_PF + len_ins_1 + len_ins_2 + len_ins_all)]
		for n in range(len_PC):
			policytree_empty_agents[n] = [None for f in range(len_PC + 1)]
		for m in range(len_ins_1+len_ins_2 + len_ins_all):
			policytree_empty_agents[len_PF+m] = [None for f in range(len_S+1)]
		policytree0.append(policytree_empty_agents)

	
	# creation of the agents
	# policy maker 1
	x = 0
	y = 0
	unique_id = 0
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	len_PC_names = ["movement", "happiness"]
	len_S_names = ["movement0", "movement1", "happy0", "happy1"]
	issuetree[unique_id][0] = [0.4, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.5, 0.6, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0.25, 0.95, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.55, 0.65, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.6, 0.35, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.35, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.65, 0.95, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy maker 2
	x = 0
	y = 1
	unique_id = 1
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.4, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.5, 0.6, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0.25, 0.95, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.55, 0.65, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.6, 0.35, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.35, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.65, 0.95, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy maker 3
	x = 0
	y = 2
	unique_id = 2
	agent_type = 'policymaker'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	len_PC_names = ["movement", "happiness"]
	len_S_names = ["movement0", "movement1", "happy0", "happy1"]
	issuetree[unique_id][0] = [0.85, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.15, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0, 0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.6, 0, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.45, 0, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.0, 0.85, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 1
	x = 1
	y = 0
	unique_id = 3
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.4, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.5, 0.6, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0.25, 0.95, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.55, 0.65, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.6, 0.35, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.35, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.65, 0.95, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 2
	x = 1
	y = 1
	unique_id = 4
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.4, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.5, 0.6, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0.25, 0.95, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.55, 0.65, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.6, 0.35, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.35, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.65, 0.95, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 3
	x = 1
	y = 2
	unique_id = 5
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.85, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.15, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0, 0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.6, 0, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.45, 0, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.0, 0.85, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 4
	x = 1
	y = 3
	unique_id = 6
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.85, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.15, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0, 0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.6, 0, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.45, 0, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.0, 0.85, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# policy entrepreneur 5
	x = 1
	y = 4
	unique_id = 7
	agent_type = 'policyentrepreneur'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.85, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.15, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0, 0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.6, 0, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.45, 0, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.0, 0.85, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# external party 1
	x = 2
	y = 0
	unique_id = 8
	agent_type = 'externalparty'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.4, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.5, 0.6, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0.25, 0.95, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.55, 0.65, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.6, 0.35, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.35, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.65, 0.95, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# external party 2
	x = 2
	y = 1
	unique_id = 9
	agent_type = 'externalparty'
	resources = 75
	affiliation = 1
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[unique_id][0] = [0.85, 0.05, 0] # DC1 - Belief, Goal, Preference
	issuetree[unique_id][1] = [0.15, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[unique_id][2] = [0, 0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[unique_id][3] = [0.6, 0, 0] # S1 - Belief, Goal, Preference
	issuetree[unique_id][4] = [0.45, 0, 0] # S2 - Belief, Goal, Preference
	issuetree[unique_id][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[unique_id][6] = [0.0, 0.85, 0] # S4 - Belief, Goal, Preference
	# causal relations
	issuetree[unique_id][7][0] = 0.2  # DC1 - PC1
	issuetree[unique_id][8][0] = 0.7  # DC1 - PC2
	issuetree[unique_id][9][0] = 0.8  # PC1 - S1
	issuetree[unique_id][10][0] = 0.9  # PC1 - S2
	issuetree[unique_id][11][0] = 0.85  # PC1 - S3
	issuetree[unique_id][12][0] = 0  # PC1 - S4
	issuetree[unique_id][13][0] = 0  # PC2 - S1
	issuetree[unique_id][14][0] = 0  # PC2 - S2
	issuetree[unique_id][15][0] = 0  # PC2 - S3
	issuetree[unique_id][16][0] = -0.5  # PC2 - S4
	# policy tree copy
	policytree = copy.deepcopy(policytree0)
	agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_update(agent, unique_id)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

def init_electorate_agents(self, len_S, len_PC, len_DC):

	# model issue tree structure
	# the format for the whole issue tree is given as:
	# [issuetree] = [DC1, ...,DCn,PC1,..,PCn,S1,...,Sn]
	# This only contains the goals of the electorate.
	issuetree0 = [0 for f in range(len_DC + len_PC + len_S)]

	# creation of the agents
	# electorate 1
	x = 11
	y = 0
	unique_id = 100
	affiliation = 0
	representativeness = 74
	issuetree = copy.deepcopy(issuetree0)
	# issue goals
	issuetree[0] = 0.05 # DC1 - Belief, Goal, Preference
	issuetree[1] = 0.6 # PC1 - Belief, Goal, Preference
	issuetree[2] = 0.95 # PC2 - Belief, Goal, Preference
	issuetree[3] = 0.65 # S1 - Belief, Goal, Preference
	issuetree[4] = 0.65 # S2 - Belief, Goal, Preference
	issuetree[5] = 1 # S3 - Belief, Goal, Preference
	issuetree[6] = 1 # S4 - Belief, Goal, Preference
	agent = ElectorateAgent((x, y), unique_id, self, affiliation, issuetree, representativeness)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# electorate 2
	x = 11
	y = 1
	unique_id = 101
	affiliation = 1
	representativeness = 26
	issuetree = copy.deepcopy(issuetree0)
	# issue goals
	issuetree[0] = 0.05 # DC1 - Belief, Goal, Preference
	issuetree[1] = 0.6 # PC1 - Belief, Goal, Preference
	issuetree[2] = 0.95 # PC2 - Belief, Goal, Preference
	issuetree[3] = 0 # S1 - Belief, Goal, Preference
	issuetree[4] = 0 # S2 - Belief, Goal, Preference
	issuetree[5] = 0.95 # S3 - Belief, Goal, Preference
	issuetree[6] = 0 # S4 - Belief, Goal, Preference
	agent = ElectorateAgent((x, y), unique_id, self, affiliation, issuetree, representativeness)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

def init_truth_agent(self, len_S, len_PC, len_DC, len_ins_1, len_ins_2, len_ins_all):

	# model issue tree structure
	# the format for the whole issue tree is given as:
	# [issuetree] = [DC1, ...,DCn,PC1,..,PCn,S1,...,Sn]
	# This only contains the states of the system.
	issuetree0 = [0 for f in range(len_DC + len_PC + len_S)]

	# model policy tree structure
	# The format for the whole tree is given as - this policy tree is filled with the perception of other agent's policy impacts:
	# [policytree] = [[PF1],...,[PFn],[PI1.1],...,[PI1.n],...,[PIn.1],...,[PIn.n]]
	# [PF1] = [PC1,...,PCn]
	# [PI1.1] = [S1,...,Sn]
	policytree0 = [0 for f in range(len_PC+len_ins_1+len_ins_2 + len_ins_all)]
	for n in range(len_PC):
		policytree0[n] = [0 for f in range(len_PC)]
	for m in range(len_ins_1+len_ins_2 + len_ins_all):
		policytree0[len_PC+m] = [0 for f in range(len_S)]

	# creation of the agent
	x = 3
	y = 3
	unique_id = 50 
	issuetree = copy.deepcopy(issuetree0)
	policytree = copy.deepcopy(policytree0)
	agent = TruthAgent(unique_id, self, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)