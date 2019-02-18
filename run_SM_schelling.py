from model_schelling import Schelling
from model_SM import PolicyEmergenceSM
import matplotlib.pyplot as plt
import numpy as np

'''
The current architecture is used for test purposes.
Ultimately, the two models should be initialised and then their for loops should be intertwined.
'''

# running the policy emergence Simplest Model
model_run_SM = PolicyEmergenceSM(10,10)

for i in range(5):
	model_run_SM.step()

'''
# running the Schelling model:
model_run_schelling = Schelling(20, 20, 0.75, 0.4)

for i in range(50):
	if model_run_schelling.happy != model_run_schelling.schedule.get_agent_count():
		print("Step: ", i)
		model_run_schelling.step()

for i in range(50):
	model_run_schelling.step()


# printing the data obtained from the Schelling model
dataPlot = model_run_schelling.datacollector.get_model_vars_dataframe()
print(dataPlot)
dataPlot.plot("step", "evenness")
dataPlot.plot("step", "happy")
plt.show()
'''