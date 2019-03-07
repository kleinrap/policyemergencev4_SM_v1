import pandas as pd
import matplotlib.pyplot as plt
import ast


# Check for the number of coalitions per step
# Check for the number of actors in coalitions per step

# experiment_chosen = [0, 1, 2, 3, 4, 5]

# for ip in experiment_chosen:

# 	experiment_number = ip
# 	print('experiment_number: ' + str(experiment_number))

total_runs = 12

coalitions_number_as = []
actors_in_coalitions_as = []
resources_as = []

coalitions_number_pf = []
actors_in_coalitions_pf = []
resources_pf = []

for file_number in range(total_runs):
	coalitions_number_as.append([0])
	actors_in_coalitions_as.append([0])
	resources_as.append([0])

	coalitions_number_pf.append([0])
	actors_in_coalitions_pf.append([0])
	resources_pf.append([0])

possible_links = 29

df_test_ACF_as = []
df_test_ACF_pf = []

for i in range(total_runs):
	df_test_ACF_as.append(pd.read_csv('1_coalitions_as_ACF_event2_' + str(i) + '.csv'))
	df_test_ACF_pf.append(pd.read_csv('1_coalitions_pf_ACF_event2_' + str(i) + '.csv'))


for file_number in range(total_runs):
	ij = 0
	for index, row in df_test_ACF_as[file_number].iterrows():
		# Increase the number when the step has passed
		# print('ij: ' + str(ij))
		if row['Step'] != ij:
			ij += 1
			coalitions_number_as[file_number].append(0)
			actors_in_coalitions_as[file_number].append(0)
			resources_as[file_number].append(0)

		coalitions_number_as[file_number][ij] += 1
		resources_as[file_number][ij] += row['Resources']

		store1 = row['Members']
		store2 = eval(store1)
		actors_in_coalitions_as[file_number][ij] += len(store2)

for file_number in range(total_runs):
	ij = 0
	for index, row in df_test_ACF_pf[file_number].iterrows():
		# Increase the number when the step has passed
		if row['Step'] != ij:
			ij += 1
			coalitions_number_pf[file_number].append(0)
			actors_in_coalitions_pf[file_number].append(0)
			resources_pf[file_number].append(0)

		coalitions_number_pf[file_number][ij] += 1
		resources_pf[file_number][ij] += row['Resources']

		store1 = row['Members']
		store2 = eval(store1)
		actors_in_coalitions_pf[file_number][ij] += len(store2)

# print(coalitions_number_as)
# print(actors_in_coalitions_as)
# print(' ')
# print(coalitions_number_pf)
# print(actors_in_coalitions_pf)

f, axarr = plt.subplots(1, 3, figsize=(11,3.5))

for file_number in range(total_runs):
	axarr[0].plot(coalitions_number_pf[file_number], 'r',  linewidth=0.5)
	axarr[0].plot(coalitions_number_as[file_number], 'k',  linewidth=0.5)
axarr[0].set_title('Number of coalitions')
axarr[0].set_xlim([0, 500])
axarr[0].set_ylim([0, 30])
axarr[0].grid(True)

for file_number in range(total_runs):
	if file_number == 0:
		axarr[1].plot(actors_in_coalitions_as[file_number], 'k', linewidth=0.5, label='AS')
		axarr[1].plot(actors_in_coalitions_pf[file_number], 'r', linewidth=0.5, label='PF')
	else:
		axarr[1].plot(actors_in_coalitions_as[file_number], 'k', linewidth=0.5)
		axarr[1].plot(actors_in_coalitions_pf[file_number], 'r', linewidth=0.5)

axarr[1].set_title('Actors in coalitions')
axarr[1].set_xlim([0, 500])
axarr[1].set_ylim([22, 31])
axarr[1].grid(True)
axarr[1].legend()

for file_number in range(total_runs):
	axarr[2].plot(resources_as[file_number], 'k', linewidth=0.5, label='AS')
	axarr[2].plot(resources_pf[file_number], 'r', linewidth=0.5, label='PF')
axarr[2].set_title('Total resources for all coalitions')
axarr[2].set_xlim([0, 500])
# axarr[1].set_ylim([11, 31])
axarr[2].grid(True)

f.savefig('Coalitions_E0_00-29.png')








