import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Apply Seaborn theme globally
sns.set_theme()


def create_dataset():
    """Create and return a fake ML dataset."""

    np.random.seed(42)

    df = pd.DataFrame({
        "age": np.random.randint(20, 60, 200),
        "salary": np.random.normal(60000, 15000, 200),
        "experience_years": np.random.randint(0, 20, 200),
        "department": np.random.choice(
            ["Engineering", "Sales", "Marketing"],
            200
        )
    })

    return df


def plot_correlation_heatmap(df):
    """Create and save a correlation heatmap."""

    # Calculate correlation matrix
    correlation = df.corr(numeric_only=True)

    # Hide the redundant upper triangle
    mask = np.triu(
        np.ones_like(correlation, dtype=bool)
    )

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()

    plt.savefig(
        "correlation_heatmap.png",
        dpi=300
    )

    plt.close()


def plot_pairplot(df):
    """Create and save a pairplot colored by department."""

    numeric_columns = [
        "age",
        "salary",
        "experience_years"
    ]

    # Show only lower triangle + diagonal
    grid = sns.pairplot(
        df,
        vars=numeric_columns,
        hue="department",
        corner=True
    )

    grid.fig.suptitle(
        "Pairplot of Numeric Features",
        y=1.02
    )

    grid.savefig(
        "pairplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(grid.fig)


def plot_salary_boxplot(df):
    """Create and save salary boxplot by department."""

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df,
        x="department",
        y="salary"
    )

    plt.title("Salary Distribution by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")

    plt.tight_layout()

    plt.savefig(
        "salary_boxplot.png",
        dpi=300
    )

    plt.close()


def plot_salary_distribution(df):
    """Create and save salary distribution plot."""

    plt.figure(figsize=(8, 6))

    sns.histplot(
        data=df,
        x="salary",
        bins=30,
        kde=True
    )

    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        "salary_distribution.png",
        dpi=300
    )

    plt.close()


def main():
    """Run the complete EDA pipeline."""

    # Create fake dataset
    df = create_dataset()

    print("Dataset shape:")
    print(df.shape)

    print("\nFirst 5 rows:")
    print(df.head())

    # Generate EDA plots
    plot_correlation_heatmap(df)
    plot_pairplot(df)
    plot_salary_boxplot(df)
    plot_salary_distribution(df)

    print("\nEDA plots created successfully!")
    print("1. correlation_heatmap.png")
    print("2. pairplot.png")
    print("3. salary_boxplot.png")
    print("4. salary_distribution.png")


if __name__ == "__main__":
    main()