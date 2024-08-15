from sklearn.metrics import f1_score

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]

f1 = f1_score(y_true, y_pred)

print("Reg no: 111722202019")
print("F1 Score:", f1)
