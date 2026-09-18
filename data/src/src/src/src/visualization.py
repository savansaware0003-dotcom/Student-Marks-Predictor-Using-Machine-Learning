import matplotlib.pyplot as plt


def plot_study_hours_vs_marks(data):
    """Create a graph of study hours versus final marks."""

    plt.figure(figsize=(8, 5))

    plt.scatter(
        data["Study_Hours"],
        data["Final_Marks"],
        color="blue",
        alpha=0.7
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Final Marks")
    plt.title("Study Hours vs Final Marks")
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("outputs/study_hours_vs_marks.png")
    plt.show()


def plot_actual_vs_predicted(actual, predicted):
    """Create actual versus predicted marks graph."""

    plt.figure(figsize=(8, 5))

    plt.scatter(
        actual,
        predicted,
        color="green",
        alpha=0.7
    )

    minimum = min(min(actual), min(predicted))
    maximum = max(max(actual), max(predicted))

    plt.plot(
        [minimum, maximum],
        [minimum, maximum],
        color="red",
        linestyle="--",
        label="Perfect Prediction"
    )

    plt.xlabel("Actual Marks")
    plt.ylabel("Predicted Marks")
    plt.title("Actual vs Predicted Marks")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("outputs/actual_vs_predicted.png")
    plt.show()
