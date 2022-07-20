# listary_flomo_script

因为没研究明白listary的插件怎么写，于是乎曲线救国决定，用python完成脚本并打包成exe文件，用listary运行exe文件实现功能。

Because I cannot figure out how to write listary plugin, I decided to use python to write the script and package it as an exe file, and use listary to run the exe file to implement the function.

# 使用方法 Usage

## 脚本 Script

```
git clone https://github.com/zhanggzzy/listary_flomo_script.git
cd listary_flomo_script
python main.py
```

首次使用会提示输入 flomo API 的 url（需要flomo pro）
```
Enter your Flomo API URL:
```

之后会在同目录生成一个txt记录该url，之后使用无需再次输入。

此时可以使用命令行测试脚本
```
python main.py <input text>
```

如果成功，会输出结果
```
Successfully Post to Flomo
```

如果失败，会输出错误信息
```
Failed to Post to Flomo
```

## Listary

使用pyinstaller生成exe文件，或从Release目录下载。

```
pyinstaller -F main.py
```

然后在 listary 设置中配置。在 选项-特性-命令 新增一个命令：

- 关键字：flomo
- 标题：发布flomo MEMO
- 路径：<脚本exe文件所在路径>
- 参数："{query}"

然后勾选静默执行

便可以在 listary 中使用该命令。