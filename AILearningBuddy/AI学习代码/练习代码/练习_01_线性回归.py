"""
练习：线性回归基础
==================
请完成以下练习，巩固线性回归的知识
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 60)
print("练习：线性回归基础")
print("=" * 60)

# ==================== 练习1 ====================
print("\n练习 1: 使用不同的随机种子生成数据")
print("-" * 60)
print("提示: 使用 np.random.seed() 设置不同的随机种子")
print("      观察模型参数（系数和截距）的变化")

# 请在下方编写你的代码
# TODO: 使用随机种子10生成数据并训练模型



# TODO: 使用随机种子20生成数据并训练模型



# 打印两个模型的参数进行比较
# print("随机种子10 - 系数: ", model1.coef_[0][0], "截距: ", model1.intercept_[0])
# print("随机种子20 - 系数: ", model2.coef_[0][0], "截距: ", model2.intercept_[0])


# ==================== 练习2 ====================
print("\n练习 2: 调整测试集比例")
print("-" * 60)
print("提示: 修改 test_size 参数，观察模型评估指标的变化")
print("      尝试 test_size=0.1, 0.3, 0.4")

# 生成数据
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 请在下方编写你的代码
# TODO: 使用不同的 test_size 划分数据集并比较结果



# ==================== 练习3 ====================
print("\n练习 3: 多变量线性回归")
print("-" * 60)
print("提示: 创建包含2个特征的数据集")
print("      目标值 y = 4 + 3*x1 + 5*x2 + noise")

# 请在下方编写你的代码
# TODO: 生成包含2个特征的数据



# TODO: 划分数据集



# TODO: 训练多变量线性回归模型



# TODO: 打印模型参数和预测结果



# ==================== 拓展练习 ====================
print("\n拓展练习: 多项式回归")
print("-" * 60)
print("提示: 使用 PolynomialFeatures 处理非线性数据")

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# 生成非线性数据
np.random.seed(42)
X_nonlinear = np.linspace(-3, 3, 100).reshape(-1, 1)
y_nonlinear = 2 + X_nonlinear + 0.5 * X_nonlinear**2 + np.random.randn(100, 1)

# 请在下方编写你的代码
# TODO: 创建多项式回归模型（2次多项式）



# TODO: 训练模型并进行预测



# TODO: 可视化结果



print("\n" + "=" * 60)
print("练习完成！请检查你的答案是否正确。")
print("=" * 60)
