---
date: 2026-04-20
tags: [AI, 已学, Python基础, 文件操作, 模块]
---

# Python 文件操作与模块

> 按照 AImaster 教学法：场景驱动 → 代码优先 → 循序渐进

---

## 步骤1：场景引入（提出问题）

**你有没有遇到这种情况？**

- 📁 训练好的模型想保存下来，下次直接用，不想重新训练？
- 📊 处理的数据在不同文件里，每次都要手动复制粘贴？
- 📦 写了一个很酷的函数，下次想在新程序里用，要 copy-paste 一大堆代码？
- 📦 别人写了个工具库，你怎么安装和使用？

**Python 的文件操作 + 模块系统就是来解决这些问题的！**

---

## 步骤2：前置知识确认

学习文件操作与模块需要了解：

- ✅ Python 基础语法
- ✅ [[Python面向对象编程]]（文件也是对象）
- ✅ [[Python异常处理]]（文件操作要处理找不到文件等情况）

---

## 步骤3：完整代码展示

```python
# ============================================
# Python 文件操作与模块 — 完整可运行代码
# ============================================

import os
import json
import csv
import pickle
import shutil
from pathlib import Path

# ============================================
# 第一部分：文件基础操作
# ============================================

print("=" * 50)
print("第一部分：文件基础操作")
print("=" * 50)

# ① 创建测试目录和文件
test_dir = Path("test_files")  # Path 对象（推荐方式）
test_dir.mkdir(exist_ok=True)   # 创建目录

# 用 Path 写文件
(test_dir / "hello.txt").write_text("Hello, Python!\n第二行内容")
print("✅ 创建文件: test_files/hello.txt")

# ② 读取文件内容
print("\n=== 2. 读取文件 ===")

# 方式1：Path.read_text()（最简单）
content = (test_dir / "hello.txt").read_text()
print(f"read_text() 读取:\n{content}")

# 方式2：with open（推荐，自动关闭）
with open(test_dir / "hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"readlines() 读取: {lines}")

# 方式3：按行读取（省内存）
print("\n按行读取:")
with open(test_dir / "hello.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"  第{i}行: {line.rstrip()}")

# ③ 写入文件
print("\n=== 3. 写入文件 ===")

# 方式1：Path.write_text()（覆盖写入）
(test_dir / "output.txt").write_text("新内容\n覆盖了原内容")
print("✅ 覆盖写入完成")

# 方式2：with open + write（追加模式）
with open(test_dir / "output.txt", "a", encoding="utf-8") as f:
    f.write("\n这是追加的内容")
    f.write("\n再追加一行")
print("✅ 追加写入完成")

print("最终文件内容:")
print((test_dir / "output.txt").read_text())

# ④ JSON 文件（最常用的数据格式）
print("\n=== 4. JSON 文件 ===")

data = {
    "name": "张三",
    "age": 28,
    "skills": ["Python", "机器学习", "深度学习"],
    "projects": [
        {"name": "房价预测", "accuracy": 0.92},
        {"name": "图像分类", "accuracy": 0.88}
    ]
}

# 写入JSON
json_path = test_dir / "user.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # ensure_ascii=False保留中文
print("✅ JSON写入完成")

# 读取JSON
with open(json_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print(f"读取JSON: {loaded_data}")
print(f"姓名: {loaded_data['name']}")
print(f"第一个项目: {loaded_data['projects'][0]}")

# ⑤ CSV 文件（表格数据）
print("\n=== 5. CSV 文件 ===")

students = [
    ["姓名", "语文", "数学", "英语"],
    ["张三", "85", "92", "88"],
    ["李四", "78", "90", "85"],
    ["王五", "92", "88", "95"],
]

csv_path = test_dir / "students.csv"
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig 让Excel能正确识别中文
    writer = csv.writer(f)
    writer.writerows(students)
print("✅ CSV写入完成")

# 读取CSV
print("\n读取CSV内容:")
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# 读取为字典列表（更方便）
print("\n读取为字典列表:")
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['姓名']}: 语文={row['语文']}, 数学={row['数学']}")

# ⑥ pickle（Python对象序列化）
print("\n=== 6. pickle（保存Python对象）===")

class Model:
    """模拟机器学习模型"""
    def __init__(self, coef, intercept):
        self.coef = coef
        self.intercept = intercept
    
    def predict(self, x):
        return self.coef * x + self.intercept
    
    def __repr__(self):
        return f"Model(coef={self.coef}, intercept={self.intercept})"

# 创建并保存模型
model = Model(coef=2.5, intercept=10)
model_path = test_dir / "model.pkl"
with open(model_path, "wb") as f:  # 注意是 "wb"
    pickle.dump(model, f)
print(f"✅ 模型保存: {model}")

# 加载模型
with open(model_path, "rb") as f:  # 注意是 "rb"
    loaded_model = pickle.load(f)
print(f"✅ 模型加载: {loaded_model}")
print(f"   预测 x=5: {loaded_model.predict(5)}")

# ============================================
# 第二部分：文件和目录操作
# ============================================

print("\n" + "=" * 50)
print("第二部分：文件和目录操作")
print("=" * 50)

# ⑦ os.path 和 Path 路径操作
print("\n=== 7. 路径操作 ===")

base = Path("test_files")
print(f"当前目录: {Path.cwd()}")
print(f"test_files 是否存在: {base.exists()}")
print(f"test_files 是目录吗: {base.is_dir()}")
print(f"test_files 是文件吗: {base.is_file()}")
print(f"test_files 的父目录: {base.parent}")
print(f"test_files 的名称: {base.name}")
print(f"test_files 的后缀: {base.suffix}")

# 路径拼接
file_path = base / "subdir" / "file.txt"
print(f"\n拼接路径: {file_path}")

# ⑧ 遍历目录
print("\n=== 8. 遍历目录 ===")

print(f"\ntest_files 目录内容:")
for item in test_dir.iterdir():
    if item.is_file():
        size = item.stat().st_size
        print(f"  📄 {item.name} ({size} bytes)")
    else:
        print(f"  📁 {item.name}/")

# 递归遍历（所有子目录）
print(f"\n递归遍历（包含子目录）:")
for item in test_dir.rglob("*"):  # rglob 递归
    print(f"  {item}")

# ⑨ 复制、移动、删除
print("\n=== 9. 复制、移动、删除 ===")

# 复制文件
shutil.copy(test_dir / "hello.txt", test_dir / "hello_copy.txt")
print("✅ 复制文件完成")

# 移动/重命名
shutil.move(test_dir / "hello_copy.txt", test_dir / "hello_moved.txt")
print("✅ 移动/重命名完成")

# 删除文件
(test_dir / "hello_moved.txt").unlink()
print("✅ 删除文件完成")

# 创建子目录
subdir = test_dir / "subdir"
subdir.mkdir(exist_ok=True)
(subdir / "nested.txt").write_text("嵌套文件")
print("✅ 创建子目录和嵌套文件")

# 删除整个目录树
shutil.rmtree(test_dir)
print("✅ 删除整个目录树")

# ============================================
# 第三部分：模块和包
# ============================================

print("\n" + "=" * 50)
print("第三部分：模块和包")
print("=" * 50)

# ⑩ 模块基础
print("\n=== 10. 模块基础 ===")

import math
from collections import Counter, defaultdict

# 使用模块
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.floor(3.7) = {math.floor(3.7)}")
print(f"math.ceil(3.2) = {math.ceil(3.2)}")

# 使用 from import
cnt = Counter(["a", "b", "a", "c", "a", "b"])
print(f"\nCounter(['a','b','a','c','a','b']) = {cnt}")
print(f"最常见: {cnt.most_common(2)}")

# defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
print(f"\ndefaultdict: {dd}")

# ⑪ 标准库速查
print("\n=== 11. 常用标准库 ===")

standard_libs = {
    "os": "操作系统接口（文件、路径、进程）",
    "sys": "系统相关（Python解释器）",
    "math": "数学运算",
    "random": "随机数",
    "datetime": "日期时间",
    "time": "时间相关",
    "json": "JSON序列化",
    "csv": "CSV文件处理",
    "pickle": "Python对象序列化",
    "pathlib": "路径操作（推荐）",
    "collections": "容器数据类型",
    "itertools": "迭代工具",
    "functools": "函数式编程工具",
    "re": "正则表达式",
    "urllib": "网络请求",
    "argparse": "命令行参数",
}

for lib, desc in standard_libs.items():
    print(f"  {lib:15s} - {desc}")

# ⑫ 第三方库安装和使用
print("\n=== 12. pip 使用 ===")

# 安装第三方库（命令行执行，不是Python代码）
# pip install numpy pandas scikit-learn

# 使用第三方库
try:
    import numpy as np
    import pandas as pd
    print("✅ NumPy 版本:", np.__version__)
    print("✅ Pandas 版本:", pd.__version__)
except ImportError as e:
    print(f"❌ 导入失败: {e}")

# ⑬ 创建自己的模块
print("\n=== 13. 创建自己的模块 ===")

print("""
创建一个模块只需要：
1. 创建一个 .py 文件
2. 在里面写函数或类
3. 其他文件 import 进来就能用

示例 - mymodule.py:
---
def add(a, b):
    return a + b

class Calculator:
    ...
---

使用:
---
import mymodule
mymodule.add(1, 2)  # 3
from mymodule import add
add(1, 2)  # 3
---
""")

# ⑭ __name__ == "__main__"
print("\n=== 14. __name__ == '__main__' ===")

print("""
当一个 .py 文件被直接运行时，
__name__ 的值是 '__main__'

当被 import 时，__name__ 是模块名

用法：
---
def main():
    print("主要逻辑")

if __name__ == '__main__':
    main()  # 直接运行时执行
else:
    # 被导入时执行的代码（初始化等）
    pass
---

这样模块可以：
1. 直接运行（做测试）
2. 被其他模块导入使用
""")

# ⑮ 包（Package）
print("\n=== 15. 包结构 ===")

print("""
包是一个目录，里面有 __init__.py

mypackage/
    __init__.py       # 包初始化
    module1.py        # 模块1
    module2.py        # 模块2
    subpackage/
        __init__.py
        module3.py

使用：
---
import mypackage.module1
from mypackage import module2
from mypackage.subpackage import module3
from mypackage.subpackage.module3 import some_function
---

__init__.py 可以为空，也可以写：
---
from .module1 import some_class
# 这样 from mypackage import some_class 也能用
---
""")

# ============================================
# 第四部分：实战练习
# ============================================

print("\n" + "=" * 50)
print("第四部分：实战练习")
print("=" * 50)

# ⑯ 实战：数据备份脚本
print("\n=== 16. 实战：数据备份脚本 ===")

def backup_data(source_dir, backup_dir):
    """备份数据目录"""
    import datetime
    
    source = Path(source_dir)
    backup = Path(backup_dir)
    
    if not source.exists():
        print(f"❌ 源目录不存在: {source}")
        return False
    
    # 创建带时间戳的备份目录
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_subdir = backup / f"backup_{timestamp}"
    backup_subdir.mkdir(parents=True, exist_ok=True)
    
    # 复制文件
    count = 0
    for file in source.rglob("*"):
        if file.is_file():
            relative = file.relative_to(source)
            dest = backup_subdir / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, dest)  # copy2 保留元数据
            count += 1
    
    print(f"✅ 备份完成！共 {count} 个文件")
    print(f"📁 备份位置: {backup_subdir}")
    return True

print("""
backup_data() 使用示例：
---
backup_data("data/", "backups/")
# 备份 data/ 目录到 backups/backup_20260420_123045/
---
""")

# ⑰ 实战：配置管理器
print("\n=== 17. 实战：配置管理器 ===")

class ConfigManager:
    """配置文件管理器"""
    
    def __init__(self, config_file):
        self.config_file = Path(config_file)
        self.config = {}
        if self.config_file.exists():
            self.load()
    
    def load(self):
        """加载配置"""
        with open(self.config_file, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        print(f"✅ 配置加载: {self.config}")
    
    def save(self):
        """保存配置"""
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
        print(f"✅ 配置保存")
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """设置配置值"""
        self.config[key] = value
    
    def __str__(self):
        return f"ConfigManager({self.config_file}, {len(self.config)} 项配置)"


print("""
config = ConfigManager("config.json")
config.set("model_name", "LinearRegression")
config.set("learning_rate", 0.01)
config.set("epochs", 100)
config.save()
print(config.get("model_name"))
""")
```

---

## 步骤4：逐行/逐模块代码详解

### 模块①：Path 对象 vs 传统 os.path

| 操作 | Path 方式 | os.path 方式 |
|------|----------|-------------|
| 创建路径 | `Path("a/b/c")` | `os.path.join("a", "b", "c")` |
| 判断存在 | `Path("x").exists()` | `os.path.exists("x")` |
| 是否文件 | `Path("x").is_file()` | `os.path.isfile("x")` |
| 是否目录 | `Path("x").is_dir()` | `os.path.isdir("x")` |
| 读取内容 | `Path("f").read_text()` | `open("f").read()` |
| 写入内容 | `Path("f").write_text("x")` | `open("f","w").write("x")` |
| 获取父目录 | `Path("f").parent` | `os.path.dirname("f")` |
| 获取名称 | `Path("f").name` | `os.path.basename("f")` |

**结论：Path 更直观，**推荐使用 Path！**

### 模块②：文件打开模式

| 模式 | 说明 | 注意事项 |
|------|------|---------|
| `"r"` | 读（默认） | 文件不存在会报错 |
| `"w"` | 覆盖写 | 文件存在会清空 |
| `"a"` | 追加写 | 在末尾添加 |
| `"x"` | 新建写 | 文件存在会报错 |
| `"rb"` / `"wb"` | 二进制模式 | 用于 pickle、图片等 |

### 模块③：JSON 操作

```python
# 写 JSON
json.dump(data, f, ensure_ascii=False, indent=2)
#            ↑ 数据对象       ↑ 保留中文  ↑ 格式化缩进

# 读 JSON
data = json.load(f)

# 字符串和 JSON 互转
json_str = json.dumps(data)          # dict → str
data = json.loads(json_str)          # str → dict
```

### 模块④：CSV 操作两种方式

```python
# 方式1：逐行处理
with open("file.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 方式2：DictReader（推荐，更方便）
with open("file.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"], row["成绩"])
```

### 模块⑤：pickle 使用场景

```python
# 适合：Python对象、模型、复杂数据结构
# 不适合：跨语言共享、需要可读（用JSON）
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
```

### 模块⑥：import 机制

```python
import module              # 导入整个模块
import module as m         # 导入并起别名
from module import func    # 导入模块中的特定函数/类
from module import *       # 导入所有（不推荐）

# 相对导入（包内部）
from . import module1              # 同级
from ..package import module2      # 上级
```

### 模块⑦：常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| `FileNotFoundError` | 文件不存在 | 用 `Path.exists()` 检查 |
| `PermissionError` | 没权限 | 检查文件权限 |
| `UnicodeDecodeError` | 编码问题 | 指定 `encoding="utf-8"` |
| `IsADirectoryError` | 把目录当文件 | 用 `.is_file()` 检查 |

---

## 步骤5：代码执行过程模拟

### 模拟1：with open 执行流程

```python
with open("file.txt", "r") as f:
    content = f.read()

执行过程：
1. 调用 open("file.txt", "r")，返回文件对象 f
2. 进入 with 块，f 可用
3. 执行 f.read()
4. 离开 with 块，自动调用 f.close()
5. 即使读取出错，也会正确关闭文件
```

### 模拟2：pickle 序列化过程

```python
# 保存
model = Model(2.5, 10)
pickle.dump(model, f)
# 等价于：
# 1. model.__dict__ 取出所有属性
# 2. 序列化成字节流
# 3. 写入文件

# 加载
loaded_model = pickle.load(f)
# 等价于：
# 1. 从文件读取字节流
# 2. 反序列化成对象
# 3. 调用 Model.__setstate__(state)
```

---

## 步骤6：完整运行结果展示

```text
==================================================
第一部分：文件基础操作
==================================================

=== 2. 读取文件 ===
read_text() 读取:
Hello, Python!
第二行内容

按行读取:
  第1行: Hello, Python!
  第2行: 第二行内容

=== 3. 写入文件 ===
最终文件内容:
新内容
覆盖了原内容
这是追加的内容
再追加一行

=== 4. JSON 文件 ===
✅ JSON写入完成
读取JSON: {'name': '张三', 'age': 28, 'skills': ['Python', '机器学习', '深度学习'], ...}
姓名: 张三
第一个项目: {'name': '房价预测', 'accuracy': 0.92}

=== 5. CSV 文件 ===
读取CSV内容:
  ['姓名', '语文', '数学', '英语']
  ['张三', '85', '92', '88']
  ...
读取为字典列表:
  张三: 语文=85, 数学=92

=== 6. pickle ===
✅ 模型保存: Model(coef=2.5, intercept=10)
✅ 模型加载: Model(coef=2.5, intercept=10)
   预测 x=5: 22.5

==================================================
第二部分：文件和目录操作
==================================================

test_files 目录内容:
  📄 hello.txt
  📄 output.txt
  📄 user.json
  📄 students.csv
  📄 model.pkl
  📁 subdir/

✅ 删除整个目录树
```

---

## 步骤7：避坑提示与知识点关联

### ⚠️ 避坑提示

| 坑 | 错误 | 正确 |
|---|------|------|
| 路径有中文 | `open("中文.txt")` | `open("中文.txt", encoding="utf-8")` |
| Windows 路径 | `"D:\data\file"` | `r"D:\data\file"` 或 Path |
| 忘记 close | `f = open()` 后忘记关 | 用 `with open()` |
| 二进制模式 | `open("img.png", "r")` | `open("img.png", "rb")` |
| pickle 安全 | `pickle.load(untrusted)` | 不要 load 不信任的数据 |

### 🔗 知识点关联

```
Python 文件操作与模块
├── → [[Python面向对象编程]]（文件也是对象）
├── → [[Python异常处理]]（文件操作要处理异常）
├── → [[Scikit-learn机器学习]]（模型保存/加载用 pickle）
├── → [[Pandas数据处理基础]]（CSV/JSON 读取）
└── → [[线性回归基础]]（模型保存是实践环节）
```

---

## 步骤8：动手练习

### 练习1（基础）
写一个程序，读取一个 CSV 文件，输出：
- 总行数
- 每列的名称
- 每列的数据类型（数值/文本）

### 练习2（进阶）
写一个配置管理器类，支持：
- 从 JSON 文件加载
- 保存到 JSON 文件
- 增删改查配置项
- 自动保存（修改后自动写回）

### 练习3（挑战）
写一个日志记录器类：
```python
class Logger:
    def __init__(self, filename):
        # 初始化日志文件
        pass
    
    def log(self, level, message):
        # 记录带时间戳的日志
        # level: INFO/WARNING/ERROR
        pass
    
    def info(self, msg): ...
    def warning(self, msg): ...
    def error(self, msg): ...
```

### 练习4（综合）
实现一个简单的任务管理器：
- 保存任务到 JSON 文件
- 添加/完成/删除任务
- 每次修改自动保存

---

## 答案参考

<details>
<summary>点击展开练习2答案</summary>

```python
import json
from pathlib import Path

class Config:
    def __init__(self, path):
        self.path = Path(path)
        self.data = {}
        if self.path.exists():
            self.load()
    
    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
    
    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def get(self, key, default=None):
        return self.data.get(key, default)
    
    def set(self, key, value):
        self.data[key] = value
        self.save()  # 自动保存
    
    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()
    
    def __repr__(self):
        return f"Config({self.path}, {len(self.data)} items)"

# 使用
config = Config("settings.json")
config.set("theme", "dark")
config.set("language", "zh-CN")
print(config.get("theme"))
config.delete("language")
```

</details>

---

> 📌 **相关概念**：[[Python基础]] | [[Python面向对象编程]] | [[Python异常处理]] | [[Pandas数据处理基础]]
> 
> 🔗 **前置知识**：[[Python异常处理]]
> 
> ⏭️ **下一节**：[[数学基础：线性代数]]

---

*本笔记按照 AImaster 教学法编写，版权所有，转载需注明出处*
