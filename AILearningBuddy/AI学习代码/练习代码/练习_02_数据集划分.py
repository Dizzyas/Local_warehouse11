"""
练习：数据集划分
================
请完成以下练习，掌握数据集划分的技巧
"""

from sklearn.model_selection import train_test_split
import numpy as np

print("=" * 60)
print("练习：数据集划分")
print("=" * 60)

# ==================== 练习1 ====================
print("\n练习 1: 不同测试集比例的影响")
print("-" * 60)
print("比较 test_size=0.1, 0.2, 0.3 时的划分结果")

# 生成数据
np.random.seed(42)
X = np.random.rand(200, 3)
y = np.random.rand(200)

test_sizes = [0.1, 0.2, 0.3]

# 请在下方编写你的代码
# TODO: 使用不同的 test_size 进行划分并记录结果



# ==================== 练习2 ====================
print("\n练习 2: 分层抽样")
print("-" * 60)
print("使用 stratify 参数保持类别分布")

# 生成分类数据（不平衡）
np.random.seed(42)
X_class = np.random.rand(1000, 5)
y_class = np.random.choice([0, 1, 2], size=1000, p=[0.5, 0.3, 0.2])

print("原始类别分布:")
for label in np.unique(y_class):
    count = np.sum(y_class == label)
    print(f"  类别 {label}: {count} 个 ({count/len(y_class)*100:.1f}%)")

# 请在下方编写你的代码
# TODO: 不使用分层抽样进行划分



# TODO: 使用分层抽样进行划分



# 比较两种方法的测试集类别分布



# ==================== 练习3 ====================
print("\n练习 3: 训练集/验证集/测试集划分")
print("-" * 60)
print("实现 60% / 20% / 20% 的划分")

# 生成数据
np.random.seed(42)
X = np.random.rand(500, 4)
y = np.random.rand(500)

# 请在下方编写你的代码
# TODO: 先划分出测试集（20%）



# TODO: 从剩余数据中划分出验证集（占原始数据的20%，即剩余数据的25%）



# TODO: 打印最终划分结果



# ==================== 拓展练习 ====================
print("\n拓展练习: 交叉验证")
print("-" * 60)
print("使用 KFold 实现5折交叉验证")

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 生成数据
np.random.seed(42)
X = np.random.rand(100, 2)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# 请在下方编写你的代码
# TODO: 创建 KFold 对象



# TODO: 进行5折交叉验证并计算每折的MSE



print("\n" + "=" * 60)
print("练习完成！请检查你的答案是否正确。")
print("=" * 60)
