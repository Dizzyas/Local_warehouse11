"""
分类算法示例代码
================
本示例展示多种分类算法的使用和比较
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# 设置随机种子
np.random.seed(42)

print("=" * 70)
print("分类算法比较示例")
print("=" * 70)

# 加载数据集
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 标准化特征
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 定义要比较的模型
models = {
    '逻辑回归': LogisticRegression(max_iter=200, random_state=42),
    '决策树': DecisionTreeClassifier(random_state=42),
    '随机森林': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

# 训练和评估模型
print("\n模型性能比较")
print("-" * 70)
print(f"{'模型名称':<15} {'训练准确率':<15} {'测试准确率':<15}")
print("-" * 70)

results = {}
for name, model in models.items():
    # 训练模型
    if name in ['逻辑回归', 'SVM', 'KNN']:
        model.fit(X_train_scaled, y_train)
        train_pred = model.predict(X_train_scaled)
        test_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)
    
    # 计算准确率
    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)
    
    results[name] = {
        'train_acc': train_acc,
        'test_acc': test_acc,
        'model': model
    }
    
    print(f"{name:<15} {train_acc:<15.4f} {test_acc:<15.4f}")

print("-" * 70)

# 找出最佳模型
best_model = max(results.items(), key=lambda x: x[1]['test_acc'])
print(f"\n最佳模型: {best_model[0]} (测试准确率: {best_model[1]['test_acc']:.4f})")

# 详细评估最佳模型
print("\n" + "=" * 70)
print(f"最佳模型 ({best_model[0]}) 详细评估")
print("=" * 70)

if best_model[0] in ['逻辑回归', 'SVM', 'KNN']:
    y_pred_best = best_model[1]['model'].predict(X_test_scaled)
else:
    y_pred_best = best_model[1]['model'].predict(X_test)

print("\n分类报告:")
print(classification_report(y_test, y_pred_best, target_names=iris.target_names))

# 可视化比较
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 子图1：模型准确率对比
model_names = list(results.keys())
train_scores = [results[name]['train_acc'] for name in model_names]
test_scores = [results[name]['test_acc'] for name in model_names]

x = np.arange(len(model_names))
width = 0.35

axes[0, 0].bar(x - width/2, train_scores, width, label='训练集', alpha=0.8)
axes[0, 0].bar(x + width/2, test_scores, width, label='测试集', alpha=0.8)
axes[0, 0].set_xlabel('模型')
axes[0, 0].set_ylabel('准确率')
axes[0, 0].set_title('不同模型的准确率对比')
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(model_names, rotation=45, ha='right')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 子图2：决策边界可视化（使用前两个特征）
X_2d = X[:, :2]
X_train_2d, X_test_2d, y_train_2d, y_test_2d = train_test_split(
    X_2d, y, test_size=0.2, random_state=42, stratify=y
)

# 训练一个模型用于可视化
clf_viz = LogisticRegression(max_iter=200)
clf_viz.fit(X_train_2d, y_train_2d)

# 创建网格
h = 0.02
x_min, x_max = X_2d[:, 0].min() - 1, X_2d[:, 0].max() + 1
y_min, y_max = X_2d[:, 1].min() - 1, X_2d[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# 预测网格点
Z = clf_viz.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[0, 1].contourf(xx, yy, Z, alpha=0.4, cmap='viridis')
axes[0, 1].scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap='viridis', edgecolors='k')
axes[0, 1].set_xlabel('花萼长度')
axes[0, 1].set_ylabel('花萼宽度')
axes[0, 1].set_title('决策边界可视化（逻辑回归）')

# 子图3：特征重要性（随机森林）
rf_model = models['随机森林']
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

axes[1, 0].bar(range(len(importances)), importances[indices])
axes[1, 0].set_xlabel('特征')
axes[1, 0].set_ylabel('重要性')
axes[1, 0].set_title('随机森林特征重要性')
axes[1, 0].set_xticks(range(len(importances)))
axes[1, 0].set_xticklabels([iris.feature_names[i] for i in indices], rotation=45, ha='right')

# 子图4：KNN不同K值的影响
k_values = range(1, 21)
knn_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    score = knn.score(X_test_scaled, y_test)
    knn_scores.append(score)

axes[1, 1].plot(k_values, knn_scores, marker='o')
axes[1, 1].set_xlabel('K值')
axes[1, 1].set_ylabel('测试准确率')
axes[1, 1].set_title('KNN不同K值的影响')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("分类算法示例完成！")
print("=" * 70)
