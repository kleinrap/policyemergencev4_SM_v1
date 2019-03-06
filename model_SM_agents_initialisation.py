import random
import copy
import pandas as pd

from model_SM_agents import ActiveAgent, ElectorateAgent, TruthAgent

def init_active_agents(self, len_S, len_PC, len_DC, len_CR, len_PF, len_ins_1, len_ins_2, len_ins_all, SM_inputs):

	# SM_inputs opening
	SM_PMs = SM_inputs[0]  # number of policy makers
	SM_PMs_aff = SM_inputs[1]  # policy maker distribution per affiliation
	SM_PEs = SM_inputs[2]  # number of policy entrepreneurs
	SM_PEs_aff = SM_inputs[3]  # policy entrepreneur distribution per affiliation
	SM_EPs = SM_inputs[4]  # number of external parties
	SM_EPs_aff = SM_inputs[5]  # external parties distribution per affiliation
	resources_aff = SM_inputs[6]  # resources per affiliation agent out of 100

	aff_number = len(resources_aff)
	if aff_number!= len(SM_PMs_aff) or aff_number != len(SM_PMs_aff) or aff_number != len(SM_EPs_aff):
		print("MISTAKE IN THE INPUTS on affiliation")

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


	# initialisation of a number of standard inputs
	x = 0
	y = 0
	unique_id = 0

	# loading the belief profiles
	belief_input = pd.read_csv('input_beliefProfiles', sep=',')
	belief_profiles = []
	for i in range(aff_number):
		belief_profiles.append(belief_input.iloc[i].tolist())

	# creation of the active agents
	for i in range(aff_number):
		# creation of the policy makers
		j = 0
		while j < SM_PMs_aff[i]:
			agent_type = 'policymaker'
			affiliation = i
			resources = resources_aff[i]
			issuetree = copy.deepcopy(issuetree0)
			# introducing the issues
			for k in range(len_DC + len_PC + len_S):
				issuetree[unique_id][k] = [0, belief_profiles[i][k+1], 0]
			# introduction of the causal relations
			for k in range(len_DC*len_PC + len_PC * len_S):
				issuetree[unique_id][len_DC + len_PC + len_S + k][0] = belief_profiles[i][len_DC + len_PC + len_S + k+1]
			policytree = copy.deepcopy(policytree0)

			agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
			self.preference_update(agent, unique_id)  # updating the issue tree preferences
			self.grid.position_agent(agent, (x, y))
			self.schedule.add(agent)

			# update of the standard inputs
			x += 1
			unique_id += 1

			j += 1

		# creation of the policy entrepreneurs
		jj = 0
		while jj < SM_PEs_aff[i]:
			agent_type = 'policyentrepreneur'
			affiliation = i
			resources = resources_aff[i]
			issuetree = copy.deepcopy(issuetree0)
			# introducing the issues
			for k in range(len_DC + len_PC + len_S):
				issuetree[unique_id][k] = [0, belief_profiles[i][k+1], 0]
			# introduction of the causal relations
			for k in range(len_DC*len_PC + len_PC * len_S):
				issuetree[unique_id][len_DC + len_PC + len_S + k][0] = belief_profiles[i][len_DC + len_PC + len_S + k+1]
			policytree = copy.deepcopy(policytree0)

			agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
			self.preference_update(agent, unique_id)  # updating the issue tree preferences
			self.grid.position_agent(agent, (x, y))
			self.schedule.add(agent)

			# update of the standard inputs
			x += 1
			y += 1
			unique_id += 1

			jj += 1

		# creation of the external parties
		jjj = 0
		while jjj < SM_EPs_aff[i]:
			agent_type = 'externalparty'
			affiliation = i
			resources = resources_aff[i]
			issuetree = copy.deepcopy(issuetree0)
			# introducing the issues
			for k in range(len_DC + len_PC + len_S):
				issuetree[unique_id][k] = [0, belief_profiles[i][k+1], 0]
			# introduction of the causal relations
			for k in range(len_DC*len_PC + len_PC * len_S):
				issuetree[unique_id][len_DC + len_PC + len_S + k][0] = belief_profiles[i][len_DC + len_PC + len_S + k+1]
			policytree = copy.deepcopy(policytree0)

			agent = ActiveAgent((x, y), unique_id, self, agent_type, resources, affiliation, issuetree, policytree)
			self.preference_update(agent, unique_id)  # updating the issue tree preferences
			self.grid.position_agent(agent, (x, y))
			self.schedule.add(agent)

			# update of the standard inputs
			x += 1
			y += 1
			unique_id += 1

			jjj += 1

	# check of the agents
	# for agent in self.schedule.agent_buffer(shuffled=False):
	# 		if isinstance(agent, ActiveAgent):
	# 			print(agent.unique_id, agent.agent_type, agent.affiliation, agent.resources, agent.issuetree[agent.unique_id])

def init_electorate_agents(self, len_S, len_PC, len_DC, SM_inputs):

	# model issue tree structure
	# the format for the whole issue tree is given as:
	# [issuetree] = [DC1, ...,DCn,PC1,..,PCn,S1,...,Sn]
	# This only contains the goals of the electorate.
	issuetree0 = [0 for f in range(len_DC + len_PC + len_S)]

	aff_number = len(SM_inputs[6])
	representativeness_aff = SM_inputs[7]

	# loading the belief profiles
	belief_input = pd.read_csv('input_beliefProfiles', sep=',')
	belief_profiles = []
	for i in range(aff_number*2):
		belief_profiles.append(belief_input.iloc[i].tolist())

	# creation of the agents
	# electorate 1
	x = 11
	y = 0
	unique_id = 100
	affiliation = 0
	representativeness = representativeness_aff[0]
	issuetree = copy.deepcopy(issuetree0)
	# issue goals
	for i in range(len_DC + len_PC + len_S):
		issuetree[i] = belief_profiles[aff_number][i+1]
	agent = ElectorateAgent((x, y), unique_id, self, affiliation, issuetree, representativeness)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	# electorate 2
	x = 11
	y = 1
	unique_id = 101
	affiliation = 1
	representativeness = representativeness_aff[1]
	issuetree = copy.deepcopy(issuetree0)
	# issue goals
	for i in range(len_DC + len_PC + len_S):
		issuetree[i] = belief_profiles[aff_number+1][i+1]
	agent = ElectorateAgent((x, y), unique_id, self, affiliation, issuetree, representativeness)
	self.grid.position_agent(agent, (x, y))
	self.schedule.add(agent)

	if aff_number == 3:
		x = 11
		y = 2
		unique_id = 102
		affiliation = 3
		representativeness = representativeness_aff[2]
		issuetree = copy.deepcopy(issuetree0)
		# issue goals
		for i in range(len_DC + len_PC + len_S):
			issuetree[i] = belief_profiles[aff_number+2][i+1]
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