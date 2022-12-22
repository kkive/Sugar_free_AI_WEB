import streamlit as st
import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
import os
import openai


# 设置网页标题，以及使用宽屏模式
st.set_page_config(
    page_title="无糖-AI",
    # page_icon="random",#  自动变换网页图标
    page_icon="🌼",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "完全由小白开发. 需要合作请联系我@"
    }
)

# 隐藏右边的菜单以及页脚


def welcome():
    st.write("欢迎光临小杰的AI殿堂 👻")
    st.sidebar.success("选择访问的页面")
    video_file = open('331941155.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)



def openai():
    st.write("""OpenAI""")
    st.sidebar.success("无时无刻都创作 📝")
    option = st.selectbox(
        '选择创作类型',
        ('图片', '文本'))
    if option == "图片":
        st.write('图片')
        st.write('还在写代码ing,先使用文本功能把')

    if option == "文本":
        txt = st.text_area('输入问题', '''''')
        if st.button('提交'):
            st.code('结果:\n', openai_api_ask(txt))




def test():
    st.write("""test""")
    st.sidebar.success("测试页面 🍺")

def openai_api_ask(a):
    import requests
    url = "http://123.60.102.67:5000/test?ask="+a
    payload={}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    return (response.text)


page_names_to_funcs = {
    "欢迎光临": welcome,
    "无糖厂创作助手": openai,
    "空白测试页面": test,
}
demo_name = st.sidebar.selectbox("页 面", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
