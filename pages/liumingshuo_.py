import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具' , '我的智慧词典' , '我的留言区'])

def page1 ():
    '''兴趣推荐'''
    pass

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小工具:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])

    if uploaded_file:
        filr_name = uploaded_file.name
        filr_type = uploaded_file.type
        filr_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img))

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



def img_change(img):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = [r, g, b]
    return, img
