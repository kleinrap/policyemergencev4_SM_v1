import random

class Technical_Model():
	
	def __init__(self, len_PC, len_ML, len_S):
		self.len_PC = len_PC
		self.len_ML = len_ML
		self.len_S = len_S
		self.belieftree_truth = [None for i in range(len_PC + len_ML + len_S)]

		self.cells_repository = []
		# belieftree_truth = []

	# Add a cell to the list of cells:
	def add(self, agent):
		self.cells_repository.append(agent)
		# print(self.cells_repository[self.pos])

	def cell_count(self, condition_name):

		"""
		Cell count function
		===========================

		This function is used to count the number of cells.
		This is a test function.
		
		"""

		return sum(test.condition == condition_name for test in self.cells_repository)

	def states_update(self, height, width, belieftree_truth, thin_burning_probability, firefighter_force):

		"""
		States update function
		===========================

		This function is used to update the states based on the current state
		of the forest fire model.

		First, all of the cells are counted. Then each of the issues present
		in the belief tree are assessed one by one. These use equations
		presented within the formalisation.
		
		"""

		# print(self.cells_repository)
		self.total_cells = height*width
		self.thin_burning_probability = thin_burning_probability
		self.belieftree_truth = belieftree_truth
		self.firefighter_force = firefighter_force

		# Current modek has 2 Pr, 3 PC and 5 S
		# Pr1 - Economy -- Pr2 - Environment
		# PC1 - Forest size -- PC2 - Tourism -- ML3 - Safety
		# S1 - Camp sites -- S2 - Planting -- S3 - Monitoring -- S4 - Firefighters -- S5 - Prevention

		
		self.campSite_cells_count = self.cell_count("Camp site")
		self.campSite_percentage = self.campSite_cells_count / self.total_cells
		self.burnt_cells_count = self.cell_count("Burnt")
		self.burnt_percentage = self.burnt_cells_count / self.total_cells
		self.thickForest_cells_count = self.cell_count("Thick forest")
		self.thickForest_percentage = self.thickForest_cells_count / self.total_cells
		self.thinForest_cells_count = self.cell_count("Thin forest")
		self.thinForest_percentage = self.thinForest_cells_count / self.total_cells
		self.empty_cells_count = self.cell_count("Empty")
		self.empty_percentage = self.empty_cells_count / self.total_cells
		print('********')
		print('This is the amount of burnt forest: ' + str(self.burnt_cells_count))
		print('This is the amount of thick forest: ' + str(self.thickForest_cells_count))
		print('This is the amount of thin forest: ' + str(self.thinForest_cells_count))
		print('This is the amount of camp sites: ' + str(self.campSite_cells_count))
		print('This is the amount of empty cells: ' + str(self.empty_cells_count))
		print('********')


		# S1 - Camp sites - A value of 1 is attributed to max 20% camp sites - everything below is graded from -1 to 1
		maxCampSites = 0.2
		if self.campSite_percentage > maxCampSites:
			self.belieftree_truth[5] = 1
		else:
			self.belieftree_truth[5] = round((self.campSite_percentage * 2)/maxCampSites - 1 , 5)

		# S2 - Planting - A value of 1 is attributed to max 60% thin forests - everything below is graded from - 1 to 1
		maxThinForest = 0.6
		if self.thinForest_percentage > maxThinForest:
			self.belieftree_truth[6] = 1
		else:
			self.belieftree_truth[6] = round((self.thinForest_percentage * 2)/maxThinForest -1, 5)

		# S3 - Monitoring - A value of 1 is attributed to max 10% probability of burning - everything below is graded from -1 to 1
		# The minus is used because the calculation is opposite to others. 1 is for when nothing is burning (0%) 
		# and -1 is for when the probability is the highest (100% or max)
		maxThin_burning_probability = 0.1
		if self.thin_burning_probability > maxThin_burning_probability:
			self.belieftree_truth[7] = -1
		else:
			self.belieftree_truth[7] = round( - (((self.thin_burning_probability) * 2)/maxThin_burning_probability - 1), 5)

		#S4 - Firefighters
		maxFirefighter_force = 0.5
		if self.firefighter_force > maxFirefighter_force:
			self.belieftree_truth[8] = -1
		else:
			self.belieftree_truth[8] = round( -(((self.firefighter_force) * 2 )/maxFirefighter_force - 1), 5)

		#S5 - Prevention
		maxEmpty = 1
		if self.empty_percentage > maxEmpty:
			self.belieftree_truth[9] = 1
		else:
			self.belieftree_truth[9] = round((self.empty_percentage * 2)/maxEmpty - 1 , 5)

		# PC1 - Forest size
		self.belieftree_truth[2] = round(((0.75 * self.thickForest_percentage + 0.25 * self.thinForest_percentage) * 2) - 1 , 5)

		# PC2 - Tourism
		self.belieftree_truth[3] = round(((0.75 * self.campSite_percentage + 0.25 * self.thickForest_percentage)* 2 ) - 1 , 5)

		# ML3 - Safety - 
		# All of the numbers in this sum are counted on the interval [0,1] depending on their respective maximum. Negative aspects go
		# down from 1 towards 0 while poisitve aspects go up from 0 to 1.
		maxThickForest = 1.0
		if self.thin_burning_probability > maxThin_burning_probability:
			ML3_P1 = 0
		else: # this is negative towards the safety grade
			ML3_P1 =  1 - self.thin_burning_probability/maxThin_burning_probability
		if self.firefighter_force > maxFirefighter_force:
			ML3_P2 = 1
		else: # this is positive towards the safety grade
			ML3_P2 = self.firefighter_force/maxFirefighter_force
		if self.empty_percentage > maxEmpty:
			ML3_P3 = 1
		else: # this is positive towards the safety grade
			ML3_P3 = self.empty_percentage/maxEmpty
		if self.campSite_percentage > maxCampSites:
			ML3_P4 = 0
		else: # this is negative towards the safety grade
			ML3_P4 = 1 - self.campSite_percentage/maxCampSites
		if self.thickForest_percentage > maxThickForest:
			ML3_P5 = 0
		else: # this is negative towards the safety grade
			ML3_P5 = 1 - self.thickForest_percentage/maxThickForest
		self.belieftree_truth[4] = round((( (ML3_P1 + ML3_P2 + ML3_P3 + ML3_P4 + ML3_P5) / 5) * 2) - 1, 5)

		# Pr1 - Economy
		self.belieftree_truth[0] = round((((self.belieftree_truth[3] + 1) / 2 + (self.belieftree_truth[4] + 1) / 2) * 2/2) - 1 , 5)

		# Pr2 - Environment
		self.belieftree_truth[1] = round((((self.belieftree_truth[2] + 1) / 2 + (self.belieftree_truth[4] + 1) / 2) * 2/2) - 1 , 5)	

		# print('This is the truth belief tree: ' + str(belieftree_truth))

		# Check for 1-1:
		for p in range(len(self.belieftree_truth)):
			if self.belieftree_truth[p] > 1 or self.belieftree_truth[p] < -1:
				for l in range(20):
					print('ERROR TRUTH TREE')
				

		print('This is the truth belief vector: ' + str(self.belieftree_truth))

	def measures_implementation(self, agenda_instrument, instruments, instrument_campSites, instrument_planting, \
		thin_burning_probability, firefighter_force, instrument_prevention):

		"""
		Policy implementation function
		===========================

		This function is used to implement the policies chosen
		by the agents. 
		
		"""

		'''

		The calculation of the implementation of the instrument is calculated bassed on the gap between the maximum
		possible value for that instrument (arbitrarly chosen) and the current value of the instrument being looked at.
		The equation that is used to calculate the impact of an instrument is given by:
		new value = old value + (max value - old value) * instrument impact
		'''
		self.agenda_instrument = agenda_instrument
		self.instruments = instruments
		
		# print(self.instruments)

		self.instrument_campSites = instrument_campSites
		self.instrument_planting = instrument_planting
		self.instrument_prevention = instrument_prevention
		self.firefighter_force = firefighter_force

		prob_update = [thin_burning_probability, self.firefighter_force]

		if agenda_instrument != None:
			# print('Lala - There is an agenda instrument')
			# print(instruments[self.agenda_instrument])
			# S1
			if instruments[self.agenda_instrument][0] > 0: # The limit increase is set at 50%
				# print('This could be a drill: '  + str(self.instrument_campSites))
				# print('This instrument has a value of: ' + str(instruments[self.agenda_instrument][0]))
				self.instrument_campSites = self.instrument_campSites + (0.5 - self.instrument_campSites)*instruments[self.agenda_instrument][0]
				# print('This is just a drill: '  + str(self.instrument_campSites))
			else:
				self.instrument_campSites = self.instrument_campSites + self.instrument_campSites*instruments[self.agenda_instrument][0]
			# S2
			if instruments[self.agenda_instrument][1] > 0:
				self.instrument_planting = self.instrument_planting + (0.5 - self.instrument_planting)*instruments[self.agenda_instrument][1]
			else:
				self.instrument_planting = self.instrument_planting + self.instrument_planting*instruments[self.agenda_instrument][1]
			# S3
			if instruments[self.agenda_instrument][2] > 0:
				prob_update[0] = prob_update[0] + (0.01 - prob_update[0])*instruments[self.agenda_instrument][2]
			else:
				prob_update[0] = prob_update[0] + prob_update[0]*instruments[self.agenda_instrument][2]
			# S4
			if instruments[self.agenda_instrument][3] > 0:
				# print('This is not a test: ' + str(prob_update[1] + (0.5 - prob_update[1])*instruments[self.agenda_instrument][3]))
				prob_update[1] = prob_update[1] + (0.5 - prob_update[1])*instruments[self.agenda_instrument][3]
			else:
				# print('This is not a test: ' + str(prob_update[1] + prob_update[1]*instruments[self.agenda_instrument][3]))
				prob_update[1] = prob_update[1] + prob_update[1]*instruments[self.agenda_instrument][3]
			# S5
			if instruments[self.agenda_instrument][4] > 0:
				self.instrument_prevention = self.instrument_prevention + (0.5 - self.instrument_prevention)*instruments[self.agenda_instrument][4]
			else:
				self.instrument_prevention = self.instrument_prevention + self.instrument_prevention*instruments[self.agenda_instrument][4]


		print('  ')
		print('Warning, the order in which these tasks are performed matters! Shuffling might be needed!')
		print('  ')

		# Policies related to S1
		for agents in self.cells_repository:
			
			if (agents.condition == "Empty" or agents.condition == "Thin forest") and random.random() < instrument_campSites:
				agents.condition = "Camp site"

		# Policies related to S2
		for agents in self.cells_repository:
			if (agents.condition == "Empty") and random.random() < instrument_planting:
				agents.condition == "Thin forest"

		# Policies related to S3
		# There is none - it is a discrete change in the probability

		# Policies related to S4
		# There is none - it is a discrete change in the probability

		# Policies related to S5:
		for agents in self.cells_repository:
			if (agents.condition == "Thin forest" or agents.condition == "Thick forest" \
				or agents.condition == "Camp site" ) and random.random() < instrument_prevention:
				agents.condition = "Empty"

		# For the update of the burning and firefighter probabilities
		return prob_update
