import numpy as np

def mean_absolute_error(y_true, y_pred):
    n = len(y_true)
    var = sum(abs(y_true[i] - y_pred[i]) for i in range(n)) / n
    return var

actual = [2, 4, 6, 8, 10]
predicted = [1.5, 4.2, 5.8, 7.5, 9.8]

var_res = mean_absolute_error(actual, predicted)

print("Reg No: 111722202019")
print(f"MAE: {var_res}")
