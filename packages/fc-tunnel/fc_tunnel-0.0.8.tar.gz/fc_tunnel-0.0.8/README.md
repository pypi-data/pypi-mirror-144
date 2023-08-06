## 简介

一个快速打通本地开发环境和阿里云云上 vpc 具体实例 tcp 网络的简洁工具

## 快速开始

### 前提条件

 - 本地已经有 python3.x
 
 - 本地已经安装了[docker](https://docs.docker.com/get-docker/)
 
 - 开通[函数计算](https://fc.console.aliyun.com/)，并登录函数计算控制台， 第一次登录会引导您完成 FCDefaultRole 授权创建

### 安装

```bash
$ pip install fc-tunnel
```

### 编写配置文件 config.json, 例如:

```json
{
  "akId": "your aliyun ak id",
  "akSecret": "your aliyun ak secret",
  "accountId": "your aliyun main account id",
  "region": "cn-beijing",
  "vpcId": "vpc-2zes9muk32e82wwt7kfef",
  "vSwitchIds": "vsw-2zek7r3kcvmu3div13bh4",
  "securityGroupId": "sg-2zed3dvbh98kzoi3cch5",
  "remoteIP": "10.20.108.195",
  "remotePorts": "8080,9000"
}
```


其中：

- 如果 ak 不是对应主账号或者具有 admin 权限的子账号， 请先给 ak 对应的子账号添加 FCFullAccess 和 自定义 RAM Policy:

```json
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "tns:*",
            "Resource": "*"
        }
    ],
    "Version": "1"
}
```

- remoteIP 表示云上阿里云 vpc 的内网地址， 具体可以是 SAE 应用的实例内部 IP， ECI 实例的内部 IP， ECS 内网 IP 等

- remotePorts 对应 remoteIP 实例映射到本地的端口


如上面的 config.json 所示， 如果您有一个 vpc 内置地址为 10.20.108.195 的 SAE 实例， 这个 SAE 实例上跑的是一个 java SpringBoot 的应用， 8080 是 web 服务端口， 9000 是远程调试的端口

![](https://img.alicdn.com/imgextra/i3/O1CN01hShP951UrZ1bdnAhO_!!6000000002571-2-tps-1253-399.png)


### 建立通道， 远程访问及调试

```bash
$ fct -c config.json
```

耐心等待， 直到输出 `Session is OK! now you can remote debug`, 注意不要关闭这个终端。

以上面那个 config.json 为例， 这个时候：

- 可以直接使用 `http://127.0.0.1:8080` 访问 SpringBoot 网站

- 直接使用本地 IDE IDEA 上的源码对实例上的 jar 包进行远程调试
    1. 在菜单栏选择 Run… > Edit Configurations 。
    2. 新建一个 Remote Debugging 。
    3. 自定义调试器名称，并将端口配置为 9000 。
        ![img](https://img.alicdn.com/imgextra/i3/O1CN01JygOEp1CMjHNUtBCP_!!6000000000067-2-tps-1061-671.png)
    4. 上述配置完成后，在 IDEA 编辑器侧边栏为函数代码增加断点，点击"开始调试"按钮。
        ![img](https://img.alicdn.com/imgextra/i1/O1CN01VRnwjr1wJUo2geQwY_!!6000000006287-2-tps-1785-432.png)

当然您也可以借助本地的代理容器实例，作为跳板机， 实现对云上具体实例的管理操作

```bash
$ docker ps -a | grep VPN-Local
d46a86c27abd   registry.cn-beijing.aliyuncs.com/aliyunfc/vpn-local-proxy:v0.0.1   "/usr/app/start.sh"   5 minutes ago   Up 5 minutes   0.0.0.0:8080->8080/tcp, 0.0.0.0:9000->9000/tcp   VPN-Local-S-5ecc9bda-6d83-4f5d-884c-6739d8a3925e

$ docker exec -it d46a86c27abd bash
root@d46a86c27abd:/usr/app# telnet 10.20.108.195 8080
Trying 10.20.108.195...
Connected to 10.20.108.195.
Escape character is '^]'.
```

### 关闭通道

调试完毕后， 直接 `CTRL+C` 结束建立通道命令执行的那个终端， 会自动执行清理 FC 资源操作， 尤其是会自动取消有付费的预留


## 其他

通道建立借助了  Serverless 的 FC 128M 实例,  FC的计费粒度精确到毫秒计费

- 函数实例资源使用量：每月前400,000 GB-秒函数实例资源使用量免费


- 即使不考虑每个月的免费额度，我们这里折算成小时， 也就是您调试 1h, 费用大约为 0.000110592元/GB-秒*128/1024*3600 =0.0497 元

[FC 计费详情](https://help.aliyun.com/document_detail/54301.html)