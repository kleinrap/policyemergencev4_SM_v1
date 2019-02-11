from model_schelling import Schelling
import matplotlib.pyplot as plt

model_run = Schelling(20, 20, 0.75, 0.4)

for i in range(50):
	if model_run.happy != model_run.schedule.get_agent_count():
		print("Step: ", i)
		model_run.step()

dataPlot = model_run.datacollector.get_model_vars_dataframe()

dataPlot.plot()
plt.show()