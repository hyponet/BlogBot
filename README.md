# 一个简单的机器人

一个倒腾在 图灵机器人 API 与 DaoVoice API 的贩子中间件。

## 部署

需要几个环境，变量，缺一不可。

`VOICE_TOKEN` ：DaoVoice 的 access_token 

`VOICE_API`：https://api.daovoice.io 

`VOICE_ADMIN_ID`：DaoVoice 用来回复的用户 admin_id 

`REBOT_API`：http://www.tuling123.com/openapi

`REBOT_TOKEN`：图灵机器人的 APIKey  

```
docker run -d -p 80:4000 -e <上面的环境变量> daocloud.io/ihypo/robot
```

还有一个选填的环境变量：

`SAY_HELLO`：当用户创建回话的默认回复  

## 使用

这个镜像开放两个 API

ping api，用来检查看有没有还活着：

```
# GET /_ping
```

hook api，直接把这个 api 添加到 DaoVoice 的 webhook 里就可以了：

```
# POST /hook
```

## 注意

只保证 `tag:latest` 能正常工作。

## 其他

更多可见：http://blog.ihypo.net/14848342546060.html
