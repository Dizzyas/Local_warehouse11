"""
数据集划分示例代码
================
本示例展示如何正确划分训练集、验证集和测试集
"""

from sklearn.model_selection import train_test_split
import numpy as np

# 设置随机种子确保可重复性
np.random.seed(42)

# 生成模拟数据
X = np.random.rand(100, 2)
y = np.random.rand(100, 1)

print("=" * 60)
print("数据集划分示例")
print("=" * 60)
print(f"原始数据集大小: {X.shape[0]} 个样本")
print()

# 第一次划分：训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("第一次划分（训练集 + 测试集）")
print("-" * 60)
print(f"训练集大小: {X_train.shape} ({len(X_train)/len(X)*100:.0f}%)")
print(f"测试集大小: {X_test.shape} ({len(X_test)/len(X)*100:.0f}%)")
print()

# 第二次划分：从训练集中划分出验证集
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.25, random_state=42
)

print("第二次划分（训练集 → 训练集 + 验证集）")
print("-" * 60)
print(f"最终训练集大小: {X_train.shape} ({len(X_train)/len(X)*100:.0f}%)")
print(f"验证集大小: {X_val.shape} ({len(X_val)/len(X)*100:.0f}%)")
print(f"测试集大小: {X_test.shape} ({len(X_test)/len(X)*100:.0f}%)")
print()

# 验证划分比例
print("=" * 60)
print("划分比例验证")
print("=" * 60)
total = len(X_train) + len(X_val) + len(X_test)
print(f"训练集: {len(X_train)/total*100:.1f}%")
print(f"验证集: {len(X_val)/total*100:.1f}%")
print(f"测试集: {len(X_test)/total*100:.1f}%")
print()

# 展示分层抽样示例（分类问题）
print("=" * 60)
print("分层抽样示例（分类问题）")
print("=" * 60)

# 生成分类数据
X_class = np.random.rand(100, 2)
y_class = np.random.choice([0, 1], size=100, p=[0.7, 0.3])

print(f"原始类别分布:")
print(f"  类别 0: {np.sum(y_class == 0)} 个 ({np.sum(y_class == 0)/len(y_class)*100:.1f}%)")
print(f"  类别 1: {np.sum(y_class == 1)} 个 ({np.sum(y_class == 1)/len(y_class)*100:.1f}%)")
print()

# 使用分层抽样
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42, stratify=y_class
)

print("分层抽样后的测试集分布:")
print(f"  类别 0: {np.sum(y_test_s == 0)} 个 ({np.sum(y_test_s == 0)/len(y_test_s)*100:.1f}%)")
print(f"  类别 1: {np.sum(y_test_s == 1)} 个 ({np.sum(y_test_s == 1)/len(y_test_s)*100:.1f}%)")
print()

print("✓ 分层抽样保持了原始数据集的类别比例！")
