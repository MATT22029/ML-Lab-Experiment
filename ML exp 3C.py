from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_scores = [0.9, 0.2, 0.8, 0.7, 0.3, 0.6, 0.1, 0.4, 0.75, 0.5]

fpr, tpr, thresholds = roc_curve(y_true, y_scores)
auc_roc = roc_auc_score(y_true, y_scores)

plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, label=f'AUC = {auc_roc:.2f}')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Random')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.legend()
plt.show()

print("Reg No: 111622201118")
print("AUC-ROC Score:", auc_roc)
