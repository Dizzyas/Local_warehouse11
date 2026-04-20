"""
聚类算法示例代码
================
本示例展示K-Means聚类算法的使用和评估
"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子
np.random.seed(42)

print("=" * 60)
print("K-Means聚类算法示例")
print("=" * 60)

# 1. 生成模拟数据
print("\n步骤 1: 生成模拟数据")
print("-" * 60)
X, y_true = make_blobs(
    n_samples=300, 
    centers=4, 
    cluster_std=0.60, 
    random_state=0
)
print(f"生成数据: {X.shape[0]} 个样本, {X.shape[1]} 个特征")
print(f"真实簇数量: {len(np.unique(y_true))}")

# 2. 确定最佳K值（肘部法则）
print("\n步骤 2: 使用肘部法则确定最佳K值")
print("-" * 60)

inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))
    print(f"K={k}: 惯性={kmeans.inertia_:.2f}, 轮廓系数={silhouette_scores[-1]:.4f}")

# 3. 使用最佳K值进行聚类
optimal_k = 4  # 根据肘部法则和轮廓系数选择
print(f"\n选择 K={optimal_k} 进行聚类")

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# 4. 评估聚类效果
print("\n步骤 3: 聚类效果评估")
print("-" * 60)
sil_score = silhouette_score(X, y_kmeans)
ch_score = calinski_harabasz_score(X, y_kmeans)

print(f"轮廓系数 (Silhouette Score): {sil_score:.4f}")
print(f"  - 范围: [-1, 1], 越接近1表示聚类效果越好")
print(f"Calinski-Harabasz指数: {ch_score:.2f}")
print(f"  - 值越大表示聚类效果越好")

# 5. 可视化结果
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 子图1：原始数据（带真实标签）
axes[0, 0].scatter(X[:, 0], X[:, 1], c=y_true, s=50, cmap='viridis', alpha=0.6)
axes[0, 0].set_title('原始数据（真实标签）')
axes[0, 0].set_xlabel('特征 1')
axes[0, 0].set_ylabel('特征 2')

# 子图2：聚类结果
scatter = axes[0, 1].scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis', alpha=0.6)
axes[0, 1].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                   c='red', s=200, alpha=0.8, marker='X', edgecolors='black', linewidths=2)
axes[0, 1].set_title('K-Means聚类结果 (K=4)')
axes[0, 1].set_xlabel('特征 1')
axes[0, 1].set_ylabel('特征 2')

# 子图3：肘部法则
axes[0, 2].plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
axes[0, 2].set_xlabel('K值')
axes[0, 2].set_ylabel('惯性 (Inertia)')
axes[0, 2].set_title('肘部法则')
axes[0, 2].grid(True, alpha=0.3)
axes[0, 2].axvline(x=optimal_k, color='red', linestyle='--', alpha=0.5, label=f'选择 K={optimal_k}')
axes[0, 2].legend()

# 子图4：轮廓系数
axes[1, 0].plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
axes[1, 0].set_xlabel('K值')
axes[1, 0].set_ylabel('轮廓系数')
axes[1, 0].set_title('轮廓系数法')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].axvline(x=optimal_k, color='red', linestyle='--', alpha=0.5, label=f'选择 K={optimal_k}')
axes[1, 0].legend()

# 子图5：非线性数据聚类（月牙形数据）
X_moons, y_moons = make_moons(n_samples=200, noise=0.1, random_state=42)
kmeans_moons = KMeans(n_clusters=2, random_state=42, n_init=10)
y_moons_pred = kmeans_moons.fit_predict(X_moons)

axes[1, 1].scatter(X_moons[:, 0], X_moons[:, 1], c=y_moons_pred, s=50, cmap='viridis', alpha=0.6)
axes[1, 1].set_title('K-Means在非线性数据上的表现')
axes[1, 1].set_xlabel('特征 1')
axes[1, 1].set_ylabel('特征 2')

# 子图6：簇大小分布
unique, counts = np.unique(y_kmeans, return_counts=True)
axes[1, 2].bar(unique, counts, color='skyblue', edgecolor='black')
axes[1, 2].set_xlabel('簇编号')
axes[1, 2].set_ylabel('样本数量')
axes[1, 2].set_title('各簇样本数量分布')
axes[1, 2].set_xticks(unique)

plt.tight_layout()
plt.show()

# 6. 聚类中心分析
print("\n步骤 4: 聚类中心分析")
print("-" * 60)
print("各簇的中心点坐标:")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"  簇 {i}: ({center[0]:.4f}, {center[1]:.4f})")

# 7. 预测新数据
print("\n步骤 5: 新数据预测")
print("-" * 60)
new_points = np.array([[0, 0], [2, 2], [-1, 3]])
predictions = kmeans.predict(new_points)
print("新数据点所属簇:")
for point, pred in zip(new_points, predictions):
    print(f"  点 {point} → 簇 {pred}")

print("\n" + "=" * 60)
print("聚类算法示例完成！")
print("=" * 60)
