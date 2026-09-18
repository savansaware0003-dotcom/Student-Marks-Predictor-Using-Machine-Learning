import pandas as pd


def generate_statistics(data):
    """Generate basic statistical information."""

    numeric_columns = [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Score",
        "Final_Marks"
    ]

    return data[numeric_columns].describe()


def calculate_correlations(data):
    """Calculate correlation between numerical features."""

    numeric_columns = [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Score",
        "Final_Marks"
    ]

    return data[numeric_columns].corr()


def get_average_marks(data):
    """Return average final marks."""

    return data["Final_Marks"].mean()


def get_average_attendance(data):
    """Return average attendance."""

    return data["Attendance"].mean()
