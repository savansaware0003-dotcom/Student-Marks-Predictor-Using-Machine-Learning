import unittest
import pandas as pd

from src.data_loader import load_data, validate_data
from src.preprocessing import prepare_data, split_data
from src.model_training import create_model, train_model
from src.prediction import validate_input, predict_marks


class TestStudentMarksPredictor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = load_data(
            "data/student_performance.csv"
        )

    def test_dataset_not_empty(self):
        self.assertGreater(len(self.data), 0)

    def test_dataset_validation(self):
        self.assertTrue(validate_data(self.data))

    def test_required_columns(self):
        required = [
            "Student_ID",
            "Study_Hours",
            "Attendance",
            "Previous_Marks",
            "Assignment_Score",
            "Final_Marks"
        ]

        for column in required:
            self.assertIn(column, self.data.columns)

    def test_prepare_data(self):
        X, y = prepare_data(self.data)

        self.assertEqual(X.shape[1], 4)
        self.assertEqual(len(X), len(y))

    def test_model_training(self):
        X, y = prepare_data(self.data)

        X_train, X_test, y_train, y_test = split_data(X, y)

        model = create_model()
        trained_model = train_model(
            model,
            X_train,
            y_train
        )

        predictions = trained_model.predict(X_test)

        self.assertEqual(
            len(predictions),
            len(y_test)
        )

    def test_input_validation(self):
        self.assertTrue(
            validate_input(5, 80, 70, 75)
        )

    def test_prediction(self):
        X, y = prepare_data(self.data)

        X_train, X_test, y_train, y_test = split_data(X, y)

        model = create_model()

        train_model(
            model,
            X_train,
            y_train
        )

        prediction = predict_marks(
            model,
            6,
            85,
            75,
            80
        )

        self.assertGreaterEqual(prediction, 0)
        self.assertLessEqual(prediction, 100)


if __name__ == "__main__":
    unittest.main()
