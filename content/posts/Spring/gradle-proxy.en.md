---
title: "Set proxy for Gradle"
date: 2022-06-17
summary: "Set proxy for Gradle"
categories:
- Spring
tags:
- Spring Boot
# hidemeta: true
---

## Global Proxy
Open or create a new file `gradle.properties` from `C:\Users\YOURNAME\.gradle`  
Add follow contents：
```properties
# gradle properties
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

## Project Proxy
In project, create `gradle.properties` in the same directory as `build.gradle` file  
Add：  
```properties
# gradle properties
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
Here is my case: Using Clash as the proxy ,both socks and http default port 7890：  
```properties
systemProp.socks.proxyHost=127.0.0.1
systemProp.socks.proxyPort=7890

systemProp.http.proxyHost=127.0.0.1
systemProp.http.proxyPort=7890

systemProp.https.proxyHost=127.0.0.1
systemProp.https.proxyPort=7890

```
