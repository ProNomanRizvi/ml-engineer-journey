# Phase 5 — Data Visualization + Math for ML

5 weeks | Month 3-4 | 4 hrs/day

## Progress

| Week | Topic | Status |
|---|---|---|
| Week 1 | Matplotlib | ✅ Done |
| Week 1 | Seaborn | ✅ Done |
| Week 2 | Plotly Express | ✅ Done |
| Week 2-3 | Linear Algebra | ⏳ Upcoming |
| Week 3-4 | Calculus | ⏳ Upcoming |
| Week 4-5 | Statistics | ⏳ Upcoming |
| Week 5 | Gradient Descent from scratch (NumPy) | ⏳ Upcoming |

## Structure
```
phase-5-visualization-math/
├── week1_matplotlib/
│ ├── 01_matplotlib_basics.py
│ ├── 02_seaborn_eda.py
│ ├── notes.md
│ ├── subplots_overview.png
│ ├── training_curve.png
│ ├── correlation_heatmap.png
│ ├── pairplot.png
│ ├── salary_boxplot.png
│ └── salary_distribution.png
└── week2_ploty_express/
├── plotly_dashboard.py
├── notes.md
├── salary_scatter.html
├── department_bar.html
├── age_histogram.html
├── experience_line.html
└── dashboard.html
```

## Week Highlights

**Week 1 — Matplotlib:** OO-style API (`fig, ax = plt.subplots()`) as the
production standard over pyplot shorthand. 2x2 subplot grid covering line,
bar, scatter, and histogram plots, plus a dedicated training-vs-validation
loss curve function — an ML-specific visualization added beyond the base
roadmap for portfolio relevance. Polished with `plt.style.use()`,
dynamic best-model highlighting via `np.argmax()`, and `ax.annotate()`
call-outs (best model, overfitting onset) to make charts communicate
insight, not just display data.

**Week 1 — Seaborn:** DataFrame-first statistical EDA on top of
Matplotlib — heatmap, pairplot, boxplot, and distribution plots on a
synthetic ML dataset (age, salary, experience, department), with `hue`
for categorical grouping. Polished with `mask` on the heatmap and
`corner=True` on the pairplot to drop the redundant upper triangle from
both.

**Week 2 — Plotly Express:** Interactive, browser-rendered EDA charts
(scatter, bar, histogram, line) on the same synthetic dataset, with
`hover_data` and `color` for interactivity and categorical grouping.
Combined into a single 2x2 dashboard using `make_subplots` and
`add_trace` from Graph Objects — including debugging and fixing two
real integration bugs: duplicated legends across subplots (fixed by
tracking seen trace names and disabling repeats) and a broken histogram
render inside the combined grid (fixed by pre-binning the data and
using `px.bar()` instead of `px.histogram()` for the dashboard view).
