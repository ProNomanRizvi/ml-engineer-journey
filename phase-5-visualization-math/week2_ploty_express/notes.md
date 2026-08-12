# Week 2 — Plotly Express

## Industry context
Plotly Express is the high-level, interactive counterpart to Matplotlib
and Seaborn. Where those two produce static images, Plotly renders in
the browser via plotly.js — hover for exact values, zoom, pan, toggle
legend items. Most real work starts in Plotly Express for fast
exploration, drops to the lower-level Graph Objects API when precise
control is needed, and only graduates to a full Dash app when
stakeholders need something they can click around in live. This
project's scope stops at Express + combined static-HTML dashboards —
Dash itself is a separate, much larger framework.

## Core concepts

**DataFrame-first, like Seaborn — but interactive**
```python
import plotly.express as px
fig = px.scatter(df, x="age", y="income", color="department")
```
Returns a `Figure` object (plotly.js-backed), not a Matplotlib `Axes`.

**Common chart functions**
- `px.scatter()` — relationships between two continuous variables.
- `px.bar()` — categorical comparison.
- `px.histogram()` — distribution shape.
- `px.line()` — trends over an ordered variable.

**Interactivity**
- `hover_data=[...]` — extra columns shown in the tooltip on hover,
  without them being plotted.
- `color=...` — categorical grouping, same role as Seaborn's `hue`.

**Saving**
- `fig.show()` — opens in browser/notebook.
- `fig.write_html(path)` — saves the interactive chart as a standalone
  HTML file; this is the real deliverable, not a PNG, since the point is
  interactivity.
- `fig.write_image(path)` — static image export (needs the `kaleido`
  package), only if a non-interactive copy is needed.

**Combining charts into one dashboard — Graph Objects territory**
- `plotly.subplots.make_subplots(rows, cols, subplot_titles=(...))`
  creates an empty grid of subplot slots.
- Each Plotly Express `fig` holds its chart data in `fig.data` (a tuple
  of traces). Traces get added into the grid one at a time with
  `dashboard.add_trace(trace, row=..., col=...)`.
- Gotcha: every source figure carries its own legend entries. Copying
  all of them into one combined figure duplicates the legend per
  subplot. Fix: track which trace names have already been added and set
  `trace.showlegend = False` on repeats.
- Gotcha: `px.histogram()` pre-aggregates data into its own binned
  trace. Feeding that trace into a combined subplot grid can render
  incorrectly (stacked/cascading instead of grouped) because the
  combined figure's layout doesn't share the same binning context as
  the original. Reliable fix: bin the data manually first (e.g.
  `pd.cut()` on the numeric column) and build a `px.bar()` on the
  pre-aggregated counts instead of relying on `px.histogram()` inside
  the dashboard.

## Task
`03_plotly_dashboard.py`
- Same synthetic dataset as the Seaborn task (`age`, `salary`,
  `experience_years`, `department`) for consistency across the phase.
- Four interactive charts, each its own function and its own HTML file:
  salary vs. experience scatter (`hover_data` for age), average salary
  by department bar, age distribution by department, and average
  salary by experience bucket (`pd.cut()` into four bins) line chart.
- Combined 2x2 dashboard built with `make_subplots` + `add_trace`,
  fixed for legend duplication and histogram rendering as described
  above.

## Output
- `salary_scatter.html`
- `department_bar.html`
- `age_histogram.html`
- `experience_line.html`
- `dashboard.html`