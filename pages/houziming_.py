from PIL import Image
import streamlit as st
page = st.sidebar.radio("保定铁路爱好者网站",["机车图片", "图片处理", "机车数据", "留言区"])

def page1():
    '机车图片'
    pass
def page2():
    '''图片处理'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img ,0,2,1))                                    
def page3():
    '机车数据'
    pass
def page4():
    '留言区'
    pass
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if page == "机车图片":
    page1()
elif page == "图片处理":
    page2()
elif page == "机车数据":
    page3()
elif page == "留言区":
    page4()


