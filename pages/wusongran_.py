'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])
'''诶嘿'''
def page1():
    '''兴趣推荐'''
    st.write("我喜欢的游戏")
    st.write(":sunglasses:《原神》:sunglasses:")
    st.write(" ")
    st.write(":sunglasses:《崩坏•星穹铁道》:sunglasses:")
    st.write(" ")
    st.write(":sunglasses:《元气骑士前传》:sunglasses:")
    st.write("-------------------------------------------------------------------")
    st.write("我喜欢的书")
    st.write("《天蓝色的彼岸》")
    st.write("-------------------------------------------------------------------")
    st.write("我最爱的电影")
    st.write("《三大队》    《临时劫案》")
    st.write("-------------------------------------------------------------------")
    
def img_change(img):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):

            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (b, g, r)
    return img
    
def page2():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:

        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        
        tab1, tab2= st.tabs(["原图","改色"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img))

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

