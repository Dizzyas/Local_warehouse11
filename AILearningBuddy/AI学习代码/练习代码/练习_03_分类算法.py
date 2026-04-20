"""
练习：分类算法
==============
请完成以下练习，掌握不同分类算法的使用
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
print("练习：分类算法")
print("=" * 60)

# ==================== 练习1 ====================
print("\n练习 1: 决策树分类器")
print("-" * 60)
print("使用决策树对鸢尾花数据进行分类")

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 请在下方编写你的代码
# TODO: 创建决策树分类器



# TODO: 训练模型



# TODO: 预测并计算准确率



# TODO: 打印混淆矩阵



# ==================== 练习2 ====================
print("\n练习 2: 随机森林分类器")
print("-" * 60)
print("使用随机森林并调整 n_estimators 参数")

# 请在下方编写你的代码
# TODO: 创建随机森林分类器，n_estimators=50



# TODO: 训练并评估



# TODO: 尝试 n_estimators=100 和 n_estimators=200，比较结果



# ==================== 练习3 ====================
print("\n练习 3: 特征重要性分析")
print("-" * 60)
print("使用随机森林的特征重要性功能")

# 请在下方编写你的代码
# TODO: 获取特征重要性



# TODO: 将特征重要性排序并可视化



# ==================== 练习4 ====================
print("\n练习 4: 多分类评估指标")
print("-" * 60)
print("计算精确率、召回率、F1分数")

# 使用逻辑回归作为示例模型
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# 请在下方编写你的代码
# TODO: 计算并打印分类报告



# TODO: 计算每个类别的精确率和召回率



# ==================== 拓展练习 ====================
print("\n拓展练习: 不平衡数据处理")
print("-" * 60)
print("使用 class_weight 参数处理类别不平衡")

# 生成不平衡数据
np.random.seed(42)
X_imbalanced = np.random.rand(1000, 2)
y_imbalanced = np.random.choice([0, 1], size=1000, p=[0.9, 0.1])

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_imbalanced, y_imbalanced, test_size=0.2, random_state=42, stratify=y_imbalanced
)

# 请在下方编写你的代码
# TODO: 不使用 class_weight 训练模型



# TODO: 使用 class_weight='balanced' 训练模型



# TODO: 比较两种方法的性能



print("\n" + "=" * 60)
print("练习完成！请检查你的答案是否正确。")
print("=" * 60)
