"""Lab 2.5: Evaluation and Error Analysis"""

confusion = {"TP": 40, "FP": 10, "FN": 8, "TN": 142}
def metrics(c):
    prec = c["TP"] / (c["TP"] + c["FP"] + 1e-9)
    rec = c["TP"] / (c["TP"] + c["FN"] + 1e-9)
    return round(prec, 3), round(rec, 3)
slice_b = {"TP": 5, "FP": 12, "FN": 6, "TN": 20}
print("overall:", metrics(confusion))
print("slice_b:", metrics(slice_b))
