'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])


def page1():
    '''兴趣推荐'''
    st.write(':red[电影兴趣推荐：]')
    st.image('美食总动员.png')
    st.write(':red[学习兴趣推荐：]')
    st.write('____________________________________')
    st.write(':red[书籍兴趣推荐：]')
    st.write('____________________________________')
    st.write(':red[游戏兴趣推荐：]')
    st.image('蛋仔派对.png')
    st.write(':red[背景兴趣推荐]')
    st.image('小兔子.png')


def page2():
    '''图片处理工具'''
    pass


def page3():
    '''智慧词典'''
    pass


def page4():
    '''留言区'''
    st.write(':red[快来写入你的留言吧！]')
    st.write('___________________________________')


if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
