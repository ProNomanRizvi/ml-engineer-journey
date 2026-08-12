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
    """
    Create and save the individual age histogram.

    This remains a real Plotly histogram as requested.
    """

    fig = px.histogram(
        df,
        x="age",
        color="department",
        barmode="overlay",
        opacity=0.6,
        title="Age Distribution by Department"
    )

    fig.write_html("age_histogram.html")

    return fig


def create_dashboard_age_chart(df):
    """
    Create a dashboard-safe age distribution chart.

    Ages are manually grouped into buckets and then
    plotted using px.bar().
    """

    df = df.copy()

    # Create age buckets
    df["age_bucket"] = pd.cut(
        df["age"],
        bins=[19, 29, 39, 49, 59],
        labels=["20-29", "30-39", "40-49", "50-59"]
    )

    # Count people in each age bucket and department
    age_counts = (
        df.groupby(
            ["age_bucket", "department"],
            observed=False
        )
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        age_counts,
        x="age_bucket",
        y="count",
        color="department",
        barmode="group",
        title="Age Distribution by Department"
    )

    return fig


def plot_experience_line(df):
    """Create and save average salary trend by experience bucket."""

    df = df.copy()

    # Create experience buckets
    df["experience_bucket"] = pd.cut(
        df["experience_years"],
        bins=[-1, 5, 10, 15, 20],
        labels=["0-5", "5-10", "10-15", "15-20"]
    )

    # Calculate average salary
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
    age_dashboard_chart,
    experience_line
):
    """Combine all charts into one 2x2 interactive dashboard."""

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

    # Track which legend names have already appeared
    seen_departments = set()

    def add_traces(fig_source, row, col):
        """
        Add traces from a Plotly figure while preventing
        duplicate legend entries.
        """

        for trace in fig_source.data:

            # Show each department in the legend only once
            if trace.name in seen_departments:
                trace.showlegend = False
            else:
                trace.showlegend = True
                seen_departments.add(trace.name)

            dashboard.add_trace(
                trace,
                row=row,
                col=col
            )

    # ---------------------------------------------------------
    # [1, 1] Salary Scatter
    # ---------------------------------------------------------
    add_traces(
        salary_scatter,
        row=1,
        col=1
    )

    # ---------------------------------------------------------
    # [1, 2] Department Bar
    # ---------------------------------------------------------
    add_traces(
        department_bar,
        row=1,
        col=2
    )

    # ---------------------------------------------------------
    # [2, 1] Dashboard-safe Age Chart
    # ---------------------------------------------------------
    add_traces(
        age_dashboard_chart,
        row=2,
        col=1
    )

    # ---------------------------------------------------------
    # [2, 2] Experience Line
    # ---------------------------------------------------------
    add_traces(
        experience_line,
        row=2,
        col=2
    )

    # Dashboard layout
    dashboard.update_layout(
        title_text="ML Dataset Interactive EDA Dashboard",
        height=900,
        width=1200,
        showlegend=True
    )

    # Save dashboard
    dashboard.write_html("dashboard.html")


def main():
    """Run the complete Plotly dashboard pipeline."""

    # Create dataset
    df = create_dataset()

    print("Dataset created successfully!")
    print(f"Shape: {df.shape}")

    # ---------------------------------------------------------
    # Individual charts
    # ---------------------------------------------------------
    salary_scatter = plot_salary_scatter(df)
    department_bar = plot_department_bar(df)

    # Real interactive histogram for individual HTML
    age_histogram = plot_age_histogram(df)

    experience_line = plot_experience_line(df)

    # ---------------------------------------------------------
    # Dashboard-specific age chart
    # ---------------------------------------------------------
    age_dashboard_chart = create_dashboard_age_chart(df)

    # ---------------------------------------------------------
    # Combined dashboard
    # ---------------------------------------------------------
    create_dashboard(
        salary_scatter,
        department_bar,
        age_dashboard_chart,
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