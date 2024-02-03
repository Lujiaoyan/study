'''梦曦の主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('梦曦の首页',["我推的","我的图片处理工具","我的智慧词典","我的留言区","音频"])

def page1():
    '''推的''' 
    tab1,tab2,tab3,tab4=st.tabs(["咒术回战","新世纪福音战士","孤独摇滚","原神"])
    with tab1:
        st.write("五条悟")
        st.write("-------------------------------------------------")
        st.image("五条悟开篇.jpg")
        st.write(":red[术式反转 赫]") 
        st.image("术式反转赫1.jpg")
        st.image("术式反转赫2.jpg")
        st.image("术式反转赫3.jpg")
        st.image("术式反转赫4.jpg")
        st.image("术式反转赫5.jpg")
        st.image("术式反转赫6.jpg")
        st.image("术式反转赫7.jpg")
        st.image("术式反转赫8.jpg")
        st.image("术式反转赫9.jpg")
        st.image("术式反转赫10.jpg")
        st.image("术式反转赫11.jpg")
        st.image("术式反转赫12.jpg")
        st.image("术式反转赫13.jpg")
        st.image("术式反转赫14.jpg")
        st.image("术式反转赫15.jpg")
        st.image("术式反转赫16.jpg")
        st.image("术式反转赫17.jpg")
        st.image("术式反转赫18.jpg")
        st.image("术式反转赫19.jpg")
        st.image("术式反转赫20.jpg")
        st.image("术式反转赫21.jpg")
        st.image("术式反转赫22.jpg")
        st.image("术式反转赫23.jpg")
        st.image("术式反转赫24.jpg")
        st.image("术式反转赫25.jpg")
        st.image("术式反转赫26.jpg")
        st.image("术式反转赫27.jpg")
        st.image("术式反转赫28.jpg")
        st.image("术式反转赫29.jpg")
        st.image("术式反转赫30.jpg")
        st.image("术式反转赫31.jpg")
        st.image("术式反转赫32.jpg")
        st.image("术式反转赫33.jpg")
        st.image("术式反转赫34.jpg")
        st.image("术式反转赫35.jpg")
        st.image("术式反转赫36.jpg")
        st.image("术式反转赫37.jpg")
    with tab2:
        st.write("新世纪福音战士")
    with tab3:
        st.write("孤独摇滚")
        st.write("-------------------------------------------------")
        st.write(":pink[波奇酱]")
        st.image("5XF686~Y[76{U`[TPYC%FCW_tmb.jpg")
        st.image("([BS4PJ913~7$$X(9S]YN}Q_tmb.jpg")
        st.image("G5{ET~P0XMW~$OKVA]XU9_D_tmb.jpg")
        st.image("DJ@([3P@UF42MEV%F%GB[6W_tmb.jpg")

    with tab4:
        st.write("原神")
    st.write("-------------------------------------------------")
    
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array= img.load()
    for x in range(width):
        for y in range(height):
            r =img_array[x,y][rc]
            g =img_array[x,y][gc]
            b =img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img


def page2():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序：sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name= uploaded_file.name
        file_type= uploaded_file.type
        file_size= uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
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
    
def page5():
    '''音频'''
    st.write("-------------------------------------------------")
    tab1,tab2,tab3,tab4=st.tabs(["ROG","音乐","经典名言","空"])
    with tab1:
        st.write("REPUBLIC OF GAMERS")
        st.image("ROG.png")
        with open ("ROG开机音效.MP3","rb") as f:
            a = f.read()
        st.audio(a, format="audio/mp3 ",start_time=0)
    with tab2:
        with open ("for ya伴奏.MP3","rb") as f:
            b = f.read()
        st.audio(b, format="audio/mp3 ",start_time=0)
    with tab3:
        with open ("原神玩家的诞生.MP3","rb") as f:
            c = f.read()
        st.audio(c, format="audio/mp3 ",start_time=0)
    with tab4:
        pass
        
if page == "我推的":
    page1()
elif page == "我的图片处理工具":
    page2()
elif page == "我的智慧词典":
    page3()
elif page == "我的留言区":
    page4()
elif page == "音频":
    page5()
