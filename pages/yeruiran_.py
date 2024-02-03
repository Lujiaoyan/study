'''我的主页'''
import streamlit as st
from PIL import Image

page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def page1():
    '''兴趣推荐'''
    st.write('头像推荐')
    st.image("头像.png")

def page2():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        #获取图片文件的名称，类型和大小
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        #st.image(img_change(img,1,2,0))
        tab1,tab2,tab3,tab4=st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
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
