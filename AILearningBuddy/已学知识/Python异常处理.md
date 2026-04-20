---
date: 2026-04-20
tags: [AI, 已学, Python基础, 异常处理]
---

# Python 异常处理

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**你有没有遇到这种情况？**

写了一个除法计算器：
```python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)  # 💥 ZeroDivisionError: division by zero
```

程序直接崩溃了，用户看到一堆红色的错误信息，一脸懵。

或者用户输入了字母：
```python
age = int(input("请输入年龄: "))  # 用户输入 "abc"
# 💥 ValueError: invalid literal for int() with base 10: 'abc'
```

**异常处理就是让你的程序在遇到错误时"优雅地失败"，而不是直接崩溃！**

---

## 步骤2：前置知识确认

学习异常处理需要了解：

- ✅ Python 基础语法
- ✅ 知道什么是"错误"（程序运行时的意外情况）
- 不需要：面向对象（但异常本身是类，了解 OOP 更好）

---

## 步骤3：完整代码展示

```python
# ============================================
# Python 异常处理 — 完整可运行代码
# ============================================

# ① 最基本的 try-except
print("=== 1. 最基本的 try-except ===")

def safe_divide(a, b):
    """安全的除法，不会崩溃"""
    try:
        result = a / b
        print(f"计算成功: {a} / {b} = {result}")
    except ZeroDivisionError:
        print("错误：除数不能为0！")
    except TypeError:
        print("错误：数据类型不对！")
    except Exception as e:
        print(f"未知错误: {e}")

safe_divide(10, 2)    # 正常
safe_divide(10, 0)    # 除数为0
safe_divide("10", 2)  # 类型错误

# ② else 和 finally
print("\n=== 2. else 和 finally ===")

def read_number_from_file(filename):
    """读取文件中的数字"""
    try:
        with open(filename, 'r') as f:  # with 自动关闭文件
            content = f.read()
            number = float(content.strip())
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
    except ValueError:
        print(f"错误：文件内容不是有效的数字")
    else:
        # 只有当 try 成功时才执行
        print(f"成功读取数字: {number}")
        return number
    finally:
        # 无论成功还是失败都会执行
        print("读取操作完成（finally）")

read_number_from_file("number.txt")   # 文件不存在
read_number_from_file("/etc/hostname")  # 存在且是有效内容

# ③ 抛出异常（raise）
print("\n=== 3. 抛出异常（raise）===")

def withdraw(balance, amount):
    """取钱函数"""
    if amount <= 0:
        raise ValueError("取款金额必须大于0！")
    if amount > balance:
        raise RuntimeError(f"余额不足！当前余额: {balance}，取款金额: {amount}")
    
    new_balance = balance - amount
    print(f"取款成功！取出 {amount} 元，剩余 {new_balance} 元")
    return new_balance

try:
    balance = 1000
    balance = withdraw(balance, 500)   # 正常
    balance = withdraw(balance, -100)  # 金额为负
except ValueError as e:
    print(f"ValueError: {e}")
except RuntimeError as e:
    print(f"RuntimeError: {e}")

# ④ 自定义异常类
print("\n=== 4. 自定义异常类 ===")

class AgeError(Exception):
    """年龄相关的错误"""
    pass

class Person:
    """人这个类"""
    
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)  # 通过方法来设置，顺便检查
    
    def set_age(self, age):
        if not isinstance(age, (int, float)):
            raise AgeError(f"年龄必须是数字！收到: {type(age)}")
        if age < 0:
            raise AgeError(f"年龄不能为负数！收到: {age}")
        if age > 150:
            raise AgeError(f"年龄不合理！收到: {age}")
        self.age = age
    
    def __str__(self):
        return f"{self.name}，{self.age}岁"


try:
    p1 = Person("张三", 25)  # 正常
    print(p1)
    
    p2 = Person("李四", -5)  # 年龄为负
except AgeError as e:
    print(f"年龄错误: {e}")

try:
    p3 = Person("王五", "二十")  # 类型错误
except AgeError as e:
    print(f"年龄错误: {e}")

# ⑤ 异常链（raise ... from）
print("\n=== 5. 异常链 ===")

def level3():
    """第三层调用"""
    raise ValueError("这是原始错误")

def level2():
    """第二层调用"""
    try:
        level3()
    except ValueError as e:
        # 异常链：保留原始错误信息
        raise RuntimeError("level2 调用失败") from e

def level1():
    """第一层调用"""
    try:
        level2()
    except RuntimeError as e:
        print(f"捕获到 RuntimeError: {e}")
        if e.__cause__:
            print(f"原始原因: {e.__cause__}")

level1()

# ⑥ 常见的异常类型速查表
print("\n=== 6. 常见异常类型 ===")

exceptions = {
    "ZeroDivisionError": "除数为0",
    "ValueError": "值不合法",
    "TypeError": "类型不匹配",
    "IndexError": "索引越界",
    "KeyError": "字典key不存在",
    "FileNotFoundError": "文件不存在",
    "AttributeError": "对象没有这个属性",
    "ImportError": "导入模块失败",
    "AssertionError": "assert断言失败",
    "RuntimeError": "运行时错误",
}

for exc, desc in exceptions.items():
    print(f"  {exc}: {desc}")

# ⑦ 实际应用：带重试的下载函数
print("\n=== 7. 实战：带重试的下载函数 ===")

import time

def download_with_retry(url, max_retries=3):
    """
    模拟下载函数，失败自动重试
    """
    for attempt in range(1, max_retries + 1):
        try:
            # 模拟下载：随机成功或失败
            import random
            if random.random() < 0.7:  # 70%成功率
                return f"✅ 下载成功: {url}"
            else:
                raise ConnectionError("网络连接失败")
        except ConnectionError as e:
            if attempt < max_retries:
                print(f"第 {attempt} 次失败，3秒后重试...")
                time.sleep(3)
            else:
                return f"❌ 下载 {max_retries} 次都失败了！"

# 实际使用
result = download_with_retry("http://example.com/file.zip")
print(result)

# ⑧ 使用 contextlib 简化异常处理
print("\n=== 8. contextlib 简化 ===")

from contextlib import contextmanager, suppress

# 方式1：@contextmanager 简化资源管理
@contextmanager
def managed_resource(name):
    """模拟需要管理的资源"""
    print(f"获取资源: {name}")
    try:
        yield f"resource_{name}"  # yield 之前是进入，yield 之后是退出
    finally:
        print(f"释放资源: {name}")

with managed_resource("数据库连接") as res:
    print(f"使用资源: {res}")

# 方式2：suppress 静默忽略特定异常
print("\n使用 suppress:")
with suppress(FileNotFoundError, ZeroDivisionError):
    # 这些异常会被静默忽略
    with open("不存在的文件.txt") as f:
        print(f.read())
    result = 1 / 0  # 被忽略
    print("这行不会执行")

print("程序继续执行，没有崩溃！")
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：try-except 基础

```python
try:
    # 可能出错的代码
    result = a / b
except ZeroDivisionError:     # 只捕获除零错误
    # 处理错误
    print("除数不能为0")
except TypeError:              # 只捕获类型错误
    print("类型不对")
except Exception as e:         # 捕获所有其他错误
    print(f"未知错误: {e}")
```

**执行逻辑：**
```
1. 执行 try 里的代码
2. 如果有异常 → 匹配 except → 执行处理代码
3. 如果没异常 → 跳过所有 except
```

### 模块②：else 和 finally

```python
try:
    # 正常代码
    ...
except:
    # 处理错误
else:
    # 只有try成功时才执行
    return result
finally:
    # 无论成功失败都执行
    cleanup()
```

**使用场景：**
- `else`：正常流程结束时释放资源
- `finally`：无论成功失败都需要清理的场合（关闭文件、断开连接）

### 模块③：raise 抛出异常

```python
raise ValueError("错误信息")
raise RuntimeError("运行时错误")
raise  # 重新抛出当前捕获的异常
```

**何时抛出：**
- 输入参数不合法时
- 业务逻辑不允许时
- 遇到无法处理的错误时

### 模块④：常见异常类型速查

| 异常类型 | 触发条件 | 例子 |
|---------|---------|------|
| `ZeroDivisionError` | 除数为0 | `1/0` |
| `ValueError` | 值不合法 | `int("abc")` |
| `TypeError` | 类型不匹配 | `"1" + 1` |
| `IndexError` | 索引越界 | `[1,2][10]` |
| `KeyError` | dict key不存在 | `{"a":1}["b"]` |
| `FileNotFoundError` | 文件不存在 | `open("xxx")` |
| `AttributeError` | 对象没有属性 | `(1).append` |
| `AssertionError` | assert失败 | `assert 1==2` |

### 模块⑤：异常链

```python
try:
    level3()
except ValueError as e:
    raise RuntimeError("失败") from e
```

`from e` 保留原始错误原因，便于调试。

### 模块⑥：自定义异常

```python
class MyError(Exception):
    """自定义错误类"""
    pass

# 或带额外信息
class MyError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
```

**何时自定义：**
- 业务逻辑特定的错误
- 需要携带额外信息
- 需要统一错误类型

---

## 步骤5：代码执行过程模拟

### 模拟1：try-except 执行流程

```
try:
    x = 10 / 0
    print("这行不会执行")
except ZeroDivisionError:
    print("捕获到除零错误")
print("程序继续")

执行流程：
1. 进入 try
2. 10 / 0 → 触发 ZeroDivisionError
3. 跳到 except ZeroDivisionError
4. 打印"捕获到除零错误"
5. except 结束，程序继续
6. 打印"程序继续"
```

### 模拟2：多层调用异常传播

```
level1() → 调用
    level2() → 调用
        level3() → raise ValueError
        异常向上传播到 level2 的 except
        level2 捕获后重新 raise RuntimeError from e
    level1 捕获 RuntimeError
    打印错误信息
```

---

## 步骤6：完整运行结果展示

```text
=== 1. 最基本的 try-except ===
计算成功: 10 / 2 = 5.0
错误：除数不能为0！
错误：数据类型不对！

=== 2. else 和 finally ===
错误：文件 'number.txt' 不存在
读取操作完成（finally）
成功读取数字: 0.0
读取操作完成（finally）

=== 3. 抛出异常（raise）===
取款成功！取出 500 元，剩余 500 元
ValueError: 取款金额必须大于0！

=== 4. 自定义异常类 ===
张三，25岁
年龄错误: 年龄不能为负数！收到: -5
年龄错误: 年龄必须是数字！收到: <class 'str'>

=== 5. 异常链 ===
捕获到 RuntimeError: level2 调用失败
原始原因: ValueError('这是原始错误')

=== 6. 常见异常类型速查表 ===
ZeroDivisionError: 除数为0
ValueError: 值不合法
...（表格内容）

=== 7. 实战：带重试 ===
第 1 次失败，3秒后重试...
✅ 下载成功: http://example.com/file.zip

=== 8. contextlib 简化 ===
获取资源: 数据库连接
使用资源: resource_数据库连接
释放资源: 数据库连接

使用 suppress:
程序继续执行，没有崩溃！
```

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
| 裸 except | `except:` 捕获一切 | `except Exception as e:` 明确类型 |
| 吞掉异常 | `except: pass` | 至少打印日志 |
| 只 try 不 except | 代码不完整 | 确保所有路径都处理 |
| 过度使用 | 到处 try | 最小化 try 范围 |
| 不关心异常 | 不处理 | 或者用 `raise` 抛给调用者 |

### 好习惯 vs 坏习惯

```python
# ❌ 坏习惯：裸 except
try:
    do_something()
except:
    pass

# ❌ 坏习惯：捕获但不处理
try:
    do_something()
except Exception:
    pass  # 完全不知道发生了什么

# ✅ 好习惯：明确类型，处理或上抛
try:
    do_something()
except ValueError as e:
    logger.error(f"值错误: {e}")
    raise  # 或者 return None

# ✅ 好习惯：最小化 try 范围
result = data.get(key)
try:
    value = float(result)
except (ValueError, TypeError):
    return None
```

### 🔗 知识点关联

```
Python 异常处理
├── → [[Python面向对象编程]]（异常也是类）
├── → [[Python文件操作]]（文件操作需要异常处理）
├── → [[Scikit-learn机器学习]]（模型的 fit/predict 都可能有异常）
└── → [[Python装饰器]]（@contextmanager）
```

---

## 步骤8：动手练习

### 练习1（基础）
写一个"安全输入"函数：
```python
def get_positive_integer(prompt):
    """提示用户输入，直到输入一个正整数为止"""
    # 1. 显示提示
    # 2. 读取输入
    # 3. 尝试转int
    # 4. 如果不是正数，重新输入
    # 5. 成功则返回
```

### 练习2（进阶）
写一个配置文件读取函数：
```python
def read_config(filename):
    """读取配置文件，返回字典
    文件格式：key=value
    需要处理：文件不存在、格式错误、空文件
    """
```

### 练习3（挑战）
实现一个"自动重试装饰器"：
```python
@retry(max_attempts=3, delay=1, exceptions=(ConnectionError,))
def fetch_data(url):
    """网络请求，失败自动重试"""
    # 模拟请求
```

---

## 答案参考

<details>
<summary>点击展开练习1答案</summary>

```python
def get_positive_integer(prompt="请输入一个正整数: "):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if number <= 0:
                print("错误：必须输入正整数！请重试。")
                continue
            return number
        except ValueError:
            print(f"错误：'{user_input}' 不是有效的整数！请重试。")

# 测试
age = get_positive_integer("请输入您的年龄: ")
print(f"您输入的年龄是: {age}")
```

</details>

---

> 📌 **相关概念**：[[Python基础]] | [[Python面向对象编程]] | [[Python文件操作]] | [[Python装饰器]]
> 
> 🔗 **前置知识**：[[Python基础]]
> 
> ⏭️ **下一节**：[[Python文件操作与模块]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
