# [Java]Gradle设置代理


## 全局代理
在`C:\Users\用户\.gradle`文件夹下打开或新建`gradle.properties`
增加内容：
```properties
# gradle 代理配置
systemProp.socks.proxyHost=xxx
systemProp.socks.proxyPort=xxx
systemProp.socks.proxyUser=xxx
systemProp.socks.proxyPassword=xxx

systemProp.http.proxyHost=xxx
systemProp.http.proxyPort=xxx
systemProp.http.proxyUser=xxx
systemProp.http.proxyPassword=xxx

systemProp.https.proxyHost=xxx
systemProp.https.proxyPort=xxx
systemProp.https.proxyUser=xxx
systemProp.https.proxyPassword=xxx
```

## 项目代理
在项目`build.gradle`同级目录下新建`gradle.properties`  
增加内容：  
分别配置socks、http、https的代理IP、代理端口、用户名和密码：
```properties
# gradle 代理配置
systemProp.socks.proxyHost=xxx
systemProp.socks.proxyPort=xxx
systemProp.socks.proxyUser=xxx
systemProp.socks.proxyPassword=xxx

systemProp.http.proxyHost=xxx
systemProp.http.proxyPort=xxx
systemProp.http.proxyUser=xxx
systemProp.http.proxyPassword=xxx

systemProp.https.proxyHost=xxx
systemProp.https.proxyPort=xxx
systemProp.https.proxyUser=xxx
systemProp.https.proxyPassword=xxx
```
---
例如我用的clash代理，默认socks和http端口均是7890，没有密码,我的配置文件为：  
```properties
systemProp.socks.proxyHost=127.0.0.1
systemProp.socks.proxyPort=7890

systemProp.http.proxyHost=127.0.0.1
systemProp.http.proxyPort=7890

systemProp.https.proxyHost=127.0.0.1
systemProp.https.proxyPort=7890

```

