"""
练习：聚类算法
==============
请完成以下练习，掌握K-Means聚类算法的使用
"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("练习：聚类算法")
print("=" * 60)

# ==================== 练习1 ====================
print("\n练习 1: 选择最佳K值")
print("-" * 60)
print("使用肘部法则和轮廓系数确定最佳K值")

# 生成数据
np.random.seed(42)
X, y_true = make_blobs(n_samples=300, centers=5, cluster_std=0.60, random_state=0)

# 请在下方编写你的代码
# TODO: 计算不同K值下的惯性(inertia)和轮廓系数



# TODO: 绘制肘部法则图



# TODO: 绘制轮廓系数图



# TODO: 根据图表选择最佳K值并进行聚类



# ==================== 练习2 ====================
print("\n练习 2: 数据标准化对聚类的影响")
print("-" * 60)
print("比较标准化前后的聚类效果")

# 生成具有不同尺度的数据
np.random.seed(42)
X_scale = np.random.rand(300, 2)
X_scale[:, 0] = X_scale[:, 0] * 100  # 第一个特征范围 0-100
X_scale[:, 1] = X_scale[:, 1] * 1    # 第二个特征范围 0-1

# 请在下方编写你的代码
# TODO: 不使用标准化直接聚类



# TODO: 使用StandardScaler标准化后聚类



# TODO: 比较两种方法的轮廓系数



# ==================== 练习3 ====================
print("\n练习 3: 聚类中心分析")
print("-" * 60)
print("分析每个簇的特征和样本数量")

# 生成数据
np.random.seed(42)
X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)

# 请在下方编写你的代码
# TODO: 进行聚类



# TODO: 分析每个簇的样本数量



# TODO: 计算每个簇的中心点



# TODO: 计算每个样本到其簇中心的距离



# ==================== 练习4 ====================
print("\n练习 4: 异常检测")
print("-" * 60)
print("使用聚类进行简单的异常检测")

# 生成数据（包含一些异常点）
np.random.seed(42)
X_normal = np.random.randn(300, 2) * 0.5
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X_mixed = np.vstack([X_normal, X_outliers])

# 请在下方编写你的代码
# TODO: 对混合数据进行聚类



# TODO: 计算每个样本到其簇中心的距离



# TODO: 设置阈值，识别异常点（距离大于阈值的点）



# TODO: 可视化正常点和异常点



# ==================== 拓展练习 ====================
print("\n拓展练习: 层次聚类")
print("-" * 60)
print("使用层次聚类并绘制树状图")

from scipy.cluster.hierarchy import dendrogram, linkage

# 生成数据
np.random.seed(42)
X, y_true = make_blobs(n_samples=50, centers=3, cluster_std=0.60, random_state=0)

# 请在下方编写你的代码
# TODO: 计算链接矩阵



# TODO: 绘制树状图



print("\n" + "=" * 60)
print("练习完成！请检查你的答案是否正确。")
print("=" * 60)
