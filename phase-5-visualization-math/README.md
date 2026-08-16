# Phase 5 — Data Visualization + Math for ML

5 weeks | Month 3-4 | 4 hrs/day

## Progress

| Week | Topic | Status |
|---|---|---|
| Week 1 | Matplotlib | ✅ Done |
| Week 1 | Seaborn | ✅ Done |
| Week 2 | Plotly Express | ✅ Done |
| Week 2-3 | Linear Algebra | ✅ Done |
| Week 3-4 | Calculus | ✅ Done |
| Week 4-5 | Statistics | ✅ Done |
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
├── week2_ploty_express/
│ ├── plotly_dashboard.py
│ ├── notes.md
│ ├── salary_scatter.html
│ ├── department_bar.html
│ ├── age_histogram.html
│ ├── experience_line.html
│ └── dashboard.html
└── week3_linear_algebra/
├── linear_algebra_basics.py
└── notes.md
└── week4_calculas/
├── calculus_basics.py
└── notes.md
└── week4_calculas_statistics/
├── calculus_basics.py
├── 01_central_tendency_spread.py
├── 02_normal_distribution.py
├── 03_binomial_distribution.py
├── 04_bayes_medical_test.py
├── 05_correlation.py
├── 06_hypothesis_testing.py
└── notes.md
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

**Week 2-3 — Linear Algebra:** Vectors (addition, subtraction, dot
product, norm), matrices (`@` vs `*`, transpose, inverse verified
against the identity matrix), and eigenvalues/eigenvectors — all
implemented and numerically verified in NumPy rather than left as
theory. Capped with a practical demo: solving Linear Regression via the
Normal Equation in one line, confirming the closed-form solution
recovers the exact known coefficients without gradient descent.

**Week 3-4 — Calculus:** Derivatives (symbolic vs. numerical central
difference), the chain rule on a composite function, partial
derivatives, and the gradient vector — every result checked two ways
rather than taken on faith. Closed with a working Gradient Descent loop
that converges `(x, y) = (10, 10)` down to near the true minimum at the
origin, and a sigmoid activation derivative (backprop-relevant, beyond
the base roadmap) verified the same way.

**Week 4-5 — Statistics:** Central tendency and spread (mean vs. median
robustness to outliers), the normal distribution (68-95-99.7 rule
verified empirically), the binomial distribution (Law of Large Numbers
demonstrated experimentally), Bayes' theorem (rare-disease example
showing the base-rate effect, cross-checked against a manual
natural-frequencies calculation), and correlation (engineered vs.
random relationships, with a correlation ≠ causation note). Extended
beyond the base roadmap with hypothesis testing — an independent t-test
comparing model accuracy scores across two scenarios (a real difference
vs. no real difference), since p-values and significance testing are
used throughout ML engineering to evaluate models and A/B tests.