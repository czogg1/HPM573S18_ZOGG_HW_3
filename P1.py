#Cheryl Zogg HW3 - Problem 1

#defining the master class
class Patient:
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


#establishing the patient types
class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        return [self.name, 'Emergency Patient']

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        return [self.name, 'Hospitalized Patient']


#defining hospital and its functions
class Hospital:
    def __init__(self, patients, cost):
        self.patients = patients
        self.cost = cost

    def admit(self, people):
        self.patients.append(people)                              #add individual patients and internally store them
                                                                        #self. internally storing
                                                                        #patients. list it is going into
                                                                        #people what is being added

    def get_total_cost(self):                                     #calculating total cost for the day
        cost = self.cost
        for patient in self.patients:
            if type(patient) == EmergencyPatient:
                cost += 1000
            elif type(patient) == HospitalizedPatient:
                cost += 2000
        return cost

    def discharge_all(self):
        for patient in self.patients:
            print(patient.discharge())                              #print list of patients discharged

        print('Total cost for the day =', self.get_total_cost())    #print total cost for the day

        self.patients.clear()                                       #remove patients from admitted list



#############
#testing code

#defining patients and hospital
P1 = EmergencyPatient(name='Amy A.')
P2 = EmergencyPatient(name='Bob B.')
P3 = EmergencyPatient(name='Charlie C.')
P4 = HospitalizedPatient(name='Denise D.')
P5 = HospitalizedPatient(name='Ellory E.')

myHospital = Hospital(patients=[], cost=0)

#admitting patients
myHospital.admit(P1)
myHospital.admit(P2)
myHospital.admit(P3)
myHospital.admit(P4)
myHospital.admit(P5)

#print(myHospital.patients) #checking that admit worked


#calling discharge function
    #three results:
    # 1. print discharge list
    # 2. invoke get_total_cost function and print the result
    # 3. remove patients from admitted patient list
myHospital.discharge_all()

#print(myHospital.patients) #checking that discharge worked
