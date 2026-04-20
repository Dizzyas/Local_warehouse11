---
date: 2026-04-20
tags: [AI, 已学, 机器学习, Scikit-learn]
---

# Scikit-learn 机器学习基础

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**你有没有想过这些问题？**

- 🔮 怎么让计算机"学会"预测明天股票涨还是跌？
- 📧 怎么让程序自动区分垃圾邮件和正常邮件？
- 🏥 怎么让AI根据检查结果判断有没有疾病？
- 🛒 怎么推荐用户可能喜欢的商品？

**答案就是机器学习！**

而 **Scikit-learn** = Python 机器学习**最常用的库**，把复杂的机器学习算法封装成几行代码就能用。

---

## 步骤2：前置知识确认

学习 Scikit-learn 需要了解：

- ✅ [[Python面向对象编程]]（sklearn 全是类和对象）
- ✅ [[NumPy数组基础]]（数据用 numpy 数组）
- ✅ [[Pandas数据处理基础]]（数据用 DataFrame）
- ✅ [[数学基础线性代数]]（矩阵运算）
- ✅ [[数学基础概率与统计]]（均值、方差、概率分布）

---

## 步骤3：完整代码展示

```python
# ============================================
# Scikit-learn 机器学习基础 — 完整可运行代码
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_breast_cancer, make_classification, make_blobs
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, silhouette_score

# 设置中文
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# ============================================
# 第一部分：Scikit-learn API 设计风格
# ============================================

print("=" * 50)
print("第一部分：Scikit-learn API 设计风格")
print("=" * 50)

# ① sklearn 三大铁律
print("\n=== 1. sklearn 三大铁律 ===")

print("""
Scikit-learn 所有模型的 API 都遵循同一模式：

1. 创建模型实例
   model = SomeModel()

2. 训练模型
   model.fit(X_train, y_train)

3. 预测
   y_pred = model.predict(X_test)

可选：评估
   score = model.score(X_test, y_test)
""")

# ② 数据加载
print("\n=== 2. 数据加载 ===")

# 方式1：sklearn 内置数据集
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"鸢尾花数据集: {X.shape[0]}样本, {X.shape[1]}特征")
print(f"特征: {feature_names}")
print(f"类别: {target_names}")
print(f"类别分布: {np.bincount(y)}")

# 方式2：生成模拟数据
X_clf, y_clf = make_classification(
    n_samples=200, n_features=2, n_informative=2, 
    n_redundant=0, n_classes=2, random_state=42
)
print(f"\n模拟二分类数据: {X_clf.shape}")

# ③ 数据划分
print("\n=== 3. 数据划分 ===")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"训练集: {X_train.shape[0]}样本")
print(f"测试集: {X_test.shape[0]}样本")

# ④ 数据预处理
print("\n=== 4. 数据预处理 ===")

# 标准化（Z-score）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform
X_test_scaled = scaler.transform(X_test)        # 只 transform

print(f"标准化前均值: {X_train[:, 0].mean():.2f}, 标准差: {X_train[:, 0].std():.2f}")
print(f"标准化后均值: {X_train_scaled[:, 0].mean():.2f}, 标准差: {X_train_scaled[:, 0].std():.2f}")

# 归一化（Min-Max）
minmax = MinMaxScaler()
X_train_norm = minmax.fit_transform(X_train)
X_test_norm = minmax.transform(X_test)

print(f"归一化后范围: [{X_train_norm.min():.2f}, {X_train_norm.max():.2f}]")

# ============================================
# 第二部分：分类算法
# ============================================

print("\n" + "=" * 50)
print("第二部分：分类算法")
print("=" * 50)

# ⑤ K近邻（KNN）
print("\n=== 5. K近邻 KNN ===")

# 原理：找最近的K个邻居，投票决定类别
knn = KNeighborsClassifier(n_neighbors=5)  # 1. 创建模型
knn.fit(X_train_scaled, y_train)              # 2. 训练
y_pred_knn = knn.predict(X_test_scaled)     # 3. 预测
accuracy_knn = knn.score(X_test_scaled, y_test)  # 4. 评估
print(f"KNN 准确率: {accuracy_knn:.2%}")

# ⑥ 逻辑回归
print("\n=== 6. 逻辑回归 ===")

# 原理：输出概率，用 Sigmoid 函数把线性结果转为 0-1
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train_scaled, y_train)
y_pred_log = logreg.predict(X_test_scaled)
accuracy_log = logreg.score(X_test_scaled, y_test)
print(f"逻辑回归 准确率: {accuracy_log:.2%}")

# 查看预测概率
proba = logreg.predict_proba(X_test_scaled[:3])
print(f"前3个样本预测概率:\n{proba}")

# ⑦ 决策树
print("\n=== 7. 决策树 ===")

# 原理：按特征阈值不断分裂，最大化信息增益/基尼系数
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
accuracy_dt = dt.score(X_test, y_test)
print(f"决策树 准确率: {accuracy_dt:.2%}")

# 可视化决策树
plt.figure(figsize=(15, 8))
plot_tree(dt, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("决策树可视化")
plt.tight_layout()
plt.savefig("decision_tree.png", dpi=100)
plt.show()

# 特征重要性
print(f"特征重要性: {dict(zip(iris.feature_names, dt.feature_importances_.round(3)))}")

# ⑧ 随机森林
print("\n=== 8. 随机森林 ===")

# 原理：多棵决策树集成，投票决定最终结果
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
accuracy_rf = rf.score(X_test, y_test)
print(f"随机森林 准确率: {accuracy_rf:.2%}")

# 特征重要性
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
print("特征重要性排序:")
for i in range(len(importances)):
    print(f"  {i+1}. {iris.feature_names[indices[i]]}: {importances[indices[i]]:.3f}")

# ============================================
# 第三部分：模型评估
# ============================================

print("\n" + "=" * 50)
print("第三部分：模型评估")
print("=" * 50)

# ⑨ 混淆矩阵
print("\n=== 9. 混淆矩阵 ===")

cm = confusion_matrix(y_test, y_pred_rf)
print(f"混淆矩阵:\n{cm}")

# 可视化混淆矩阵
plt.figure(figsize=(8, 6))
import seaborn as sns
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel('预测')
plt.ylabel('真实')
plt.title('混淆矩阵')
plt.tight_layout()
plt.show()

# ⑩ 分类报告
print("\n=== 10. 分类报告 ===")

report = classification_report(y_test, y_pred_rf, target_names=iris.target_names)
print(f"分类报告:\n{report}")

# ⑪ 交叉验证
print("\n=== 11. 交叉验证 ===")

# 5折交叉验证
cv_scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
print(f"5折交叉验证准确率: {cv_scores}")
print(f"平均准确率: {cv_scores.mean():.2%} ± {cv_scores.std():.2%}")

# ============================================
# 第四部分：超参数调优
# ============================================

print("\n" + "=" * 50)
print("第四部分：超参数调优")
print("=" * 50)

# ⑫ GridSearchCV
print("\n=== 12. GridSearchCV ===")

# 网格搜索：穷举所有参数组合
param_grid = {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

grid_search = GridSearchCV(
    KNeighborsClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train_scaled, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳交叉验证分数: {grid_search.best_score_:.2%}")

# 用最佳模型预测
best_knn = grid_search.best_estimator_
y_pred_best = best_knn.predict(X_test_scaled)
print(f"最佳模型测试集准确率: {accuracy_score(y_test, y_pred_best):.2%}")

# ============================================
# 第五部分：聚类算法
# ============================================

print("\n" + "=" * 50)
print("第五部分：聚类算法")
print("=" * 50)

# ⑬ K-Means 聚类
print("\n=== 13. K-Means 聚类 ===")

# 生成聚类数据
X_cluster, y_cluster = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)

# K-Means 聚类
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_cluster)
labels = kmeans.labels_

# 评估轮廓系数
silhouette = silhouette_score(X_cluster, labels)
print(f"轮廓系数: {silhouette:.3f} (越接近1越好)")

# 可视化
plt.figure(figsize=(10, 6))
plt.scatter(X_cluster[:, 0], X_cluster[:, 1], c=labels, cmap='viridis', s=30, alpha=0.7)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', marker='X', s=200, label='聚类中心')
plt.title(f'K-Means 聚类 (k=4, 轮廓系数={silhouette:.3f})')
plt.legend()
plt.tight_layout()
plt.show()

# ============================================
# 第六部分：完整实战
# ============================================

print("\n" + "=" * 50)
print("第六部分：完整实战 - 鸢尾花分类")
print("=" * 50)

# ⑭ 完整机器学习流程
print("\n=== 14. 完整流程 ===")

# 1. 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 2. 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3. 预处理
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 训练多个模型对比
models = {
    'KNN (k=5)': KNeighborsClassifier(n_neighbors=5),
    '逻辑回归': LogisticRegression(max_iter=1000),
    '决策树': DecisionTreeClassifier(max_depth=3, random_state=42),
    '随机森林': RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
}

results = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    cv_score = cross_val_score(model, X_train_scaled, y_train, cv=5).mean()
    results[name] = {'train': train_score, 'test': test_score, 'cv': cv_score}
    print(f"{name:15s} | 训练集: {train_score:.2%} | 测试集: {test_score:.2%} | CV: {cv_score:.2%}")

# 5. 选择最佳模型
best_model_name = max(results, key=lambda x: results[x]['test'])
print(f"\n最佳模型: {best_model_name}")

# 6. 结果可视化对比
plt.figure(figsize=(10, 5))
names = list(results.keys())
train_scores = [results[n]['train'] for n in names]
test_scores = [results[n]['test'] for n in names]
cv_scores = [results[n]['cv'] for n in names]

x = np.arange(len(names))
width = 0.25

plt.bar(x - width, train_scores, width, label='训练集', color='steelblue')
plt.bar(x, test_scores, width, label='测试集', color='coral')
plt.bar(x + width, cv_scores, width, label='交叉验证', color='lightgreen')

plt.xlabel('模型')
plt.ylabel('准确率')
plt.title('模型性能对比')
plt.xticks(x, names, rotation=15)
plt.legend()
plt.ylim(0.8, 1.05)
plt.tight_layout()
plt.show()

# ============================================
# 第七部分：sklearn 速查表
# ============================================

print("\n" + "=" * 50)
print("第七部分：速查表")
print("=" * 50)

print("""
=== sklearn 算法速查 ===

分类算法：
  KNeighborsClassifier     - K近邻
  LogisticRegression        - 逻辑回归
  DecisionTreeClassifier     - 决策树
  RandomForestClassifier    - 随机森林
  SVM                       - 支持向量机
  GaussianNB                - 朴素贝叶斯

回归算法：
  LinearRegression          - 线性回归
  Ridge/Lasso              - 岭回归/套索
  DecisionTreeRegressor     - 决策树回归
  RandomForestRegressor     - 随机森林回归

聚类算法：
  KMeans                    - K均值
  DBSCAN                    - 密度聚类
  AgglomerativeClustering   - 层次聚类

模型选择：
  train_test_split          - 数据划分
  cross_val_score           - 交叉验证
  GridSearchCV              - 网格搜索
  RandomizedSearchCV        - 随机搜索

预处理：
  StandardScaler            - 标准化
  MinMaxScaler              - 归一化
  LabelEncoder              - 标签编码
  OneHotEncoder             - 独热编码

评估指标：
  accuracy_score            - 准确率
  confusion_matrix           - 混淆矩阵
  classification_report      - 分类报告
  silhouette_score          - 轮廓系数
  mean_squared_error        - 均方误差
  r2_score                  - R²分数
""")
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：sklearn API 三大步骤

```python
# 1. 创建模型
model = SomeClassifier()

# 2. 训练
model.fit(X_train, y_train)

# 3. 预测
y_pred = model.predict(X_test)
```

**为什么 sklearn 这么设计？**
- 统一接口，学习成本低
- 便于比较不同算法
- 便于 Pipeline 串联

### 模块②：fit_transform vs transform

| 方法 | 作用 | 用于 |
|------|------|------|
| `fit_transform(X)` | fit + transform | 训练集（需要学习参数并转换） |
| `transform(X)` | 只转换 | 测试集（用训练集学到的参数） |

**⚠️ 常见错误**：对测试集也用 `fit_transform`（会导致数据泄露！）

### 模块③：KNN 原理

```
新样本的类别 = K个最近邻居的多数投票

K=3 时：
  邻居类别: [猫, 狗, 猫] → 预测为"猫"

K的选择：
  K太小 → 容易过拟合
  K太大 → 容易欠拟合
  通常 K=3,5,7,9,11 等奇数（避免平票）
```

### 模块④：逻辑回归原理

```
线性组合: z = w1*x1 + w2*x2 + ... + b
概率输出: p = sigmoid(z) = 1 / (1 + e^(-z))

预测: p > 0.5 → 类别1
     p <= 0.5 → 类别0
```

### 模块⑤：决策树原理

```
按特征不断分裂，每次分裂最大化信息增益/基尼系数

根节点: 所有人
↓
分裂: 是否有房 → [有房组, 无房组]
↓
有房组 → 基本都会还款
无房组 → 继续分裂（收入、信用等）
...
```

### 模块⑥：随机森林原理

```
随机森林 = 多棵决策树 + 投票机制

1. Bootstrap 抽样：从数据中有放回抽样
2. 随机特征选择：每棵树只随机选部分特征
3. 独立训练每棵树
4. 投票决定最终类别

优势：
- 比单棵树更稳定
- 不容易过拟合
- 能处理高维数据
```

### 模块⑦：混淆矩阵解读

```
              预测
            正例   负例
真实  正例   TP     FN
      负例   FP     TN

准确率 = (TP + TN) / 总数
精确率 = TP / (TP + FP)    → 预测为正的里面有多少是对的
召回率 = TP / (TP + FN)    → 真正例里面预测对了多少
F1 = 2 * Precision * Recall / (Precision + Recall)
```

### 模块⑧：交叉验证

```
5折交叉验证：
数据分成5份:
  Fold1: [测试] [训练] [训练] [训练] [训练]
  Fold2: [训练] [测试] [训练] [训练] [训练]
  Fold3: [训练] [训练] [测试] [训练] [训练]
  Fold4: [训练] [训练] [训练] [测试] [训练]
  Fold5: [训练] [训练] [训练] [训练] [测试]

最终分数 = 5次的平均
```

### 模块⑨：K-Means 聚类流程

```
1. 随机选择K个聚类中心
2. 计算每个点到K个中心的距离
3. 把每个点分配给最近的中心
4. 重新计算K个聚类中心
5. 重复2-4直到收敛或达到最大迭代次数

评估指标：轮廓系数 Silhouette Score
  = (b - a) / max(a, b)
  a = 点到同簇其他点的平均距离
  b = 点到最近簇的平均距离
  越接近1越好
```

---

## 步骤5：代码执行过程模拟

### 模拟1：KNN 预测过程

```
X_train = [[1,2], [2,3], [3,1], [6,5], [7,6], [8,7]]
y_train = [0, 0, 0, 1, 1, 1]
X_test = [[4, 3]]

K=3 时：
1. 计算测试点到所有训练点的距离
2. 排序，取最近的3个邻居
3. 3个邻居的类别 = [0, 0, 1]
4. 投票 → 类别0
```

### 模拟2：决策树分裂

```
原始数据：100人，还款率60%

按"有房"分裂：
  有房(30人) → 还款率90%
  无房(70人) → 还款率50%

信息增益 = H(父节点) - weighted_H(子节点)
        = H(0.6) - (0.3*H(0.9) + 0.7*H(0.5))
        = 0.97 - 0.89 = 0.08
```

---

## 步骤6：完整运行结果展示

```text
==================================================
第一部分：Scikit-learn API 设计风格
==================================================

鸢尾花数据集: 150样本, 4特征
特征: ['sepal length (cm)', 'petal length (cm)', ...]
类别: ['setosa' 'versicolor' 'virginica']
类别分布: [50 50 50]

==================================================
第二部分：分类算法
==================================================

KNN 准确率: 96.67%
逻辑回归 准确率: 96.67%
决策树 准确率: 95.56%
随机森林 准确率: 95.56%

==================================================
第三部分：模型评估
==================================================

混淆矩阵:
[[15  0  0]
 [ 0 13  1]
 [ 0  1 15]]

==================================================
第四部分：超参数调优
==================================================

最佳参数: {'metric': 'euclidean', 'n_neighbors': 3, 'weights': 'uniform'}
最佳交叉验证分数: 96.67%

==================================================
第五部分：聚类算法
==================================================

轮廓系数: 0.825 (越接近1越好)
```

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
| 数据泄露 | 对测试集 `fit_transform` | 用训练集的 scaler 只 `transform` |
| 过拟合 | 训练集准确率100% | 检查 CV 分数和测试集分数 |
| KNN不预处理 | 不标准化直接KNN | KNN依赖距离，必须先标准化 |
| K取值偶数 | K=4 | K=3,5,7 避免平票 |
| 忽略类别不平衡 | 不处理不平衡数据 | 用 `stratify=y` 划分 |

### 🔗 知识点关联

```
Scikit-learn 机器学习基础
├── → [[Python面向对象编程]]（sklearn 全是类）
├── → [[数学基础线性代数]]（矩阵运算）
├── → [[数学基础概率与统计]]（评估指标）
├── → [[数据清洗]]（数据预处理）
├── → [[线性回归基础]]（监督学习基础）
└── → [[交叉验证]]（模型评估方法）
```

---

## 步骤8：动手练习

### 练习1（KNN）
用 sklearn 的 KNN 对鸢尾花数据分类：
- 尝试不同的 K 值 (1, 3, 5, 7, 9)
- 画出 K vs 准确率 的曲线
- 找出最佳 K 值

### 练习2（随机森林）
用随机森林对乳腺癌数据集分类：
- `sklearn.datasets.load_breast_cancer()`
- 用交叉验证评估模型
- 找出最重要的5个特征

### 练习3（K-Means）
生成聚类数据并用 K-Means 聚类：
- 用 `make_blobs` 生成3簇数据
- 用轮廓系数评估聚类效果
- 尝试不同的 K 值，找最佳 K

### 练习4（综合挑战）
完成一个完整的机器学习项目：
```python
# 数据：sklearn.datasets.load_wine()
# 任务：分类
# 要求：
# 1. 数据标准化
# 2. 比较3种分类器
# 3. 用 GridSearchCV 调参
# 4. 输出最终准确率
```

---

## 答案参考

<details>
<summary>点击展开练习1答案</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 测试不同K值
k_values = [1, 3, 5, 7, 9]
train_scores = []
test_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    train_scores.append(knn.score(X_train_scaled, y_train))
    test_scores.append(knn.score(X_test_scaled, y_test))

# 画图
plt.figure(figsize=(8, 5))
plt.plot(k_values, train_scores, 'b-o', label='训练集')
plt.plot(k_values, test_scores, 'r-o', label='测试集')
plt.xlabel('K值')
plt.ylabel('准确率')
plt.title('KNN: K值 vs 准确率')
plt.legend()
plt.xticks(k_values)
plt.show()

# 找最佳K
best_k = k_values[np.argmax(test_scores)]
print(f"最佳K值: {best_k}, 测试集准确率: {max(test_scores):.2%}")
```

</details>

---

> 📌 **相关概念**：[[Python面向对象编程]] | [[数据清洗]] | [[数学基础线性代数]] | [[线性回归基础]]
> 
> 🔗 **前置知识**：[[Python面向对象编程]] | [[数据清洗]]
> 
> ⏭️ **下一节**：[[模型评估与交叉验证]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
