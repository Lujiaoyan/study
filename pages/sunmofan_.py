'''Website'''
import streamlit as st
from PIL import Image,ImageFilter

page = st.sidebar.radio('首页',['兴趣推荐','图片处理','词典','留言'])

def img_rgbchange(img,rgb_c=list):
    width, height = img.size
    img_arry = img.load()
    rgb = {'r':'r','g':'g','b':'b'}
    for x in range(width):
        for y in range(height):
            rgb['r'] = img_arry[x,y][0]
            rgb['g'] = img_arry[x,y][1]
            rgb['b'] = img_arry[x,y][2]
            img_arry[x,y] = (rgb[rgb_c[0]],rgb[rgb_c[1]],rgb[rgb_c[2]])
    return img

def img_gaussblur(img):
    gauessimg = img.filter(ImageFilter.GaussianBlur(5))
    return gauessimg

def page1():
    '''兴趣推荐'''
    st.write('Game')
    st.write('----Minecraft')
    st.write('------------------------------------------------------')
    st.write('----Steam')
    st.write('------------------------------------------------------')
    st.write('----吃鸡')
    st.write('------------------------------------------------------')
    st.write('----王者')
    st.write('------------------------------------------------------')
    st.write('----元气骑士')
    st.write('------------------------------------------------------')
    st.write('----暗区')
    st.write('------------------------------------------------------')
    
def page2():
    '''图片处理'''
    st.write('图片处理工具')
    uploaded_file = st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(['原图','模糊图像','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_gaussblur(img))
        with tab3:
            st.image(img_rgbchange(img,['r','b','g']))
        with tab4:
            st.image(img_rgbchange(img,['g','r','b']))
        with tab5:
            st.image(img_rgbchange(img,['b','g','r']))
    
def page3():
    '''词典'''
    pass
    
def page4():
    '''留言'''
    pass

if page == '兴趣推荐':
    page1()
elif page == '图片处理':
    page2()
elif page == '词典':
    page3()
elif page == '留言':
    page4()
