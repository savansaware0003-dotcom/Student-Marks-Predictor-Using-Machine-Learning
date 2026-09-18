from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def create_model():
    """Create Linear Regression model."""

    return LinearRegression()


def train_model(model, X_train, y_train):
    """Train the Machine Learning model."""

    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return {
        "MAE": mae,
        "MSE": mse,
        "R2": r2
    }


def get_predictions(model, X_test):
    """Generate predictions."""

    return model.predict(X_test)
