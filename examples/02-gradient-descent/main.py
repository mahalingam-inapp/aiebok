"""Fit y = wx + b with batch gradient descent."""
DATA = [(0, 1), (1, 3), (2, 5), (3, 7)]
w = b = 0.0
rate = 0.05

for step in range(501):
    dw = db = loss = 0.0
    for x, y in DATA:
        error = (w * x + b) - y
        loss += error * error
        dw += 2 * error * x / len(DATA)
        db += 2 * error / len(DATA)
    w -= rate * dw
    b -= rate * db
    if step % 100 == 0:
        print(f"step={step:3d} loss={loss/len(DATA):.6f} w={w:.3f} b={b:.3f}")
