'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    '''兴趣推荐'''
    st.write("我喜欢的游戏")
    st.write("《原神》")
    st.write(" ")
    st.write("《崩坏•星穹铁道》")
    st.write(" ")
    st.write("《元气骑士前传》")
    st.write("-------------------------------------------------------------------")
    st.write("我喜欢的书")
    st.write("《天蓝色的彼岸》")
    st.write("-------------------------------------------------------------------")
    st.write("我最爱的电影")
    st.write("《三大队》    《临时劫案》")
    st.write("-------------------------------------------------------------------")
    
    

def page2():
    '''图片处理工具'''
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