from model_schelling import Schelling
from model_SM import PolicyEmergenceSM
import matplotlib.pyplot as plt
import copy

from model_SM_policyImpact import policy_impact_evaluation
from model_module_interface import issue_mapping
from model_SM_agents import TruthAgent

'''
The architecture present here is to be used for performing experiments. A batch runner algorithm will be used such that a set of experiments can be run at the same time.
'''

# running parameters
run_tick = 50
interval_tick = 5
warmup_tick = interval_tick

# initialisation of both models
model_run_SM = PolicyEmergenceSM(10,10)

# parameters of the Schelling model
sch_height = 30  # height of the grid
sch_width = 30  # width of the grid
sch_density = 0.8  # agent percentage density on the grid
sch_minority_pc = 0.4  # percentage of type 1 agents compared to type 0
sch_homophilyType0 = 0.5  # homophily of type 0 agents
sch_homophilyType1 = 0.5  # homophily of type 1 agents
sch_movementQuota = 0.30  # initial movement quota
sch_happyCheckRadius = 5  # initial happiness check radius
sch_moveCheckRadius = 10  # initial movement check radius
sch_last_move_quota = 5  # initial last moment quota

# initialisation of the Schelling model
model_run_schelling = Schelling(sch_height, sch_width, sch_density, sch_minority_pc, sch_homophilyType0, sch_homophilyType1, sch_movementQuota, sch_happyCheckRadius, sch_moveCheckRadius, sch_last_move_quota)


print("\n")
print("************************")
print("Start of the simulation:", "\n")
for i in range(run_tick):

	print(" ")
	print("************************")
	print("Tick number: ", i)

	# warm up time
	# this is also used as a warmup time
	if i == 0:
		policy_chosen = [None for ite in range(len(model_run_SM.policy_instruments[0]))]
		for warmup_time in range(warmup_tick):
			IssueInit, type0agents, type1agents = model_run_schelling.step(policy_chosen)

	# policy impact evaluation
	policy_impact_evaluation(model_run_SM, model_run_schelling, IssueInit, interval_tick)

	# running the policy emergence model
	if i == 0:
		KPIs = issue_mapping(IssueInit, type0agents, type1agents)
	else:
		KPIs = issue_mapping(KPIs, type0agents, type1agents)
	policy_chosen = model_run_SM.step(KPIs)

	# run of the segregation model for n ticks
	for p in range(interval_tick):
		KPIs, type0agents, type1agents = model_run_schelling.step(policy_chosen)
		policy_chosen = [None for ite in range(len(model_run_SM.policy_instruments[0]))] # reset policy after it has been implemented once

# printing the data obtained from the Schelling model
dataPlot_Schelling_model = model_run_schelling.datacollector.get_model_vars_dataframe()
print("done - dataPlot_Schelling_model")
dataPlot_Schelling_agent = model_run_schelling.datacollector.get_agent_vars_dataframe()
print("done - dataPlot_Schelling_agent")
print(dataPlot_Schelling_model)
print(dataPlot_Schelling_agent)
dataPlot_Schelling_model.plot("step", "evenness")
dataPlot_Schelling_model.plot("step", ["happy", "happytype0", "happytype1"])
dataPlot_Schelling_model.plot("step", ["movement", "movementtype0", "movementtype1"])

dataPlot_SM_model = model_run_SM.datacollector.get_model_vars_dataframe()
dataPlot_SM_model.to_csv('Test_SM_model.csv')
print("done - dataPlot_SM_model")
dataPlot_SM_agents = model_run_SM.datacollector.get_agent_vars_dataframe()
print(dataPlot_SM_agents)
dataPlot_SM_agents.to_csv('Test_SM_agents.csv')

# plt.show()