from model_schelling import Schelling
from model_SM import PolicyEmergenceSM
import matplotlib.pyplot as plt
import copy

from model_module_interface import issue_mapping
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

		# policy impact evaluation
		issues = [0 for l in range(model_run_SM.len_S + model_run_SM.len_PC + model_run_SM.len_DC)]
		for q in range(model_run_SM.len_S + model_run_SM.len_PC + model_run_SM.len_DC):
			issues[q] = [0 for l in range(len(model_run_SM.policy_instruments))]
		
		for j in range(len(model_run_SM.policy_instruments)):
			# copy of the model in its current state
			model_run_schelling_PI_test = copy.deepcopy(model_run_schelling)

			# run the simulation with policy introduced and collect data
			for k in range(interval_tick):
				S1e, S2e, S3e, S4e, PC1e, PC2e, DC1e, type0agents, type1agents = model_run_schelling_PI_test.step(model_run_SM.policy_instruments[j])

			# store the final state of the belief (last simulation)
			issues[0][j], issues[1][j], issues[2][j], issues[3][j], issues[4][j], issues[5][j], issues[6][j] = S1e, S2e, S3e, S4e, PC1e, PC2e, DC1e

		# change the policy tree accordingly
		for j in range(len(model_run_SM.policy_instruments)-1):

			# calculating the percentage change from no policy to a policy
			impact_policy = [0 for l in range(model_run_SM.len_S)]
			for q in range(model_run_SM.len_S):
				if issues[0][j] != 0:
					impact_policy[q] = issues[0][-1]/issues[0][j] - 1
				else:
					impact_policy[q] = 0  # in case the denominator is 0

			# selecting the agents of the main simulation
			# updating the policy tree of the truth agent
			for agent in model_run_SM.schedule.agent_buffer(shuffled=True):
				if isinstance(agent, TruthAgent):
					agent.policytree[model_run_SM.len_PC + j][q] = impact_policy[q]		
					print(agent.policytree)

			'''
			TO DO to complete the impact of policies:
			- Implementation of the policy - changes in the Segregation model
			- Calculation of the beliefs on interval [-1, 1]
			- Calculate impact of the policies (for this, it needs to be compared to where the model would have been - or it needs to be compared to where the model is now?)
			- Introduce safeguards such that policy instruments that are forbideen (go over max or below min) are not introduced
			- Introduce policy impact to the active agents through the TruthAgent (in the agent class)
			- In the calculation of the impact, consider if the numerator is 0, what is the value that should be included then
			- Move the policy impact evaluation entire part into a module interface file
			'''


		policy = model_run_SM.step()
		policy = [None, None, None, None, None]
		for p in range(interval_tick):
			model_run_schelling.step(policy)


	# printing the data obtained from the Schelling model
	dataPlot = model_run_schelling.datacollector.get_model_vars_dataframe()
	print(dataPlot)
	dataPlot.plot("step", "evenness")
	dataPlot.plot("step", ["happy", "happytype0", "happytype1"])
	dataPlot.plot("step", ["movement", "movementtype0", "movementtype1"])
	plt.show()