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

#defining hospital functions
class Hospital:
    def __init__(self, patients):
        self.patients = patients

    def admit(self):
        admit_total = 0
        i=0
        for patient in self.patients:
            admit_total += 1
            i += 1
        return admit_total

    def discharge_all(self):
        discharges = dict()
        for patient in self.patients:
            discharges[patient.name] = patient.discharge()
        return discharges

    def get_total_cost(self):
        cost = 0
        i=0
        for patient in self.patients:
            if patient.discharge() == [patient.name, 'Emergency Patient']:
                cost += 1000
            elif patient.discharge() == [patient.name, 'Hospitalized Patient']:
                cost += 2000
            i += 1
        return cost


#######################
#testing code
P1 = EmergencyPatient(name='Amy A.')
P2 = EmergencyPatient(name='Bob B.')
P3 = EmergencyPatient(name='Charlie C.')
P4 = HospitalizedPatient(name='Denise D.')
P5 = HospitalizedPatient(name='Ellory E.')

Hospital = Hospital(patients=[P1, P2, P3, P4, P5])

#running hospital functions
print(Hospital.admit(), Hospital.discharge_all())
print(Hospital.get_total_cost())
