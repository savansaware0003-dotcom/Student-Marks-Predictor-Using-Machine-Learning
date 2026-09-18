from src.data_loader import load_data, validate_data
from src.data_analysis import (
    generate_statistics,
    calculate_correlations,
    get_average_marks,
    get_average_attendance
)
from src.preprocessing import prepare_data, split_data
from src.model_training import (
    create_model,
    train_model,
    evaluate_model,
    get_predictions
)
from src.prediction import predict_marks, validate_input
from src.visualization import (
    plot_study_hours_vs_marks,
    plot_actual_vs_predicted
)


DATA_PATH = "data/student_performance.csv"


def display_header():
    print("=" * 60)
    print("       STUDENT MARKS PREDICTOR")
    print("       USING MACHINE LEARNING")
    print("=" * 60)


def main():

    display_header()

    # -----------------------------------------
    # MODULE 1: DATA MANAGEMENT
    # -----------------------------------------

    print("\n[1] Loading student dataset...")

    data = load_data(DATA_PATH)

    try:
        validate_data(data)
        print("Dataset validation successful.")
    except ValueError as error:
        print(f"Dataset Error: {error}")
        return

    print(f"Total student records: {len(data)}")

    # -----------------------------------------
    # MODULE 2: DATA ANALYSIS
    # -----------------------------------------

    print("\n[2] Student Performance Analysis")
    print("-" * 40)

    print(f"Average Final Marks: {get_average_marks(data):.2f}")
    print(
        f"Average Attendance: "
        f"{get_average_attendance(data):.2f}%"
    )

    print("\nStatistical Summary:")
    print(generate_statistics(data))

    print("\nCorrelation Matrix:")
    print(calculate_correlations(data).round(2))

    # -----------------------------------------
    # MODULE 3: PREPROCESSING
    # -----------------------------------------

    print("\n[3] Preparing data for Machine Learning...")

    X, y = prepare_data(data)

    X_train, X_test, y_train, y_test = split_data(X, y)

    print(f"Training records: {len(X_train)}")
    print(f"Testing records: {len(X_test)}")

    # -----------------------------------------
    # MODULE 4: MODEL TRAINING
    # -----------------------------------------

    print("\n[4] Training Linear Regression Model...")

    model = create_model()
    train_model(model, X_train, y_train)

    print("Model training completed successfully.")

    # -----------------------------------------
    # MODULE 5: MODEL EVALUATION
    # -----------------------------------------

    print("\n[5] Model Evaluation")
    print("-" * 40)

    metrics = evaluate_model(model, X_test, y_test)

    print(f"Mean Absolute Error: {metrics['MAE']:.2f}")
    print(f"Mean Squared Error: {metrics['MSE']:.2f}")
    print(f"R2 Score: {metrics['R2']:.2f}")

    # -----------------------------------------
    # MODULE 6: VISUALIZATION
    # -----------------------------------------

    print("\n[6] Generating visualizations...")

    predictions = get_predictions(model, X_test)

    plot_study_hours_vs_marks(data)
    plot_actual_vs_predicted(y_test, predictions)

    print("Graphs saved inside the outputs folder.")

    # -----------------------------------------
    # MODULE 7: NEW STUDENT PREDICTION
    # -----------------------------------------

    print("\n" + "=" * 60)
    print("          PREDICT STUDENT MARKS")
    print("=" * 60)

    try:
        study_hours = float(
            input("Enter study hours: ")
        )

        attendance = float(
            input("Enter attendance percentage: ")
        )

        previous_marks = float(
            input("Enter previous marks: ")
        )

        assignment_score = float(
            input("Enter assignment score: ")
        )

        validate_input(
            study_hours,
            attendance,
            previous_marks,
            assignment_score
        )

        prediction = predict_marks(
            model,
            study_hours,
            attendance,
            previous_marks,
            assignment_score
        )

        print("\nPrediction Result")
        print("-" * 40)
        print(
            f"Predicted Final Marks: "
            f"{prediction:.2f}/100"
        )

    except ValueError as error:
        print(f"\nInput Error: {error}")

    print("\n" + "=" * 60)
    print("             PROGRAM COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
