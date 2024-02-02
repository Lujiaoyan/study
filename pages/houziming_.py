import streamlit as st
page = st.sidebar.radio("保定铁路爱好者网站",["机车图片", "图片处理", "机车数据", "留言区"])

def page1():
    '机车图片'
    pass
def page2():
    '图片处理'
    pass
def page3():
    '机车数据'
    pass
def page4():
    '留言区'
    pass
if page == "机车图片":
    page1()
elif page == "图片处理":
    page2()
elif page == "机车数据":
    page3()
elif page == "留言区":
    page4()
with open('歌曲.mp3', 'rb')as f:
    mymp3 = f.read()
st.audio(mymp3, format='audio/mp3', start_time = 0)