"""
练习答案：聚类算法
==================
"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("练习答案：聚类算法")
print("=" * 60)

# ==================== 练习1答案 ====================
print("\n练习 1: 选择最佳K值")
print("-" * 60)

np.random.seed(42)
X, y_true = make_blobs(n_samples=300, centers=5, cluster_std=0.60, random_state=0)

# 计算不同K值下的指标
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))

# 绘制肘部法则图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
axes[0].set_xlabel('K值')
axes[0].set_ylabel('惯性 (Inertia)')
axes[0].set_title('肘部法则')
axes[0].grid(True, alpha=0.3)

axes[1].plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
axes[1].set_xlabel('K值')
axes[1].set_ylabel('轮廓系数')
axes[1].set_title('轮廓系数法')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 选择最佳K值（这里选择K=5）
best_k = 5
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

print(f"选择 K={best_k}")
print(f"轮廓系数: {silhouette_score(X, y_kmeans):.4f}")

# ==================== 练习2答案 ====================
print("\n练习 2: 数据标准化对聚类的影响")
print("-" * 60)

np.random.seed(42)
X_scale = np.random.rand(300, 2)
X_scale[:, 0] = X_scale[:, 0] * 100
X_scale[:, 1] = X_scale[:, 1] * 1

# 不使用标准化
kmeans_no_scale = KMeans(n_clusters=3, random_state=42, n_init=10)
y_no_scale = kmeans_no_scale.fit_predict(X_scale)
sil_no_scale = silhouette_score(X_scale, y_no_scale)

# 使用标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_scale)
kmeans_scale = KMeans(n_clusters=3, random_state=42, n_init=10)
y_scale = kmeans_scale.fit_predict(X_scaled)
sil_scale = silhouette_score(X_scaled, y_scale)

print(f"不使用标准化 - 轮廓系数: {sil_no_scale:.4f}")
print(f"使用标准化 - 轮廓系数: {sil_scale:.4f}")
print("\n说明：标准化后聚类效果更好，因为消除了特征尺度差异的影响。")

# ==================== 练习3答案 ====================
print("\n练习 3: 聚类中心分析")
print("-" * 60)

np.random.seed(42)
X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# 分析每个簇的样本数量
unique, counts = np.unique(y_kmeans, return_counts=True)
print("各簇样本数量:")
for cluster_id, count in zip(unique, counts):
    print(f"  簇 {cluster_id}: {count} 个样本")

# 聚类中心
print("\n各簇中心点:")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"  簇 {i}: ({center[0]:.4f}, {center[1]:.4f})")

# 计算每个样本到其簇中心的距离
distances = []
for i, x in enumerate(X):
    center = kmeans.cluster_centers_[y_kmeans[i]]
    dist = np.linalg.norm(x - center)
    distances.append(dist)

avg_distances = []
for cluster_id in unique:
    cluster_distances = [distances[i] for i in range(len(X)) if y_kmeans[i] == cluster_id]
    avg_dist = np.mean(cluster_distances)
    avg_distances.append(avg_dist)
    print(f"\n簇 {cluster_id} 平均距离: {avg_dist:.4f}")

# ==================== 练习4答案 ====================
print("\n练习 4: 异常检测")
print("-" * 60)

np.random.seed(42)
X_normal = np.random.randn(300, 2) * 0.5
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X_mixed = np.vstack([X_normal, X_outliers])

# 聚类
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X_mixed)

# 计算每个样本到其簇中心的距离
distances = []
for i, x in enumerate(X_mixed):
    center = kmeans.cluster_centers_[y_kmeans[i]]
    dist = np.linalg.norm(x - center)
    distances.append(dist)

# 设置阈值（使用95百分位数）
threshold = np.percentile(distances, 95)
outliers = np.where(np.array(distances) > threshold)[0]

print(f"阈值: {threshold:.4f}")
print(f"检测到 {len(outliers)} 个异常点")

# 可视化
plt.figure(figsize=(10, 6))
normal_points = [i for i in range(len(X_mixed)) if i not in outliers]
plt.scatter(X_mixed[normal_points, 0], X_mixed[normal_points, 1], 
           c='blue', label='正常点', alpha=0.6)
plt.scatter(X_mixed[outliers, 0], X_mixed[outliers, 1], 
           c='red', label='异常点', alpha=0.8, s=100, marker='x')
plt.xlabel('特征 1')
plt.ylabel('特征 2')
plt.title('使用聚类进行异常检测')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==================== 拓展练习答案 ====================
print("\n拓展练习: 层次聚类")
print("-" * 60)

np.random.seed(42)
X, y_true = make_blobs(n_samples=50, centers=3, cluster_std=0.60, random_state=0)

# 计算链接矩阵
linked = linkage(X, method='ward')

# 绘制树状图
plt.figure(figsize=(10, 6))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('层次聚类树状图')
plt.xlabel('样本索引')
plt.ylabel('距离')
plt.show()

print("树状图显示了样本之间的层次关系，可以通过切割树来得到不同的聚类数量。")

print("\n" + "=" * 60)
print("所有练习完成！")
print("=" * 60)
