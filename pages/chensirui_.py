'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的主页', [ "我的兴趣推荐", "我的图片处理工具", "我的智慧词典", "我的留言区"])

def page1():
    '''兴趣推荐'''
    st.write("我的书籍推荐")
    st.write("流浪地球     刘慈欣")
    st.write("--------------------------")
    st.image("chensirui 1.png")
    st.write(" 太阳内部氢转化成氦的速度突然加快，人类面临灭顶之灾,各个国家决定实施一项长达2500年的宏大计划：建造行星发动机将地球推离太阳系。突出了无处安身的人们面对家园毁灭时的无奈、痛苦、恐惧、绝望，反映了人在自然、宇宙面前的渺小，着重刻画了“人在灾难中”的情状。")
    st.write("--------------------------")
    st.write('我的电影推荐')
    st.image("chensirui 2.png")
    st.write("  该片以盛唐为背景，讲述安史之乱后，整个长安因战争而陷入混乱，身处局势之中的高适回忆起自己与李白的过往的故事")
    st.write("--------------------------")
    st.write("我的美术作品推荐")
    st.write("  梵高是世界最为著名的艺术家之一，他的艺术作品总能使观者身临其境")
    st.image("chensirui 3.png")
    st.image("chensirui 4.png")
    st.image("chensirui 5.png")
    st.image("chensirui 6.png")
    st.write("--------------------------")
def page2():
    from PIL import Image
    '''图片处理'''
    st.write("sunglass:图片处理小程序：sunglasses")
    uploaded_file = st.file_uploader("上传图片", type=["png", "jpeg", "jpg"])
    if uploaded_file:
        # 获取文件的名称类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # st.image(img)
        # st.image(img_change(img,0, 2, 1))
    tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
    with tab1:
        st.image(img)
    with tab2:
        st.image(img_change(img, 0, 2, 1))
    with tab3:
        st.image(img_change(img, 1, 2, 0))
    with tab4:
        st.image(img_change(img, 1, 0, 2))
        
def img_change(img, rc, bc, gc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

        
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