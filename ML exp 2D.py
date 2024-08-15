import numpy as np

def mean_squared_error(y_true, y_pred):
    squared_diff = (y_true - y_pred) ** 2
    mse = np.mean(squared_diff)
    return mse

y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.2, 0.0, 2, 8])

mse = mean_squared_error(y_true, y_pred)

print("Reg no: 111722202019")
print(f"mse: {mse}")
