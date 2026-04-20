"""
线性回归基础示例代码
===================
本示例展示如何使用scikit-learn进行线性回归分析
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 生成模拟数据
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 数据可视化
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.5)
plt.xlabel('特征 (X)')
plt.ylabel('目标值 (y)')
plt.title('模拟数据集')
plt.grid(True, alpha=0.3)
plt.show()

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 查看模型参数
print("=" * 50)
print("模型训练结果")
print("=" * 50)
print(f"模型系数 (θ1): {model.coef_[0][0]:.4f}")
print(f"截距 (θ0): {model.intercept_[0]:.4f}")
print(f"真实关系: y = 4 + 3x + noise")
print()

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 模型评估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("模型评估指标")
print("-" * 50)
print(f"均方误差 (MSE): {mse:.4f}")
print(f"R² 评分: {r2:.4f}")
print()

# 可视化模型预测结果
plt.figure(figsize=(12, 5))

# 子图1：测试集真实值 vs 预测值
plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test, color='blue', label='真实值', alpha=0.6)
plt.plot(X_test, y_pred, color='red', linewidth=2, label='预测值')
plt.xlabel('特征 (X)')
plt.ylabel('目标值 (y)')
plt.title('线性回归模型预测结果')
plt.legend()
plt.grid(True, alpha=0.3)

# 子图2：残差图
plt.subplot(1, 2, 2)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, color='green', alpha=0.6)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('预测值')
plt.ylabel('残差')
plt.title('残差图')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 使用模型进行新数据预测
print("=" * 50)
print("新数据预测示例")
print("=" * 50)
new_X = np.array([[0.5], [1.0], [1.5]])
new_predictions = model.predict(new_X)
for i, (x, pred) in enumerate(zip(new_X, new_predictions)):
    print(f"输入 X = {x[0]:.1f}, 预测 y = {pred[0]:.4f}")
