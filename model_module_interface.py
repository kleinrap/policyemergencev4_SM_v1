

def policy_instrument_input(self, len_ins_1, len_ins_2, len_ins_exo):

	'''
	This is the function that is used to insert the policy instruments into the model
	'''

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

	return policy_instruments