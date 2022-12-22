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


断开shell之后接口和web无法运行,使用linux自带的nohup
nohup flask run --host=0.0.0.0 >/dev/null &
nohup streamlit run app.py > /dev/null &
