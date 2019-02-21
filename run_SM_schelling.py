from model_schelling import Schelling
from model_SM import PolicyEmergenceSM
import matplotlib.pyplot as plt
import copy

from model_module_interface import issue_mapping_zeroOne
from model_SM_agents import TruthAgent

'''
The current architecture is used for test purposes.
Ultimately, the two models should be initialised and then their for loops should be intertwined.
'''

# 1 - policy emergence alone
# 2 - segregation alone
# 3 - both
run_type = 3

if run_type == 1:
	# running the policy emergence Simplest Model
	model_run_SM = PolicyEmergenceSM(10,10)

	for i in range(5):
		model_run_SM.step()

if run_type == 2:
	# running the Schelling model:
	model_run_schelling = Schelling(20, 20, 0.75, 0.4)

	for i in range(25):
		if model_run_schelling.happy != model_run_schelling.schedule.get_agent_count():
			print("Step: ", i)
			model_run_schelling.step()

if run_type == 3:

	# running parameters
	interval_tick = 2

	# initialisation of both models
	model_run_SM = PolicyEmergenceSM(10,10)
	model_run_schelling = Schelling(20, 20, 0.75, 0.4)


	print("\n")
	print("************************")
	print("Start of the simulation:", "\n")
	for i in range(3):

		# run the system once at the beginning of the simulation to obtain KPIs
		# this is also used as a warmup time
		if i == 0:
			policy_chosen = [None, None, None, None, None]
			for warmup_time in range(5):
				S1init, S2init, S3init, S4init, PC1init, PC2init, DC1init, type0agents, type1agents = model_run_schelling.step(policy_chosen)

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
				S1e, S2e, S3e, S4e, PC1e, PC2e, DC1e, type0agents, type1agents = model_run_schelling_PI_test.step(policy)
				policy = [None for f in range(len(model_run_SM.policy_instruments[j]))]  # reset policy vector after it has been implemented once

			# mapping the outcomes to a [0,1] interval
			S1e, S2e, S3e, S4e, PC1e, PC2e, DC1e = issue_mapping_zeroOne([S1e, S2e, S3e, S4e], [PC1e, PC2e], [DC1e], type0agents, type1agents)

			# store the final state of the belief (last simulation)
			issues[0][j], issues[1][j], issues[2][j], issues[3][j], issues[4][j], issues[5][j], issues[6][j] = S1e, S2e, S3e, S4e, PC1e, PC2e, DC1e

		# change the policy tree accordingly
		# transforming initial KPIs to [0,1] interval
		S1init, S2init, S3init, S4init, PC1init, PC2init, DC1init = issue_mapping_zeroOne([S1init, S2init, S3init, S4init], [PC1init, PC2init], [DC1init], type0agents, type1agents)
		Sinit = [S1init, S2init, S3init, S4init]

		# looking at one policy instrument after the other
		for j in range(len(model_run_SM.policy_instruments)):

			# calculating the percentage change from no policy to a policy
			impact_policy = [0 for l in range(model_run_SM.len_S)]
			for q in range(model_run_SM.len_S):
				# if there is a increase in value
				if Sinit[q] < issues[q][j]:
					impact_policy[q] = round(1 - (Sinit[q]/issues[q][j]), 3)
				# if there is a decrease in value
				if Sinit[q] > issues[q][j]:
					impact_policy[q] = round((issues[q][j]/Sinit[q]) - 1, 3)
				# if there is no increase or decrease
				if Sinit[q] == issues[q][j]:
					impact_policy[q] = 0

			# selecting the agents of the main simulation
			for agent in model_run_SM.schedule.agent_buffer(shuffled=True):
				if isinstance(agent, TruthAgent):
					# updating the policy tree of the truth agent
					agent.policytree[model_run_SM.len_PC + j] = impact_policy

			'''
			TO DO to complete the impact of policies:
			- Introduce policy impact to the active agents through the TruthAgent (in the agent class)
			- Move the policy impact evaluation entire part into a module interface file
			'''

		# running the policy emergence model
		policy_chosen = model_run_SM.step()

		# run of the segregation model for n ticks
		for p in range(interval_tick):
			S1init, S2init, S3init, S4init, PC1init, PC2init, DC1init, type0agents, type1agents = model_run_schelling.step(policy_chosen)
			policy_chosen = [None, None, None, None, None] # reset policy after it has been implemented once


	# printing the data obtained from the Schelling model
	dataPlot = model_run_schelling.datacollector.get_model_vars_dataframe()
	print(dataPlot)
	dataPlot.plot("step", "evenness")
	dataPlot.plot("step", ["happy", "happytype0", "happytype1"])
	dataPlot.plot("step", ["movement", "movementtype0", "movementtype1"])
	plt.show()