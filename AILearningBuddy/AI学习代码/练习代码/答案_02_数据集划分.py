"""
练习答案：数据集划分
====================
"""

from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

print("=" * 60)
print("练习答案：数据集划分")
print("=" * 60)

# ==================== 练习1答案 ====================
print("\n练习 1: 不同测试集比例的影响")
print("-" * 60)

np.random.seed(42)
X = np.random.rand(200, 3)
y = np.random.rand(200)

test_sizes = [0.1, 0.2, 0.3]
results = []

for test_size in test_sizes:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    results.append({
        'test_size': test_size,
        'train_size': len(X_train),
        'test_samples': len(X_test)
    })
    print(f"test_size={test_size}: 训练集={len(X_train)}, 测试集={len(X_test)}")

# ==================== 练习2答案 ====================
print("\n练习 2: 分层抽样")
print("-" * 60)

np.random.seed(42)
X_class = np.random.rand(1000, 5)
y_class = np.random.choice([0, 1, 2], size=1000, p=[0.5, 0.3, 0.2])

print("原始类别分布:")
for label in np.unique(y_class):
    count = np.sum(y_class == label)
    print(f"  类别 {label}: {count} 个 ({count/len(y_class)*100:.1f}%)")

# 不使用分层抽样
X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42
)

print("\n不使用分层抽样的测试集分布:")
for label in np.unique(y_test_ns):
    count = np.sum(y_test_ns == label)
    print(f"  类别 {label}: {count} 个 ({count/len(y_test_ns)*100:.1f}%)")

# 使用分层抽样
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42, stratify=y_class
)

print("\n使用分层抽样的测试集分布:")
for label in np.unique(y_test_s):
    count = np.sum(y_test_s == label)
    print(f"  类别 {label}: {count} 个 ({count/len(y_test_s)*100:.1f}%)")

print("\n说明：分层抽样保持了原始数据集的类别比例！")

# ==================== 练习3答案 ====================
print("\n练习 3: 训练集/验证集/测试集划分")
print("-" * 60)

np.random.seed(42)
X = np.random.rand(500, 4)
y = np.random.rand(500)

# 先划分出测试集（20%）
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 从剩余数据中划分出验证集（占原始数据的20%，即剩余数据的25%）
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42
)

print(f"最终划分结果:")
print(f"  训练集: {len(X_train)} 个样本 ({len(X_train)/len(X)*100:.1f}%)")
print(f"  验证集: {len(X_val)} 个样本 ({len(X_val)/len(X)*100:.1f}%)")
print(f"  测试集: {len(X_test)} 个样本 ({len(X_test)/len(X)*100:.1f}%)")

# ==================== 拓展练习答案 ====================
print("\n拓展练习: 交叉验证")
print("-" * 60)

np.random.seed(42)
X = np.random.rand(100, 2)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# 创建 KFold 对象
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# 进行5折交叉验证
mse_scores = []
fold = 1

for train_index, val_index in kf.split(X):
    X_train_cv, X_val_cv = X[train_index], X[val_index]
    y_train_cv, y_val_cv = y[train_index], y[val_index]
    
    model = LinearRegression()
    model.fit(X_train_cv, y_train_cv)
    y_pred_cv = model.predict(X_val_cv)
    
    mse = mean_squared_error(y_val_cv, y_pred_cv)
    mse_scores.append(mse)
    print(f"折 {fold}: MSE = {mse:.4f}")
    fold += 1

print(f"\n5折交叉验证平均MSE: {np.mean(mse_scores):.4f}")
print(f"标准差: {np.std(mse_scores):.4f}")

print("\n" + "=" * 60)
print("所有练习完成！")
print("=" * 60)
