---
title: "Set Clash Proxy for wsl"
date: 2022-11-28
summary: "Set clash proxy for wsl"
categories:
- linux
tags:
- linux
- proxy
# hidemeta: true
---

## Create proxy.sh

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
`chmod +x proxy.sh` command make it executable

## 使用说明
1. windows open clash
2. wsl command `source proxy.sh [set]` for open
3. wsl command `source proxy.sh unset` for close
