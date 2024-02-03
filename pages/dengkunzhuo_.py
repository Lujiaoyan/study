import streamlit as st
from PIL import Image

page = st.sidebar.radio("首页",["简介","汉化作品","打赏区","交流群","留言区"])

# 图像处理
def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x,y] = (b, r, g)
    return img

# 1-1
def page1():
    st.write(":red[啥也没写doge]")


#1-2
def page2():
    with open("screamingwall.mp3","rb") as f:
        bgm = f.read()
    tab1, tab2, tab3, tab4 = st.tabs([":green[Las Monjas]",":red[The Other Roles]",":orange[Town Of Us]","Town Of Host"])
    with tab1:
        st.audio(bgm, format = "mp3", start_time = 0)
        st.write(":green[Las Monjas v3.7.1]")
        st.write(":green[Las Monjas v3.7.0]")
        st.write(":green[Las Monjas v3.6.0]")
    with tab2:
        pass
    with tab3:
        pass
    with tab4:
        pass

#1-3
def page3():
    pass

#1-4
def page4():
    st.write(":orange[QQ交流1群]")
    st.write(":orange[QQ交流2群]")

#1-5
def page5():
    st.write(":orange[有建议或者反馈请在下方留言]")
    tab1, tab2, tab3, tab4 = st.tabs(["原图","效果1","效果2","效果3"])
    uploaded_file = st.file_uploader("图片上传", type=["png","jpg","jpeg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
    with tab1:
        if uploaded_file:
            st.image(img)
    with tab2:
        if uploaded_file:
            st.image(img_change(img, 2, 0, 1))
    with tab3:
        if uploaded_file:
            st.image(img_change(img, 1, 2, 0))
    with tab4:
        if uploaded_file:
            st.image(img_change(img, 0, 1, 2))
        

if page == "模组分享":
    page1()
elif page == "汉化作品":
    page2()
elif page == "打赏区":
    page3()
elif page == "交流群":
    page4()
elif page == "留言区":
    page5()

