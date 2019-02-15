import random
import copy

from model_SM_active_agents import ActiveAgent, ElectorateAgent

def init_active_agents(self, len_S, len_PC, len_DC, number_causalrelation, len_PF, len_ins_1, len_ins_2, number_activeagents):

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

	# creation of the agents
	# policy maker 1
	x = 0
	y = 0
	ID = 0
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	len_PC_names = ["freedom", "happiness"]
	len_S_names = ["vision", "movement", "last_movement", "type0preferences", "type1preferences"]
	issuetree[ID][0] = [0.7, -0.9, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, 1.0, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.75, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.9, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, -0.7, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, -0.7, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.preference_udapte(agent, ID)  # updating the issue tree preferences
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, -0.9, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, 1.0, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.75, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.9, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, -0.7, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, -0.7, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	len_PC_names = ["freedom", "happiness"]
	len_S_names = ["vision", "movement", "last_movement", "type0preferences", "type1preferences"]
	issuetree[ID][0] = [0.7, 0.0, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.5, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, -0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.5, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.0, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, -0.1, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, 0.2, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, 0.2, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, -0.9, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, 1.0, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.75, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.9, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, -0.7, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, -0.7, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, -0.9, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, 1.0, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.75, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.9, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, -0.7, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, -0.7, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, 0.0, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.5, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, -0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.5, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.0, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, -0.1, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, 0.2, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, 0.2, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, 0.0, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.5, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, -0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.5, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.0, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, -0.1, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, 0.2, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, 0.2, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, 0.0, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.5, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, -0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.5, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.0, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, -0.1, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, 0.2, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, 0.2, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, -0.9, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, 1.0, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.75, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.9, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, -0.7, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, -0.7, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
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
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, 0.0, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.5, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, -0.5, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.5, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.0, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, -0.1, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, 0.2, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, 0.2, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)


def init_electorate_agents(self, len_S, len_PC, len_DC):


	# model issue tree structure
	issuetree0 = [None]
	# the format for the whole issue tree is then given as - this issue tree is filled with the perception of other agent's issues beliefs, goals and preferences.
	# [issuetree] = [[issuetree_owner],[issuetree_agent1],...[issuetree_agentn]]
	# the format of the issue tree of one agent is:
	# [issuetree_owner] = [[issues], [causal relations]]
	# [issues] = [[DC1], ...,[DCn],[PC1],..,[PCn],[S1],...,[Sn]]
	# [causal relations] = [[DC1-PC1],...,[DC1-PCn],...,[DCn-PCn],[PC1-S1],...,[PC1-Sn],...,[PCn-Sn],]
	# the format of the issue is: [X] = [0, 0, 0] = [beliefs, goals, preferences]
	issuetree_empty_issues = [0 for f in range(len_DC + len_PC + len_S)]
	issuetree_full = issuetree_empty_issues
	issuetree0[0] = issuetree_full

	# creation of the agents
	# electorate 1
	x = 0
	y = 0
	ID = 100
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue goals
	issuetree[0] = -0.9 # DC1 - Belief, Goal, Preference
	issuetree[1] = 0.8 # PC1 - Belief, Goal, Preference
	issuetree[2] = 1.0 # PC2 - Belief, Goal, Preference
	issuetree[3] = 0.75 # S1 - Belief, Goal, Preference
	issuetree[4] = 0.9 # S2 - Belief, Goal, Preference
	issuetree[5] = 0.95 # S3 - Belief, Goal, Preference
	issuetree[6] = -0.7 # S4 - Belief, Goal, Preference
	issuetree[7] = -0.7 # S5 - Belief, Goal, Preference
	print(issuetree)
	agent = PassiveAgent((x, y), ID, self, affiliation, issuetree)
	self.preference_udapte(agent, ID)  # updating the issue tree preferences
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	'''
	# policy maker 2
	x = 0
	y = 1
	ID = 1
	agent_type = 'policymaker'
	resources = 75
	affiliation = 0
	issuetree = copy.deepcopy(issuetree0)
	# issue beliefs, goals and preferences
	issuetree[ID][0] = [0.7, -0.9, 0] # DC1 - Belief, Goal, Preference
	issuetree[ID][1] = [0.0, 0.8, 0] # PC1 - Belief, Goal, Preference
	issuetree[ID][2] = [0.8, 1.0, 0] # PC2 - Belief, Goal, Preference
	issuetree[ID][3] = [-0.4, 0.75, 0] # S1 - Belief, Goal, Preference
	issuetree[ID][4] = [0.0, 0.9, 0] # S2 - Belief, Goal, Preference
	issuetree[ID][5] = [0.0, 0.95, 0] # S3 - Belief, Goal, Preference
	issuetree[ID][6] = [0.0, -0.7, 0] # S4 - Belief, Goal, Preference
	issuetree[ID][7] = [0.0, -0.7, 0] # S5 - Belief, Goal, Preference
	# causal relations
	issuetree[ID][8][0] = 0.2  # DC1 - PC1
	issuetree[ID][9][0] = 0.7  # DC1 - PC2
	issuetree[ID][10][0] = 0.8  # PC1 - S1
	issuetree[ID][11][0] = 0.9  # PC1 - S2
	issuetree[ID][12][0] = 0.85  # PC1 - S3
	issuetree[ID][13][0] = 0  # PC1 - S4
	issuetree[ID][14][0] = 0  # PC1 - S5
	issuetree[ID][15][0] = 0  # PC2 - S1
	issuetree[ID][16][0] = 0  # PC2 - S2
	issuetree[ID][17][0] = 0  # PC2 - S3
	issuetree[ID][18][0] = -0.5  # PC2 - S4
	issuetree[ID][19][0] = -0.5  # PC2 - S5
	policytree = copy.deepcopy(policytree0)
	# policy families
	policytree[ID][0] = [1, 1]  # PF1 - PC1,PC2
	policytree[ID][1] = [1, 1] # PF2 - PC1, PC2
	policytree[ID][2] = [-1, -1, -1 ,-1 ,-1]  # PI1.1 - S1,S2,S3,S4,S5
	policytree[ID][3] = [-1, -1, -1 ,-1 ,-1]  # PI1.2 - S1,S2,S3,S4,S5
	policytree[ID][4] = [-1, -1, -1 ,-1 ,-1]  # PI1.3 - S1,S2,S3,S4,S5
	policytree[ID][5] = [-1, -1, -1 ,-1 ,-1]  # PI1.4 - S1,S2,S3,S4,S5
	policytree[ID][6] = [-1, -1, -1 ,-1 ,-1]  # PI2.1 - S1,S2,S3,S4,S5
	policytree[ID][7] = [-1, -1, -1 ,-1 ,-1]  # PI2.2 - S1,S2,S3,S4,S5
	policytree[ID][8] = [-1, -1, -1 ,-1 ,-1]  # PI2.3 - S1,S2,S3,S4,S5
	policytree[ID][9] = [-1, -1, -1 ,-1 ,-1]  # PI2.4 - S1,S2,S3,S4,S5
	policytree[ID][10] = [-1, -1, -1 ,-1 ,-1]  # PI2.5 - S1,S2,S3,S4,S5
	policytree[ID][11] = [-1, -1, -1 ,-1 ,-1]  # PI2.6 - S1,S2,S3,S4,S5
	agent = ActiveAgent((x, y), ID, self, agent_type, resources, affiliation, issuetree, policytree)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)
	'''