---
date: 2026-04-20
tags: [AI, 已学, Python数据处理, Seaborn]
---

# Seaborn 统计可视化进阶

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**Matplotlib 已经很强了，为什么还要学 Seaborn？**

用 Matplotlib 画一个分组柱状图：
```python
# Matplotlib：代码繁琐
import matplotlib.pyplot as plt
groups = ['A', 'B', 'C']
men_means = [20, 35, 30]
women_means = [25, 32, 35]
x = np.arange(len(groups))
width = 0.35
plt.bar(x - width/2, men_means, width)
plt.bar(x + width/2, women_means, width)
plt.xticks(x, groups)
```

用 Seaborn 画同样的图：
```python
# Seaborn：一行搞定！
import seaborn as sns
import pandas as pd
df = pd.DataFrame({'group': groups*2, 'mean': men_means + women_means, 'gender': ['男']*3 + ['女']*3})
sns.barplot(x='group', y='mean', hue='gender', data=df)
```

**Seaborn = Matplotlib 的高级封装，专门为统计可视化而生！**

---

## 步骤2：前置知识确认

学习 Seaborn 需要了解：

- ✅ [[Matplotlib数据可视化基础]]（Seaborn 基于 Matplotlib）
- ✅ [[Pandas数据处理基础]]（数据格式）
- ✅ [[NumPy数组基础]]（数据组织）

---

## 步骤3：完整代码展示

```python
# ============================================
# Seaborn 统计可视化 — 完整可运行代码
# ============================================

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文字体和风格
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")  # whitegrid/darkgrid/dark/white/ticks

# ============================================
# 第一部分：关系图（Relational）
# ============================================

print("=" * 50)
print("第一部分：关系图")
print("=" * 50)

# ① 散点图 + 回归线
print("\n=== 1. 散点图 + regression ===")

# 加载示例数据
tips = sns.load_dataset("tips")  # 餐厅小费数据
print(f"数据形状: {tips.shape}")
print(f"列名: {tips.columns.tolist()}")
print(tips.head())

# 基础散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(x="total_bill", y="tip", data=tips, alpha=0.6)
plt.title("账单 vs 小费")
plt.show()

# 带回归线的散点图（自动拟合一条直线）
plt.figure(figsize=(10, 6))
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("账单 vs 小费（含回归线）")
plt.show()

# 按类别分组（用 hue）
plt.figure(figsize=(10, 6))
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", data=tips, alpha=0.7)
plt.title("账单 vs 小费（按性别/吸烟分组）")
plt.show()

# ============================================
# 第二部分：分布图（Distribution）
# ============================================

print("\n" + "=" * 50)
print("第二部分：分布图")
print("=" * 50)

# ② 直方图 + KDE（核密度估计）
print("\n=== 2. 直方图 + KDE ===")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(tips["total_bill"], kde=True, bins=20)
plt.title("账单分布（直方图 + KDE）")

plt.subplot(1, 2, 2)
sns.kdeplot(data=tips["total_bill"], fill=True)
plt.title("账单分布（纯KDE）")

plt.tight_layout()
plt.show()

# ③ 多变量分布
print("\n=== 3. 多变量分布 ===")

plt.figure(figsize=(8, 6))
sns.displot(data=tips, x="total_bill", hue="sex", kind="kde", fill=True)
plt.title("按性别分组的账单分布")
plt.show()

# ④ 箱线图 + 小提琴图
print("\n=== 4. 箱线图 + 小提琴图 ===")

plt.figure(figsize=(14, 5))

plt.subplot(1, 3, 1)
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("各日期账单箱线图")

plt.subplot(1, 3, 2)
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("各日期账单小提琴图")

plt.subplot(1, 3, 3)
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set2")
plt.title("各日期账单（按性别分组）")

plt.tight_layout()
plt.show()

# ============================================
# 第三部分：分类图（Categorical）
# ============================================

print("\n" + "=" * 50)
print("第三部分：分类图")
print("=" * 50)

# ⑤ 柱状图
print("\n=== 5. 柱状图 ===")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.countplot(x="day", data=tips, palette="pastel")
plt.title("各日期顾客数量")

plt.subplot(1, 2, 2)
sns.countplot(x="day", hue="sex", data=tips, palette="Set2")
plt.title("各日期顾客数量（按性别分组）")

plt.tight_layout()
plt.show()

# ⑥ 条形图
print("\n=== 6. 条形图 ===")

plt.figure(figsize=(10, 5))
sns.barplot(x="day", y="total_bill", data=tips, estimator=np.mean, ci="sd", palette="muted")
plt.title("各日期平均账单（含标准差）")
plt.show()

# ============================================
# 第四部分：热力图
# ============================================

print("\n" + "=" * 50)
print("第四部分：热力图")
print("=" * 50)

# ⑦ 相关性热力图
print("\n=== 7. 相关性热力图 ===")

# 选择数值列
numeric_cols = tips.select_dtypes(include=[np.number]).columns
corr_matrix = tips[numeric_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0, square=True)
plt.title("相关性热力图")
plt.show()

# ⑧ 交叉表热力图
print("\n=== 8. 交叉表热力图 ===")

# 创建一个交叉表
cross_tab = pd.crosstab(tips["day"], tips["smoker"])
print("交叉表:")
print(cross_tab)

plt.figure(figsize=(8, 6))
sns.heatmap(cross_tab, annot=True, fmt="d", cmap="YlGnBu", cbar=True)
plt.title("日期 vs 吸烟交叉表")
plt.show()

# ============================================
# 第五部分：PairPlot 和 JointPlot
# ============================================

print("\n" + "=" * 50)
print("第五部分：高级图表")
print("=" * 50)

# ⑨ PairPlot（散点图矩阵）
print("\n=== 9. PairPlot ===")

# 选择少量变量避免太慢
small_tips = tips[["total_bill", "tip", "size"]]
sns.pairplot(small_tips, diag_kind="kde", hue="size", palette="viridis")
plt.suptitle("PairPlot: total_bill, tip, size", y=1.02)
plt.show()

# ⑩ JointPlot（联合分布图）
print("\n=== 10. JointPlot ===")

plt.figure(figsize=(8, 8))
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
plt.suptitle("JointPlot: 账单与小费的关系", y=1.02)
plt.show()

# ============================================
# 第六部分：实战 - 完整数据分析图表
# ============================================

print("\n" + "=" * 50)
print("第六部分：实战综合")
print("=" * 50)

# ⑪ 完整的探索性数据分析
print("\n=== 11. 餐厅小费数据分析 ===")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 1. 账单分布
sns.histplot(tips["total_bill"], kde=True, ax=axes[0, 0], color="skyblue")
axes[0, 0].set_title("1. 账单分布")

# 2. 小费分布
sns.histplot(tips["tip"], kde=True, ax=axes[0, 1], color="salmon")
axes[0, 1].set_title("2. 小费分布")

# 3. 账单 vs 小费（按是否吸烟着色）
sns.scatterplot(x="total_bill", y="tip", hue="smoker", data=tips, ax=axes[0, 2], alpha=0.6)
axes[0, 2].set_title("3. 账单 vs 小费（吸烟分组）")

# 4. 各日期平均小费率
tips["tip_percent"] = tips["tip"] / tips["total_bill"] * 100
sns.barplot(x="day", y="tip_percent", data=tips, ax=axes[1, 0], estimator=np.mean, color="lightgreen")
axes[1, 0].set_title("4. 各日期平均小费率(%)")

# 5. 各日期账单箱线图
sns.boxplot(x="day", y="total_bill", data=tips, ax=axes[1, 1], palette="pastel")
axes[1, 1].set_title("5. 各日期账单分布")

# 6. 相关性热力图
corr = tips[["total_bill", "tip", "size", "tip_percent"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=axes[1, 2], square=True)
axes[1, 2].set_title("6. 相关性热力图")

plt.suptitle("餐厅小费数据探索性分析", fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

# ============================================
# 第七部分：风格和调色板
# ============================================

print("\n" + "=" * 50)
print("第七部分：风格和调色板")
print("=" * 50)

# ⑫ Seaborn 风格对比
print("\n=== 12. 风格对比 ===")

styles = ["whitegrid", "darkgrid", "white", "dark", "ticks"]
fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for i, style in enumerate(styles):
    sns.set_style(style)
    sns.boxplot(x="day", y="total_bill", data=tips, ax=axes[i])
    axes[i].set_title(style)

plt.suptitle("Seaborn 5种风格对比", y=1.05)
plt.tight_layout()
plt.show()

# 恢复默认风格
sns.set()

# ⑬ 调色板
print("\n=== 13. 调色板 ===")

palettes = ["deep", "muted", "pastel", "bright", "dark", "colorblind"]
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, palette in enumerate(palettes):
    sns.set_palette(palette)
    sns.barplot(x=["A", "B", "C", "D"], y=[3, 5, 2, 7], ax=axes[i], palette=palette)
    axes[i].set_title(f"调色板: {palette}")

plt.suptitle("Seaborn 调色板示例", y=1.02)
plt.tight_layout()
plt.show()

# ============================================
# 第八部分：常用参数速查
# ============================================

print("\n" + "=" * 50)
print("第八部分：常用参数速查")
print("=" * 50)

print("""
=== Seaborn 图表类型速查 ===

关系图：
  sns.scatterplot()     - 散点图
  sns.lineplot()        - 折线图
  sns.regplot()        - 带回归线的散点图

分布图：
  sns.histplot()       - 直方图（可加KDE）
  sns.kdeplot()        - KDE密度图
  sns.displot()        - 通用分布图
  sns.boxplot()        - 箱线图
  sns.violinplot()     - 小提琴图
  sns.stripplot()      - 带状散点图
  sns.swarmplot()       - 群状散点图

分类图：
  sns.barplot()        - 柱状图
  sns.countplot()      - 计数柱状图
  sns.catplot()        - 通用分类图

其他：
  sns.heatmap()        - 热力图
  sns.pairplot()       - 散点图矩阵
  sns.jointplot()      - 联合分布图
  sns.FacetGrid()      - 分面网格
  sns.lmplot()         - 带回归线的分面图

=== 常用参数 ===
  x, y                 - x/y轴数据
  hue                  - 分组颜色
  style                - 分组线型
  size                 - 分组大小
  data                 - DataFrame数据
  palette              - 调色板
  ci                   - 置信区间
  estimator            - 聚合函数
""")
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：Seaborn vs Matplotlib

| 特性 | Matplotlib | Seaborn |
|------|-----------|---------|
| 语法 | 底层，命令式 | 高级，声明式 |
| 分组 | 手动循环 | `hue` 参数自动 |
| 美观 | 需手动调整 | 默认就好看 |
| 绑定数据 | 用numpy数组 | 直接用DataFrame |

### 模块②：核心概念

```python
# Seaborn 的核心是 DataFrame
tips = sns.load_dataset("tips")

# 通用模式
sns.图表类型(x="列名", y="列名", data=DataFrame, hue="分组列")
```

### 模块③：常用图表选择

| 目的 | 推荐图表 |
|------|---------|
| 看两个变量的关系 | `scatterplot` / `regplot` |
| 看分布 | `histplot` / `kdeplot` / `violinplot` |
| 比较多组 | `barplot` / `boxplot` |
| 看相关性 | `heatmap` |
| 多变量关系 | `pairplot` / `jointplot` |

### 模块④：KDE（核密度估计）

```python
# KDE = Kernel Density Estimation
# 用平滑曲线估计数据的概率密度
sns.kdeplot(data, fill=True)  # 填充颜色
```

### 模块⑤：箱线图 vs 小提琴图

| 图表 | 优点 | 适用场景 |
|------|------|---------|
| 箱线图 | 清晰显示分位数和异常值 | 有异常值/需要标注 |
| 小提琴图 | 显示分布形状 | 看数据分布形态 |

---

## 步骤5：代码执行过程模拟

### 模拟1：heatmap 执行流程

```
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

1. 读取 corr_matrix（相关性矩阵）
2. 将数值映射到颜色（coolwarm色图）
3. 如果 annot=True，在每个格子写数字
4. 添加颜色条（colorbar）
5. 渲染显示
```

---

## 步骤6：完整运行结果展示

```text
=== 11. 餐厅小费数据分析 ===
生成了 6 个子图组成的综合分析面板：
- 直方图（账单分布）
- 直方图（小费分布）
- 散点图（按吸烟分组）
- 柱状图（各日期小费率）
- 箱线图（各日期账单）
- 热力图（相关性）

=== 12. 风格对比 ===
展示了 5 种不同背景风格的箱线图：
whitegrid/darkgrid/white/dark/ticks
```

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
| 中文字体乱码 | 不设置 | 加 `plt.rcParams` |
| 数据不是DataFrame | 传numpy数组 | 先转DataFrame |
| 样式被覆盖 | 混用seaborn和matplotlib | `sns.set()` 后统一 |
| pairplot太慢 | 用大数据集 | 先选子集 `pairplot(df[[...]])` |

### 🔗 知识点关联

```
Seaborn 统计可视化
├── 基于 [[Matplotlib数据可视化基础]]
├── 基于 [[Pandas数据处理基础]]
├── → [[Scikit-learn机器学习]]（模型结果可视化）
└── → [[数据分析实战]]（EDA探索性分析）
```

---

## 步骤8：动手练习

### 练习1
用 `sns.load_dataset("iris")` 画一个 pairplot，查看四种花萼/花瓣的分布关系。

### 练习2
用 seaborn 画一个热力图，显示鸢尾花各特征之间的相关性。

### 练习3
用小费数据集，分析：
- 男性和女性的平均小费是否有显著差异
- 吸烟者和非吸烟者的小费分布

---

> 📌 **相关概念**：[[Matplotlib数据可视化基础]] | [[Pandas数据处理基础]] | [[Scikit-learn机器学习基础]]
> 
> 🔗 **前置知识**：[[Matplotlib数据可视化基础]]
> 
> ⏭️ **下一节**：[[数据清洗]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
