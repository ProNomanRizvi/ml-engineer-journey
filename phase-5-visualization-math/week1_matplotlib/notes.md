# Week 1 — Matplotlib

## Industry context
Matplotlib is the workhorse visualization library in the Python ML stack —
used alongside NumPy and Pandas for EDA, model comparison charts, and
training diagnostics. Seaborn and Plotly build on top of it for statistical
plots and interactive dashboards respectively, but Matplotlib remains the
lowest-level, most controllable option and the one production code defaults
to.

## Core concepts

**Figure vs Axes**
- `Figure` = the whole canvas/page.
- `Axes` = a single plot living inside that canvas (confusingly not the
  same as "axis" — an Axes has an x-axis and a y-axis).

**Two APIs**
- Pyplot (state-based): `plt.plot(...)` — implicit "current axes", fine for
  quick throwaway scripts.
- Object-oriented (OO): `fig, ax = plt.subplots()` then `ax.plot(...)` —
  explicit, reusable, and the standard for production code, multi-panel
  figures, and any plotting logic wrapped in a function.

**`plt.subplots(nrows, ncols)`**
- First argument = rows, second = columns.
- `(1, 1)` → single Axes object (not an array).
- `(1, N)` or `(N, 1)` → 1D array of Axes, indexed `axes[i]`.
- `(N, M)` with both > 1 → 2D array of Axes, indexed `axes[row, col]`.

**Plot types and when to use them**
- Line (`ax.plot`) — trends over ordered/continuous data (time series,
  training curves).
- Bar (`ax.bar`) — comparing categories (e.g. accuracy across models).
- Scatter (`ax.scatter`) — relationship between two continuous variables.
- Histogram (`ax.hist`) — distribution shape of a single variable.

**Housekeeping**
- `plt.tight_layout()` — fixes overlapping labels/titles in multi-subplot
  figures.
- `plt.savefig(path, dpi=300)` — save for reports/portfolio instead of only
`plt.show()`.
- `plt.close(fig)` — releases the figure from memory; matters when
  generating many plots in a loop or pipeline.

## Task
`01_matplotlib_basics.py`
- 2x2 OO-style subplot grid: sine wave (line), fake ML model accuracy
  (bar), random relationship (scatter), normal distribution (histogram).
- Each subplot has a title, xlabel, ylabel.
- Separate `plot_training_curve()` function plotting training vs.
  validation loss on one Axes with a legend — deliberately added beyond
  the roadmap since loss curves are one of the most common ML-specific
  visualizations in real work.

## Output
- `subplots_overview.png`
- `training_curve.png`

---

# Week 1 — Seaborn

## Industry context
Seaborn builds on top of Matplotlib and targets statistical EDA — it's
designed for insight discovery, not deployment. Where Matplotlib gives
full manual control, Seaborn trades some of that control for speed:
it's DataFrame-first, understands categorical grouping natively, and
produces statistically-aware plots (distributions, correlations) in far
fewer lines.

## Core concepts

**DataFrame-first API**
- Matplotlib: pass raw arrays (`ax.plot(x, y)`).
- Seaborn: pass a DataFrame + column names
  (`sns.scatterplot(data=df, x="age", y="income", hue="gender")`).

**`hue` parameter**
- Encodes a third categorical column as color automatically. Doing this
  manually in Matplotlib would mean looping and plotting each category
  separately.

**Plot types and when to use them**
- Heatmap (`sns.heatmap`) — color-coded matrix, most commonly used for
  a correlation matrix to spot related features before modeling.
- Pairplot (`sns.pairplot`) — scatter plot for every numeric column pair
  in a grid, with distributions on the diagonal; fast way to get a full
  dataset overview in one call.
- Boxplot (`sns.boxplot`) — distribution (median, quartiles, outliers)
  of a numeric variable across categories.
- Distribution plot (`sns.histplot`, `kde=True`) — histogram with an
  optional smooth density curve overlay, can be split by `hue`.

**Housekeeping**
- `sns.set_theme()` — Seaborn-native equivalent of `plt.style.use()`;
  applied once, globally, at the top of the file.
- Seaborn plots still return Matplotlib `Axes` objects underneath, so
  everything learned about `ax`, `savefig`, and `close` still applies.
- `sns.pairplot()` returns a `PairGrid`, not an `Axes` — save it with
  `grid.savefig(...)` and close with `plt.close(grid.fig)`, and set its
  title via `grid.fig.suptitle(...)` since `plt.title()` doesn't apply.

**Polish**
- `np.triu()` as a `mask` on `sns.heatmap()` hides the redundant upper
  triangle of a symmetric correlation matrix.
- `corner=True` on `sns.pairplot()` does the same for pairplots — only
  the lower triangle + diagonal are shown, freeing up space for the
  legend.

## Task
`02_seaborn_eda.py`
- Fake ML dataset (`age`, `salary`, `experience_years`, `department`)
  built with `pandas`/`numpy`.
- Four EDA plots, each in its own function and saved to its own PNG:
  correlation heatmap (masked), pairplot (cornered, colored by
  `department`), salary boxplot by department, salary distribution
  with KDE overlay.

## Output
- `correlation_heatmap.png`
- `pairplot.png`
- `salary_boxplot.png`
- `salary_distribution.png`