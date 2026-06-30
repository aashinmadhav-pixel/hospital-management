"""Simple appointment booking."""

from datetime import datetime

APPOINTMENTS = []


def book_appointment(patient_id, doctor, date_str):
    """Book an appointment for a patient."""
    appointment = {
        "id": len(APPOINTMENTS) + 1,
        "patient_id": patient_id,
        "doctor": doctor,
        "date": date_str,
        "booked_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    APPOINTMENTS.append(appointment)
    return appointment


def list_appointments():
    """Return all appointments."""
    return APPOINTMENTS
