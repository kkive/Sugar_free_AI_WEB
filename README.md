# Sugar_free_AI_WEB
无糖-人工智能创作平台
<summary>轻松使用</summary>

```bash

git clone https://github.com/kkive/Sugar_free_AI_WEB.git

cd Sugar_free_AI_WEB

将您的API加入app.py

export FLASK_APP=app.py

flask run --host=0.0.0.0

streamlit run app.py

访问您服务器公网地址8501端口就可以了

```

<div align="center">
<img src="https://user-images.githubusercontent.com/51246778/209045072-01e4a2a1-3daf-477f-86a6-daa8998eb108.jpg"/>
</div>

断开shell之后接口和web无法运行,使用linux自带的nohup

```bash
nohup flask run --host=0.0.0.0 >/dev/null &
nohup streamlit run app.py > /dev/null &
```


openai,chatapt,人工智能,自动对话,聊天机器人,微信chat,
