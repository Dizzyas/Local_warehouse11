"""
AI模型训练完整流程示例
=====================
本示例展示从数据准备到模型评估的完整AI模型训练流程
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("AI模型训练完整流程")
print("=" * 60)

# 1. 加载数据集
print("\n步骤 1: 加载数据集")
print("-" * 60)
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"数据集名称: 鸢尾花数据集 (Iris Dataset)")
print(f"样本数量: {X.shape[0]}")
print(f"特征数量: {X.shape[1]}")
print(f"类别数量: {len(np.unique(y))}")
print(f"特征名称: {feature_names}")
print(f"类别名称: {list(target_names)}")

# 2. 数据探索
print("\n步骤 2: 数据探索")
print("-" * 60)
print("前5个样本:")
for i in range(5):
    print(f"  样本 {i+1}: 特征={X[i]}, 类别={target_names[y[i]]}")

# 3. 数据预处理 - 划分数据集
print("\n步骤 3: 划分数据集")
print("-" * 60)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"训练集大小: {X_train.shape[0]} 个样本")
print(f"测试集大小: {X_test.shape[0]} 个样本")

# 4. 数据预处理 - 特征标准化
print("\n步骤 4: 特征标准化")
print("-" * 60)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✓ 特征已标准化（均值为0，方差为1）")

# 5. 创建并训练模型
print("\n步骤 5: 创建并训练模型")
print("-" * 60)
model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train_scaled, y_train)
print("✓ 逻辑回归模型训练完成")
print(f"  模型参数: max_iter=200")

# 6. 模型预测
print("\n步骤 6: 模型预测")
print("-" * 60)
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)
print("✓ 测试集预测完成")
print(f"  预测类别示例: {y_pred[:5]}")
print(f"  预测概率示例:\n{y_pred_proba[:3]}")

# 7. 模型评估
print("\n步骤 7: 模型评估")
print("-" * 60)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"准确率: {accuracy:.4f} ({accuracy*100:.2f}%)")
print()
print("混淆矩阵:")
print(conf_matrix)
print()
print("分类报告:")
print(classification_report(y_test, y_pred, target_names=target_names))

# 8. 可视化结果
print("\n步骤 8: 结果可视化")
print("-" * 60)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 子图1：特征分布
axes[0, 0].scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50, alpha=0.6)
axes[0, 0].set_xlabel('花萼长度')
axes[0, 0].set_ylabel('花萼宽度')
axes[0, 0].set_title('鸢尾花数据集特征分布')

# 子图2：混淆矩阵
im = axes[0, 1].imshow(conf_matrix, interpolation='nearest', cmap='Blues')
axes[0, 1].set_title('混淆矩阵')
tick_marks = np.arange(len(target_names))
axes[0, 1].set_xticks(tick_marks)
axes[0, 1].set_yticks(tick_marks)
axes[0, 1].set_xticklabels(target_names, rotation=45)
axes[0, 1].set_yticklabels(target_names)

# 在混淆矩阵中添加数值
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        axes[0, 1].text(j, i, format(conf_matrix[i, j], 'd'),
                       ha="center", va="center", color="black")

# 子图3：预测结果对比
axes[1, 0].scatter(range(len(y_test)), y_test, 
                   c='blue', label='真实值', alpha=0.6, s=100)
axes[1, 0].scatter(range(len(y_pred)), y_pred, 
                   c='red', label='预测值', alpha=0.6, s=100, marker='x')
axes[1, 0].set_xlabel('样本索引')
axes[1, 0].set_ylabel('类别')
axes[1, 0].set_title('真实值 vs 预测值')
axes[1, 0].legend()
axes[1, 0].set_yticks([0, 1, 2])
axes[1, 0].set_yticklabels(target_names)

# 子图4：特征重要性（系数绝对值平均）
feature_importance = np.abs(model.coef_).mean(axis=0)
axes[1, 1].barh(feature_names, feature_importance)
axes[1, 1].set_xlabel('重要性')
axes[1, 1].set_title('特征重要性')

plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("模型训练流程完成！")
print("=" * 60)
