import numpy as np
import matplotlib.pyplot as plt


# Apply professional built-in Matplotlib style
plt.style.use("seaborn-v0_8")


def create_subplots_overview():
    """Create and save a 2x2 grid of different plot types."""

    # Create 2x2 subplot grid
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # ---------------------------------------------------------
    # [0, 0] Line Plot — Sine Wave
    # ---------------------------------------------------------
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    ax[0, 0].plot(x, y)
    ax[0, 0].set_title("Sine Wave")
    ax[0, 0].set_xlabel("X")
    ax[0, 0].set_ylabel("sin(X)")

    # ---------------------------------------------------------
    # [0, 1] Bar Plot — ML Model Accuracy
    # ---------------------------------------------------------
    models = ["Logistic Reg", "Random Forest", "SVM", "XGBoost"]
    accuracy = [0.84, 0.91, 0.87, 0.94]

    # Highlight XGBoost
    colors = [
        "steelblue",
        "steelblue",
        "steelblue",
        "darkorange"
    ]

    ax[0, 1].bar(
        models,
        accuracy,
        color=colors
    )

    ax[0, 1].set_title("ML Model Accuracy")
    ax[0, 1].set_xlabel("Model")
    ax[0, 1].set_ylabel("Accuracy")

    # Annotate the best model
    best_index = np.argmax(accuracy)
    best_model = models[best_index]
    best_accuracy = accuracy[best_index]

    ax[0, 1].annotate(
        "Best",
        xy=(best_model, best_accuracy),
        xytext=(0, 20),
        textcoords="offset points",
        ha="center",
        arrowprops=dict(arrowstyle="->")
    )

    # ---------------------------------------------------------
    # [1, 0] Scatter Plot — Random Relationship
    # ---------------------------------------------------------
    x_random = np.random.randn(100)
    y_random = np.random.randn(100)

    ax[1, 0].scatter(x_random, y_random)
    ax[1, 0].set_title("Random Scatter Plot")
    ax[1, 0].set_xlabel("X")
    ax[1, 0].set_ylabel("Y")

    # ---------------------------------------------------------
    # [1, 1] Histogram — Normal Distribution
    # ---------------------------------------------------------
    data = np.random.normal(
        loc=50,
        scale=10,
        size=1000
    )

    ax[1, 1].hist(data, bins=30)
    ax[1, 1].set_title("Normal Distribution")
    ax[1, 1].set_xlabel("Value")
    ax[1, 1].set_ylabel("Frequency")

    # Improve subplot spacing
    plt.tight_layout()

    # Save the complete figure
    plt.savefig("subplots_overview.png", dpi=300)

    # Close figure
    plt.close(fig)


def plot_training_curve(train_loss, val_loss):
    """
    Plot training and validation loss over epochs
    and save the figure as a PNG.
    """

    epochs = range(1, len(train_loss) + 1)

    # Create single axes
    fig, ax = plt.subplots(figsize=(8, 5))

    # Training loss — solid line
    ax.plot(
        epochs,
        train_loss,
        label="Training Loss",
        linestyle="-"
    )

    # Validation loss — dashed line
    ax.plot(
        epochs,
        val_loss,
        label="Validation Loss",
        linestyle="--"
    )

    ax.set_title("Training vs Validation Loss")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")

    # Annotate where overfitting starts
    ax.annotate(
        "Overfitting starts",
        xy=(9, val_loss[8]),
        xytext=(6.5, 0.65),
        arrowprops=dict(arrowstyle="->"),
    )

    # Show legend
    ax.legend()

    plt.tight_layout()

    # Save training curve
    plt.savefig("training_curve.png", dpi=300)

    # Close figure
    plt.close(fig)


def main():
    """Run both plotting tasks."""

    # Create 2x2 subplot figure
    create_subplots_overview()

    # Fake decreasing training loss for 10 epochs
    train_loss = [
        0.95, 0.80, 0.68, 0.57, 0.48,
        0.41, 0.35, 0.30, 0.26, 0.23
    ]

    # Validation loss starts increasing around epoch 9
    val_loss = [
        1.00, 0.87, 0.75, 0.66, 0.59,
        0.54, 0.51, 0.49, 0.48, 0.50
    ]

    # Create training curve
    plot_training_curve(train_loss, val_loss)

    print("Plots created successfully!")
    print("1. subplots_overview.png")
    print("2. training_curve.png")


if __name__ == "__main__":
    main()
