"""Hospital Management System — simple CLI demo."""

from patient import add_patient, list_patients
from appointment import book_appointment, list_appointments


def show_menu():
    print("\n--- Hospital Management ---")
    print("1. Add patient")
    print("2. List patients")
    print("3. Book appointment")
    print("4. List appointments")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Patient name: ")
            age = input("Age: ")
            condition = input("Condition: ")
            patient = add_patient(name, int(age), condition)
            print(f"Added patient #{patient['id']}: {patient['name']}")

        elif choice == "2":
            patients = list_patients()
            if not patients:
                print("No patients yet.")
            for p in patients:
                print(f"  [{p['id']}] {p['name']}, age {p['age']} — {p['condition']}")

        elif choice == "3":
            patient_id = int(input("Patient ID: "))
            doctor = input("Doctor name: ")
            date_str = input("Date (YYYY-MM-DD): ")
            appt = book_appointment(patient_id, doctor, date_str)
            print(f"Booked appointment #{appt['id']} with Dr. {appt['doctor']}")

        elif choice == "4":
            appointments = list_appointments()
            if not appointments:
                print("No appointments yet.")
            for a in appointments:
                print(f"  [{a['id']}] Patient {a['patient_id']} — Dr. {a['doctor']} on {a['date']}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
