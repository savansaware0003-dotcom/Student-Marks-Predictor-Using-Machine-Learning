import pandas as pd


REQUIRED_COLUMNS = [
    "Student_ID",
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Score",
    "Final_Marks"
]


def load_data(file_path):
    """Load student data from a CSV file."""
    data = pd.read_csv(file_path)
    return data


def validate_data(data):
    """Validate the dataset structure and values."""

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if data.empty:
        raise ValueError("Dataset is empty.")

    numeric_columns = [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Score",
        "Final_Marks"
    ]

    if data[numeric_columns].isnull().any().any():
        raise ValueError("Dataset contains missing numerical values.")

    if (data["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    for column in [
        "Attendance",
        "Previous_Marks",
        "Assignment_Score",
        "Final_Marks"
    ]:
        if ((data[column] < 0) | (data[column] > 100)).any():
            raise ValueError(
                f"{column} must contain values between 0 and 100."
            )

    return True
