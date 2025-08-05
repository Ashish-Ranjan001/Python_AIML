import json

# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender
        }

class Patient(Person):
    def __init__(self, name, age, gender, disease):
        super().__init__(name, age, gender)
        self.disease = disease

    def get_details(self):
        details = super().get_details()
        details["Disease"] = self.disease
        return details


class Doctor(Person):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.specialization = specialization

    def get_details(self):
        details = super().get_details()
        details["Specialization"] = self.specialization
        return details

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added.")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor '{doctor.name}' added.")

    def show_patients(self):
        print("\nPatient List:")
        for p in self.patients:
            print(p.get_details())

    def show_doctors(self):
        print("\nDoctor List:")
        for d in self.doctors:
            print(d.get_details())

    def save_data(self):
        data = {
            "patients": [p.get_details() for p in self.patients],
            "doctors": [d.get_details() for d in self.doctors]
        }
        with open("hospital_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved to 'hospital_data.json'.")

# Menu-driven interface
def main():
    hospital = Hospital()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Show Patients")
        print("4. Show Doctors")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Patient Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            disease = input("Disease: ")
            patient = Patient(name, age, gender, disease)
            hospital.add_patient(patient)

        elif choice == "2":
            name = input("Doctor Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            specialization = input("Specialization: ")
            doctor = Doctor(name, age, gender, specialization)
            hospital.add_doctor(doctor)

        elif choice == "3":
            hospital.show_patients()

        elif choice == "4":
            hospital.show_doctors()

        elif choice == "5":
            hospital.save_data()

        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()