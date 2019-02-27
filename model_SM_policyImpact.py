from model_module_interface import issue_mapping
from model_SM_agents import TruthAgent
import copy

def policy_impact_evaluation(model_run_SM, model_run_schelling, IssueInit, interval_tick):

	'''
	[Change policy tree/policy instruments -> Change in this function]
	This function is used to estimate the impact of the policy instruments and likelihood of impact of the policy families.

	'''
	# policy impact evaluation
	# initialisation of the vector that will store the KPIs of the mock simulation for each policy instrument
	issues = [0 for l in range(model_run_SM.len_S + model_run_SM.len_PC + model_run_SM.len_DC)]
	for q in range(model_run_SM.len_S + model_run_SM.len_PC + model_run_SM.len_DC):
		issues[q] = [0 for l in range(len(model_run_SM.policy_instruments))]

	# simulating all policy instruments for n ticks to obtain KPIs at the final state
	for j in range(len(model_run_SM.policy_instruments)):
		# copy of the model in its current state
		model_run_schelling_PI_test = copy.deepcopy(model_run_schelling)

		# run the simulation with policy introduced and collect data
		policy = model_run_SM.policy_instruments[j]  # set policy vector for one step
		for k in range(interval_tick):
			IssueE, type0agents, type1agents = model_run_schelling_PI_test.step(policy)
			policy = [None for f in range(len(model_run_SM.policy_instruments[j]))]  # reset policy vector after it has been implemented once

		# mapping the outcomes to a [0,1] interval
		IssueE = issue_mapping(IssueE, type0agents, type1agents)

		# store the final state of the belief (last simulation)
		for p in range(model_run_SM.len_S + model_run_SM.len_PC + model_run_SM.len_DC):
			issues[p][j] = IssueE[p]

	# change the policy tree accordingly
	# transforming initial KPIs to [0,1] interval
	IssueInit = issue_mapping(IssueInit, type0agents, type1agents)

	# looking at one policy instrument after the other
	impact_policy = [[0 for l in range(model_run_SM.len_S+model_run_SM.len_PC)] for r in range(len(model_run_SM.policy_instruments))]
	for j in range(len(model_run_SM.policy_instruments)):

		# calculating the percentage change from no policy to a policy
		for q in range(model_run_SM.len_PC+model_run_SM.len_S):
			if issues[q][j] != 0:
				impact_policy[j][q] = round((IssueInit[model_run_SM.len_DC+q] - issues[q][j])/issues[q][j], 3)
			if issues[q][j] == 0 and IssueInit[model_run_SM.len_DC+q] == 0:
				impact_policy[j][q] = 0
			if issues[q][j] == 0 and IssueInit[model_run_SM.len_DC+q] != 0:
				impact_policy[j][q] = 1

		# selecting the agents of the main simulation
		for agent in model_run_SM.schedule.agent_buffer(shuffled=True):
			if isinstance(agent, TruthAgent):
				# updating the policy tree of the truth agent
				agent.policytree[model_run_SM.len_PC + j] = impact_policy[j][0:model_run_SM.len_S]
				# print("Policy instrument: ", j, " - \n", agent.policytree[model_run_SM.len_PC + j])

	# considering the policy families
	# policy family 1 (instruments: 0, 1, 2, 3, 8, 9, 10)
	# policy family 2 (instruments: 4, 5, 6, 7, 8, 9, 10)
	likelihood_PF1 = [0 for f in range(model_run_SM.len_PC)]
	len_PF1 = 7
	likelihood_PF2 = [0 for f in range(model_run_SM.len_PC)]
	len_PF2 = 7
	# average the absolute value of their impact per 
	for j in range(len(model_run_SM.policy_instruments)):
		# selecting only policy instruments related to policy family 1
		if j == 0 or j == 1 or j == 2 or j == 3 or j == 8 or j == 9 or j == 10:
			likelihood_PF1[0] += impact_policy[j][model_run_SM.len_S] / len_PF1
			likelihood_PF1[1] += impact_policy[j][model_run_SM.len_S+1] / len_PF1
		# selecting only policy instruments related to policy family 2
		if j == 4 or j == 5 or j == 6 or j == 7 or j == 8 or j == 9 or j == 10:
			likelihood_PF2[0] += impact_policy[j][model_run_SM.len_S] / len_PF2
			likelihood_PF2[1] += impact_policy[j][model_run_SM.len_S+1] / len_PF2

	# rounding values
	likelihood_PF1[0] = round(likelihood_PF1[0], 3)
	likelihood_PF1[1] = round(likelihood_PF1[1], 3)
	likelihood_PF2[0] = round(likelihood_PF2[0], 3)
	likelihood_PF2[1] = round(likelihood_PF2[1], 3)

	for agent in model_run_SM.schedule.agent_buffer(shuffled=True):
		if isinstance(agent, TruthAgent):
			# updating the policy tree of the truth agent
			agent.policytree[0] = likelihood_PF1
			agent.policytree[1] = likelihood_PF2
