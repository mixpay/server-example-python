server-example-python
=====================

聚易付服务器端示例-Python版

# 简介
本项目包含两个功能示例：

1. 对HTTP请求参数进行数字签名，使用场景：客户端向服务器请求参数签名(RSA私钥存放在服务端）
2. 接收聚易付的订单通知

# 运行需求
1. python运行环境
2. Flask
3. pyOpenSSL>=0.11

# 准备工作

### 生成RSA密钥

使用OpenSSL生成RSA公钥和私钥文件

```
openssl genrsa -out rsa_private_key.pem 1024
openssl rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem
```

# 安装相关组件
这里以easy_install为例：

```
easy_install flask
easy_install pyOpenSSL==0.11  #不能低于0.11版本
```

#使用

启动Flask Http Server, 默认端口 5000

```
python server.py
```

### GET|POST /sign 

对HTTP请求参数做符合聚易付规则的RSA数字签名

如：获得param1=value1&param2＝value2的RSA数字签名（已经过URLEncode）
已GET方法为例：

```
http://ip:5000/sign?param1=value1&param2＝value2
```

### POST /notify 

接收聚易付的订单通知，并且返回"success"确认码