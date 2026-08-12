# Phase 5 — Data Visualization + Math for ML

5 weeks | Month 3-4 | 4 hrs/day

## Progress

| Week | Topic | Status |
|---|---|---|
| Week 1 | Matplotlib | ✅ Done |
| Week 1 | Seaborn | ✅ Done |
| Week 2 | Plotly Express | ⏳ Upcoming |
| Week 2-3 | Linear Algebra | ⏳ Upcoming |
| Week 3-4 | Calculus | ⏳ Upcoming |
| Week 4-5 | Statistics | ⏳ Upcoming |
| Week 5 | Gradient Descent from scratch (NumPy) | ⏳ Upcoming |

## Structure
```
phase-5-visualization-math/
└── week1_matplotlib/
├── 01_matplotlib_basics.py
├── 02_seaborn_eda.py
├── notes.md
├── subplots_overview.png
├── training_curve.png
├── correlation_heatmap.png
├── pairplot.png
├── salary_boxplot.png
└── salary_distribution.png
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
