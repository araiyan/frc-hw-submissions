patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
	return weight / (height ** 2)
for patient in range(len(patients)):
	weight, height = patients[patient]
	bmi = calculate_bmi(weight, height)
	print "Patient's BMI is:" + str(bmi)