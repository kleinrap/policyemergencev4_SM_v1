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
	len_ins_1_names = ["Vi-1", "Vi+1", "Mo-5", "Mo+5", "LMo-1", "LMo+1"]  # PI related to PF 1
	len_ins_2_names = ["Vi-1", "Vi+1", "T0P-5", "T0P+5", "T1P-5", "T1P+5"]  # PI related to PF 2
	len_ins_exo_names = ["Vi", "Mo", "LMo", "T0P", "T1P"]  # exogenous parameter abbreviations
	
	len_ins_1 = len(len_ins_1_names)
	len_ins_2 = len(len_ins_2_names)
	len_ins_exo = len(len_ins_exo_names)


	# Introducing the policy instrument impact on the system
	policy_instruments = [0 for f in range(len_ins_1+len_ins_2)]
	for m in range(len_ins_1+len_ins_2):
		policy_instruments[m] = [0 for f in range(len_ins_exo)]
	
	policy_instruments[0] = [-1, 0, 0, 0, 0]  # PI1.1 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[1] = [+1, 0, 0, 0, 0]  # PI1.2 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[2] = [0, -5, 0, 0, 0]  # PI1.3 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[3] = [0, +5, 0, 0, 0]  # PI1.4 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[4] = [0, 0, -1, 0, 0]  # PI1.5 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[5] = [0, 0, +1, 0, 0]  # PI1.6 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[6] = [-1, 0, 0, 0, 0]  # PI2.1 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[7] = [+1, 0, 0, 0, 0]  # PI2.2 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[8] = [0, 0, 0,-5, 0]  # PI2.3 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[9] = [0, 0, 0, +5, 0]  # PI2.4 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[10] = [0, 0, 0, 0, -5]  # PI2.5 - Vi,Mo,LMo,T0P,T1P
	policy_instruments[11] = [0, 0, 0, 0, +5]  # PI2.6 - Vi,Mo,LMo,T0P,T1P

	return policy_instruments, len_ins_1, len_ins_2