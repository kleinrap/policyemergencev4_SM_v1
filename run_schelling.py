from model_schelling import Schelling

model_run = Schelling(20, 20, 0.8, 0.2)

for i in range(500):
	if model_run.happy != model_run.schedule.get_agent_count():
		print("Step: ", i)
		model_run.step()
