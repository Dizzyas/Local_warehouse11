---
date: 2026-04-20
tags: [AI, 已学, Python数据处理, Matplotlib]
---

# Matplotlib 数据可视化基础

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**数据处理完了，怎么让别人看懂？**

你跑模型算出了一堆数字：
```
MSE: 0.917, R²: 0.765, 准确率: 87.3%
```

光给数字，别人一头雾水。但如果画成图：

- 📈 折线图：看趋势变化
- 📊 柱状图：比大小
- 🥧 饼图：看占比
- 🔥 热力图：看分布
- 📉 散点图：看关系

**一张好图胜过千言万语！**

Matplotlib 是 Python 可视化的鼻祖，几乎所有其他可视化库（Seaborn、Plotly）都是基于它封装的。

---

## 步骤2：前置知识确认

学习 Matplotlib 需要了解：

- ✅ Python 基础语法
- ✅ [[NumPy数组基础]]（绑定了 Matplotlib）
- ✅ [[Pandas数据处理基础]]（处理好的数据喂给 Matplotlib 画图）

---

## 步骤3：完整代码展示

```python
# ============================================
# Matplotlib 数据可视化基础 — 完整可运行代码
# ============================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文字体支持（重要！否则中文显示乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# ============================================
# 基础篇：7种最常用图表
# ============================================

# ① 折线图（Line Plot）— 看趋势
print("=== 1. 折线图 ===")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 5))  # figsize=(宽, 高)，单位英寸
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2, linestyle='-')
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')
plt.title('三角函数图像', fontsize=16)  # 标题
plt.xlabel('X轴', fontsize=12)          # X轴标签
plt.ylabel('Y轴', fontsize=12)          # Y轴标签
plt.legend()                            # 显示图例
plt.grid(True)                          # 显示网格
plt.show()                              # 显示图像

# ② 散点图（Scatter Plot）— 看相关性
print("\n=== 2. 散点图 ===")
np.random.seed(42)
x = np.random.rand(50) * 100
y = x * 0.8 + np.random.randn(50) * 15  # 添加一些噪声

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=y, cmap='viridis', alpha=0.7, s=60)  # c=颜色，alpha=透明度，s=大小
plt.colorbar(label='数值')  # 显示颜色条
plt.title('散点图示例（身高vs体重）', fontsize=14)
plt.xlabel('X（体重 kg）', fontsize=12)
plt.ylabel('Y（身高 cm）', fontsize=12)
plt.grid(True, alpha=0.3)  # alpha=透明度
plt.show()

# ③ 柱状图（Bar Chart）— 比大小
print("\n=== 3. 柱状图 ===")
cities = ['北京', '上海', '深圳', '广州', '杭州']
populations = [2154, 2487, 1344, 1530, 1220]  # 单位：万

plt.figure(figsize=(10, 6))
bars = plt.bar(cities, populations, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
# 给柱子顶部加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
             ha='center', va='bottom', fontsize=10)
plt.title('各城市人口对比（2024）', fontsize=16)
plt.xlabel('城市', fontsize=12)
plt.ylabel('人口（万）', fontsize=12)
plt.show()

# ④ 直方图（Histogram）— 看分布
print("\n=== 4. 直方图 ===")
data = np.random.randn(1000)  # 生成1000个正态分布随机数

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='steelblue', edgecolor='white', alpha=0.7)
plt.axvline(x=0, color='red', linestyle='--', linewidth=2, label='均值=0')
plt.title('正态分布直方图', fontsize=16)
plt.xlabel('数值', fontsize=12)
plt.ylabel('频数', fontsize=12)
plt.legend()
plt.show()

# ⑤ 饼图（Pie Chart）— 看占比
print("\n=== 5. 饼图 ===")
labels = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
sizes = [30, 20, 25, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.05, 0, 0, 0, 0)  # 第一个块突出

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('编程语言使用占比', fontsize=16)
plt.axis('equal')  # 让饼图是圆的，不是椭圆
plt.show()

# ⑥ 子图（Subplot）— 一图多表
print("\n=== 6. 子图 ===")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2行2列共4个子图

# 子图1：正弦
axes[0, 0].plot(x, np.sin(x), 'b-')
axes[0, 0].set_title('sin(x)')

# 子图2：余弦
axes[0, 1].plot(x, np.cos(x), 'r-')
axes[0, 1].set_title('cos(x)')

# 子图3：正切
axes[1, 0].plot(x, np.tan(x), 'g-')
axes[1, 0].set_ylim(-5, 5)  # 限制Y轴范围
axes[1, 0].set_title('tan(x)')

# 子图4：随机散点
axes[1, 1].scatter(np.random.rand(50), np.random.rand(50), alpha=0.6)
axes[1, 1].set_title('Random Scatter')

plt.suptitle('四大三角函数子图', fontsize=16, y=1.02)  # 总标题
plt.tight_layout()
plt.show()

# ============================================
# 进阶篇：机器学习专属可视化
# ============================================

# ⑦ 模型训练曲线（Loss/Accuracy）
print("\n=== 7. 训练曲线 ===")
epochs = range(1, 21)
train_loss = [2.5, 1.8, 1.4, 1.1, 0.9, 0.75, 0.65, 0.55, 0.48, 0.42,
              0.38, 0.35, 0.32, 0.30, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23]
val_loss = [2.6, 1.9, 1.5, 1.3, 1.2, 1.1, 1.05, 1.0, 0.98, 0.96,
            0.95, 0.94, 0.93, 0.93, 0.92, 0.92, 0.92, 0.91, 0.91, 0.91]
train_acc = [0.3, 0.45, 0.58, 0.68, 0.75, 0.80, 0.84, 0.87, 0.89, 0.91,
             0.92, 0.93, 0.94, 0.94, 0.95, 0.95, 0.96, 0.96, 0.96, 0.97]
val_acc = [0.28, 0.42, 0.54, 0.62, 0.68, 0.72, 0.75, 0.77, 0.79, 0.80,
           0.81, 0.81, 0.82, 0.82, 0.82, 0.82, 0.82, 0.82, 0.82, 0.82]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Loss曲线
ax1.plot(epochs, train_loss, 'b-', label='训练集Loss', linewidth=2)
ax1.plot(epochs, val_loss, 'r-', label='验证集Loss', linewidth=2)
ax1.set_title('Loss 曲线', fontsize=14)
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Accuracy曲线
ax2.plot(epochs, train_acc, 'b-', label='训练集Accuracy', linewidth=2)
ax2.plot(epochs, val_acc, 'r-', label='验证集Accuracy', linewidth=2)
ax2.set_title('Accuracy 曲线', fontsize=14)
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle('模型训练监控', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

# ⑧ 混淆矩阵可视化
print("\n=== 8. 混淆矩阵 ===")
from sklearn.metrics import confusion_matrix
import seaborn as sns

y_true = [0, 1, 2, 2, 1, 0, 2, 1, 0, 1, 2, 0, 1, 2, 0]
y_pred = [0, 0, 2, 2, 1, 0, 1, 2, 0, 1, 2, 0, 0, 2, 1]

cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['类0', '类1', '类2'],
            yticklabels=['类0', '类1', '类2'])
plt.title('混淆矩阵', fontsize=14)
plt.xlabel('预测标签', fontsize=12)
plt.ylabel('真实标签', fontsize=12)
plt.show()

# ⑨ 特征重要性（随机森林）
print("\n=== 9. 特征重要性 ===")
features = ['年龄', '收入', '信用分', '工作年限', '负债率', '贷款额']
importances = [0.15, 0.28, 0.25, 0.12, 0.10, 0.10]

plt.figure(figsize=(10, 6))
plt.barh(features, importances, color='steelblue')
plt.xlabel('重要性', fontsize=12)
plt.title('随机森林特征重要性', fontsize=14)
plt.show()

# ============================================
# 保存图片的3种方式
# ============================================
print("\n=== 保存图片 ===")
# 方式1：保存到文件
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig('plot.png', dpi=300, bbox_inches='tight')  # dpi=分辨率，bbox_inches去掉白边
plt.savefig('plot.pdf')  # 矢量图格式，适合论文
plt.savefig('plot.svg')  # SVG格式，网页常用

# 方式2：保存到内存（BytesIO），可用于API返回
from io import BytesIO
img_buffer = BytesIO()
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig(img_buffer, format='png')
img_buffer.seek(0)
# image_base64 = base64.b64encode(img_buffer.read()).decode()
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：中文字体设置（必须设置！）

```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
```

**不加这行代码，中文全显示成方块！**

如果你是 Mac：`'Arial Unicode MS'`
如果你是 Linux：`['WenQuanYi Micro Hei', 'SimHei']`

### 模块②：7种基础图表对比

| 图表 | 函数 | 适用场景 |
|------|------|---------|
| 折线图 | `plt.plot(x, y)` | 时间序列、趋势变化 |
| 散点图 | `plt.scatter(x, y)` | 两变量相关性 |
| 柱状图 | `plt.bar(x, y)` | 类别对比 |
| 直方图 | `plt.hist(data, bins)` | 数据分布 |
| 饼图 | `plt.pie(sizes)` | 占比展示 |
| 热力图 | `sns.heatmap()` | 相关性矩阵、混淆矩阵 |
| 子图 | `plt.subplots(行, 列)` | 多图对比 |

### 模块③：常用参数速查

```python
plt.plot(x, y,
    color='red',        # 颜色
    linewidth=2,        # 线宽
    linestyle='--',     # 线型：'-'实线 '--'虚线 ':'点线
    marker='o',         # 数据点标记：'o'圆点 's'方块 '*'星
    alpha=0.7,          # 透明度（0-1）
    label='数据A'        # 图例标签
)

plt.scatter(x, y,
    c=colors,           # 颜色（可以是数值数组，用于渐变色）
    cmap='viridis',     # 颜色映射
    s=100,              # 点的大小
    marker='o'          # 点的形状
)
```

### 模块④：机器学习可视化三件套

```python
# 1. 训练曲线 — 判断过拟合
plt.plot(epochs, train_loss, label='训练Loss')
plt.plot(epochs, val_loss, label='验证Loss')
# 如果验证Loss持续上升 → 过拟合

# 2. 混淆矩阵 — 看分类错误分布
sns.heatmap(cm, annot=True, fmt='d')
# 对角线是正确分类，非对角线是错误

# 3. 特征重要性 — 决定性因素
plt.barh(features, importances)
# 越长越重要
```

### 模块⑤：保存图片参数

```python
plt.savefig('output.png',
    dpi=300,              # 分辨率，印刷用300，网页用72
    bbox_inches='tight', # 去掉周围白边
    format='png',         # 格式选择
    transparent=True      # 透明背景
)
```

---

## 步骤5：代码执行过程模拟

### 模拟1：plt.plot() 的执行流程

```
plt.plot([1,2,3], [1,4,9])

1. 内部创建 Figure 对象（画布）
2. 创建 Axes 对象（坐标系）
3. 调用 Axes.plot() 在坐标系中画线
4. 返回 Line2D 对象
5. plt.show() 调用 GUI 渲染显示
```

### 模拟2：subplots 创建多图

```python
fig, axes = plt.subplots(2, 2)
# 等价于：
# fig = plt.figure()
# axes[0,0] = fig.add_subplot(2, 2, 1)
# axes[0,1] = fig.add_subplot(2, 2, 2)
# axes[1,0] = fig.add_subplot(2, 2, 3)
# axes[1,1] = fig.add_subplot(2, 2, 4)
```

---

## 步骤6：完整运行结果展示

（图形无法用文字展示，以下描述图形特征）

**1. 折线图**：
- 蓝色 sin(x) 曲线和红色 cos(x) 曲线
- X轴 0-10，Y轴 -1 到 1
- 带网格和图例

**2. 散点图**：
- 50个点组成的斜向分布（正相关）
- 颜色根据Y值渐变（viridis色图）
- 带颜色条

**3. 柱状图**：
- 5个城市人口对比柱状图
- 每根柱子上方有数值标签

**4. 直方图**：
- 钟形分布（正态分布）
- 红色虚线标记均值位置

**5. 饼图**：
- 5块组成的饼图
- Python块略微突出

**6. 子图**：
- 2×2网格，分别展示 sin/cos/tan/随机散点

**7. 训练曲线**：
- 左图：Loss下降曲线，训练Loss和验证Loss差距逐渐拉大
- 右图：Accuracy上升曲线，最终趋于稳定

**8. 混淆矩阵**：
- 3×3热力图
- 对角线颜色深（正确分类多）

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
| 中文乱码 | 不设置字体 | 加 `rcParams` 设置 |
| 图像不显示 | 代码最后没加 `plt.show()` | 加上，或用 `plt.savefig()` |
| 内存泄漏 | 循环中频繁 `plt.figure()` 不关闭 | 用 `plt.clf()` 或 `plt.close()` |
| 子图重叠 | `tight_layout()` 忘记加 | 加上 |
| 保存白边 | 直接 `savefig()` | 加 `bbox_inches='tight'` |
| 显示不出 | 在循环外 `plt.show()` | 每次画图后 `plt.show()` |

### 🔗 知识点关联

```
Matplotlib 数据可视化
├── 基于 [[NumPy数组基础]]（底层数据）
├── 基于 [[Pandas数据处理基础]]（数据来源）
├── → [[Scikit-learn机器学习]]（可视化模型结果）
└── → [[线性回归基础]]（配合可视化）
```

---

## 步骤8：动手练习

### 练习1（基础）
用 Matplotlib 画一个学生的成绩单柱状图：
- 学生：张三、李四、王五、赵六
- 语文：85、92、78、88
- 数学：90、85、95、92
- 要求：分组柱状图（每个学生一组，两个科目并排）

### 练习2（数据分析）
生成 1000 个符合正态分布的随机数，分别：
- 画直方图（bins=20, 50, 100 对比）
- 标注均值和标准差

### 练习3（机器学习）
模拟一个二分类模型的训练过程：
- 生成 train_acc 和 val_acc 曲线
- 标注出"过拟合开始点"（验证集开始下降的点）
- 解释图形的含义

### 练习4（挑战）
用 Pandas 读取一个 CSV 文件（可用随机数据生成后保存），然后：
1. 画出行列对应的图表
2. 保存为 PNG 和 PDF 两种格式

---

## 答案参考

<details>
<summary>点击展开练习1答案</summary>

```python
students = ['张三', '李四', '王五', '赵六']
chinese = [85, 92, 78, 88]
math = [90, 85, 95, 92]

x = np.arange(len(students))  # [0, 1, 2, 3]
width = 0.35  # 柱子宽度

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, chinese, width, label='语文', color='#1f77b4')
bars2 = ax.bar(x + width/2, math, width, label='数学', color='#ff7f0e')

ax.set_xlabel('学生', fontsize=12)
ax.set_ylabel('成绩', fontsize=12)
ax.set_title('学生成绩对比', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(students)
ax.legend()
ax.set_ylim(0, 100)  # 成绩范围0-100

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
            ha='center', va='bottom')
for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
            ha='center', va='bottom')

plt.tight_layout()
plt.show()
```

</details>

---

> 📌 **相关概念**：[[NumPy数组基础]] | [[Pandas数据处理基础]] | [[Matplotlib]]
> 
> 🔗 **前置知识**：[[NumPy数组基础]] | [[Pandas数据处理基础]]
> 
> ⏭️ **下一节**：[[Scikit-learn机器学习基础]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
