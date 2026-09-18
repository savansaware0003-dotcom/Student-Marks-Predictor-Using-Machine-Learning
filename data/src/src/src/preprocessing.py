from sklearn.model_selection import train_test_split


FEATURE_COLUMNS = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Score"
]

TARGET_COLUMN = "Final_Marks"


def prepare_data(data):
    """Separate features and target."""

    X = data[FEATURE_COLUMNS]
    y = data[TARGET_COLUMN]

    return X, y


def split_data(X, y, test_size=0.2):
    """Split data into training and testing sets."""

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )
