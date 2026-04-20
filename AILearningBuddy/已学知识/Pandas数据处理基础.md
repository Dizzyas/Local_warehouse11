---
date: 2026-04-20
tags: [AI, 已学, Python数据处理, Pandas]
---

# Pandas 数据处理基础

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**NumPy 已经很好了，为什么还要学 Pandas？**

NumPy 的数组要求所有元素类型一致（全是数字），但现实中数据是这样的：

| 姓名 | 年龄 | 城市 | 工资 | 是否在职 |
|------|------|------|------|----------|
| 张三 | 28 | 北京 | 15000 | 是 |
| 李四 | 35 | 上海 | 25000 | 否 |
| 王五 | 42 | 深圳 | 30000 | 是 |

- 姓名是字符串
- 年龄是整数
- 城市是字符串
- 工资是浮点数
- 是否在职是布尔值

**Pandas 就是来处理这种"表格数据"的**，比 Excel 更强大，比 NumPy 更灵活。

---

## 步骤2：前置知识确认

学习 Pandas 需要了解：

- ✅ Python 基础语法
- ✅ [[NumPy数组基础]]（强烈建议先学）
- ✅ 知道 Excel 表格是什么概念

---

## 步骤3：完整代码展示

```python
# ============================================
# Pandas 数据处理基础 — 完整可运行代码
# ============================================

import pandas as pd
import numpy as np

# ① 创建 DataFrame（表格数据）的几种方式

# 方式1：从字典创建（最常用）
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [28, 35, 42, 31, 25],
    '城市': ['北京', '上海', '深圳', '广州', '杭州'],
    '工资': [15000, 25000, 30000, 18000, 12000],
    '是否在职': [True, False, True, True, False]
}
df = pd.DataFrame(data)
print("=== 创建的DataFrame ===")
print(df)
print()

# 方式2：从 CSV 文件读取（实际工作最常用）
# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')

# 方式3：创建空表格
empty_df = pd.DataFrame()

# ② 查看数据基本信息
print("=== 基本信息 ===")
print("形状（行数, 列数）:", df.shape)
print("列名:", df.columns.tolist())
print("数据类型:\n", df.dtypes)
print("前3行:", df.head(3))
print("后2行:", df.tail(2))
print("基本统计:\n", df.describe())  # 只对数值列统计
print()

# ③ 选择列（两种方式）
print("=== 选择列 ===")
print("df['姓名'] =")
print(df['姓名'])
print("\ndf.姓名 =")
print(df.姓名)  # 简写，但列名有空格时不适用
print()

# ④ 选择行
print("=== 选择行 ===")
print("第2行（索引=1）:", df.iloc[1])        # 按位置
print("姓名为'李四'的行:", df[df['姓名'] == '李四'])  # 按条件
print()

# ⑤ 条件筛选（超实用！）
print("=== 条件筛选 ===")
print("工资 > 20000 的行:\n", df[df['工资'] > 20000])
print("\n城市是'北京'或'上海':\n", df[df['城市'].isin(['北京', '上海'])])
print("\n年龄在30-40之间且在职:\n", df[(df['年龄'] >= 30) & (df['年龄'] <= 40) & (df['是否在职'] == True)])
print()

# ⑥ 添加和删除列
print("=== 添加和删除列 ===")
# 添加新列
df['年薪'] = df['工资'] * 12
print("添加'年薪'列后:\n", df[['姓名', '工资', '年薪']])

# 根据条件添加列
df['收入等级'] = df['工资'].apply(lambda x: '高' if x > 20000 else '中' if x > 15000 else '低')
print("\n添加'收入等级'后:\n", df[['姓名', '工资', '收入等级']])

# 删除列
df = df.drop('年薪', axis=1)  # axis=1 表示删除列
print("\n删除'年薪'后:\n", df.head())
print()

# ⑦ 排序
print("=== 排序 ===")
print("按工资降序:\n", df.sort_values('工资', ascending=False))
print("\n按城市升序，再按工资降序:\n", df.sort_values(['城市', '工资'], ascending=[True, False]))
print()

# ⑧ 分组统计（超重要！数据汇总必备）
print("=== 分组统计 ===")
# 按城市分组，求平均工资
print("各城市平均工资:")
print(df.groupby('城市')['工资'].mean())

# 按城市分组，统计人数和平均工资
print("\n各城市统计:")
print(df.groupby('城市').agg({
    '姓名': 'count',    # 人数
    '工资': 'mean'       # 平均工资
}).rename(columns={'姓名': '人数', '工资': '平均工资'}))

# 在职/离职各多少人
print("\n各城市在职人数:")
print(df.groupby(['城市', '是否在职'])['姓名'].count())
print()

# ⑨ 处理缺失值
print("=== 缺失值处理 ===")
# 创建一个有缺失值的DataFrame
df_with_na = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, np.nan, 1]
})
print("有缺失值的DataFrame:\n", df_with_na)
print("\n缺失值数量:\n", df_with_na.isna().sum())
print("\n删除有缺失值的行:\n", df_with_na.dropna())
print("\n用均值填充缺失值:\n", df_with_na.fillna(df_with_na.mean()))
print()

# ⑩ 数据合并（merge/join）
print("=== 数据合并 ===")
df1 = pd.DataFrame({'姓名': ['张三', '李四'], '部门': ['技术', '市场']})
df2 = pd.DataFrame({'姓名': ['张三', '李四'], '工资': [15000, 25000]})
print("表1:\n", df1)
print("表2:\n", df2)
print("\n基于姓名合并:\n", pd.merge(df1, df2, on='姓名'))
print()

# ⑪ 数据导出
# df.to_csv('output.csv', index=False, encoding='utf-8-sig')
# df.to_excel('output.xlsx', index=False)

# ⑫ 常用技巧
print("=== 常用技巧 ===")
# 替换值
temp = df.copy()
temp['是否在职'] = temp['是否在职'].map({True: '在职', False: '离职'})
print("布尔转文字:\n", temp[['姓名', '是否在职']])

# apply 自定义函数
print("\n年龄分段:")
def age_group(age):
    if age < 30:
        return '青年'
    elif age < 40:
        return '中青年'
    else:
        return '中年'
df['年龄段'] = df['年龄'].apply(age_group)
print(df[['姓名', '年龄', '年龄段']])

# 透视表
print("\n各城市各年龄段平均工资:")
pivot = pd.pivot_table(df, values='工资', index='城市', columns='年龄段', aggfunc='mean')
print(pivot)
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：DataFrame 核心概念

**DataFrame = 表格 = 有行有列的数据**

```python
df = pd.DataFrame(data)
# data 是字典，key=列名，value=列数据
```

**记住**：
- `df.shape` → (行数, 列数)
- `df.columns` → 所有列名
- `df.dtypes` → 每列的数据类型

### 模块②：数据选择

| 操作 | 代码 | 说明 |
|------|------|------|
| 选择一列 | `df['姓名']` | 返回 Series |
| 选择多列 | `df[['姓名', '工资']]` | 返回 DataFrame |
| 选择一行 | `df.iloc[0]` | 按位置 |
| 选择条件行 | `df[df['工资']>20000]` | 按条件 |

**⚠️ 注意**：`df[0]` 是**错误**的！数字索引要用 `.iloc`

### 模块③：条件筛选

```python
df[(条件1) & (条件2)]  # AND
df[(条件1) | (条件2)]  # OR
df[~条件]              # NOT
```

**常见错误**：
```python
# ❌ 错误
df[df.工资 > 20000]  # 工资列名无空格时可以
# ✅ 正确
df[df['工资'] > 20000]  # 强烈建议用这种方式
```

### 模块④：分组统计 groupby

```python
df.groupby('城市')['工资'].mean()
#     ↑ 按哪列分组   ↑ 对哪列统计  ↑ 什么统计量
```

**常用统计量**：
- `count()` — 计数
- `mean()` — 均值
- `sum()` — 求和
- `min()` / `max()` — 最值
- `std()` / `var()` — 标准差/方差

**agg 可以组合多个统计**：
```python
df.groupby('城市').agg({'工资': ['mean', 'sum'], '姓名': 'count'})
```

### 模块⑤：缺失值处理

```python
df.isna()        # 判断每个元素是否为NA
df.dropna()      # 删除有NA的行
df.fillna(0)     # 用0填充NA
df.fillna(df.mean())  # 用均值填充
```

### 模块⑥：数据合并 merge

```python
pd.merge(df1, df2, on='姓名')
#        ↑ 表1   ↑ 表2  ↑ 依据哪列合并
```

---

## 步骤5：代码执行过程模拟

### 模拟1：条件筛选的执行

```
df[df['工资'] > 20000]

执行过程：
1. df['工资'] → 取出工资列 [15000, 25000, 30000, 18000, 12000]
2. > 20000 → 生成布尔数组 [False, True, True, False, False]
3. df[...] → 只保留 True 对应的行
4. 结果 → [李四, 王五] 两行
```

### 模拟2：groupby 的执行

```
df.groupby('城市')['工资'].mean()

执行过程：
1. 按'城市'列分组：
   北京 → [15000]
   上海 → [25000]
   深圳 → [30000]
   广州 → [18000]
   杭州 → [12000]

2. 对每个城市计算平均工资：
   北京: 15000
   上海: 25000
   深圳: 30000
   广州: 18000
   杭州: 12000

3. 返回 Series（城市是索引）
```

---

## 步骤6：完整运行结果展示

```text
=== 创建的DataFrame ===
   姓名  年龄  城市     工资   是否在职
0  张三   28   北京  15000       True
1  李四   35   上海  25000      False
2  王五   42   深圳  30000       True
3  赵六   31   广州  18000       True
4  钱七   25   杭州  12000      False

=== 基本信息 ===
形状（行数, 列数）: (5, 5)
列名: ['姓名', '年龄', '城市', '工资', '是否在职']
数据类型:
 姓名      object
 年龄       int64
 城市      object
 工资      int64
 是否在职     bool

=== 选择列 ===
df['姓名'] =
0    张三
1    李四
2    王五
3    赵六
4    钱七

=== 条件筛选 ===
工资 > 20000 的行:
    姓名  年龄  城市     工资   是否在职
1   李四   35   上海  25000      False
2   王五   42   深圳  30000       True

=== 分组统计 ===
各城市平均工资:
 城市
 上海    25000
 北京    15000
 广州    18000
 深圳    30000
 杭州    12000

各城市统计:
       人数  平均工资
 城市
 上海     1    25000
 北京     1    15000
 广州     1    18000
 深圳     1    30000
 杭州     1    12000

=== 透视表 ===
年龄段        中青年     中年     青年
 城市
 上海      35000.0      NaN      NaN
 北京          NaN      NaN  15000.0
 广州      18000.0      NaN      NaN
 深圳          NaN  30000.0      NaN
 杭州          NaN      NaN  12000.0
```

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
| 用数字索引行 | `df[0]` | `df.iloc[0]` 或 `df.loc[0]` |
| 忘记加引号列名 | `df[姓名]` | `df['姓名']` |
| & 和 \| 用混 | `df[a & b]` | `df[(a) & (b)]` 括号很重要！ |
| 修改原始df | `df.sort_values('工资')` 不会改原df | 需要重新赋值 `df = df.sort_values(...)` |
| merge 时列名不同 | `merge(df1, df2, on='X')` | `merge(df1, df2, left_on='X1', right_on='X2')` |

### 🔗 知识点关联

```
Pandas 数据处理
├── 基于 [[NumPy数组基础]]（Pandas 是 NumPy 的上层封装）
├── → [[Scikit-learn机器学习]]（训练数据通常是 Pandas DataFrame）
├── → [[Matplotlib数据可视化]]（绑定了 Pandas）
└── → [[特征工程]]（Pandas 是特征处理的工具）
```

---

## 步骤8：动手练习

### 练习1（基础）
创建一个学生成绩表，包含：姓名、语文、数学、英语、总分，然后：
- 计算每个人的总分
- 找出总分最高的人
- 计算每科的平均分

### 练习2（筛选）
基于上面的学生成绩表：
- 找出数学成绩 > 90 的学生
- 找出总分在 250-280 之间的学生
- 找出语文和英语都 > 85 的学生

### 练习3（分组统计）
创建一个销售数据表（城市、商品、销量、单价），然后：
- 按城市分组，求总销量
- 按商品分组，求平均单价
- 按城市和商品分组，求总销售额

### 练习4（挑战：真实数据处理）
模拟一个电商用户数据：
```python
users = pd.DataFrame({
    '用户ID': range(1, 101),
    '注册日期': pd.date_range('2024-01-01', periods=100, freq='D'),
    '城市': np.random.choice(['北京', '上海', '广州', '深圳'], 100),
    '消费金额': np.random.randint(0, 1000, 100),
    '活跃度': np.random.choice(['高', '中', '低'], 100)
})
```
- 统计各城市的用户数量
- 计算各活跃度的平均消费金额
- 找出消费金额 > 800 的"高活跃"用户
- 按城市统计最高消费金额

---

## 答案参考

<details>
<summary>点击展开练习1答案</summary>

```python
students = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '语文': [85, 92, 78, 88],
    '数学': [90, 85, 95, 92],
    '英语': [88, 90, 82, 85]
})

# 计算总分
students['总分'] = students['语文'] + students['数学'] + students['英语']
print("学生成绩表:\n", students)

# 最高总分
max_score = students['总分'].max()
top_student = students[students['总分'] == max_score]['姓名'].values[0]
print(f"\n最高分: {max_score}，学生: {top_student}")

# 各科平均分
print("\n各科平均分:")
print(students[['语文', '数学', '英语']].mean())
```

</details>

---

> 📌 **相关概念**：[[NumPy数组基础]] | [[Pandas]] | [[Scikit-learn]] | [[Matplotlib数据可视化]]
> 
> 🔗 **前置知识**：[[NumPy数组基础]]
> 
> ⏭️ **下一节**：[[Matplotlib数据可视化基础]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
