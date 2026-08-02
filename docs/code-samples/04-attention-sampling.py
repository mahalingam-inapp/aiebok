"""Scaled dot-product attention and temperature sampling without dependencies."""
from math import exp, sqrt
from random import Random


def softmax(values, temperature=1.0):
    scaled = [v / temperature for v in values]; peak = max(scaled)
    weights = [exp(v - peak) for v in scaled]; total = sum(weights)
    return [w / total for w in weights]


def attention(query, keys, values):
    scores = [sum(q * k for q, k in zip(query, key)) / sqrt(len(query)) for key in keys]
    weights = softmax(scores)
    output = [sum(weight * value[i] for weight, value in zip(weights, values)) for i in range(len(values[0]))]
    return weights, output


weights, output = attention([1, 0], [[1, 0], [0, 1]], [[10, 0], [0, 10]])
print("attention_weights=", [round(x, 3) for x in weights], "output=", [round(x, 3) for x in output])
for temperature in (0.3, 1.0, 2.0):
    probabilities = softmax([3.0, 2.0, 1.0], temperature)
    print(f"temperature={temperature}: {[round(x, 3) for x in probabilities]}")
