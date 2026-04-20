"""
练习答案：分类算法
==================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

print("=" * 60)
print("练习答案：分类算法")
print("=" * 60)

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ==================== 练习1答案 ====================
print("\n练习 1: 决策树分类器")
print("-" * 60)

# 创建决策树分类器
dt_model = DecisionTreeClassifier(random_state=42)

# 训练模型
dt_model.fit(X_train, y_train)

# 预测并计算准确率
y_pred_dt = dt_model.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)

print(f"决策树准确率: {accuracy_dt:.4f}")
print("\n混淆矩阵:")
print(confusion_matrix(y_test, y_pred_dt))

# ==================== 练习2答案 ====================
print("\n练习 2: 随机森林分类器")
print("-" * 60)

for n_est in [50, 100, 200]:
    rf_model = RandomForestClassifier(n_estimators=n_est, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    print(f"n_estimators={n_est}: 准确率 = {accuracy_rf:.4f}")

print("\n说明：增加树的数量通常会提高性能，但也会增加计算成本。")

# ==================== 练习3答案 ====================
print("\n练习 3: 特征重要性分析")
print("-" * 60)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 获取特征重要性
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

print("特征重要性排序:")
for i in indices:
    print(f"  {iris.feature_names[i]}: {importances[i]:.4f}")

# 可视化
plt.figure(figsize=(8, 5))
plt.bar(range(len(importances)), importances[indices])
plt.xticks(range(len(importances)), [iris.feature_names[i] for i in indices], rotation=45)
plt.ylabel('重要性')
plt.title('随机森林特征重要性')
plt.tight_layout()
plt.show()

# ==================== 练习4答案 ====================
print("\n练习 4: 多分类评估指标")
print("-" * 60)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

print("分类报告:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 计算每个类别的精确率和召回率
from sklearn.metrics import precision_recall_fscore_support

precision, recall, f1, support = precision_recall_fscore_support(y_test, y_pred)

print("\n各类别指标:")
for i, name in enumerate(iris.target_names):
    print(f"  {name}:")
    print(f"    精确率: {precision[i]:.4f}")
    print(f"    召回率: {recall[i]:.4f}")
    print(f"    F1分数: {f1[i]:.4f}")
    print(f"    样本数: {support[i]}")

# ==================== 拓展练习答案 ====================
print("\n拓展练习: 不平衡数据处理")
print("-" * 60)

# 生成不平衡数据
np.random.seed(42)
X_imbalanced = np.random.rand(1000, 2)
y_imbalanced = np.random.choice([0, 1], size=1000, p=[0.9, 0.1])

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_imbalanced, y_imbalanced, test_size=0.2, random_state=42, stratify=y_imbalanced
)

print("原始类别分布:")
print(f"  类别 0: {np.sum(y_train_i == 0)} 个")
print(f"  类别 1: {np.sum(y_train_i == 1)} 个")

# 不使用 class_weight
model_no_weight = LogisticRegression(max_iter=200, random_state=42)
model_no_weight.fit(X_train_i, y_train_i)
y_pred_no_weight = model_no_weight.predict(X_test_i)

print("\n不使用 class_weight:")
print(classification_report(y_test_i, y_pred_no_weight, target_names=['类0', '类1']))

# 使用 class_weight='balanced'
model_balanced = LogisticRegression(max_iter=200, random_state=42, class_weight='balanced')
model_balanced.fit(X_train_i, y_train_i)
y_pred_balanced = model_balanced.predict(X_test_i)

print("\n使用 class_weight='balanced':")
print(classification_report(y_test_i, y_pred_balanced, target_names=['类0', '类1']))

print("\n说明：class_weight='balanced' 自动调整类别权重，")
print("      使模型更关注少数类，提高对少数类的识别能力。")

print("\n" + "=" * 60)
print("所有练习完成！")
print("=" * 60)
