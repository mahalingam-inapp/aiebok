"""Lab 2.2: Supervised Learning"""

X = [[1.0, 0.5], [1.0, 1.2], [1.0, 2.0]]
y = [0, 0, 1]
w = [0.0, 0.0]
lr = 0.3
for _ in range(30):
    for xi, yi in zip(X, y):
        z = sum(wj*xij for wj, xij in zip(w, xi))
        pred = 1 / (1 + pow(2.718281828, -z))
        err = pred - yi
        w = [wj - lr * err * xij for wj, xij in zip(w, xi)]
print("weights:", [round(v, 3) for v in w])
