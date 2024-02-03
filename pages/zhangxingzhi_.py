'''我的主页'''
import streamlit as st
from PIL import Image,ImageOps,ImageFilter

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '''兴趣推荐'''
    st.write("---------------兴趣推荐--------------")
    tab1,tab2,tab3,tab4 = st.tabs(["音乐","动漫","游戏","名梗"])
    with tab1:
        st.write(" :red[——————————MUSIC——————————]")
        with open('平凡之路.wav','rb') as f:
            mywav = f.read()
        st.audio(mywav,format='audio/wav',start_time=0)
        st.image("Image1.jpg")
        st.image("Image2.jpg")
    with tab2:
        st.write(" :red[——————————动漫——————————]")
        st.image("Image3.jpg")
        st.image("Image4.jpg")
        st.write("角都：我马上就会把你送进换金所了！")
        st.image("奥义1.png")
        st.write("迪达拉：艺术就是爆炸！")
        st.image("奥义2.jpg")
        st.write("蝎：没有腐朽，永恒的美才是艺术！")
        st.image("奥义3.jpg")
        st.write("鼬：花筒写轮眼的幻术是难以逃避的！")
        st.image("奥义4.jpg")
        st.write("小南：以神的旨意......审判你！")
        st.image("奥义5.jpg")
        st.write("佩恩：从现在起，让世界感受痛苦！")
        st.image("奥义6.jpg")
        st.write("阿飞（带土）：耶！不愧是我的忍术！帅，太帅了！")
        st.image("奥义7.jpg")
        st.write("鬼鲛：哼哼，我的鲨鱼今天可以加菜了！")
        st.image("奥义8.jpg")
        st.write("飞段：这可是很痛的，你要有所觉悟啊！")
        st.image("奥义9.jpg")
    with tab3:
        st.write(" :orange[——————————游戏——————————]")
        st.image("Image5.jpg")
        st.image("Image6.jpg")
        
    with tab4:
        st.write(" :blue[——————————名梗——————————]")
        st.write("我的任务完成啦！")
        st.image("Image7.jpg")
        st.write("今晚8点......")
        st.image("Image8.jpg")
def page2():
    '''图片处理器'''
    st.write(":sunglasses:图片处理器:sunglasses:") 
    uploaded_file =st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    st.write("录入图片前会有报错")    
    if uploaded_file:
        #获取数值
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_name = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","换色一","换色二","换色三"])
    with tab1:
        st.image(img_change(img,0,1,2))
    with tab2:
        st.image(img_change(img,1,2,0))
    with tab3:
        st.image(img_change(img,2,1,0))
    with tab4:
        st.image(img_change(img,2,0,1))
def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
