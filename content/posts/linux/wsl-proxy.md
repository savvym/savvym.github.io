---
title: "wsl配置使用本地clash代理"
date: 2022-11-28
summary: "Set clash proxy for wsl"
categories:
- linux
tags:
- linux
- proxy
# hidemeta: true
---

## 创建proxy.sh文件

```shell
#!/bin/bash
hostip=$(cat /etc/resolv.conf |grep -oP '(?<=nameserver\ ).*')
https_proxy="http://${hostip}:7890"
http_proxy="http://${hostip}:7890"

function set_proxy() {
	export http_proxy="${http_proxy}"
	export https_proxy="${https_proxy}"
	echo "env http/https proxy set."
}

function unset_proxy(){
	unset http_proxy
	unset https_proxy
	echo "env proxy unset"
}

if [ "$1" = "set" ]; then
	set_proxy
elif [ "$1" = "unset" ]; then
	unset_proxy
else
	set_proxy
fi
```
保存之后`chmod +x proxy.sh`

## 使用说明
1. windows开启clash
2. wsl运行`source proxy.sh [set]` 开启
3. wsl运行`source proxy.sh unset` 关闭
