import pandas as pd


def predict_marks(
    model,
    study_hours,
    attendance,
    previous_marks,
    assignment_score
):
    """Predict final marks for a new student."""

    input_data = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks],
        "Assignment_Score": [assignment_score]
    })

    prediction = model.predict(input_data)[0]

    # Keep prediction within realistic marks range.
    prediction = max(0, min(100, prediction))

    return prediction


def validate_input(
    study_hours,
    attendance,
    previous_marks,
    assignment_score
):
    """Validate user input."""

    if study_hours < 0:
        raise ValueError("Study hours cannot be negative.")

    if not 0 <= attendance <= 100:
        raise ValueError("Attendance must be between 0 and 100.")

    if not 0 <= previous_marks <= 100:
        raise ValueError("Previous marks must be between 0 and 100.")

    if not 0 <= assignment_score <= 100:
        raise ValueError(
            "Assignment score must be between 0 and 100."
        )

    return True
