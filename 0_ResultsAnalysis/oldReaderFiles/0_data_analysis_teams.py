import pandas as pd
import matplotlib.pyplot as plt
import ast


# Check for the number of teams per step
# Check for the number of actors in teams per step

# experiment_chosen = [0, 1, 2, 3, 4, 5]

# for ip in experiment_chosen:

# 	experiment_number = ip
# 	print('experiment_number: ' + str(experiment_number))

total_runs = 30

teams_number_as = []
actors_in_teams_as = []
resources_as = []

teams_number_pf = []
actors_in_teams_pf = []
resources_pf = []

for file_number in range(total_runs):
	teams_number_as.append([0])
	actors_in_teams_as.append([0])
	resources_as.append([0])

	teams_number_pf.append([0])
	actors_in_teams_pf.append([0])
	resources_pf.append([0])


df_test_3S_as = []
df_test_3S_pf = []

for i in range(total_runs):
	df_test_3S_as.append(pd.read_csv('1_teams_as_3s_event2_' + str(i) + '.csv'))
	df_test_3S_pf.append(pd.read_csv('1_teams_pf_3S_event2_' + str(i) + '.csv'))


for file_number in range(total_runs):
	ij = 0
	for index, row in df_test_3S_as[file_number].iterrows():
		# Increase the number when the step has passed
		# print('ij: ' + str(ij))
		if row['Step'] != ij:
			ij += 1
			teams_number_as[file_number].append(0)
			actors_in_teams_as[file_number].append(0)
			resources_as[file_number].append(0)

		teams_number_as[file_number][ij] += 1
		resources_as[file_number][ij] += row['Resources']

		store1 = row['Members']
		store2 = eval(store1)
		actors_in_teams_as[file_number][ij] += len(store2)

for file_number in range(total_runs):
	ij = 0
	for index, row in df_test_3S_pf[file_number].iterrows():
		# Increase the number when the step has passed
		if row['Step'] != ij:
			ij += 1
			teams_number_pf[file_number].append(0)
			actors_in_teams_pf[file_number].append(0)
			resources_pf[file_number].append(0)

		teams_number_pf[file_number][ij] += 1
		resources_pf[file_number][ij] += row['Resources']

		store1 = row['Members']
		store2 = eval(store1)
		actors_in_teams_pf[file_number][ij] += len(store2)

# print(teams_number_as)
# print(actors_in_teams_as)
# print(' ')
# print(teams_number_pf)
# print(actors_in_teams_pf)

f, axarr = plt.subplots(1, 3, figsize=(11,3.5))

for file_number in range(total_runs):
	axarr[0].plot(teams_number_pf[file_number], 'r',  linewidth=0.5)
	axarr[0].plot(teams_number_as[file_number], 'k',  linewidth=0.5)
axarr[0].set_title('Number of teams')
axarr[0].set_xlim([0, 500])
# axarr[0].set_ylim([0, 30])
axarr[0].grid(True)

for file_number in range(total_runs):
	if file_number == 0:
		axarr[1].plot(actors_in_teams_as[file_number], 'k', linewidth=0.5, label='AS')
		axarr[1].plot(actors_in_teams_pf[file_number], 'r', linewidth=0.5, label='PF')
	else:
		axarr[1].plot(actors_in_teams_as[file_number], 'k', linewidth=0.5)
		axarr[1].plot(actors_in_teams_pf[file_number], 'r', linewidth=0.5)

axarr[1].set_title('Actors in teams')
axarr[1].set_xlim([0, 500])
# axarr[1].set_ylim([22, 31])
axarr[1].grid(True)
axarr[1].legend()

for file_number in range(total_runs):
	axarr[2].plot(resources_as[file_number], 'k', linewidth=0.5, label='AS')
	axarr[2].plot(resources_pf[file_number], 'r', linewidth=0.5, label='PF')
axarr[2].set_title('Total resources for all teams')
axarr[2].set_xlim([0, 500])
# axarr[1].set_ylim([11, 31])
axarr[2].grid(True)

f.savefig('Teams_E0_00-29.png')








