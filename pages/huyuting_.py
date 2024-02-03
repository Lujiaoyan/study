'''我的主页'''
import streamlit as st
from PIL import Image

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
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 1, 0, 2))
        tab1, tab2, tab3, tab4 = st.tabs(['改色1',  '改色2',  '原图',  '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))


def page3():
    '''智慧词典'''
    pass


def page4():
    '''留言区'''
    st.write(':red[快来写入你的留言吧！]')
    st.write('___________________________________')


def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (g, b, r)
    return img


if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
