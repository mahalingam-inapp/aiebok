"""Lab 2.4: Neural Networks"""

def relu(x):
    return max(0.0, x)
x, w1, b1, w2, b2 = 1.5, 0.8, -0.2, 1.2, 0.1
hidden = relu(x * w1 + b1)
y = hidden * w2 + b2
loss = (y - 1.0) ** 2
grad_w2 = 2 * (y - 1.0) * hidden
print({"hidden": round(hidden, 3), "y": round(y, 3), "grad_w2": round(grad_w2, 3)})
