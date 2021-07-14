# py-common

## 初始化

```shell
pip install virtualenv
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
```

## 意外处理

> Windows执行 `venv\scripts\activate` 提示错误：无法加载文件 xxx.ps1，因为在此系统-中禁止执行脚本。  

```
以管理员身份打开PowerShell, 输入Set-ExecutionPolicy RemoteSigned，执行策略更改。
```
### 生成项目依赖到 requirements.txt
```shell
pip freeze > requirements.txt
```
