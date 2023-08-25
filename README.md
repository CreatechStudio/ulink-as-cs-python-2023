# ulink-as-cs-python-2023

## 前言

欢迎来到这个Computer Science的Python作业仓库，本仓库旨在交流与学习。请在下载后的24小时内删除。

## 提交规范

1. 按照作业名称进行文件夹命名，按照提交顺序界定

> 如：`password_strength`是由`lightum_cc`第一次提交的，则所有属于此项目的python文件必须加入此文件夹内

2. 按照作业名称_作者进行提交

> 如：OpenAI ChatGPT 3.5创作的`password_strength`项目的作品需要被重命名为：`password_strength_gpt`

| 作者               | 后缀       |
| ------------------ | ---------- |
| OpenAI ChatGPT 3.5 | gpt        |
| OpenAI ChatGPT 4+  | gpt4       |
| Google Bard        | bard       |
| 通义千问           | ali        |
| 文心一言           | baidu      |
| 人工创作           | 姓名首字母 |

3. 文件名中不允许包含中文
4. 若使用生成式AI创作，必须在文件开头标注Prompt

```python
'''
你能否书写一段程序，来判断一个密码是否符合以下条件：
1. 至少8位
2. 至少一个大写字母，一个小写字母，一个数字，一个特殊字符
3. 不能包含个人信息（个人信息可以事先通过 input 获取）
'''
```

5. 文件内不应该包含敏感内容
5. 提交信息应当有意义

> 如：新增`password_strength_gpt.py`文件，应当使用`add: password_strength_gpt `

| 含义   | 信息         |
| ------ | ------------ |
| add    | 新增文件     |
| rm     | 删除文件     |
| fix    | 修复问题     |
| update | 更新逻辑/新增功能     |
| tuning | 优化逻辑     |
| rb     | 回滚代码     |
| rename | 重命名文件   |
| sugg   | PR中修改意见 |

7. 文件名内不允许使用中划线，只允许使用下划线
8. 若需要import一个本地文件，需要新建文件夹并将所需文件放入文件夹内，并将文件夹名称改为`项目名_作者`
9. 路径应使用`Linux/macOS`格式并采用相对路径
10. 不可在一次commit内包含多个内容
11. 使用必要的注释
