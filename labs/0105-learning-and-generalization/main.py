"""Lab 1.5: Learning and Generalization"""

data = [(1, 0), (2, 0), (3, 1), (4, 1), (5, 2)]
labels = [0, 0, 1, 1, 0]
def mse_line(m, b, pts):
    return sum((m*x + b - y)**2 for x, y in pts) / len(pts)
best = min(((m, b, mse_line(m, b, data)) for m in [0, 0.5, 1.0] for b in [0, 0.5]), key=lambda t: t[2])
holdout = [(6, 1), (7, 1)]
test_err = mse_line(best[0], best[1], holdout)
print({"fit": best[:2], "train_mse": round(best[2], 3), "holdout_mse": round(test_err, 3)})
