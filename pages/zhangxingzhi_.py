'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '''兴趣推荐'''
    st.write("---------------兴趣推荐--------------")
    st.write(" :red[——————————MUSIC——————————]")
    with open('平凡之路.wav','rb') as f:
        mywav = f.read()
    st.audio(mywav,format='audio/wav',start_time=0)
    st.image("Image1.jpg")
    st.image("Image2.jpg")
    st.write(" :red[——————————动漫——————————]")
    st.image("Image3.jpg")
    st.image("Image4.jpg")
    st.write(" :orange[——————————游戏——————————]")
    st.image("Image5.jpg")
    st.image("Image6.jpg")
    st.write(" :blue[——————————名梗——————————]")
    st.write("我的任务完成啦！")
    st.image("Image7.jpg")
    st.write("今晚8点......")
    st.image("Image8.jpg")
def page2():
    '''图片处理器'''
    pass
def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()