import pandas as pd
import matplotlib.pyplot as plt
import ast


experiment_chosen = [0, 1, 2, 3, 4, 5]

for ip in experiment_chosen:

	experiment_number = ip
	print('experiment_number: ' + str(experiment_number))

	agent_studied = [12, 13]

	for agents in agent_studied:

		print('Agent: ' + str(agents))

		ticks_Bplus = []
		trust_Bplus = []

		ticks_3S = []
		trust_3S = []

		ticks_ACF = []
		trust_ACF = []

		possible_links = 29

		for i in range(possible_links):
			trust_Bplus.append([])
			trust_ACF.append([])


		total_runs_B = 50
		total_runs_Bplus = 2
		total_runs_3S = 0
		total_runs_ACF = 9

		df_test_Bplus = pd.read_csv('2_links_B+_event1_' + str(experiment_number) + '.csv')

		# df_test_3S = pd.read_csv('2_links_3S_event1_' + str(experiment_number) + '.csv')

		df_test_ACF = pd.read_csv('2_links_ACF_event1_' + str(experiment_number) + '.csv')

		ij = 0
		for index, row in df_test_Bplus.iterrows():
			ticks_Bplus.append(index)
			if row['Agent1'] == ('Policy entrepreneur: ' + str(agents)) or row['Agent2'] == ('Policy entrepreneur: ' + str(agents)):
			# if row['Agent1'] == ('Policy maker: ' + str(agents)) or row['Agent2'] == ('Policy maker: ' + str(agents)):
				trust_Bplus[ij].append(row['Agent3'])
				ij += 1
				if ij > possible_links - 1:
					ij = 0

		# ij = 0
		# for index, row in df_test_3S.iterrows():
		# 	ticks_3S.append(index)
		# 	if row['Agent1'] == ('Policy maker: ' + str(agents)) or row['Agent2'] == ('Policy maker: ' + str(agents)):
		# 		trust_3S[ij].append(row['Agent3'])
		# 		ij += 1
		# 		if ij > possible_links - 1:
		# 			ij = 0

		ij = 0
		for index, row in df_test_ACF.iterrows():
			if row['Agent1'] == ('Policy entrepreneur: ' + str(agents)) or row['Agent2'] == ('Policy entrepreneur: ' + str(agents)):
			# if row['Agent1'] == ('Policy maker: ' + str(agents)) or row['Agent2'] == ('Policy maker: ' + str(agents)):
				trust_ACF[ij].append(row['Agent3'])
				ij += 1
				if ij > possible_links - 1:
					ij = 0

		f, axarr = plt.subplots(1, 3, figsize=(11,3.5))

		for p in range(possible_links):
			axarr[0].plot(trust_Bplus[p], linewidth=1)
		axarr[0].set_title('Backbone+')
		axarr[0].set_xlim([0, 500])
		axarr[0].set_ylim([-1, 1])
		axarr[0].grid(True)
		axarr[0].axes.get_yaxis().set_ticklabels([])

		# for p in range(possible_links):
		# 	axarr[0].plot(trust_3S[p], linewidth=1)
		axarr[1].set_title('Three streams')
		axarr[1].set_xlim([0, 500])
		axarr[1].set_ylim([-1, 1])
		axarr[1].grid(True)
		axarr[1].axes.get_yaxis().set_ticklabels([])

		for p in range(possible_links):
			axarr[2].plot(trust_ACF[p], linewidth=1)
		axarr[2].set_title('ACF')
		axarr[2].set_xlim([0, 500])
		axarr[2].set_ylim([-1, 1])
		axarr[2].grid(True)
		axarr[2].axes.get_yaxis().set_ticklabels([])
		f.savefig('Links_Agent_' + str(agents) + '_E0_' + str(experiment_number) + '.png')








