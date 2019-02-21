'''
This file is a large input file for all the parameters and inputs related to the module interface that are used to populate the policy emergence model.
'''


def issue_tree_input(self):

	'''
	This is the function that is used to create the structure of the issue tree.
	'''

	# input of the issue tree
	len_S_names = ["movement0", "movement1", "happy0", "happy1"]  # secondary issues names
	len_PC_names = ["movement", "happiness"]  # policy core issues names
	len_DC_names = ["evenness"]  # deep core issues names

	len_S = len(len_S_names)
	len_PC = len(len_PC_names)
	len_DC = len(len_DC_names)
	len_CR = len_DC*len_PC + len_PC*len_S

	return len_S, len_PC, len_DC, len_CR

def policy_instrument_input(self, len_PC):

	'''
	This is the function that is used to insert the policy instruments into the model. This function can be changed for new policy instruments designed by the modeller
	'''
 
	len_PF = len_PC
	len_ins_1_names = ["Mo-5", "Mo+5", "LMo-1", "LMo+1"]  # PI related to PF 1
	len_ins_2_names = ["T0P-5", "T0P+5", "T1P-5", "T1P+5"]  # PI related to PF 2
	len_ins_all_names = ["Vi-1", "Vi+1", "None"]  # PI related to all families
	len_ins_exo_names = ["Vi", "Mo", "LMo", "T0P", "T1P"]  # exogenous parameter abbreviations
	
	len_ins_1 = len(len_ins_1_names)
	len_ins_2 = len(len_ins_2_names)
	len_ins_all = len(len_ins_all_names)
	len_ins_exo = len(len_ins_exo_names)


	# Introducing the policy instrument impact on the system
	policy_instruments = [0 for f in range(len_ins_1+len_ins_2+len_ins_all)]
	for m in range(len_ins_1+len_ins_2):
		policy_instruments[m] = [0 for f in range(len_ins_exo)]
	
	policy_instruments[0] = [None, -0.05, None, None, None]  # PI1.1 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[1] = [None, +0.05, None, None, None]  # PI1.2 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[2] = [None, None, -1, None, None]  # PI1.3 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[3] = [None, None, +1, None, None]  # PI1.4 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[4] = [None, None, None,-0.05, None]  # PI2.1 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[5] = [None, None, None, +0.05, None]  # PI2.2 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[6] = [None, None, None, None, -0.05]  # PI2.3 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[7] = [None, None, None, None, +0.05]  # PI2.4 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[8] = [-1, None, None, None, None]  # PIA.1 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[9] = [+1, None, None, None, None]  # PI2.2 - Vi,Mo,LMo,T0P,T1P
	# the no policy option is always presented to the agents as the last instrument
	policy_instruments[10] = [None, None, None, None, None]  # PINone - Vi,Mo,LMo,T0P,T1P

	return policy_instruments, len_ins_1, len_ins_2, len_ins_all

	# issue_mapping([S], [PC], [DC], type0agents, type1agents)

def issue_mapping_zeroOne(S_issues, PC_issues, DC_issues, type0agents, type1agents):

	'''
	This function takes the KPIs and transforms them onto an interval of 0 to 1 for the agent beliefs and other applications within the model.
	'''

	# secondary issues
	# S1 conversion - movement type 0 agents
	S1_min = 0
	S1_max = type0agents
	S1 = round(S_issues[0]/(S1_max - S1_min), 3)

	# S2 conversion - movement type 1 agents
	S2_min = 0
	S2_max = type1agents
	S2 = round(S_issues[1]/(S2_max - S2_min), 3)
	
	# S3 conversion - happiness type 0 agents
	S3_min = 0
	S3_max = type0agents
	S3 = round(S_issues[2]/(S3_max - S3_min), 3)

	# S4 conversion - happiness type 1 agents
	S4_min = 0
	S4_max = type1agents
	S4 = round(S_issues[3]/(S4_max - S4_min), 3)

	# PC1 conversion - movement of all agents
	PC1_min = 0
	PC1_max = type0agents + type1agents
	PC1 = round(PC_issues[0]/(PC1_max - PC1_min), 3)

	# PC2 conversion - happiness of all agents
	PC2_min = 0
	PC2_max = type0agents + type1agents
	PC2 = round(PC_issues[1]/(PC2_max - PC2_min), 3)

	# DC conversion - evenness
	DC1_min = 0  # miminum value of evenness (by definition)
	DC1_max = 1  # maximum value of evenness (by definition)
	DC1 = round(DC_issues[0]/(DC1_max - DC1_min), 3)

	return S1, S2, S3, S4, PC1, PC2, DC1

def issue_mapping_minusOneOne(S_issues, PC_issues, DC_issues, type0agents, type1agents):

	'''
	This function takes the KPIs and transforms them onto an interval of -1 to 1 for the agent beliefs and other applications within the model. It uses the function issue_mapping_zeroOne as a piggy back to calculate this
	'''

	S1, S2, S3, S4, PC1, PC2, DC1 = issue_mapping_zeroOne(S_issues, PC_issues, DC_issues, type0agents, type1agents)

	# secondary issues
	# S1 conversion - movement type 0 agents
	S1 = round((2 * S1) - 1, 3)

	# S2 conversion - movement type 1 agents
	S2_min = 0
	S2_max = type1agents
	S2 = round((2 * S2) - 1, 3)
	
	# S3 conversion - happiness type 0 agents
	S3 = round((2 * S3) - 1, 3)

	# S4 conversion - happiness type 1 agents
	S4 = round((2 * S4) - 1, 3)

	# PC1 conversion - movement of all agents
	PC1 = round((2 * PC1) - 1, 3)

	# PC2 conversion - happiness of all agents
	PC2 = round((2 * PC2) - 1, 3)

	# DC conversion - evenness
	DC1 = round((2 * DC1) - 1, 3)

	return S1, S2, S3, S4, PC1, PC2, DC1