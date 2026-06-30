"""Patient model and storage helpers."""

import json
from pathlib import Path

DATA_FILE = Path("data/patients.json")


def load_patients():
    """Load patients from JSON file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_patients(patients):
    """Save patients to JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(patients, f, indent=2)


def add_patient(name, age, condition):
    """Add a new patient and return the created record."""
    patients = load_patients()
    patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": age,
        "condition": condition,
    }
    patients.append(patient)
    save_patients(patients)
    return patient


def list_patients():
    """Return all patients."""
    return load_patients()
