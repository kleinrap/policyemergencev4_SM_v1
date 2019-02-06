import random
import copy

from mesa.space import MultiGrid
from schedule import RandomActivationByBreed
from technical_model import Technical_Model
from tree_cell import TreeCell
from datacollection import DataCollector

from agent import Policymakers, Electorate, Externalparties, Truth, Policyentres
from network_creation import PolicyNetworkLinks

def initial_values_exploration(inputs_dict, experiment_input, run_number, agent_inputs, AS_theory, PF_theory):

	if experiment_input[16][run_number] != False:
		inputs_dict["coalition_threshold"] = experiment_input[16][run_number]
	else:
		inputs_dict["coalition_threshold"] = 0.35

	if experiment_input[13][run_number] != False:
		inputs_dict["team_gap_threshold"] = experiment_input[13][run_number]
	else:
		inputs_dict["team_gap_threshold"] = 0.8
	if experiment_input[14][run_number] != False:
		inputs_dict["team_belief_problem_threshold"] = experiment_input[14][run_number]
	else:
		inputs_dict["team_belief_problem_threshold"] = 0.5
	if experiment_input[15][run_number] != False:
		inputs_dict["team_belief_policy_threshold"] = experiment_input[15][run_number]
	else:
		inputs_dict["team_belief_policy_threshold"] = 0.5


	agenda_as_issue = None
	agenda_instrument = None
	agenda_prob_3S = None
	agenda_poli_3S = None
	inputs_dict["Agenda_inputs"] = [agenda_as_issue, agenda_instrument, agenda_prob_3S, agenda_poli_3S]


	# Creating the canvas for the forest fire model
	inputs_dict["height"] = 100
	inputs_dict["width"] = 100

	# Technical model inputs
	instrument_campSites = 0.1
	instrument_planting = 0.1
	thin_burning_probability = 0.002
	firefighter_force = 0.1
	instrument_prevention = 0.02
	inputs_dict["technical_input"] = [instrument_campSites, instrument_planting, thin_burning_probability, firefighter_force, instrument_prevention]	

	# Agents inputs
	affiliation_number = 3 # CURRENTLY THIS NUMBER CANNOT BE CHANGED OR THE CODE WONT WORK
	# affiliation_weights = [0.75, 0.85, 0.95]
	affiliation_weights = [experiment_input[1][run_number], experiment_input[2][run_number], experiment_input[3][run_number]]
	inputs_dict["affiliation_input"] =  [affiliation_number, affiliation_weights]
	
	policymaker_number = agent_inputs[0]# 9
	policyentre_number = 3 * policymaker_number
	externalparties_number = agent_inputs[1] #15
	electorate_number = affiliation_number
	inputs_dict["total_agent_number"] =  [externalparties_number, policymaker_number, policyentre_number]


	# Belief tree structure inputs
	inputs_dict["deep_core"] = ["Pr1", "Pr2"]
	len_PC = len(inputs_dict["deep_core"])
	inputs_dict["mid_level"] = ["PC1", "PC2", "PC3"]
	len_ML = len(inputs_dict["mid_level"])
	inputs_dict["secondary"] = ["S1", "S2", "S3", "S4", "S5"]
	len_S = len(inputs_dict["secondary"])

	# Inputs for the external parties state selection:
	issues_number = len_PC + len_ML + len_S
	# 1 means that the external party will collect the information, 0 not
	# The number of lists used will depend on the number of external parties used
	# IMPORTANT NOTE - THE CODE IS MADE IN SUCH A WAY THAT ONLY THE SECONDARY ISSUES CAN BE NOT CONSIDERED
	# TO ALSO NOT CONSIDER THE DEEP AND POLICY CORE, SIGNIFICANT CHANGES WILL BE NEEDED IN THE PREFERENCE CALCULATIONS
	no_interest_states = [[1] for i in range(externalparties_number)]
	no_interest_states_empty = [1 for i in range(issues_number)]
	for p in range(externalparties_number):
		no_interest_states[p] = no_interest_states_empty
	# no_interest_states[0] = [1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
	# no_interest_states[1] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
	# no_interest_states[2] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
	# no_interest_states[3] = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
	# no_interest_states[4] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
	# no_interest_states[5] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
	# no_interest_states[6] = [1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
	# no_interest_states[7] = [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
	# no_interest_states[8] = [1, 1, 1, 1, 1, 0, 0, 1, 0, 1]
	# no_interest_states[9] = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
	# no_interest_states[10] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
	# no_interest_states[11] = [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
	inputs_dict["No_interest_states"] = no_interest_states

	# Policies inputs (three streams only)
	policies_number = 10
	policies_start = [0 for i in range(len_S)]
	policies = []
	for k in range(policies_number):
		policies.append(copy.copy(policies_start))
	# policy 1 - More forest size
	policies[0] = [0.5, 0, 0]
	# policy 2 - Less forest size
	policies[1] = [-0.5, 0, 0]
	# policy 3 - More tourism
	policies[2] = [0, 0.5, 0]
	# policy 4 - Less tourism
	policies[3] = [0, -0.5, 0]
	# policy 5 - More safety
	policies[4] = [0, 0, 0.5]
	# policy 6 - Less safety
	policies[5] = [0, 0, -0.5]
	inputs_dict["Policies"] = policies

	# Instruments inputs
	intstruments_number = 16
	instruments_start = [0 for i in range(len_S)]
	instruments = []
	for k in range(intstruments_number):
		instruments.append(copy.copy(instruments_start))
		# policy instrument 1 - More camp fires
	instruments[0] = [0.5, 0, 0, 0, 0]
	# policy instrument 2 - Less camp fires
	instruments[1] = [-0.5, 0, 0, 0, 0]
	# policy instrument 3 - More planting
	instruments[2] = [0, 0.5, 0, 0, 0]
	# policy instrument 4 - Less planting
	instruments[3] = [0, -0.5, 0, 0, 0]
	# policy instrument 5 - More monitoring
	instruments[4] = [0, 0, 0.5, 0, 0]
	# policy instrument 6 - Less monitoring
	instruments[5] = [0, 0, -0.5, 0, 0]
	# policy instrument 7 - More firefigthers
	instruments[6] = [0, 0, 0, 0.5, 0]
	# policy instrument 8 - Less firefigthers
	instruments[7] = [0, 0, 0, -0.5, 0]
	# policy instrument 9 - More prevention
	instruments[8] = [0, 0, 0, 0, 0.5]
	# policy instrument 10 - Less prevention
	instruments[9] = [0, 0, 0, 0, -0.5]
	# policy instrument 11
	instruments[10] = [0, 0.2, 0.3, 0, 0.5]
	# policy instrument 12
	instruments[11] = [0, -0.2, 0.3, 0, -0.5]
	# policy instrument 13
	instruments[12] = [-0.4, 0.5, 0.1, -0.9, -0.5]
	# policy instrument 14
	instruments[13] = [0.4, -0.5, -0.1, 0.9, 0.5]
	# policy instrument 15
	instruments[14] = [-0.8, 0, 0, 0.9, 0]
	# policy instrument 16
	instruments[15] = [0.8, 0, 0, -0.9, 0]

	inputs_dict["Instruments"] = instruments

	team_strategy = 1

	# Creation of the truth agent
	x = random.randrange(inputs_dict["width"])
	y = random.randrange(inputs_dict["height"])

	# Parameters inputs:
	grid = MultiGrid(inputs_dict["height"], inputs_dict["width"], torus=True)
	# technical_model = Technical_Model(len_PC, len_ML, len_S)

	# Derived inputs:
	total_agent_number = externalparties_number + policymaker_number + policyentre_number
	# For the truth agents
	belieftree_truth = [None for i in range(issues_number)]
	# For the electorate
	belieftree_electorate = [None for i in range(issues_number)]
	# For all other agents
	causalrelation_number = len_PC*len_ML + len_ML*len_S
	belieftree = [[None] for i in range(total_agent_number)]
	for i in range(len(belieftree)):
		# STATE - AIM - PREFERENCE for the issues and None - VALUE - NONE for the causal relations
		belieftree[i] = [[None, None, None] for i in range(len_PC + len_ML + len_S + causalrelation_number)]

	# Each of the active agent is assigned a unique ID
	unique_id = 0

	inputs_dict["Agents"] = []

	############################
	# Creation of the truth agent
	x = random.randrange(inputs_dict["width"])
	y = random.randrange(inputs_dict["height"])
	# print('Truth agent beliefs: ' + str(self.belieftree_truth))
	truthagent = Truth((x, y), belieftree_truth)
	# master_list.append(truthagent)
	inputs_dict["Agents"].append(truthagent)

	############################
	# Creation of the electorate

	# inputs_dict["representation"] = [0.2, 0.5, 0.3]

	inputs_dict["electorate_influence_coefficient"] = experiment_input[6][run_number]
	
	inputs_dict["representation"] = [experiment_input[4][run_number]/100, experiment_input[5][run_number]/100, 1 - (experiment_input[4][run_number]/100 + experiment_input[5][run_number]/100)]


	if sum(inputs_dict["representation"]) != 1 or len(inputs_dict["representation"]) != affiliation_number:
		print('There is a problem in the electorate representation calculation')
	for i in range(electorate_number):
		x = random.randrange(inputs_dict["width"])
		y = random.randrange(inputs_dict["height"])

		belieftree_electorate = [[None, None, None] for i in range(issues_number)] # self.belieftree_electorate
		affiliation = i
		# Creating the initial values for the belief tree per affiliation - Self aims
		if affiliation == 0:
			belieftree_electorate[0][1] = 0		# Pr1 - Economy
			belieftree_electorate[1][1] = 1	 	# Pr2 - Environment
			belieftree_electorate[2][1] = 1 		# PC1 - Forest size
			belieftree_electorate[3][1] = -0.6		# PC2 - Tourism
			belieftree_electorate[4][1] = 0.2		# PC3 - Safety
			belieftree_electorate[5][1] = -0.5		# S1 - Camp sites
			belieftree_electorate[6][1] = 0.9		# S2 - Planting
			belieftree_electorate[7][1] = 0.3		# S3 - Monitoring
			belieftree_electorate[8][1] = -0.4		# S4 - Firefighters
			belieftree_electorate[9][1] = -0.9		# S5 - Prevention
			for j in range(len(belieftree_electorate)):
				belieftree_electorate[j][1] = round(belieftree_electorate[j][1] + (random.random()/10) - 0.05, 5)
				belieftree_electorate[j][1] = one_minus_one_check(belieftree_electorate[j][1])
		if affiliation == 1:
			belieftree_electorate[0][1] = 1		# Pr1
			belieftree_electorate[1][1] = 0	 	# Pr2
			belieftree_electorate[2][1] = 0.5 		# PC1
			belieftree_electorate[3][1] = 1		# PC2
			belieftree_electorate[4][1] = -0.5		# PC3
			belieftree_electorate[5][1] = 0.9		# S1
			belieftree_electorate[6][1] = 0.1		# S2
			belieftree_electorate[7][1] = 0.8		# S3
			belieftree_electorate[8][1] = 1		# S4
			belieftree_electorate[9][1] = 0.3		# S5
			for j in range(len(belieftree_electorate)):
				belieftree_electorate[j][1] = round(belieftree_electorate[j][1] + (random.random()/10) - 0.05, 5)
				belieftree_electorate[j][1] = one_minus_one_check(belieftree_electorate[j][1])
		if affiliation == 2:
			belieftree_electorate[0][1] = 1		# Pr1
			belieftree_electorate[1][1] = 1	 	# Pr2
			belieftree_electorate[2][1] = 1		# PC1
			belieftree_electorate[3][1] = -0.7		# PC2
			belieftree_electorate[4][1] = 1		# PC3
			belieftree_electorate[5][1] = -0.9		# S1
			belieftree_electorate[6][1] = -0.2		# S2
			belieftree_electorate[7][1] = -1		# S3
			belieftree_electorate[8][1] = -1		# S4
			belieftree_electorate[9][1] = 0.75		# S5
			for j in range(len(belieftree_electorate)):
				belieftree_electorate[j][1] = round(belieftree_electorate[j][1] + (random.random()/10) - 0.05, 5)
				belieftree_electorate[j][1] = one_minus_one_check(belieftree_electorate[j][1])
		electorate = Electorate(run_number, (x, y), affiliation, belieftree_electorate, inputs_dict["representation"][i])
		# master_list.append(electorate)
		inputs_dict["Agents"].append(electorate)

	############################
	# Creation of the external parties
	for i in range(externalparties_number):
		x = random.randrange(inputs_dict["width"])
		y = random.randrange(inputs_dict["height"])
		agent_id = i
		affiliation = random.randrange(affiliation_number)
		# CURRENTLY THE BELIEF TREE DOES NOT CONTAIN THE KNOWLEDGE ABOUT THE OTHER AGENTS FOR THE EXTERNAL PARTIES

		# Creation of the total belief tree (number of agents + 1)
		belieftree = [None]
		# print(len(belieftree))
		# print('    ')
		# print('Initial belief tree: ' + str(belieftree))
		# Creation of the first part of the own belief tree containing the issues
		belieftree_empty_issues = [[None, 0, 0] for f in range(len_PC + len_ML + len_S)]
		# print('    ')
		# print('Issue belief tree: ' + str(belieftree_empty_issues))
		# print('    ')
		belieftree_full = belieftree_empty_issues
		# Addition at the end of the own belief tree for the causal relation beliefs
		for p in range(causalrelation_number):
			belieftree_full.append([0])
		# print('    ')
		# print('Full belief tree: ' + str(belieftree_full))
		# print('    ')
		# Placement of the own belief tree in the total belief tree as the first spot.
		belieftree[0] = belieftree_full
		# print('Total belief tree: ' + str(belieftree))
		# Creation of the simplified agent tree for other agents (partial knowledge part)
		
		# print(belieftree_empty_agents)
		# print('   ')
		# Addition of the simplified agent tree after the first spot in the total belief tree

		for r in range(total_agent_number):
			belieftree_empty_agents = [[None, None, None] for p in range(len_PC + len_ML + len_S)]
			for l in range(causalrelation_number):
				belieftree_empty_agents.append([None])
			belieftree.append(belieftree_empty_agents)
		# print('    ')
		# print(belieftree)

		# Creation of the policy belief tree
		belieftree_policy_structure1 = [None for f in range(len_ML)]
		belieftree_policy = []
		for ij in range(total_agent_number + 1):
			belieftree_policy_structure2 = []
			for pk in range(len(policies)):
				belieftree_policy_structure2.append(copy.copy(belieftree_policy_structure1))
			belieftree_policy.append(copy.copy(belieftree_policy_structure2))

		# Creation of the instrument belief tree
		belieftree_instrument_structure1 = [None for f in range(len_S)]
		belieftree_instrument = []
		for ij in range(total_agent_number + 1):
			belieftree_instrument_structure2 = []
			for pk in range(len(instruments)):
				belieftree_instrument_structure2.append(copy.copy(belieftree_instrument_structure1))
			belieftree_instrument.append(copy.copy(belieftree_instrument_structure2))
		# print('Instruments: ' + str(belieftree_instrument))
		# This is the case where the agents from:
		# affiliation 1 will have high aim beleif
		# affiliation 2 will have low aim beliefs (opposite)
		# affiliation 3 will have mild aim beleifs (random)
		if experiment_input[0][run_number] == 0:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				# resources = 1
				belieftree[0][0][1] = -0.8 		# Pr1 - Economy
				belieftree[0][1][1] = 0.7 		# Pr2 - Environment
				belieftree[0][2][1] = 1 		# PC1 - Forest Size
				belieftree[0][3][1] = -0.7		# PC2 - Tourism
				belieftree[0][4][1] = 0.8		# PC3 - Safety
				belieftree[0][5][1] = -0.7		# S1 - Camp sites
				belieftree[0][6][1] = 0.9		# S2 - Planting
				belieftree[0][7][1] = -0.7		# S3 - Monitoring
				belieftree[0][8][1] = -0.8		# S4 - Firefighters
				belieftree[0][9][1] = -0.9		# S5 - Prevention
				belieftree[0][10][0] = 0.9		# Pr1 - PC1
				belieftree[0][11][0] = 0.8		# Pr1 - PC2
				belieftree[0][12][0] = -0.7		# Pr1 - PC3
				belieftree[0][13][0] = 0.9		# Pr2 - PC1
				belieftree[0][14][0] = -0.9		# Pr2 - PC2
				belieftree[0][15][0] = 0.6		# Pr2 - PC3
				belieftree[0][16][0] = -0.6		# PC1 - S1
				belieftree[0][17][0] = 0.9		# PC1 - S2
				belieftree[0][18][0] = 0.6		# PC1 - S3
				belieftree[0][19][0] = 0.8		# PC1 - S4
				belieftree[0][20][0] = 0.7		# PC1 - S5
				belieftree[0][21][0] = 1		# PC2 - S1
				belieftree[0][22][0] = -0.6		# PC2 - S2
				belieftree[0][23][0] = -0.7		# PC2 - S3
				belieftree[0][24][0] = -0.8		# PC2 - S4
				belieftree[0][25][0] = -0.8		# PC2 - S5
				belieftree[0][26][0] = -0.6		# PC3 - S1
				belieftree[0][27][0] = 0		# PC3 - S2
				belieftree[0][28][0] = 0		# PC3 - S3
				belieftree[0][29][0] = 0.6		# PC3 - S4
				belieftree[0][30][0] = -0.8		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same beliefs but different (opposing for 1 and 2) causal relations
		if experiment_input[0][run_number] == 1:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				# resources = 1
				belieftree[0][0][1] = 1 		# Pr1 - Economy
				belieftree[0][1][1] = 1 		# Pr2 - Environment
				belieftree[0][2][1] = 1 		# PC1 - Forest Size
				belieftree[0][3][1] = 1			# PC2 - Tourism
				belieftree[0][4][1] = 1			# PC3 - Safety
				belieftree[0][5][1] = 1			# S1 - Camp sites
				belieftree[0][6][1] = 1			# S2 - Planting
				belieftree[0][7][1] = 1			# S3 - Monitoring
				belieftree[0][8][1] = 1			# S4 - Firefighters
				belieftree[0][9][1] = 1			# S5 - Prevention
				belieftree[0][10][0] = 1		# Pr1 - PC1
				belieftree[0][11][0] = 1		# Pr1 - PC2
				belieftree[0][12][0] = 1		# Pr1 - PC3
				belieftree[0][13][0] = 1		# Pr2 - PC1
				belieftree[0][14][0] = 1		# Pr2 - PC2
				belieftree[0][15][0] = 1		# Pr2 - PC3
				belieftree[0][16][0] = 1		# PC1 - S1
				belieftree[0][17][0] = 1		# PC1 - S2
				belieftree[0][18][0] = 1		# PC1 - S3
				belieftree[0][19][0] = 1		# PC1 - S4
				belieftree[0][20][0] = 1		# PC1 - S5
				belieftree[0][21][0] = 1		# PC2 - S1
				belieftree[0][22][0] = 1		# PC2 - S2
				belieftree[0][23][0] = 1		# PC2 - S3
				belieftree[0][24][0] = 1		# PC2 - S4
				belieftree[0][25][0] = 1		# PC2 - S5
				belieftree[0][26][0] = 1		# PC3 - S1
				belieftree[0][27][0] = 1		# PC3 - S2
				belieftree[0][28][0] = 1		# PC3 - S3
				belieftree[0][29][0] = 1		# PC3 - S4
				belieftree[0][30][0] = 1		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same causal relations but different (opposing for 1 and 2) beliefs
		if experiment_input[0][run_number] == 2:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				belieftree[0][0][1] = -1 		# Pr1 - Economy
				belieftree[0][1][1] = -1 		# Pr2 - Environment
				belieftree[0][2][1] = -1 		# PC1 - Forest Size
				belieftree[0][3][1] = -1		# PC2 - Tourism
				belieftree[0][4][1] = -1		# PC3 - Safety
				belieftree[0][5][1] = -1		# S1 - Camp sites
				belieftree[0][6][1] = -1		# S2 - Planting
				belieftree[0][7][1] = -1		# S3 - Monitoring
				belieftree[0][8][1] = -1		# S4 - Firefighters
				belieftree[0][9][1] = -1		# S5 - Prevention
				belieftree[0][10][0] = -1		# Pr1 - PC1
				belieftree[0][11][0] = -1		# Pr1 - PC2
				belieftree[0][12][0] = -1		# Pr1 - PC3
				belieftree[0][13][0] = -1		# Pr2 - PC1
				belieftree[0][14][0] = -1		# Pr2 - PC2
				belieftree[0][15][0] = -1		# Pr2 - PC3
				belieftree[0][16][0] = -1		# PC1 - S1
				belieftree[0][17][0] = -1		# PC1 - S2
				belieftree[0][18][0] = -1		# PC1 - S3
				belieftree[0][19][0] = -1		# PC1 - S4
				belieftree[0][20][0] = -1		# PC1 - S5
				belieftree[0][21][0] = -1		# PC2 - S1
				belieftree[0][22][0] = -1		# PC2 - S2
				belieftree[0][23][0] = -1		# PC2 - S3
				belieftree[0][24][0] = -1		# PC2 - S4
				belieftree[0][25][0] = -1		# PC2 - S5
				belieftree[0][26][0] = -1		# PC3 - S1
				belieftree[0][27][0] = -1		# PC3 - S2
				belieftree[0][28][0] = -1		# PC3 - S3
				belieftree[0][29][0] = -1		# PC3 - S4
				belieftree[0][30][0] = -1		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same causal relations but different (opposing for 1 and 2) beliefs
		if experiment_input[0][run_number] == 3:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				belieftree[0][0][1] = 0 		# Pr1 - Economy
				belieftree[0][1][1] = 0 		# Pr2 - Environment
				belieftree[0][2][1] = 0 		# PC1 - Forest Size
				belieftree[0][3][1] = 0			# PC2 - Tourism
				belieftree[0][4][1] = 0			# PC3 - Safety
				belieftree[0][5][1] = 0			# S1 - Camp sites
				belieftree[0][6][1] = 0			# S2 - Planting
				belieftree[0][7][1] = 0			# S3 - Monitoring
				belieftree[0][8][1] = 0			# S4 - Firefighters
				belieftree[0][9][1] = 0			# S5 - Prevention
				belieftree[0][10][0] = 0		# Pr1 - PC1
				belieftree[0][11][0] = 0		# Pr1 - PC2
				belieftree[0][12][0] = 0		# Pr1 - PC3
				belieftree[0][13][0] = 0		# Pr2 - PC1
				belieftree[0][14][0] = 0		# Pr2 - PC2
				belieftree[0][15][0] = 0		# Pr2 - PC3
				belieftree[0][16][0] = 0		# PC1 - S1
				belieftree[0][17][0] = 0		# PC1 - S2
				belieftree[0][18][0] = 0		# PC1 - S3
				belieftree[0][19][0] = 0		# PC1 - S4
				belieftree[0][20][0] = 0		# PC1 - S5
				belieftree[0][21][0] = 0		# PC2 - S1
				belieftree[0][22][0] = 0		# PC2 - S2
				belieftree[0][23][0] = 0		# PC2 - S3
				belieftree[0][24][0] = 0		# PC2 - S4
				belieftree[0][25][0] = 0		# PC2 - S5
				belieftree[0][26][0] = 0		# PC3 - S1
				belieftree[0][27][0] = 0		# PC3 - S2
				belieftree[0][28][0] = 0		# PC3 - S3
				belieftree[0][29][0] = 0		# PC3 - S4
				belieftree[0][30][0] = 0		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		resources = [0, 0] # Initial resources, current resources
		if affiliation == 0:
			network_strategy = 2
		if affiliation == 1 or affiliation == 2:
			network_strategy = 1
		# print('   ')
		# print('Original Belief Tree: ')
		# print(belieftree)
		select_as_issue = None
		select_pinstrument = None
		select_issue_3S_as = None
		select_problem_3S_as = None
		select_policy_3S_as = None
		select_issue_3S_pf = None
		select_problem_3S_pf = None
		select_policy_3S_pf = None
		# The creation of the instrument preference array includes the presence of other agents (partial knowledge)
		instrument_preferences_base = [0 for h in range(len(instruments))]
		instrument_preferences = [instrument_preferences_base]
		for _ in range(total_agent_number):
			instrument_preferences.append(copy.copy(instrument_preferences_base))
		# team_strategy 0 is all agents, 1 is minimum amount of agents
		team = [None, None, team_strategy] # starting with no team (as and pf)
		coalition = [None, None]
		externalparty = Externalparties(run_number, agent_id, unique_id, (x, y), network_strategy, affiliation, resources, \
			belieftree, instrument_preferences, belieftree_policy, belieftree_instrument, select_as_issue, select_pinstrument, \
			select_issue_3S_as, select_problem_3S_as, select_policy_3S_as, select_issue_3S_pf, select_problem_3S_pf, select_policy_3S_pf, team, copy.copy(team), coalition, copy.copy(coalition))
		# print(externalparty.unique_id)
		unique_id += 1
		# print('These are the resources of this external party: ' + str(externalparty.resources))
		# master_list.append(externalparty)
		# agent_action_list.append(externalparty)
		inputs_dict["Agents"].append(externalparty)

	############################
	# Creation of the policy makers
	for i in range(policymaker_number):
		agent_id = i
		x = random.randrange(inputs_dict["width"])
		y = random.randrange(inputs_dict["height"])
		affiliation = random.randrange(affiliation_number)
		# Belief tree:
		belieftree = [None]
		belieftree_empty_issues = [[0, 0, 0] for f in range(len_PC + len_ML + len_S)]
		belieftree_full = belieftree_empty_issues
		for p in range(causalrelation_number):
			belieftree_full.append([0])
		belieftree[0] = belieftree_full
		for r in range(total_agent_number):
			belieftree_empty_agents = [[None, None, None] for p in range(len_PC + len_ML + len_S)]
			for l in range(causalrelation_number):
				belieftree_empty_agents.append([None])
			belieftree.append(belieftree_empty_agents)

		# Creation of the policy belief tree
		belieftree_policy_structure1 = [None for f in range(len_ML)]
		belieftree_policy = []
		for ij in range(total_agent_number + 1):
			belieftree_policy_structure2 = []
			for pk in range(len(policies)):
				belieftree_policy_structure2.append(copy.copy(belieftree_policy_structure1))
			belieftree_policy.append(copy.copy(belieftree_policy_structure2))

		# Creation of the instrument belief tree
		belieftree_instrument_structure1 = [None for f in range(len_S)]
		belieftree_instrument = []
		for ij in range(total_agent_number + 1):
			belieftree_instrument_structure2 = []
			for pk in range(len(instruments)):
				belieftree_instrument_structure2.append(copy.copy(belieftree_instrument_structure1))
			belieftree_instrument.append(copy.copy(belieftree_instrument_structure2))
		# print('Instruments: ' + str(belieftree_instrument))

		# Creating the initial values for the belief tree per affiliation
		# Aims of the actor itself:
			# This is the case where the agents from:
		# affiliation 1 will have high aim beleif
		# affiliation 2 will have low aim beliefs (opposite)
		# affiliation 3 will have mild aim beleifs (random)
		if experiment_input[0][run_number] == 0:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				# resources = 1
				belieftree[0][0][1] = -0.8 		# Pr1 - Economy
				belieftree[0][1][1] = 0.7 		# Pr2 - Environment
				belieftree[0][2][1] = 1 		# PC1 - Forest Size
				belieftree[0][3][1] = -0.7		# PC2 - Tourism
				belieftree[0][4][1] = 0.8		# PC3 - Safety
				belieftree[0][5][1] = -0.7		# S1 - Camp sites
				belieftree[0][6][1] = 0.9		# S2 - Planting
				belieftree[0][7][1] = -0.7		# S3 - Monitoring
				belieftree[0][8][1] = -0.8		# S4 - Firefighters
				belieftree[0][9][1] = -0.9		# S5 - Prevention
				belieftree[0][10][0] = 0.9		# Pr1 - PC1
				belieftree[0][11][0] = 0.8		# Pr1 - PC2
				belieftree[0][12][0] = -0.7		# Pr1 - PC3
				belieftree[0][13][0] = 0.9		# Pr2 - PC1
				belieftree[0][14][0] = -0.9		# Pr2 - PC2
				belieftree[0][15][0] = 0.6		# Pr2 - PC3
				belieftree[0][16][0] = -0.6		# PC1 - S1
				belieftree[0][17][0] = 0.9		# PC1 - S2
				belieftree[0][18][0] = 0.6		# PC1 - S3
				belieftree[0][19][0] = 0.8		# PC1 - S4
				belieftree[0][20][0] = 0.7		# PC1 - S5
				belieftree[0][21][0] = 1		# PC2 - S1
				belieftree[0][22][0] = -0.6		# PC2 - S2
				belieftree[0][23][0] = -0.7		# PC2 - S3
				belieftree[0][24][0] = -0.8		# PC2 - S4
				belieftree[0][25][0] = -0.8		# PC2 - S5
				belieftree[0][26][0] = -0.6		# PC3 - S1
				belieftree[0][27][0] = 0		# PC3 - S2
				belieftree[0][28][0] = 0		# PC3 - S3
				belieftree[0][29][0] = 0.6		# PC3 - S4
				belieftree[0][30][0] = -0.8		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same beliefs but different (opposing for 1 and 2) causal relations
		if experiment_input[0][run_number] == 1:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				# resources = 1
				belieftree[0][0][1] = 1 		# Pr1 - Economy
				belieftree[0][1][1] = 1 		# Pr2 - Environment
				belieftree[0][2][1] = 1 		# PC1 - Forest Size
				belieftree[0][3][1] = 1			# PC2 - Tourism
				belieftree[0][4][1] = 1			# PC3 - Safety
				belieftree[0][5][1] = 1			# S1 - Camp sites
				belieftree[0][6][1] = 1			# S2 - Planting
				belieftree[0][7][1] = 1			# S3 - Monitoring
				belieftree[0][8][1] = 1			# S4 - Firefighters
				belieftree[0][9][1] = 1			# S5 - Prevention
				belieftree[0][10][0] = 1		# Pr1 - PC1
				belieftree[0][11][0] = 1		# Pr1 - PC2
				belieftree[0][12][0] = 1		# Pr1 - PC3
				belieftree[0][13][0] = 1		# Pr2 - PC1
				belieftree[0][14][0] = 1		# Pr2 - PC2
				belieftree[0][15][0] = 1		# Pr2 - PC3
				belieftree[0][16][0] = 1		# PC1 - S1
				belieftree[0][17][0] = 1		# PC1 - S2
				belieftree[0][18][0] = 1		# PC1 - S3
				belieftree[0][19][0] = 1		# PC1 - S4
				belieftree[0][20][0] = 1		# PC1 - S5
				belieftree[0][21][0] = 1		# PC2 - S1
				belieftree[0][22][0] = 1		# PC2 - S2
				belieftree[0][23][0] = 1		# PC2 - S3
				belieftree[0][24][0] = 1		# PC2 - S4
				belieftree[0][25][0] = 1		# PC2 - S5
				belieftree[0][26][0] = 1		# PC3 - S1
				belieftree[0][27][0] = 1		# PC3 - S2
				belieftree[0][28][0] = 1		# PC3 - S3
				belieftree[0][29][0] = 1		# PC3 - S4
				belieftree[0][30][0] = 1		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same causal relations but different (opposing for 1 and 2) beliefs
		if experiment_input[0][run_number] == 2:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				belieftree[0][0][1] = -1 		# Pr1 - Economy
				belieftree[0][1][1] = -1 		# Pr2 - Environment
				belieftree[0][2][1] = -1 		# PC1 - Forest Size
				belieftree[0][3][1] = -1		# PC2 - Tourism
				belieftree[0][4][1] = -1		# PC3 - Safety
				belieftree[0][5][1] = -1		# S1 - Camp sites
				belieftree[0][6][1] = -1		# S2 - Planting
				belieftree[0][7][1] = -1		# S3 - Monitoring
				belieftree[0][8][1] = -1		# S4 - Firefighters
				belieftree[0][9][1] = -1		# S5 - Prevention
				belieftree[0][10][0] = -1		# Pr1 - PC1
				belieftree[0][11][0] = -1		# Pr1 - PC2
				belieftree[0][12][0] = -1		# Pr1 - PC3
				belieftree[0][13][0] = -1		# Pr2 - PC1
				belieftree[0][14][0] = -1		# Pr2 - PC2
				belieftree[0][15][0] = -1		# Pr2 - PC3
				belieftree[0][16][0] = -1		# PC1 - S1
				belieftree[0][17][0] = -1		# PC1 - S2
				belieftree[0][18][0] = -1		# PC1 - S3
				belieftree[0][19][0] = -1		# PC1 - S4
				belieftree[0][20][0] = -1		# PC1 - S5
				belieftree[0][21][0] = -1		# PC2 - S1
				belieftree[0][22][0] = -1		# PC2 - S2
				belieftree[0][23][0] = -1		# PC2 - S3
				belieftree[0][24][0] = -1		# PC2 - S4
				belieftree[0][25][0] = -1		# PC2 - S5
				belieftree[0][26][0] = -1		# PC3 - S1
				belieftree[0][27][0] = -1		# PC3 - S2
				belieftree[0][28][0] = -1		# PC3 - S3
				belieftree[0][29][0] = -1		# PC3 - S4
				belieftree[0][30][0] = -1		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same causal relations but different (opposing for 1 and 2) beliefs
		if experiment_input[0][run_number] == 3:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				belieftree[0][0][1] = 0 		# Pr1 - Economy
				belieftree[0][1][1] = 0 		# Pr2 - Environment
				belieftree[0][2][1] = 0 		# PC1 - Forest Size
				belieftree[0][3][1] = 0			# PC2 - Tourism
				belieftree[0][4][1] = 0			# PC3 - Safety
				belieftree[0][5][1] = 0			# S1 - Camp sites
				belieftree[0][6][1] = 0			# S2 - Planting
				belieftree[0][7][1] = 0			# S3 - Monitoring
				belieftree[0][8][1] = 0			# S4 - Firefighters
				belieftree[0][9][1] = 0			# S5 - Prevention
				belieftree[0][10][0] = 0		# Pr1 - PC1
				belieftree[0][11][0] = 0		# Pr1 - PC2
				belieftree[0][12][0] = 0		# Pr1 - PC3
				belieftree[0][13][0] = 0		# Pr2 - PC1
				belieftree[0][14][0] = 0		# Pr2 - PC2
				belieftree[0][15][0] = 0		# Pr2 - PC3
				belieftree[0][16][0] = 0		# PC1 - S1
				belieftree[0][17][0] = 0		# PC1 - S2
				belieftree[0][18][0] = 0		# PC1 - S3
				belieftree[0][19][0] = 0		# PC1 - S4
				belieftree[0][20][0] = 0		# PC1 - S5
				belieftree[0][21][0] = 0		# PC2 - S1
				belieftree[0][22][0] = 0		# PC2 - S2
				belieftree[0][23][0] = 0		# PC2 - S3
				belieftree[0][24][0] = 0		# PC2 - S4
				belieftree[0][25][0] = 0		# PC2 - S5
				belieftree[0][26][0] = 0		# PC3 - S1
				belieftree[0][27][0] = 0		# PC3 - S2
				belieftree[0][28][0] = 0		# PC3 - S3
				belieftree[0][29][0] = 0		# PC3 - S4
				belieftree[0][30][0] = 0		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# print(' ')
		# print(belieftree[0])
		if affiliation == 0:
			network_strategy = 2
		if affiliation == 1 or affiliation == 2:
			network_strategy = 1
		resources = [0, 0] # Initial resources, current resources
		select_as_issue = None
		select_pinstrument = None
		select_issue_3S_as = None
		select_problem_3S_as = None
		select_policy_3S_as = None
		select_issue_3S_pf = None
		select_problem_3S_pf = None
		select_policy_3S_pf = None
		# The creation of the instrument preference array includes the presence of other agents (partial knowledge)
		instrument_preferences_base = [0 for h in range(len(instruments))]
		instrument_preferences = [instrument_preferences_base]
		for _ in range(total_agent_number):
			instrument_preferences.append(copy.copy(instrument_preferences_base))
		# team_strategy 0 is all agents, 1 is minimum amount of agents
		team = [None, None, team_strategy] # starting with no team (as and pf)
		coalition = [None, None]
		policymaker = Policymakers(run_number, agent_id, unique_id, (x, y), network_strategy, affiliation, resources, belieftree, \
		 instrument_preferences, belieftree_policy, belieftree_instrument ,select_as_issue, select_pinstrument, \
		 select_issue_3S_as, select_problem_3S_as, select_policy_3S_as, select_issue_3S_pf, select_problem_3S_pf, select_policy_3S_pf, team, copy.copy(team), coalition, copy.copy(coalition))
		unique_id += 1
		# master_list.append(policymaker)
		# agent_action_list.append(policymaker)
		inputs_dict["Agents"].append(policymaker)

	############################
	# Creation of the policy entrepreneurs
	for i in range(policyentre_number):
		x = random.randrange(inputs_dict["width"])
		y = random.randrange(inputs_dict["height"])
		affiliation = random.randrange(affiliation_number)
		agent_id = i
		# Belief tree:
		belieftree = [None]
		belieftree_empty_issues = [[0, 0, 0] for f in range(len_PC + len_ML + len_S)]
		belieftree_full = belieftree_empty_issues
		for p in range(causalrelation_number):
			belieftree_full.append([0])
		belieftree[0] = belieftree_full
		for r in range(total_agent_number):
			belieftree_empty_agents = [[None, None, None] for p in range(len_PC + len_ML + len_S)]
			for l in range(causalrelation_number):
				belieftree_empty_agents.append([None])
			belieftree.append(belieftree_empty_agents)

		# Creation of the policy belief tree
		belieftree_policy_structure1 = [None for f in range(len_ML)]
		belieftree_policy = []
		for ij in range(total_agent_number + 1):
			belieftree_policy_structure2 = []
			for pk in range(len(policies)):
				belieftree_policy_structure2.append(copy.copy(belieftree_policy_structure1))
			belieftree_policy.append(copy.copy(belieftree_policy_structure2))

		# Creation of the instrument belief tree
		belieftree_instrument_structure1 = [None for f in range(len_S)]
		belieftree_instrument = []
		for ij in range(total_agent_number + 1):
			belieftree_instrument_structure2 = []
			for pk in range(len(instruments)):
				belieftree_instrument_structure2.append(copy.copy(belieftree_instrument_structure1))
			belieftree_instrument.append(copy.copy(belieftree_instrument_structure2))
		# print('Instruments: ' + str(belieftree_instrument))

		# Creating the initial values for the belief tree per affiliation
			# This is the case where the agents from:
		# affiliation 1 will have high aim beleif
		# affiliation 2 will have low aim beliefs (opposite)
		# affiliation 3 will have mild aim beleifs (random)
		if experiment_input[0][run_number] == 0:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				# resources = 1
				belieftree[0][0][1] = -0.8 		# Pr1 - Economy
				belieftree[0][1][1] = 0.7 		# Pr2 - Environment
				belieftree[0][2][1] = 1 		# PC1 - Forest Size
				belieftree[0][3][1] = -0.7		# PC2 - Tourism
				belieftree[0][4][1] = 0.8		# PC3 - Safety
				belieftree[0][5][1] = -0.7		# S1 - Camp sites
				belieftree[0][6][1] = 0.9		# S2 - Planting
				belieftree[0][7][1] = -0.7		# S3 - Monitoring
				belieftree[0][8][1] = -0.8		# S4 - Firefighters
				belieftree[0][9][1] = -0.9		# S5 - Prevention
				belieftree[0][10][0] = 0.9		# Pr1 - PC1
				belieftree[0][11][0] = 0.8		# Pr1 - PC2
				belieftree[0][12][0] = -0.7		# Pr1 - PC3
				belieftree[0][13][0] = 0.9		# Pr2 - PC1
				belieftree[0][14][0] = -0.9		# Pr2 - PC2
				belieftree[0][15][0] = 0.6		# Pr2 - PC3
				belieftree[0][16][0] = -0.6		# PC1 - S1
				belieftree[0][17][0] = 0.9		# PC1 - S2
				belieftree[0][18][0] = 0.6		# PC1 - S3
				belieftree[0][19][0] = 0.8		# PC1 - S4
				belieftree[0][20][0] = 0.7		# PC1 - S5
				belieftree[0][21][0] = 1		# PC2 - S1
				belieftree[0][22][0] = -0.6		# PC2 - S2
				belieftree[0][23][0] = -0.7		# PC2 - S3
				belieftree[0][24][0] = -0.8		# PC2 - S4
				belieftree[0][25][0] = -0.8		# PC2 - S5
				belieftree[0][26][0] = -0.6		# PC3 - S1
				belieftree[0][27][0] = 0		# PC3 - S2
				belieftree[0][28][0] = 0		# PC3 - S3
				belieftree[0][29][0] = 0.6		# PC3 - S4
				belieftree[0][30][0] = -0.8		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same beliefs but different (opposing for 1 and 2) causal relations
		if experiment_input[0][run_number] == 1:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				# resources = 1
				belieftree[0][0][1] = 1 		# Pr1 - Economy
				belieftree[0][1][1] = 1 		# Pr2 - Environment
				belieftree[0][2][1] = 1 		# PC1 - Forest Size
				belieftree[0][3][1] = 1			# PC2 - Tourism
				belieftree[0][4][1] = 1			# PC3 - Safety
				belieftree[0][5][1] = 1			# S1 - Camp sites
				belieftree[0][6][1] = 1			# S2 - Planting
				belieftree[0][7][1] = 1			# S3 - Monitoring
				belieftree[0][8][1] = 1			# S4 - Firefighters
				belieftree[0][9][1] = 1			# S5 - Prevention
				belieftree[0][10][0] = 1		# Pr1 - PC1
				belieftree[0][11][0] = 1		# Pr1 - PC2
				belieftree[0][12][0] = 1		# Pr1 - PC3
				belieftree[0][13][0] = 1		# Pr2 - PC1
				belieftree[0][14][0] = 1		# Pr2 - PC2
				belieftree[0][15][0] = 1		# Pr2 - PC3
				belieftree[0][16][0] = 1		# PC1 - S1
				belieftree[0][17][0] = 1		# PC1 - S2
				belieftree[0][18][0] = 1		# PC1 - S3
				belieftree[0][19][0] = 1		# PC1 - S4
				belieftree[0][20][0] = 1		# PC1 - S5
				belieftree[0][21][0] = 1		# PC2 - S1
				belieftree[0][22][0] = 1		# PC2 - S2
				belieftree[0][23][0] = 1		# PC2 - S3
				belieftree[0][24][0] = 1		# PC2 - S4
				belieftree[0][25][0] = 1		# PC2 - S5
				belieftree[0][26][0] = 1		# PC3 - S1
				belieftree[0][27][0] = 1		# PC3 - S2
				belieftree[0][28][0] = 1		# PC3 - S3
				belieftree[0][29][0] = 1		# PC3 - S4
				belieftree[0][30][0] = 1		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same causal relations but different (opposing for 1 and 2) beliefs
		if experiment_input[0][run_number] == 2:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				belieftree[0][0][1] = -1 		# Pr1 - Economy
				belieftree[0][1][1] = -1 		# Pr2 - Environment
				belieftree[0][2][1] = -1 		# PC1 - Forest Size
				belieftree[0][3][1] = -1		# PC2 - Tourism
				belieftree[0][4][1] = -1		# PC3 - Safety
				belieftree[0][5][1] = -1		# S1 - Camp sites
				belieftree[0][6][1] = -1		# S2 - Planting
				belieftree[0][7][1] = -1		# S3 - Monitoring
				belieftree[0][8][1] = -1		# S4 - Firefighters
				belieftree[0][9][1] = -1		# S5 - Prevention
				belieftree[0][10][0] = -1		# Pr1 - PC1
				belieftree[0][11][0] = -1		# Pr1 - PC2
				belieftree[0][12][0] = -1		# Pr1 - PC3
				belieftree[0][13][0] = -1		# Pr2 - PC1
				belieftree[0][14][0] = -1		# Pr2 - PC2
				belieftree[0][15][0] = -1		# Pr2 - PC3
				belieftree[0][16][0] = -1		# PC1 - S1
				belieftree[0][17][0] = -1		# PC1 - S2
				belieftree[0][18][0] = -1		# PC1 - S3
				belieftree[0][19][0] = -1		# PC1 - S4
				belieftree[0][20][0] = -1		# PC1 - S5
				belieftree[0][21][0] = -1		# PC2 - S1
				belieftree[0][22][0] = -1		# PC2 - S2
				belieftree[0][23][0] = -1		# PC2 - S3
				belieftree[0][24][0] = -1		# PC2 - S4
				belieftree[0][25][0] = -1		# PC2 - S5
				belieftree[0][26][0] = -1		# PC3 - S1
				belieftree[0][27][0] = -1		# PC3 - S2
				belieftree[0][28][0] = -1		# PC3 - S3
				belieftree[0][29][0] = -1		# PC3 - S4
				belieftree[0][30][0] = -1		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		# This is the case where the agents have the same causal relations but different (opposing for 1 and 2) beliefs
		if experiment_input[0][run_number] == 3:
			# Creating the initial values for the belief tree per affiliation - Self aims
			if affiliation == 0 or affiliation == 1 or affiliation == 2:
				belieftree[0][0][1] = 0 		# Pr1 - Economy
				belieftree[0][1][1] = 0 		# Pr2 - Environment
				belieftree[0][2][1] = 0 		# PC1 - Forest Size
				belieftree[0][3][1] = 0			# PC2 - Tourism
				belieftree[0][4][1] = 0			# PC3 - Safety
				belieftree[0][5][1] = 0			# S1 - Camp sites
				belieftree[0][6][1] = 0			# S2 - Planting
				belieftree[0][7][1] = 0			# S3 - Monitoring
				belieftree[0][8][1] = 0			# S4 - Firefighters
				belieftree[0][9][1] = 0			# S5 - Prevention
				belieftree[0][10][0] = 0		# Pr1 - PC1
				belieftree[0][11][0] = 0		# Pr1 - PC2
				belieftree[0][12][0] = 0		# Pr1 - PC3
				belieftree[0][13][0] = 0		# Pr2 - PC1
				belieftree[0][14][0] = 0		# Pr2 - PC2
				belieftree[0][15][0] = 0		# Pr2 - PC3
				belieftree[0][16][0] = 0		# PC1 - S1
				belieftree[0][17][0] = 0		# PC1 - S2
				belieftree[0][18][0] = 0		# PC1 - S3
				belieftree[0][19][0] = 0		# PC1 - S4
				belieftree[0][20][0] = 0		# PC1 - S5
				belieftree[0][21][0] = 0		# PC2 - S1
				belieftree[0][22][0] = 0		# PC2 - S2
				belieftree[0][23][0] = 0		# PC2 - S3
				belieftree[0][24][0] = 0		# PC2 - S4
				belieftree[0][25][0] = 0		# PC2 - S5
				belieftree[0][26][0] = 0		# PC3 - S1
				belieftree[0][27][0] = 0		# PC3 - S2
				belieftree[0][28][0] = 0		# PC3 - S3
				belieftree[0][29][0] = 0		# PC3 - S4
				belieftree[0][30][0] = 0		# PC3 - S5
				# Randomising the issues
				for j in range(len_PC + len_ML + len_S):
					belieftree[0][j][1] = round(belieftree[0][j][1] + (random.random()/10) - 0.05, 5)
					belieftree[0][j][1] = one_minus_one_check(belieftree[0][j][1])
				# Randomising the causal relations
				for q in range(causalrelation_number):
					belieftree[0][q + len_PC + len_ML + len_S][0] = round(belieftree[0][q + len_PC + len_ML + len_S][0] + (random.random()/10) - 0.05, 5)
					belieftree[0][q + len_PC + len_ML + len_S][0] = one_minus_one_check(belieftree[0][q + len_PC + len_ML + len_S][0])
				# Policies belief tree
				belieftree_policy[0][0][0] = 0.5
				belieftree_policy[0][0][1] = 0
				belieftree_policy[0][0][2] = 0
				belieftree_policy[0][1][0] = -0.5
				belieftree_policy[0][1][1] = 0
				belieftree_policy[0][1][2] = 0
				belieftree_policy[0][2][0] = 0
				belieftree_policy[0][2][1] = 0.5
				belieftree_policy[0][2][2] = 0
				belieftree_policy[0][3][0] = 0
				belieftree_policy[0][3][1] = -0.5
				belieftree_policy[0][3][2] = 0
				belieftree_policy[0][4][0] = 0
				belieftree_policy[0][4][1] = 0
				belieftree_policy[0][4][2] = 0.5
				belieftree_policy[0][5][0] = 0
				belieftree_policy[0][5][1] = 0
				belieftree_policy[0][5][2] = -0.5
				belieftree_policy[0][6][0] = 0
				belieftree_policy[0][6][1] = 0
				belieftree_policy[0][6][2] = -0.5
				belieftree_policy[0][7][0] = 0
				belieftree_policy[0][7][1] = 0
				belieftree_policy[0][7][2] = -0.5
				belieftree_policy[0][8][0] = 0
				belieftree_policy[0][8][1] = 0
				belieftree_policy[0][8][2] = -0.5
				belieftree_policy[0][9][0] = 0
				belieftree_policy[0][9][1] = 0
				belieftree_policy[0][9][2] = -0.5
				for q in range(len(policies)):
					for p in range(len_ML):
						belieftree_policy[0][q][p] = belieftree_policy[0][q][p] + (random.random()/10) - 0.05
						belieftree_policy[0][q][p] = one_minus_one_check(belieftree_policy[0][q][p])
				# Instruments belief tree
				belieftree_instrument[0][0][0] = 0.5
				belieftree_instrument[0][0][1] = 0
				belieftree_instrument[0][0][2] = 0
				belieftree_instrument[0][0][3] = 0
				belieftree_instrument[0][0][4] = 0
				belieftree_instrument[0][1][0] = -0.5
				belieftree_instrument[0][1][1] = 0
				belieftree_instrument[0][1][2] = 0
				belieftree_instrument[0][1][3] = 0
				belieftree_instrument[0][1][4] = 0
				belieftree_instrument[0][2][0] = 0
				belieftree_instrument[0][2][1] = 0.5
				belieftree_instrument[0][2][2] = 0
				belieftree_instrument[0][2][3] = 0
				belieftree_instrument[0][2][4] = 0
				belieftree_instrument[0][3][0] = 0
				belieftree_instrument[0][3][1] = -0.5
				belieftree_instrument[0][3][2] = 0
				belieftree_instrument[0][3][3] = 0
				belieftree_instrument[0][3][4] = 0
				belieftree_instrument[0][4][0] = 0
				belieftree_instrument[0][4][1] = 0
				belieftree_instrument[0][4][2] = 0.5
				belieftree_instrument[0][4][3] = 0
				belieftree_instrument[0][4][4] = 0
				belieftree_instrument[0][5][0] = 0
				belieftree_instrument[0][5][1] = 0
				belieftree_instrument[0][5][2] = -0.5
				belieftree_instrument[0][5][3] = 0
				belieftree_instrument[0][5][4] = 0
				belieftree_instrument[0][6][0] = 0
				belieftree_instrument[0][6][1] = 0
				belieftree_instrument[0][6][2] = 0
				belieftree_instrument[0][6][3] = 0.5
				belieftree_instrument[0][6][4] = 0
				belieftree_instrument[0][7][0] = 0
				belieftree_instrument[0][7][1] = 0
				belieftree_instrument[0][7][2] = 0
				belieftree_instrument[0][7][3] = -0.5
				belieftree_instrument[0][7][4] = 0
				belieftree_instrument[0][8][0] = 0
				belieftree_instrument[0][8][1] = 0
				belieftree_instrument[0][8][2] = 0
				belieftree_instrument[0][8][3] = 0
				belieftree_instrument[0][8][4] = 0.5
				belieftree_instrument[0][9][0] = 0
				belieftree_instrument[0][9][1] = 0
				belieftree_instrument[0][9][2] = 0
				belieftree_instrument[0][9][3] = 0
				belieftree_instrument[0][9][4] = -0.5
				belieftree_instrument[0][10][0] = 0
				belieftree_instrument[0][10][1] = 0.2
				belieftree_instrument[0][10][2] = 0.3
				belieftree_instrument[0][10][3] = 0
				belieftree_instrument[0][10][4] = 0.5
				belieftree_instrument[0][11][0] = 0
				belieftree_instrument[0][11][1] = -0.2
				belieftree_instrument[0][11][2] = -0.3
				belieftree_instrument[0][11][3] = 0
				belieftree_instrument[0][11][4] = -0.5
				belieftree_instrument[0][12][0] = -0.4
				belieftree_instrument[0][12][1] = 0.5
				belieftree_instrument[0][12][2] = 0.1
				belieftree_instrument[0][12][3] = -0.9
				belieftree_instrument[0][12][4] = -0.5
				belieftree_instrument[0][13][0] = 0.4
				belieftree_instrument[0][13][1] = -0.5
				belieftree_instrument[0][13][2] = -0.1
				belieftree_instrument[0][13][3] = 0.9
				belieftree_instrument[0][13][4] = 0.5
				belieftree_instrument[0][14][0] = -0.8
				belieftree_instrument[0][14][1] = 0
				belieftree_instrument[0][14][2] = 0
				belieftree_instrument[0][14][3] = 0.9
				belieftree_instrument[0][14][4] = 0
				belieftree_instrument[0][15][0] = 0.8
				belieftree_instrument[0][15][1] = 0
				belieftree_instrument[0][15][2] = 0
				belieftree_instrument[0][15][3] = -0.9
				belieftree_instrument[0][15][4] = 0
				for q in range(len(instruments)):
					for p in range(len_S):
						belieftree_instrument[0][q][p] = belieftree_instrument[0][q][p] + (random.random()/10) - 0.05
						belieftree_instrument[0][q][p] = one_minus_one_check(belieftree_instrument[0][q][p])
		resources = [0, 0] # Initial resources, current resources
		if affiliation == 0:
			network_strategy = 2
		if affiliation == 1 or affiliation == 2:
			network_strategy = 1
		select_as_issue = None
		select_pinstrument = None
		select_issue_3S_as = None
		select_problem_3S_as = None
		select_policy_3S_as = None
		select_issue_3S_pf = None
		select_problem_3S_pf = None
		select_policy_3S_pf = None
		# The creation of the instrument preference array includes the presence of other agents (partial knowledge)
		instrument_preferences_base = [0 for h in range(len(instruments))]
		instrument_preferences = [instrument_preferences_base]
		for _ in range( total_agent_number):
			instrument_preferences.append(copy.copy(instrument_preferences_base))
		# team_strategy 0 is all agents, 1 is minimum amount of agents
		team = [None, None, team_strategy] # starting with no team (as and pf)
		coalition = [None, None]
		policyentre = Policyentres(run_number, agent_id, unique_id, (x, y), network_strategy, affiliation, resources, belieftree, \
		 instrument_preferences, belieftree_policy, belieftree_instrument, select_as_issue, select_pinstrument, \
		 select_issue_3S_as, select_problem_3S_as, select_policy_3S_as, select_issue_3S_pf, select_problem_3S_pf, select_policy_3S_pf, team, copy.copy(team), coalition, copy.copy(coalition))
		# print('These are the resources of this policy entrepreneur: ' + str(policyentre.resources))
		unique_id += 1
		# master_list.append(policyentre)
		# agent_action_list.append(policyentre)
		inputs_dict["Agents"].append(policyentre)

	if experiment_input[7][run_number] != False:
		inputs_dict["resources_potency"] = experiment_input[7][run_number]
	else:
		inputs_dict["resources_potency"] = 1

	
	if experiment_input[8][run_number] != False:
		inputs_dict["resources_weight_action"] = experiment_input[8][run_number]
	else:
		inputs_dict["resources_weight_action"] = 0.1

	if experiment_input[10][run_number] != False and experiment_input[11][run_number] != False and experiment_input[12][run_number] != False:
		inputs_dict["conflict_level_coef"] = [experiment_input[10][run_number], experiment_input[11][run_number], experiment_input[12][run_number]]
	else:
		inputs_dict["conflict_level_coef"] = [0.75, 0.85, 0.95]


	# ############################
	# # Creation of the network
	# This is the actual creation of the network.
	inputs_dict["Link_list"] = []
	agent_action_list = []
	for agents in inputs_dict["Agents"]:
		if type(agents) == Policymakers or type(agents) == Policyentres or type(agents) == Externalparties:
			# print(agents)
			agent_action_list.append(agents)

	print('')

	if experiment_input[9][run_number] != False:
		inputs_dict["Trust_decay_coefficient"] = experiment_input[9][run_number]
	else:
		inputs_dict["Trust_decay_coefficient"] = 0.05


	conflict_level_1 = [[inputs_dict["conflict_level_coef"][1], inputs_dict["conflict_level_coef"][1]] for i in range(len_PC + len_ML + len_S + len_PC*len_ML + len_ML*len_S)]
	conflict_level_2 = [[inputs_dict["conflict_level_coef"][1], inputs_dict["conflict_level_coef"][1]] for i in range(len_PC + len_ML + len_S + len_PC*len_ML + len_ML*len_S)]
	conflict_level = [conflict_level_1, conflict_level_2]
	# print('*************')
	# print('This is the conflict level')
	# print(conflict_level)
	# print('*************')
	link_id = 0
	nw_test = 1
	for i in range(len(agent_action_list)):
		for j in range(len(agent_action_list) - nw_test):
			# print('(' + str(i) + ',' + str(j + nw_test) + ')')
			# Defining the aware level
			aware_check = random.random()
			if aware_check < 0.1 and (type(agent_action_list[i]) != Policymakers and type(agent_action_list[j + nw_test]) != Policymakers):
				aware = -1
			if aware_check < 0.5 and aware_check >= 0.1:
				aware = 0
			if aware_check >= 0.5:
				aware = random.random()

			policynetworklink = PolicyNetworkLinks(link_id, agent_action_list[i], agent_action_list[j + nw_test], aware, inputs_dict["Trust_decay_coefficient"], conflict_level)
			inputs_dict["Link_list"].append(policynetworklink)
			# link_list.append(policynetworklink)
			# print(policynetworklink)
			link_id += 1
		nw_test += 1
	# print(link_list)
	# print(len(self.link_list[PolicyNetworkLinks]))

	conflict_level_update(inputs_dict["Link_list"], len_PC, len_ML, len_S, inputs_dict["conflict_level_coef"])

	# print(' ')
	# print(inputs_dict)
	# print(' ')

	return inputs_dict

def one_minus_one_check(to_be_checked_parameter):

	checked_parameter = 0
	if to_be_checked_parameter > 1:
		checked_parameter = 1
	elif to_be_checked_parameter < -1:
		checked_parameter = -1
	else:
		checked_parameter = to_be_checked_parameter
	return checked_parameter

def add(self, agent):
	agent_class = type(agent)
	self.agent_action_dict[agent_class].append(agent)

def conflict_level_update(link_list, len_PC, len_ML, len_S, conflict_level_coef):

		"""
		The conflict level update function
		===========================

		The description here is currently missing.

		"""

		for links in link_list:
			# print(links)
			conflict_level_temp = copy.copy(links.conflict_level)
			for issues in range(len_PC + len_ML + len_S):
				# This is all based on partial knowledge
				# AGENT 1 - based on the partial knowledge he has of 
				# For the calculation of the state conflict level:

				# If one of the beliefs is known to be 'No' then assign 'No' to the conflict level
				if links.agent1.belieftree[1 + links.agent2.unique_id][issues][0] == 'No' or links.agent1.belieftree[0][issues][0] == 'No':
					links.conflict_level[0][issues][0] = 'No'
				# If there is no knowledge of the other agent's beliefs, the conflict level is set to 0.85 by default
				elif links.agent1.belieftree[1 + links.agent2.unique_id][issues][0] == None:
					links.conflict_level[0][issues][0] = conflict_level_coef[1]
				# If all beliefs are known, calculate the conflict level
				else:
					conflict_level_temp[0][issues][0] = abs(links.agent1.belieftree[0][issues][0] - links.agent1.belieftree[1 + links.agent2.unique_id][issues][0])
					if conflict_level_temp[0][issues][0] <= 0.25:
						links.conflict_level[0][issues][0] = conflict_level_coef[0]
					if conflict_level_temp[0][issues][0] > 0.25 and conflict_level_temp[0][issues][0] <= 1.75:
						links.conflict_level[0][issues][0] = conflict_level_coef[2]
					if conflict_level_temp[0][issues][0] > 1.75:
						links.conflict_level[0][issues][0] = conflict_level_coef[1]

				# For the calculation of the aim conflict level:
				if links.agent1.belieftree[1 + links.agent2.unique_id][issues][1] == 'No' or links.agent1.belieftree[0][issues][1] == 'No':
					links.conflict_level[0][issues][1] = 'No'
				elif links.agent1.belieftree[1 + links.agent2.unique_id][issues][1] == None:
					links.conflict_level[0][issues][1] = conflict_level_coef[1]
				else:
					conflict_level_temp[0][issues][1] = abs(links.agent1.belieftree[0][issues][1] - links.agent1.belieftree[1 + links.agent2.unique_id][issues][1])
					if conflict_level_temp[0][issues][1] <= 0.25:
						links.conflict_level[0][issues][1] = conflict_level_coef[0]
					if conflict_level_temp[0][issues][1] > 0.25 and conflict_level_temp[0][issues][1] <= 1.75:
						links.conflict_level[0][issues][1] = conflict_level_coef[2]
					if conflict_level_temp[0][issues][1] > 1.75:
						links.conflict_level[0][issues][1] = conflict_level_coef[1]
				
				# AGENT 2
				# For the calculation of the state conflict level:
				if links.agent2.belieftree[1 + links.agent1.unique_id][issues][0] == 'No' or links.agent2.belieftree[0][issues][0] == 'No':
					links.conflict_level[1][issues][0] = 'No'
				elif links.agent2.belieftree[1 + links.agent1.unique_id][issues][0] == None:
					links.conflict_level[1][issues][0] = conflict_level_coef[1]
				else:
					conflict_level_temp[1][issues][0] = abs(links.agent2.belieftree[0][issues][0] - links.agent2.belieftree[1 + links.agent1.unique_id][issues][0])
					if conflict_level_temp[1][issues][0] <= 0.25:
						links.conflict_level[1][issues][0] = conflict_level_coef[0]
					if conflict_level_temp[1][issues][0] > 0.25 and conflict_level_temp[1][issues][0] <= 1.75:
						links.conflict_level[1][issues][0] = conflict_level_coef[2]
					if conflict_level_temp[1][issues][0] > 1.75:
						links.conflict_level[1][issues][0] = conflict_level_coef[1]
				# For the calculation of the aim conflict level:
				if links.agent2.belieftree[1 + links.agent1.unique_id][issues][1] == 'No' or links.agent2.belieftree[0][issues][1] == 'No':
					links.conflict_level[1][issues][1] = 'No'
				elif links.agent2.belieftree[1 + links.agent1.unique_id][issues][1] == None:
					links.conflict_level[1][issues][1] = conflict_level_coef[1]
				else:
					conflict_level_temp[1][issues][1] = abs(links.agent2.belieftree[0][issues][1] - links.agent2.belieftree[1 + links.agent1.unique_id][issues][1])
					if conflict_level_temp[1][issues][1] <= 0.25:
						links.conflict_level[1][issues][1] = conflict_level_coef[0]
					if conflict_level_temp[1][issues][1] > 0.25 and conflict_level_temp[1][issues][1] <= 1.75:
						links.conflict_level[1][issues][1] = conflict_level_coef[2]
					if conflict_level_temp[1][issues][1] > 1.75:
						links.conflict_level[1][issues][1] = conflict_level_coef[1]
			# print(links.conflict_level)