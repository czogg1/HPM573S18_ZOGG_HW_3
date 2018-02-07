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
        print(self.name, 'Emergency Patient')

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        print(self.name, 'Hospitalized Patient')


#defining hospital and its functions
class Hospital:
    def __init__(self):
        self.patients = []
        self.cost = 0

    def admit(self, people):
        self.patients.append(people)                              #add individual patients and internally store them
                                                                        #self. - internally storing
                                                                        #patients. - list it is going into
                                                                        #people - what is being added

    def discharge_all(self):
        for patient in self.patients:
            patient.discharge()                                   #call list of patients discharged

            if type(patient) == EmergencyPatient:                 #update cost on discharge
                self.cost += 1000
            elif type(patient) == HospitalizedPatient:
                self.cost += 2000

        self.patients.clear()                                     #remove patients from admitted list


    def get_total_cost(self):                                     #return total cost for the day
        return self.cost


#############
#testing code

#defining patients and hospital
P1 = EmergencyPatient(name='Amy A.')
P2 = EmergencyPatient(name='Bob B.')
P3 = EmergencyPatient(name='Charlie C.')
P4 = HospitalizedPatient(name='Denise D.')
P5 = HospitalizedPatient(name='Ellory E.')

myHospital = Hospital()

#admitting patients
myHospital.admit(P1)
myHospital.admit(P2)
myHospital.admit(P3)
myHospital.admit(P4)
myHospital.admit(P5)

#print(myHospital.patients) #checking that admit worked

#calling discharge function:
    # 1. print discharge list
    # 2. update cost
    # 3. remove patients from admitted patient list
myHospital.discharge_all()

#print(myHospital.patients) #checking that discharge worked

#getting total cost for the day
print(myHospital.get_total_cost())