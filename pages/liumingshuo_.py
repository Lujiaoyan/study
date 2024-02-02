import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具' , '我的智慧词典' , '我的留言区'])

def page1 ():
    '''兴趣推荐'''
    pass

def page2 ():
    '''图片处理工具'''
    pass

def page3 ():
    '''智慧词典'''
    pass

def page4 ():
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