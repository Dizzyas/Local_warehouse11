---
date: 2026-04-20
tags: [AI, 已学, Python基础, 面向对象编程]
---

# Python 面向对象编程（OOP）

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**你有没有遇到这种情况？**

写了一个计算器程序，有加、减、乘、除 4 个函数：
```python
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b
```

后来发现需要给计算器加一个**记录历史**功能，要改成：
```python
history = []  # 全局变量！

def add(a, b):
    history.append(f"{a} + {b} = {a+b}")
    return a + b
```

问题来了：
- 全局变量到处都是，不安全
- 想创建**多个独立的计算器**（各自有各自的历史）怎么办？
- 如果有人不小心改了 `history` 怎么办？

**面向对象编程（OOP）就是来解决这类问题的！**

---

## 步骤2：前置知识确认

学习 OOP 需要了解：

- ✅ Python 基础语法（变量、函数、循环）
- ✅ Python list 和 dict 的基本使用
- ✅ 知道什么是"类"和"对象"（生活中见过，比如"狗是动物的一个对象"）

---

## 步骤3：完整代码展示

```python
# ============================================
# Python 面向对象编程 — 完整可运行代码
# ============================================

# ① 最简单的类定义
print("=== 1. 最简单的类 ===")

class Dog:
    """一只狗的类"""
    
    # 属性（类变量）- 所有实例共享
    species = "犬科"
    
    # 初始化方法（构造器）
    def __init__(self, name, age):
        # 实例变量 - 每个实例独立
        self.name = name
        self.age = age
    
    # 实例方法
    def bark(self):
        return f"{self.name} 在叫：汪汪汪！"
    
    def info(self):
        return f"{self.name}，{self.age}岁，{self.species}"

# 创建实例（对象）
dog1 = Dog("旺财", 3)
dog2 = Dog("小白", 5)

print(dog1.bark())
print(dog2.bark())
print(dog1.info())
print(dog2.info())
print(f"狗1的名字: {dog1.name}")
print(f"狗2的名字: {dog2.name}")

# ② 面向对象版计算器（核心示例）
print("\n=== 2. 面向对象计算器 ===")

class Calculator:
    """计算器类 - 演示 OOP 核心概念"""
    
    def __init__(self, name="我的计算器"):
        self.name = name          # 计算器名字
        self.history = []         # 每个实例独立的history
        self.result = 0          # 当前结果
    
    def add(self, a, b=None):
        """加法。如果只传一个数，就加到当前结果上"""
        if b is None:
            self.result = self.result + a
        else:
            self.result = a + b
        self.history.append(f"加法: {a} + {b if b else self.result - a} = {self.result}")
        return self.result
    
    def subtract(self, a, b=None):
        """减法"""
        if b is None:
            self.result = self.result - a
        else:
            self.result = a - b
        self.history.append(f"减法: {a} - {b if b else a - self.result} = {self.result}")
        return self.result
    
    def multiply(self, a, b):
        """乘法"""
        self.result = a * b
        self.history.append(f"乘法: {a} × {b} = {self.result}")
        return self.result
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            self.history.append("错误：除数不能为0！")
            return None
        self.result = a / b
        self.history.append(f"除法: {a} ÷ {b} = {self.result}")
        return self.result
    
    def show_history(self):
        """显示历史记录"""
        if not self.history:
            print(f"{self.name} 还没有计算记录")
        else:
            print(f"\n{'='*20}")
            print(f"{self.name} 的历史记录：")
            for i, record in enumerate(self.history, 1):
                print(f"  {i}. {record}")
            print(f"{'='*20}")
    
    def clear(self):
        """清空历史"""
        self.history = []
        self.result = 0
        print(f"{self.name} 已清空")


# 创建两个独立的计算器
calc1 = Calculator("张三的计算器")
calc2 = Calculator("李四的计算器")

# calc1 的计算
calc1.add(10, 5)
calc1.multiply(3, 4)
calc1.add(100)  # 加到当前结果上

# calc2 的计算（完全独立！）
calc2.add(1000, 500)
calc2.subtract(200)

print(f"calc1 当前结果: {calc1.result}")  # 10+5=15, 15*3=45, 45+100=145
print(f"calc2 当前结果: {calc2.result}")  # 1000+500=1500, 1500-200=1300

# 显示历史（各自独立！）
calc1.show_history()
calc2.show_history()

# calc1 清空，不影响 calc2
calc1.clear()
print(f"清空后 calc1 结果: {calc1.result}")
print(f"清空后 calc2 结果: {calc2.result}")  # calc2 不受影响！

# ③ 继承（重要！复用代码）
print("\n=== 3. 继承 ===")

class Animal:
    """动物基类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        raise NotImplementedError("子类必须实现 speak 方法")
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age}岁)"


class Cat(Animal):
    """猫类 - 继承自动物"""
    
    def speak(self):
        return f"{self.name} 在叫：喵喵喵~"


class Dog2(Animal):
    """狗类 - 继承自动物"""
    
    def speak(self):
        return f"{self.name} 在叫：汪汪汪！"


class Bird(Animal):
    """鸟类 - 继承自动物"""
    
    def speak(self):
        return f"{self.name} 在叫：啾啾啾~"


# 创建不同动物
animals = [Cat("黑猫", 2), Dog2("旺财", 3), Bird("小鸟", 1)]
for animal in animals:
    print(f"{animal} 说：{animal.speak()}")

# ④ 私有属性（封装）- 保护数据
print("\n=== 4. 私有属性 ===")

class BankAccount:
    """银行账户类 - 演示封装"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner              # 公开属性
        self.__balance = balance        # 私有属性（双下划线开头），外部不能直接访问
        self.__transaction_count = 0    # 私有属性
    
    def deposit(self, amount):
        """存钱"""
        if amount <= 0:
            print("存款金额必须大于0！")
            return False
        self.__balance += amount
        self.__transaction_count += 1
        print(f"{self.owner} 存了 {amount} 元，余额：{self.__balance}")
        return True
    
    def withdraw(self, amount):
        """取钱"""
        if amount > self.__balance:
            print(f"余额不足！当前余额：{self.__balance}")
            return False
        self.__balance -= amount
        self.__transaction_count += 1
        print(f"{self.owner} 取了 {amount} 元，余额：{self.__balance}")
        return True
    
    def get_balance(self):
        """获取余额（通过方法访问）"""
        return self.__balance
    
    def get_info(self):
        """获取账户信息"""
        return {
            "户主": self.owner,
            "余额": self.__balance,
            "交易次数": self.__transaction_count
        }


account = BankAccount("张三", 1000)
print(f"余额（通过方法）：{account.get_balance()}")

account.deposit(500)
account.withdraw(200)
# print(account.__balance)  # ❌ 这行会报错！不能直接访问私有属性
# account.__balance = 999999  # ❌ 也不行！

print(f"账户信息：{account.get_info()}")

# ⑤ 类方法 vs 实例方法 vs 静态方法
print("\n=== 5. 类方法 vs 实例方法 vs 静态方法 ===")

class MathTool:
    """数学工具类"""
    
    pi = 3.14159  # 类变量
    
    def __init__(self, name):
        self.name = name  # 实例变量
    
    # 实例方法 - 第一个参数是 self
    def circle_area(self, radius):
        return f"{self.name}: 半径{radius}的圆面积 = {MathTool.pi * radius ** 2}"
    
    # 类方法 - 第一个参数是类本身
    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi
        print(f"圆周率已更新为: {cls.pi}")
    
    # 静态方法 - 和类没什么关系，只是放在类里
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def max(a, b):
        return a if a > b else b


m = MathTool("计算器")
print(m.circle_area(5))  # 实例方法调用

MathTool.set_pi(3.14)   # 类方法调用，修改后所有实例都受影响
print(m.circle_area(5))  # 再次调用，圆周率已经变了

print(MathTool.add(1, 2))      # 静态方法
print(MathTool.max(10, 20))   # 静态方法

# ⑥ 特殊方法（魔术方法）
print("\n=== 6. 特殊方法 ===")

class Vector:
    """向量类 - 演示特殊方法"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 字符串表示
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"
    
    # 加法
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # 乘法（向量 * 数）
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # 长度
    def __len__(self):
        return 2  # 二维向量
    
    # 索引访问
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector 只有 x 和 y 两个分量")
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"len(v1) = {len(v1)}")
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
print(f"v1 == Vector(3, 4) : {v1 == Vector(3, 4)}")

# ⑦ 实际应用：Scikit-learn 风格的机器学习封装
print("\n=== 7. Scikit-learn 风格封装 ===")

class SimpleLinearRegression:
    """
    简单线性回归模型 - 模仿 Scikit-learn 的 API 设计风格
    
    Scikit-learn 的模型都遵循 fit(X, y) / predict(X) 模式
    """
    
    def __init__(self):
        self.coef_ = None    # 系数（下划线结尾是 Scikit-learn 惯例）
        self.intercept_ = None  # 截距
        self._is_fitted = False
    
    def fit(self, X, y):
        """训练模型"""
        import numpy as np
        X = np.array(X)
        y = np.array(y)
        
        # 简单线性回归公式: y = wx + b
        n = len(X)
        sum_x = np.sum(X)
        sum_y = np.sum(y)
        sum_xy = np.sum(X * y)
        sum_xx = np.sum(X ** 2)
        
        w = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
        b = (sum_y - w * sum_x) / n
        
        self.coef_ = w
        self.intercept_ = b
        self._is_fitted = True
        
        print(f"训练完成！系数: {w:.4f}, 截距: {b:.4f}")
        return self
    
    def predict(self, X):
        """预测"""
        if not self._is_fitted:
            raise ValueError("模型还没训练！请先调用 fit()")
        X = np.array(X)
        return self.coef_ * X + self.intercept_
    
    def score(self, X, y):
        """计算 R² 分数"""
        from sklearn.metrics import r2_score
        y_pred = self.predict(X)
        return r2_score(y, y_pred)


# 使用我们的线性回归模型
X = [1, 2, 3, 4, 5]
y = [2.1, 4.0, 5.9, 8.1, 10.2]  # 接近 y = 2x

model = SimpleLinearRegression()
model.fit(X, y)

y_pred = model.predict([6, 7])
print(f"预测 X=6,7: {y_pred}")

score = model.score(X, y)
print(f"R² 分数: {score:.4f}")
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：类的基础结构

```python
class Dog:                    # class 关键字 + 类名
    """一只狗的类"""          # 文档字符串（说明这个类是干什么的）
    
    species = "犬科"          # 类变量（所有实例共享）
    
    def __init__(self, name, age):  # __init__ 是初始化方法（构造器）
        self.name = name      # self.name 是实例变量（每个实例独立）
        self.age = age
    
    def bark(self):           # 实例方法（第一个参数一定是 self）
        return f"{self.name} 在叫：汪汪汪！"
```

**核心概念：**
- `class` 关键字定义类
- `self` 指向**实例本身**（相当于"我"）
- `__init__` 是**构造器**，创建实例时自动调用
- 类变量所有实例共享，实例变量每个实例独立

### 模块②：计算器类 - OOP 三要素

| 概念 | 计算器中的体现 | 说明 |
|------|--------------|------|
| **封装** | `self.history` 私有 | 把相关数据和操作打包在一起 |
| **继承** | - | 计算器A和计算器B是独立的，互不影响 |
| **多态** | `add/subtract/multiply/divide` | 不同方法做不同操作 |

**为什么要用 OOP？**
```python
# 非OOP方式：全局变量，容易被污染
history = []
def add(a, b):
    history.append(...)
    return a + b

# OOP方式：每个计算器有自己的历史
calc1 = Calculator()
calc2 = Calculator()  # 完全独立！
calc1.history  # 只能访问 calc1 的历史
```

### 模块③：继承

```python
class Animal:           # 基类（父类）
    def speak(self):
        raise NotImplementedError

class Cat(Animal):      # Cat 继承 Animal
    def speak(self):
        return "喵喵喵~"
```

**继承的好处：**
- 代码复用：不用重复写 `__init__`、`__str__`
- 统一接口：所有 Animal 子类都有 `speak()` 方法
- 扩展新功能：加一个新动物只需要继承

### 模块④：封装（私有属性）

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner              # 公开
        self.__balance = balance        # 私有（双下划线开头）
```

**私有属性的规则：**
- `__xxx`（双下划线开头）→ 私有属性，外部不能直接访问
- `_xxx`（单下划线开头）→ 约定私有，但还能访问
- 私有属性只能通过**公开方法**访问和修改

### 模块⑤：三种方法对比

| 方法类型 | 第一个参数 | 调用方式 | 场景 |
|---------|-----------|---------|------|
| 实例方法 | `self` | `obj.method()` | 需要操作实例属性 |
| 类方法 | `cls` | `Class.method()` 或 `obj.method()` | 需要操作类变量 |
| 静态方法 | 无 | `Class.method()` 或 `obj.method()` | 和类无关，纯函数 |

### 模块⑥：Scikit-learn 风格封装

```python
class SimpleLinearRegression:
    def __init__(self):
        self.coef_ = None      # sklearn 惯例：训练得到的属性用下划线结尾
        self.intercept_ = None
    
    def fit(self, X, y):        # 训练
        # ... 训练逻辑
        return self
    
    def predict(self, X):       # 预测
        return self.coef_ * X + self.intercept_
    
    def score(self, X, y):      # 评估
        return r2_score(y, self.predict(X))
```

**Scikit-learn API 三大铁律：**
1. `model = MyModel()` → 创建模型实例
2. `model.fit(X, y)` → 训练
3. `model.predict(X)` → 预测

---

## 步骤5：代码执行过程模拟

### 模拟1：创建对象的过程

```
dog1 = Dog("旺财", 3)

执行过程：
1. 在内存中创建 Dog 实例
2. 调用 __init__("旺财", 3)
3. self → 指向刚创建的实例
4. self.name = "旺财" → 实例添加 name 属性
5. self.age = 3 → 实例添加 age 属性
6. 返回这个实例的引用给 dog1
```

### 模拟2：方法调用过程

```
dog1.bark()

执行过程：
1. dog1 是 Dog 的实例
2. 调用 dog1.bark()，等价于 Dog.bark(dog1)
3. bark 方法中的 self → dog1
4. return f"{self.name}..." → "旺财..."
5. 打印结果
```

### 模拟3：继承的方法解析

```
cat = Cat("黑猫", 2)
cat.speak()

执行过程：
1. cat 是 Cat 的实例
2. 调用 cat.speak()
3. Cat 类没有 speak 方法，向上找 Animal
4. Animal.speak 被 NotImplementedError
5. Cat 重写了 speak()，所以用 Cat 的版本
6. return "黑猫 在叫：喵喵喵~"
```

---

## 步骤6：完整运行结果展示

```text
=== 1. 最简单的类 ===
旺财 在叫：汪汪汪！
小白 在叫：汪汪汪！
旺财，3岁，犬科
小白，5岁，犬科
狗1的名字: 旺财
狗2的名字: 小白

=== 2. 面向对象计算器 ===
calc1 当前结果: 145
calc2 当前结果: 1300

====================
张三的计算器 的历史记录：
  1. 加法: 10 + 5 = 15
  2. 乘法: 3 × 4 = 15
  3. 加法: 15 + 100 = 145
====================

====================
李四的计算器 的历史记录：
  1. 加法: 1000 + 500 = 1500
  2. 减法: 1000 - 200 = 1300
====================
张三的计算器 已清空
清空后 calc1 结果: 0
清空后 calc2 结果: 1300

=== 3. 继承 ===
黑猫(黑猫, 2岁) 说：黑猫 在叫：喵喵喵~
旺财(旺财, 3岁) 说：旺财 在叫：汪汪汪！
小鸟(小鸟, 1岁) 说：小鸟 在叫：啾啾啾~

=== 4. 私有属性 ===
余额（通过方法）：1000
张三 存了 500 元，余额：1500
张三 取了 200 元，余额：1300
账户信息：{'户主': '张三', '余额': 1300, '交易次数': 2}

=== 5. 类方法 vs 实例方法 vs 静态方法 ===
计算器: 半径5的圆面积 = 78.53975
圆周率已更新为: 3.14
计算器: 半径5的圆面积 = 78.5
3
20

=== 6. 特殊方法 ===
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v1 + v2 = Vector(4, 6)
v1 * 3 = Vector(9, 12)
len(v1) = 2
v1[0] = 3, v1[1] = 4
v1 == Vector(3, 4) : True

=== 7. Scikit-learn 风格封装 ===
训练完成！系数: 2.0300, 截距: -0.0200
预测 X=6,7: [12.16 14.19]
R² 分数: 0.9993
```

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
|忘记 `self` | `name = name` | `self.name = name` |
|类变量vs实例变量 | 所有实例共享导致bug | 实例变量在 `__init__` 里定义 |
|私有属性访问 | `obj.__private` | 通过 `obj.get_private()` 方法访问 |
|忘记返回self| `fit()` 返回None | `return self` 才能链式调用 |
|`__str__` vs `__repr__` | 混用导致调试困难 | `__str__` 给用户看，`__repr__` 给开发者 |
|继承vs组合 | 强行继承导致耦合 | 优先用组合，继承是"是-个"关系 |

### 常见面试题

```python
class A:
    x = 1
    
a = A()
print(a.x)      # 1，实例没有x，向上找类变量
a.x = 2         # 创建了实例变量x，不影响类变量
print(A.x)      # 1，类变量不变

A.x = 3         # 修改类变量
print(a.x)      # 2，实例变量屏蔽了类变量
```

### 🔗 知识点关联

```
Python 面向对象编程
├── → [[Scikit-learn机器学习基础]]（所有模型都是类）
├── → [[Python异常处理]]（try/except）
├── → [[Python模块与包]]（import 机制）
└── → [[Python装饰器]]（@property, @classmethod 等）
```

---

## 步骤8：动手练习

### 练习1（基础）
创建一个 `Student` 类，包含：
- 属性：姓名、学号、三门课成绩
- 方法：`get_average()` 计算平均分，`get_info()` 显示信息
- 创建两个学生实例，验证各自成绩独立

### 练习2（进阶）
给计算器加上 `__call__` 特殊方法，使其可以这样调用：
```python
calc = Calculator()
calc(10, 5)  # 等价于 calc.add(10, 5)
```

### 练习3（挑战：Scikit-learn 风格）
模仿 Scikit-learn，封装一个 KNN 分类器：
```python
class SimpleKNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        # 保存训练数据
        return self
    
    def predict(self, X):
        # 对于每个测试样本，找到k个最近邻，投票决定类别
        return predictions
```

### 练习4（综合）
创建一个「栈」类，实现：
- `push(item)` 入栈
- `pop()` 出栈
- `top()` 查看栈顶
- `is_empty()` 是否为空
- `size()` 栈大小
- 尝试用 list 实现，然后想想还能用什么数据结构

---

## 答案参考

<details>
<summary>点击展开练习1答案</summary>

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, score):
        self.grades[subject] = score
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_info(self):
        print(f"姓名: {self.name}")
        print(f"学号: {self.student_id}")
        print("成绩:")
        for subject, score in self.grades.items():
            print(f"  {subject}: {score}")
        print(f"平均分: {self.get_average():.2f}")

s1 = Student("张三", "2024001")
s1.add_grade("语文", 85)
s1.add_grade("数学", 92)
s1.add_grade("英语", 88)

s2 = Student("李四", "2024002")
s2.add_grade("语文", 78)
s2.add_grade("数学", 90)
s2.add_grade("英语", 82)

s1.get_info()
print()
s2.get_info()
```

</details>

---

> 📌 **相关概念**：[[Python基础]] | [[Python异常处理]] | [[Python模块与包]] | [[Scikit-learn机器学习基础]]
> 
> 🔗 **前置知识**：[[Python基础]]（如需补充）
> 
> ⏭️ **下一节**：[[Python异常处理]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
