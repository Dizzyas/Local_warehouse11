"""
练习答案：线性回归基础
======================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

print("=" * 60)
print("练习答案：线性回归基础")
print("=" * 60)

# ==================== 练习1答案 ====================
print("\n练习 1: 使用不同的随机种子生成数据")
print("-" * 60)

# 使用随机种子10
np.random.seed(10)
X1 = 2 * np.random.rand(100, 1)
y1 = 4 + 3 * X1 + np.random.randn(100, 1)

model1 = LinearRegression()
model1.fit(X1, y1)

# 使用随机种子20
np.random.seed(20)
X2 = 2 * np.random.rand(100, 1)
y2 = 4 + 3 * X2 + np.random.randn(100, 1)

model2 = LinearRegression()
model2.fit(X2, y2)

print("随机种子10 - 系数:", model1.coef_[0][0], "截距:", model1.intercept_[0])
print("随机种子20 - 系数:", model2.coef_[0][0], "截距:", model2.intercept_[0])
print("\n说明：不同的随机种子会产生不同的数据分布，")
print("      导致模型学习的参数略有差异，但都应该接近真实值（系数≈3，截距≈4）")

# ==================== 练习2答案 ====================
print("\n练习 2: 调整测试集比例")
print("-" * 60)

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

for test_size in [0.1, 0.2, 0.3]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\n测试集比例 {test_size*100:.0f}%:")
    print(f"  测试集大小: {len(X_test)}")
    print(f"  MSE: {mse:.4f}")
    print(f"  R²: {r2:.4f}")

print("\n说明：测试集比例越小，评估的样本越少，结果波动可能越大；")
print("      比例越大，训练数据越少，模型可能学习不充分。")

# ==================== 练习3答案 ====================
print("\n练习 3: 多变量线性回归")
print("-" * 60)

# 生成多变量数据
np.random.seed(42)
X = np.random.rand(100, 2)  # 2个特征
y = 4 + 3 * X[:, 0:1] + 5 * X[:, 1:2] + np.random.randn(100, 1)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

print("模型参数:")
print(f"  系数: {model.coef_[0]}")
print(f"  截距: {model.intercept_[0]}")
print(f"\n真实关系: y = 4 + 3*x1 + 5*x2 + noise")
print(f"学习到的关系: y = {model.intercept_[0]:.4f} + {model.coef_[0][0]:.4f}*x1 + {model.coef_[0][1]:.4f}*x2")

# 预测
y_pred = model.predict(X_test)
print(f"\n预测值示例: {y_pred[:5].flatten()}")
print(f"真实值示例: {y_test[:5].flatten()}")

# ==================== 拓展练习答案 ====================
print("\n拓展练习: 多项式回归")
print("-" * 60)

# 生成非线性数据
np.random.seed(42)
X_nonlinear = np.linspace(-3, 3, 100).reshape(-1, 1)
y_nonlinear = 2 + X_nonlinear + 0.5 * X_nonlinear**2 + np.random.randn(100, 1)

# 创建多项式回归模型
model_poly = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model_poly.fit(X_nonlinear, y_nonlinear)

# 预测
X_new = np.linspace(-3, 3, 100).reshape(-1, 1)
y_pred_poly = model_poly.predict(X_new)

# 可视化
plt.figure(figsize=(10, 6))
plt.scatter(X_nonlinear, y_nonlinear, label='原始数据', alpha=0.6)
plt.plot(X_new, y_pred_poly, color='red', linewidth=2, label='多项式回归')
plt.xlabel('X')
plt.ylabel('y')
plt.title('多项式回归拟合非线性数据')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("多项式回归可以拟合非线性关系！")

print("\n" + "=" * 60)
print("所有练习完成！")
print("=" * 60)
