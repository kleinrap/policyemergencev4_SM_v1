import pandas as pd
import matplotlib.pyplot as plt
import ast


df_B = []
df_Bplus = []
df_3S = []
df_ACF = []

total_runs = 5
total_runs_B = total_runs
total_runs_Bplus = total_runs 
total_runs_3S = total_runs 
total_runs_ACF = total_runs 

agent_trees_B = []
agent_trees_Bplus = []
agent_trees_3S = []
agent_trees_ACF = []

# We first read all the files into arrays that contains each entire file

for i in range(total_runs):
	print('Run read: ' + str(i))
	df_B.append(pd.read_csv('2_agents_B_event2_' + str(i) + '.csv'))
	agent_trees_B.append([])

	df_Bplus.append(pd.read_csv('1_agents_B+_event2_' + str(i) + '.csv'))
	agent_trees_Bplus.append([])

	df_3S.append(pd.read_csv('1_agents_3S_event2_' + str(i) + '.csv'))
	agent_trees_3S.append([])

	df_ACF.append(pd.read_csv('1_agents_ACF_event2_' + str(i) + '.csv'))
	agent_trees_ACF.append([])

# This batch is related to the electorate influence on the policy makers,
# we are therefore interested in only studying the six policy makers.
# If we record everything, we do not have to use the if statement in the index,row loop which
# should make this whole process much faster.
agents_studied = 12


for file_number in range(total_runs):
	for i in range(agents_studied):
		agent_trees_B[file_number].append([])
	for i in range(agents_studied):
		agent_trees_Bplus[file_number].append([])
	for i in range(agents_studied):
		agent_trees_3S[file_number].append([])
	for i in range(agents_studied):
		agent_trees_ACF[file_number].append([])

# Looking at the agents
for file_number in range(total_runs):
	for index, row in df_B[file_number].iterrows():
		if row['AgentID'] >= 12 and row['AgentID'] < 24:
			print(row['AgentID'])
			store1 = row['Belieftree']
			store2 = eval(store1)
			agent_trees_B[file_number][row['AgentID'] - 12].append(store2)
	for index, row in df_Bplus[file_number].iterrows():
		if row['AgentID'] >= 12 and row['AgentID'] < 24:
			store1 = row['Belieftree']
			store2 = eval(store1)
			agent_trees_Bplus[file_number][row['AgentID'] - 12].append(store2)
	for index, row in df_3S[file_number].iterrows():
		if row['AgentID'] >= 12 and row['AgentID'] < 24:
			store1 = row['Belieftree']
			store2 = eval(store1)
			agent_trees_3S[file_number][row['AgentID'] - 12].append(store2)
	for index, row in df_ACF[file_number].iterrows():
		if row['AgentID'] >= 12 and row['AgentID'] < 24:
			store1 = row['Belieftree']
			store2 = eval(store1)
			agent_trees_ACF[file_number][row['AgentID'] - 12].append(store2)

agent_trees = []
for file_number in range(total_runs):
	agent_trees_2 = [[],[],[],[]]
	agent_trees.append(agent_trees_2)

# issue_10 = [[],[],[], []] # P1-PC1
# issue_11 = [[],[],[], []] # P1-PC2
# issue_12 = [[],[],[], []] # P1-PC3
# issue_13 = [[],[],[], []] # P2-PC1
# issue_14 = [[],[],[], []] # P2-PC2
# issue_15 = [[],[],[], []] # P2-PC3
# issue_16 = [[],[],[], []] # PC1-S1
# issue_17 = [[],[],[], []] # PC1-S2
# issue_18 = [[],[],[], []] # PC1-S3
# issue_19 = [[],[],[], []] # PC1-S4
# issue_20 = [[],[],[], []] # PC1-S5
# issue_21 = [[],[],[], []] # PC2-S1
# issue_22 = [[],[],[], []] # PC2-S2
# issue_23 = [[],[],[], []] # PC2-S3
# issue_24 = [[],[],[], []] # PC2-S4
# issue_25 = [[],[],[], []] # PC2-S5
# issue_26 = [[],[],[], []] # PC3-S1
# issue_27 = [[],[],[], []] # PC3-S2
# issue_28 = [[],[],[], []] # PC3-S3
# issue_29 = [[],[],[], []] # PC3-S4
# issue_30 = [[],[],[], []] # PC3-S5

for file_number in range(total_runs):
	for j in range(4):
		for i in range(agents_studied):
			agent_trees[file_number][j].append([])

for file_number in range(total_runs): # File selected
	for k in range(4): # Number of models considered
		for j in range(agents_studied): # Number of agents considered
			for i in range(500): # Number of ticks in a run
				if k == 0: # Outputs from the backbone
					agent_trees[file_number][k][j].append(agent_trees_B[file_number][j][i])

				if k == 1: #Outputs from the backbon+
					agent_trees[file_number][k][j].append(agent_trees_Bplus[file_number][j][i])

				if k == 2: #Outputs from the three streams
					agent_trees[file_number][k][j].append(agent_trees_3S[file_number][j][i])

				if k == 3:
					agent_trees[file_number][k][j].append(agent_trees_ACF[file_number][j][i])

colour_range = ['k', 'c', 'b', 'y', 'r', 'm']
colour_range2 = ['k--', 'c--', 'b--', 'y--', 'r--', 'm--']
label_names = ['PE1', 'PE2', 'PE3', 'PE4', 'PE5', 'PE6']

# For issue 0
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 0
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])

				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P1')
	if j == 1:
		axarr[j].set_title('Backbone+ - P1')
	if j == 2:
		axarr[j].set_title('Three streams - P1')
	if j == 3:
		axarr[j].set_title('ACF - P1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('6EPs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 1
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 1
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P2')
	if j == 1:
		axarr[j].set_title('Backbone+ - P2')
	if j == 2:
		axarr[j].set_title('Three streams - P2')
	if j == 3:
		axarr[j].set_title('ACF - P2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 2
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 2
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC1')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC1')
	if j == 2:
		axarr[j].set_title('Three streams - PC1')
	if j == 3:
		axarr[j].set_title('ACF - PC1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 3
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 3
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC2')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC2')
	if j == 2:
		axarr[j].set_title('Three streams - PC2')
	if j == 3:
		axarr[j].set_title('ACF - PC2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 4
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 4
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC3')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC3')
	if j == 2:
		axarr[j].set_title('Three streams - PC3')
	if j == 3:
		axarr[j].set_title('ACF - PC3')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 5
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 5
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - S1')
	if j == 1:
		axarr[j].set_title('Backbone+ - S1')
	if j == 2:
		axarr[j].set_title('Three streams - S1')
	if j == 3:
		axarr[j].set_title('ACF - S1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 6
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 6
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - S2')
	if j == 1:
		axarr[j].set_title('Backbone+ - S2')
	if j == 2:
		axarr[j].set_title('Three streams - S2')
	if j == 3:
		axarr[j].set_title('ACF - S2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 7
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 7
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - S3')
	if j == 1:
		axarr[j].set_title('Backbone+ - S3')
	if j == 2:
		axarr[j].set_title('Three streams - S3')
	if j == 3:
		axarr[j].set_title('ACF - S3')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 8
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 8
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - S4')
	if j == 1:
		axarr[j].set_title('Backbone+ - S4')
	if j == 2:
		axarr[j].set_title('Three streams - S4')
	if j == 3:
		axarr[j].set_title('ACF - S4')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 9
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 9
for j in range(4):
	# We are only interested in the policy makers:
	# for k in range(agents_studied):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_state = []
			temp_aim = []
			for i in range(500):
				temp_state.append(agent_trees[file_number][j][k][i][issue][0])
				temp_aim.append(agent_trees[file_number][j][k][i][issue][1])
			if file_number == 0:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1, label = label_names[k])
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
			else:
				axarr[j].plot(temp_state, colour_range[k], linewidth=1)
				axarr[j].plot(temp_aim, colour_range2[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - S5')
	if j == 1:
		axarr[j].set_title('Backbone+ - S5')
	if j == 2:
		axarr[j].set_title('Three streams - S5')
	if j == 3:
		axarr[j].set_title('ACF - S5')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])
	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 10
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 10
for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P1-PC1')
	if j == 1:
		axarr[j].set_title('Backbone+ - P1-PC1')
	if j == 2:
		axarr[j].set_title('Three streams - P1-PC1')
	if j == 3:
		axarr[j].set_title('ACF - P1-PC1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])
	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 11
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 11
for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P1-PC2')
	if j == 1:
		axarr[j].set_title('Backbone+ - P1-PC2')
	if j == 2:
		axarr[j].set_title('Three streams - P1-PC2')
	if j == 3:
		axarr[j].set_title('ACF - P1-PC2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 12
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 12
for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):

				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P1-PC3')
	if j == 1:
		axarr[j].set_title('Backbone+ - P1-PC3')
	if j == 2:
		axarr[j].set_title('Three streams - P1-PC3')
	if j == 3:
		axarr[j].set_title('ACF - P1-PC1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 13
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 13

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P2-PC1')
	if j == 1:
		axarr[j].set_title('Backbone+ - P2-PC1')
	if j == 2:
		axarr[j].set_title('Three streams - P2-PC1')
	if j == 3:
		axarr[j].set_title('ACF - P2-PC1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')


# For issue 14
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 14

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P2-PC2')
	if j == 1:
		axarr[j].set_title('Backbone+ - P2-PC2')
	if j == 2:
		axarr[j].set_title('Three streams - P2-PC2')
	if j == 3:
		axarr[j].set_title('ACF - P2-PC2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 15
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 15

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - P2-PC3')
	if j == 1:
		axarr[j].set_title('Backbone+ - P2-PC3')
	if j == 2:
		axarr[j].set_title('Three streams - P2-PC3')
	if j == 3:
		axarr[j].set_title('ACF - P2-PC3')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 16
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 16

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC1-S1')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC1-S1')
	if j == 2:
		axarr[j].set_title('Three streams - PC1-S1')
	if j == 3:
		axarr[j].set_title('ACF - PC1-S1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 17
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 17

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC1-S2')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC1-S2')
	if j == 2:
		axarr[j].set_title('Three streams - PC1-S2')
	if j == 3:
		axarr[j].set_title('ACF - PC1-S2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 18
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 18

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC1-S3')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC1-S3')
	if j == 2:
		axarr[j].set_title('Three streams - PC1-S3')
	if j == 3:
		axarr[j].set_title('ACF - PC1-S1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 19
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 19

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC1-S4')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC1-S4')
	if j == 2:
		axarr[j].set_title('Three streams - PC1-S4')
	if j == 3:
		axarr[j].set_title('ACF - PC1-S4')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 20
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 20

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC1-S5')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC1-S5')
	if j == 2:
		axarr[j].set_title('Three streams - PC1-S5')
	if j == 3:
		axarr[j].set_title('ACF - PC1-S4')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 21
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 21

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC2-S1')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC2-S1')
	if j == 2:
		axarr[j].set_title('Three streams - PC2-S1')
	if j == 3:
		axarr[j].set_title('ACF - PC2-S1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 22
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 22

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC2-S2')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC2-S2')
	if j == 2:
		axarr[j].set_title('Three streams - PC2-S2')
	if j == 3:
		axarr[j].set_title('ACF - PC2-S1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 23
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 23

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC2-S3')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC2-S3')
	if j == 2:
		axarr[j].set_title('Three streams - PC2-S3')
	if j == 3:
		axarr[j].set_title('ACF - PC2-S3')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 24
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 24

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC2-S4')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC2-S4')
	if j == 2:
		axarr[j].set_title('Three streams - PC2-S4')
	if j == 3:
		axarr[j].set_title('ACF - PC2-S4')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 25
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 25

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC2-S5')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC2-S5')
	if j == 2:
		axarr[j].set_title('Three streams - PC2-S5')
	if j == 3:
		axarr[j].set_title('ACF - PC2-S5')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 26
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 26

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC3-S1')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC3-S1')
	if j == 2:
		axarr[j].set_title('Three streams - PC3-S1')
	if j == 3:
		axarr[j].set_title('ACF - PC3-S1')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 27
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 27

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC3-S2')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC3-S2')
	if j == 2:
		axarr[j].set_title('Three streams - PC3-S2')
	if j == 3:
		axarr[j].set_title('ACF - PC3-S2')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 28
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 28

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC3-S3')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC3-S3')
	if j == 2:
		axarr[j].set_title('Three streams - PC3-S3')
	if j == 3:
		axarr[j].set_title('ACF - PC3-S3')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 29
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 29

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC3-S4')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC3-S4')
	if j == 2:
		axarr[j].set_title('Three streams - PC3-S4')
	if j == 3:
		axarr[j].set_title('ACF - PC3-S4')
	axarr[j].set_xlim([0, 500])
	axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# For issue 30
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
issue = 30

for j in range(4):
	for k in range(3):
		for file_number in range(total_runs): # Going through each of the file one by one
			temp_CR = []
			for i in range(500):
				temp_CR.append(agent_trees[file_number][j][k][i][issue][0])
			if file_number == 0:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1, label = label_names[k])
			else:
				axarr[j].plot(temp_CR, colour_range[k], linewidth=1)
	if j == 0:
		axarr[j].set_title('Backbone - PC3-S5')
	if j == 1:
		axarr[j].set_title('Backbone+ - PC3-S5')
	if j == 2:
		axarr[j].set_title('Three streams - PC3-S5')
	if j == 3:
		axarr[j].set_title('ACF - PC3-S5')
	# axarr[j].set_xlim([0, 500])
	# axarr[j].set_ylim([-1, 1])

	axarr[j].grid(True)
	if j != 0:
		axarr[j].axes.get_yaxis().set_ticklabels([])
axarr[3].legend()
f.savefig('3PEs_' + str(issue) + '_4Model_E0_00-29.png')

# plt.show()




