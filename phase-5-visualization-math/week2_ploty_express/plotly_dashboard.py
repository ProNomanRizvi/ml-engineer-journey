import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots


def create_dataset():
    """Create and return the fake ML dataset."""

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


def plot_salary_scatter(df):
    """Create and save salary vs experience scatter plot."""

    fig = px.scatter(
        df,
        x="experience_years",
        y="salary",
        color="department",
        hover_data=["age"],
        title="Salary vs Experience"
    )

    fig.write_html("salary_scatter.html")

    return fig


def plot_department_bar(df):
    """Create and save department-wise average salary bar chart."""

    average_salary = (
        df.groupby("department")["salary"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        average_salary,
        x="department",
        y="salary",
        color="department",
        title="Average Salary by Department"
    )

    fig.write_html("department_bar.html")

    return fig


def plot_age_histogram(df):
    """Create and save age distribution histogram."""

    fig = px.histogram(
        df,
        x="age",
        color="department",
        title="Age Distribution by Department"
    )

    fig.write_html("age_histogram.html")

    return fig


def plot_experience_line(df):
    """Create and save average salary trend by experience bucket."""

    # Create four experience buckets
    df = df.copy()

    df["experience_bucket"] = pd.cut(
        df["experience_years"],
        bins=[-1, 5, 10, 15, 20],
        labels=["0-5", "5-10", "10-15", "15-20"]
    )

    # Calculate average salary for each bucket and department
    average_salary = (
        df.groupby(
            ["experience_bucket", "department"],
            observed=False
        )["salary"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        average_salary,
        x="experience_bucket",
        y="salary",
        color="department",
        markers=True,
        title="Average Salary by Experience"
    )

    fig.write_html("experience_line.html")

    return fig


def create_dashboard(
    salary_scatter,
    department_bar,
    age_histogram,
    experience_line
):
    """Combine all Plotly charts into one 2x2 dashboard."""

    dashboard = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Salary vs Experience",
            "Average Salary by Department",
            "Age Distribution by Department",
            "Average Salary by Experience"
        )
    )

    # ---------------------------------------------------------
    # [1, 1] Salary Scatter
    # ---------------------------------------------------------
    for trace in salary_scatter.data:
        dashboard.add_trace(
            trace,
            row=1,
            col=1
        )

    # ---------------------------------------------------------
    # [1, 2] Department Bar
    # ---------------------------------------------------------
    for trace in department_bar.data:
        dashboard.add_trace(
            trace,
            row=1,
            col=2
        )

    # ---------------------------------------------------------
    # [2, 1] Age Histogram
    # ---------------------------------------------------------
    for trace in age_histogram.data:
        dashboard.add_trace(
            trace,
            row=2,
            col=1
        )

    # ---------------------------------------------------------
    # [2, 2] Experience Line
    # ---------------------------------------------------------
    for trace in experience_line.data:
        dashboard.add_trace(
            trace,
            row=2,
            col=2
        )

    # Dashboard title
    dashboard.update_layout(
        title_text="ML Dataset Interactive EDA Dashboard",
        height=900,
        width=1200,
        showlegend=True
    )

    # Save combined dashboard
    dashboard.write_html("dashboard.html")


def main():
    """Run the complete Plotly dashboard pipeline."""

    # Create dataset
    df = create_dataset()

    print("Dataset created successfully!")
    print(f"Shape: {df.shape}")

    # Create individual interactive charts
    salary_scatter = plot_salary_scatter(df)
    department_bar = plot_department_bar(df)
    age_histogram = plot_age_histogram(df)
    experience_line = plot_experience_line(df)

    # Create combined dashboard
    create_dashboard(
        salary_scatter,
        department_bar,
        age_histogram,
        experience_line
    )

    print("\nInteractive HTML files created successfully!")
    print("1. salary_scatter.html")
    print("2. department_bar.html")
    print("3. age_histogram.html")
    print("4. experience_line.html")
    print("5. dashboard.html")


if __name__ == "__main__":
    main()