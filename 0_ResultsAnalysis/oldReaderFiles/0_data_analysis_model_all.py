import pandas as pd
import matplotlib.pyplot as plt
import ast


df_test_B = []
ticks_B = []
Burnt_B = []
Camp_site_B = []
Empty_B = []
Thick_forest_B = []
Thin_forest_B = []
Agenda_issue_B = []
Instrument_B = []
Firefigthers_B = []
Prevention_B = []

df_test_Bplus = []
ticks_Bplus = []
Burnt_Bplus = []
Camp_site_Bplus = []
Empty_Bplus = []
Thick_forest_Bplus = []
Thin_forest_Bplus = []
Agenda_issue_Bplus = []
Instrument_Bplus = []
Firefigthers_Bplus = []
Prevention_Bplus = []

df_test_3S = []
ticks_3S = []
Burnt_3S = []
Camp_site_3S = []
Empty_3S = []
Thick_forest_3S = []
Thin_forest_3S = []
Agenda_issue_3S = []
Instrument_3S = []
Firefigthers_3S = []
Prevention_3S = []

df_test_ACF = []
ticks_ACF = []
Burnt_ACF = []
Camp_site_ACF = []
Empty_ACF = []
Thick_forest_ACF = []
Thin_forest_ACF = []
Agenda_issue_ACF = []
Instrument_ACF = []
Firefigthers_ACF = []
Prevention_ACF = []

total_runs = 4
total_runs_B = total_runs
total_runs_Bplus = total_runs
total_runs_3S = total_runs
total_runs_ACF = total_runs

for i in range(total_runs_B):
	df_test_B.append(pd.read_csv('2_model_B_event2_' + str(i) + '.csv'))
	ticks_B.append([])
	Burnt_B.append([])
	Camp_site_B.append([])
	Empty_B.append([])
	Thick_forest_B.append([])
	Thin_forest_B.append([])
	Agenda_issue_B.append([])
	Instrument_B.append([])
	Firefigthers_B.append([])
	Prevention_B.append([])

for i in range(total_runs_Bplus):
	df_test_Bplus.append(pd.read_csv('1_model_B+_event2_' + str(i) + '.csv'))
	ticks_Bplus.append([])
	Burnt_Bplus.append([])
	Camp_site_Bplus.append([])
	Empty_Bplus.append([])
	Thick_forest_Bplus.append([])
	Thin_forest_Bplus.append([])
	Agenda_issue_Bplus.append([])
	Instrument_Bplus.append([])
	Firefigthers_Bplus.append([])
	Prevention_Bplus.append([])

for i in range(total_runs_3S):
	df_test_3S.append(pd.read_csv('1_model_3S_event2_' + str(i) + '.csv'))
	ticks_3S.append([])
	Burnt_3S.append([])
	Camp_site_3S.append([])
	Empty_3S.append([])
	Thick_forest_3S.append([])
	Thin_forest_3S.append([])
	Agenda_issue_3S.append([])
	Instrument_3S.append([])
	Firefigthers_3S.append([])
	Prevention_3S.append([])

for i in range(total_runs_ACF):
	df_test_ACF.append(pd.read_csv('1_model_ACF_event2_' + str(i) + '.csv'))
	ticks_ACF.append([])
	Burnt_ACF.append([])
	Camp_site_ACF.append([])
	Empty_ACF.append([])
	Thick_forest_ACF.append([])
	Thin_forest_ACF.append([])
	Agenda_issue_ACF.append([])
	Instrument_ACF.append([])
	Firefigthers_ACF.append([])
	Prevention_ACF.append([])

for i in range(total_runs_B):
	for index, row in df_test_B[i].iterrows():
			ticks_B[i].append(index)
			Burnt_B[i].append(row['Burnt'])
			Camp_site_B[i].append(row['Camp_site'])
			Empty_B[i].append(row['Empty'])
			Thick_forest_B[i].append(row['Thick_forest'])
			Thin_forest_B[i].append(row['Thin_forest'])
			Agenda_issue_B[i].append(row['Agenda_issue'])
			Instrument_B[i].append(row['Chosen_instrument'])
			Firefigthers_B[i].append(row['Firefighters'])
			Prevention_B[i].append(row['Prevention'])

for i in range(total_runs_Bplus):
	for index, row in df_test_Bplus[i].iterrows():
			ticks_Bplus[i].append(index)
			Burnt_Bplus[i].append(row['Burnt'])
			Camp_site_Bplus[i].append(row['Camp_site'])
			Empty_Bplus[i].append(row['Empty'])
			Thick_forest_Bplus[i].append(row['Thick_forest'])
			Thin_forest_Bplus[i].append(row['Thin_forest'])
			Agenda_issue_Bplus[i].append(row['Agenda_issue'])
			Instrument_Bplus[i].append(row['Chosen_instrument'])
			Firefigthers_Bplus[i].append(row['Firefighters'])
			Prevention_Bplus[i].append(row['Prevention'])

for i in range(total_runs_3S):
	for index, row in df_test_3S[i].iterrows():
			ticks_3S[i].append(index)
			Burnt_3S[i].append(row['Burnt'])
			Camp_site_3S[i].append(row['Camp_site'])
			Empty_3S[i].append(row['Empty'])
			Thick_forest_3S[i].append(row['Thick_forest'])
			Thin_forest_3S[i].append(row['Thin_forest'])
			Agenda_issue_3S[i].append(row['Agenda_issue'])
			Instrument_3S[i].append(row['Chosen_instrument'])
			Firefigthers_3S[i].append(row['Firefighters'])
			Prevention_3S[i].append(row['Prevention'])

for i in range(total_runs_ACF):
	for index, row in df_test_ACF[i].iterrows():
			ticks_ACF[i].append(index)
			Burnt_ACF[i].append(row['Burnt'])
			Camp_site_ACF[i].append(row['Camp_site'])
			Empty_ACF[i].append(row['Empty'])
			Thick_forest_ACF[i].append(row['Thick_forest'])
			Thin_forest_ACF[i].append(row['Thin_forest'])
			Agenda_issue_ACF[i].append(row['Agenda_issue'])
			Instrument_ACF[i].append(row['Chosen_instrument'])
			Firefigthers_ACF[i].append(row['Firefighters'])
			Prevention_ACF[i].append(row['Prevention'])

# Looking at all the models at once for all technical model variables
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr[0].plot(ticks_B[i], Burnt_B[i], color = 'b', linewidth=1, label='Burnt patches')
	axarr[0].plot(ticks_B[i], Camp_site_B[i], color = 'g', linewidth=1, label='Camp sites')
	axarr[0].plot(ticks_B[i], Empty_B[i], color = 'k', linewidth=1, label='Empty patches')
	axarr[0].plot(ticks_B[i], Thick_forest_B[i], color = 'r', linewidth=1, label='Thick forests')
	axarr[0].plot(ticks_B[i], Thin_forest_B[i], color = 'm', linewidth=1, label='Thin forests')
# plt.legend(handles=[burnt_line, camp_site_line, empy_line, thick_forest_line, thin_forest_line])
axarr[0].set_title('Backbone')
axarr[0].set_xlim([0, 500])
axarr[0].set_ylim([0, 6500])
axarr[0].legend
axarr[0].grid(True)

for i in range(total_runs_Bplus):
	axarr[1].plot(ticks_Bplus[i], Burnt_Bplus[i], color = 'b', linewidth=1, label='Burnt patches')
	axarr[1].plot(ticks_Bplus[i], Camp_site_Bplus[i], color = 'g', linewidth=1, label='Camp sites')
	axarr[1].plot(ticks_Bplus[i], Empty_Bplus[i], color = 'k', linewidth=1, label='Empty patches')
	axarr[1].plot(ticks_Bplus[i], Thick_forest_Bplus[i], color = 'r', linewidth=1, label='Thick forests')
	axarr[1].plot(ticks_Bplus[i], Thin_forest_Bplus[i], color = 'm', linewidth=1, label='Thin forests')
# plt.legend(handles=[burnt_line, camp_site_line, empy_line, thick_forest_line, thin_forest_line])
axarr[1].set_title('Backbone+')
axarr[1].set_xlim([0, 500])
axarr[1].set_ylim([0, 6500])
axarr[1].legend
axarr[1].grid(True)
axarr[1].axes.get_yaxis().set_ticklabels([])

for i in range(total_runs_3S):
	axarr[2].plot(ticks_3S[i], Burnt_3S[i], color = 'b', linewidth=1, label='Burnt patches')
	axarr[2].plot(ticks_3S[i], Camp_site_3S[i], color = 'g', linewidth=1, label='Camp sites')
	axarr[2].plot(ticks_3S[i], Empty_3S[i], color = 'k', linewidth=1, label='Empty patches')
	axarr[2].plot(ticks_3S[i], Thick_forest_3S[i], color = 'r', linewidth=1, label='Thick forests')
	axarr[2].plot(ticks_3S[i], Thin_forest_3S[i], color = 'm', linewidth=1, label='Thin forests')
# plt.legend(handles=[burnt_line, camp_site_line, empy_line, thick_forest_line, thin_forest_line])
axarr[2].set_title('Three streams')
axarr[2].set_xlim([0, 500])
axarr[2].set_ylim([0, 6500])
axarr[2].legend
axarr[2].grid(True)
axarr[2].axes.get_yaxis().set_ticklabels([])

for i in range(total_runs_ACF):
	axarr[3].plot(ticks_ACF[i], Burnt_ACF[i], color = 'b', linewidth=1)
	axarr[3].plot(ticks_ACF[i], Camp_site_ACF[i], color = 'g', linewidth=1)
	axarr[3].plot(ticks_ACF[i], Empty_ACF[i], color = 'k', linewidth=1)
	axarr[3].plot(ticks_ACF[i], Thick_forest_ACF[i], color = 'r', linewidth=1)
	axarr[3].plot(ticks_ACF[i], Thin_forest_ACF[i], color = 'm', linewidth=1)

axarr[3].plot(ticks_ACF[0], Burnt_ACF[0], color = 'b', linewidth=1, label='Burnt patches')
axarr[3].plot(ticks_ACF[0], Camp_site_ACF[0], color = 'g', linewidth=1, label='Camp sites')
axarr[3].plot(ticks_ACF[0], Empty_ACF[0], color = 'k', linewidth=1, label='Empty patches')
axarr[3].plot(ticks_ACF[0], Thick_forest_ACF[0], color = 'r', linewidth=1, label='Thick forests')
axarr[3].plot(ticks_ACF[0], Thin_forest_ACF[0], color = 'm', linewidth=1, label='Thin forests')
# plt.legend(handles=[burnt_line, camp_site_line, empy_line, thick_forest_line, thin_forest_line])
axarr[3].set_title('ACF')
axarr[3].set_xlim([0, 500])
axarr[3].set_ylim([0, 6500])
axarr[3].legend()
axarr[3].grid(True)
axarr[3].axes.get_yaxis().set_ticklabels([])
f.savefig('Model_total_E0_00-29.png')

# plt.grid(True)
# axes = plt.gca()
# axes.set_xlim([0,500])
# axes.set_ylim([0,6500])


# Looking at the agenda and the instruments being implemented
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr[0].plot(ticks_B[i], Agenda_issue_B[i], color = 'b', linewidth=1)
	axarr[0].plot(ticks_B[i], Instrument_B[i], color = 'g', linewidth=1)
axarr[0].set_title('Backbone')
axarr[0].set_xlim([0, 500])
axarr[0].set_ylim([0, 20])
axarr[0].legend
axarr[0].grid(True)

for i in range(total_runs_Bplus):
	axarr[1].plot(ticks_Bplus[i], Agenda_issue_Bplus[i], color = 'b', linewidth=1)
	axarr[1].plot(ticks_Bplus[i], Instrument_ACF[i], color = 'g', linewidth=1)
axarr[1].set_title('Backbone+')
axarr[1].set_xlim([0, 500])
axarr[1].set_ylim([0, 20])
axarr[1].legend
axarr[1].grid(True)
axarr[1].axes.get_yaxis().set_ticklabels([])

for i in range(total_runs_3S):
	axarr[2].plot(ticks_3S[i], Agenda_issue_3S[i], color = 'b', linewidth=1)
	axarr[2].plot(ticks_3S[i], Instrument_3S[i], color = 'g', linewidth=1)
axarr[2].set_title('Three streams')
axarr[2].set_xlim([0, 500])
axarr[2].set_ylim([0, 20])
axarr[2].legend
axarr[2].grid(True)
axarr[2].axes.get_yaxis().set_ticklabels([])

for i in range(total_runs_ACF):
	axarr[3].plot(ticks_ACF[i], Agenda_issue_ACF[i], color = 'b', linewidth=1)
	axarr[3].plot(ticks_ACF[i], Instrument_ACF[i], color = 'g', linewidth=1)
axarr[3].plot(ticks_ACF[0], Agenda_issue_ACF[0], color = 'b', linewidth=1, label='Agenda issue')
axarr[3].plot(ticks_ACF[0], Instrument_ACF[0], color = 'g', linewidth=1, label='Instrument')
axarr[3].set_title('ACF')
axarr[3].set_xlim([0, 500])
axarr[3].set_ylim([0, 20])
axarr[3].legend()
axarr[3].grid(True)
axarr[3].axes.get_yaxis().set_ticklabels([])
f.savefig('Agenda_Instrument_4Models_E0_00-29.png')

# Looking at all the models at once for only the burnt property
f, axarr = plt.subplots(1, 1, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr.plot(ticks_B[i], Burnt_B[i], color = 'b', linewidth=1)
	axarr.plot(ticks_Bplus[i], Burnt_Bplus[i], color = 'g', linewidth=1)
	axarr.plot(ticks_3S[i], Burnt_3S[i], color = 'k', linewidth=1)
	axarr.plot(ticks_ACF[i], Burnt_ACF[i], color = 'r', linewidth=1)
axarr.plot(ticks_B[0], Burnt_B[0], color = 'b', linewidth=1, label='Backbone')
axarr.plot(ticks_Bplus[0], Burnt_Bplus[0], color = 'g', linewidth=1, label='Backbone+')
axarr.plot(ticks_3S[0], Burnt_3S[0], color = 'k', linewidth=1, label='Three streams')
axarr.plot(ticks_ACF[0], Burnt_ACF[0], color = 'r', linewidth=1, label='ACF')
axarr.set_title('Burnt patches')
axarr.set_xlim([0, 500])
axarr.set_ylim([0, 6500])
axarr.legend()
axarr.grid(True)
f.savefig('Model_total_BurntPatches_E0_00-29.png')

# Looking at all the models at once for only the empty property
f, axarr = plt.subplots(1, 1, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr.plot(ticks_B[i], Empty_B[i], color = 'b', linewidth=1)
	axarr.plot(ticks_Bplus[i], Empty_Bplus[i], color = 'g', linewidth=1)
	axarr.plot(ticks_3S[i], Empty_3S[i], color = 'k', linewidth=1)
	axarr.plot(ticks_ACF[i], Empty_ACF[i], color = 'r', linewidth=1)
axarr.plot(ticks_B[0], Empty_B[0], color = 'b', linewidth=1, label='Backbone')
axarr.plot(ticks_Bplus[0], Empty_Bplus[0], color = 'g', linewidth=1, label='Backbone+')
axarr.plot(ticks_3S[0], Empty_3S[0], color = 'k', linewidth=1, label='Three streams')
axarr.plot(ticks_ACF[0], Empty_ACF[0], color = 'r', linewidth=1, label='ACF')
axarr.set_title('Empty patches')
axarr.set_xlim([0, 500])
axarr.set_ylim([0, 6500])
axarr.legend()
axarr.grid(True)
f.savefig('Model_total_EmptyPatches_E0_00-29.png')

# Looking at all the models at once for only the camp sites property
f, axarr = plt.subplots(1, 1, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr.plot(ticks_B[i], Camp_site_B[i], color = 'b', linewidth=1)
	axarr.plot(ticks_Bplus[i], Camp_site_Bplus[i], color = 'g', linewidth=1)
	axarr.plot(ticks_3S[i], Camp_site_3S[i], color = 'k', linewidth=1)
	axarr.plot(ticks_ACF[i], Camp_site_ACF[i], color = 'r', linewidth=1)
axarr.plot(ticks_B[0], Camp_site_B[0], color = 'b', linewidth=1, label='Backbone')
axarr.plot(ticks_Bplus[0], Camp_site_Bplus[0], color = 'g', linewidth=1, label='Backbone+')
axarr.plot(ticks_3S[0], Camp_site_3S[0], color = 'k', linewidth=1, label='Three streams')
axarr.plot(ticks_ACF[0], Camp_site_ACF[0], color = 'r', linewidth=1, label='ACF')
axarr.set_title('Camp site patches')
axarr.set_xlim([0, 500])
axarr.set_ylim([0, 3000])
axarr.legend()
axarr.grid(True)
f.savefig('Model_total_Camp_sitePatches_E0_00-29.png')

# Looking at all the models at once for only the burnt property
f, axarr = plt.subplots(1, 1, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr.plot(ticks_B[i], Thick_forest_B[i], color = 'b', linewidth=1)
	axarr.plot(ticks_Bplus[i], Thick_forest_Bplus[i], color = 'g', linewidth=1)
	axarr.plot(ticks_3S[i], Thick_forest_3S[i], color = 'k', linewidth=1)
	axarr.plot(ticks_ACF[i], Thick_forest_ACF[i], color = 'r', linewidth=1)
axarr.plot(ticks_B[0], Thick_forest_B[0], color = 'b', linewidth=1, label='Backbone')
axarr.plot(ticks_Bplus[0], Thick_forest_Bplus[0], color = 'g', linewidth=1, label='Backbone+')
axarr.plot(ticks_3S[0], Thick_forest_3S[0], color = 'k', linewidth=1, label='Three streams')
axarr.plot(ticks_ACF[0], Thick_forest_ACF[0], color = 'r', linewidth=1, label='ACF')
axarr.set_title('Thick forest patches')
axarr.set_xlim([0, 500])
axarr.set_ylim([0, 2000])
axarr.legend()
axarr.grid(True)
f.savefig('Model_total_Thick_forestPatches_E0_00-29.png')

# Looking at all the models at once for only the burnt property
f, axarr = plt.subplots(1, 1, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr.plot(ticks_B[i], Thin_forest_B[i], color = 'b', linewidth=1)
	axarr.plot(ticks_Bplus[i], Thin_forest_Bplus[i], color = 'g', linewidth=1)
	axarr.plot(ticks_3S[i], Thin_forest_3S[i], color = 'k', linewidth=1)
	axarr.plot(ticks_ACF[i], Thin_forest_ACF[i], color = 'r', linewidth=1)
axarr.plot(ticks_B[0], Thin_forest_B[0], color = 'b', linewidth=1, label='Backbone')
axarr.plot(ticks_Bplus[0], Thin_forest_Bplus[0], color = 'g', linewidth=1, label='Backbone+')
axarr.plot(ticks_3S[0], Thin_forest_3S[0], color = 'k', linewidth=1, label='Three streams')
axarr.plot(ticks_ACF[0], Thin_forest_ACF[0], color = 'r', linewidth=1, label='ACF')
axarr.set_title('Thin forest patches')
axarr.set_xlim([0, 500])
axarr.set_ylim([0, 3000])
axarr.legend()
axarr.grid(True)
f.savefig('Model_total_Thin_forestPatches_E0_00-29.png')



# Looking at the firefighters and prevention coefficients
f, axarr = plt.subplots(1, 4, figsize=(11,3.5))
for i in range(total_runs_B):
	axarr[0].plot(ticks_B[i], Firefigthers_B[i], color = 'b', linewidth=1)
	axarr[0].plot(ticks_B[i], Prevention_B[i], color = 'g', linewidth=1)
axarr[0].set_title('Backbone')
axarr[0].set_xlim([0, 500])
axarr[0].set_ylim([0, 0.6])
axarr[0].legend
axarr[0].grid(True)

for i in range(total_runs_Bplus):
	axarr[1].plot(ticks_Bplus[i], Firefigthers_Bplus[i], color = 'b', linewidth=1)
	axarr[1].plot(ticks_Bplus[i], Prevention_ACF[i], color = 'g', linewidth=1)
axarr[1].set_title('Backbone+')
axarr[1].set_xlim([0, 500])
axarr[1].set_ylim([0, 0.6])
axarr[1].legend
axarr[1].grid(True)
axarr[1].axes.get_yaxis().set_ticklabels([])

for i in range(total_runs_3S):
	axarr[2].plot(ticks_3S[i], Firefigthers_3S[i], color = 'b', linewidth=1)
	axarr[2].plot(ticks_3S[i], Prevention_3S[i], color = 'g', linewidth=1)
axarr[2].set_title('Three streams')
axarr[2].set_xlim([0, 500])
axarr[2].set_ylim([0, 0.6])
axarr[2].legend
axarr[2].grid(True)
axarr[2].axes.get_yaxis().set_ticklabels([])

for i in range(total_runs_ACF):
	axarr[3].plot(ticks_ACF[i], Firefigthers_ACF[i], color = 'b', linewidth=1)
	axarr[3].plot(ticks_ACF[i], Prevention_ACF[i], color = 'g', linewidth=1)
axarr[3].plot(ticks_ACF[0], Firefigthers_ACF[0], color = 'b', linewidth=1, label='Firefighters coefficient')
axarr[3].plot(ticks_ACF[0], Prevention_ACF[0], color = 'g', linewidth=1, label='Prevention coefficient')
axarr[3].set_title('ACF')
axarr[3].set_xlim([0, 500])
axarr[3].set_ylim([0, 0.6])
axarr[3].legend()
axarr[3].grid(True)
axarr[3].axes.get_yaxis().set_ticklabels([])
f.savefig('Firefighters_Prevention_4Models_E0_00-29.png')



plt.show()






