'''梦曦の主页'''
import streamlit as st
page = st.sidebar.radio('梦曦の首页',["我推的","我的图片处理工具","我的智慧词典","我的留言区","音频"])

def page1():
    '''推的''' 
    st.write("-------------------------------------------------")
    st.write("五条悟")
    st.image("我的网络根据地/五条悟开篇.jpg")
    st.write(":red[术式反转 赫]")
    st.image("我的网络根据地/术式反转赫1.jpg")
    st.image("我的网络根据地/术式反转赫2.jpg")
    st.image("我的网络根据地/术式反转赫3.jpg")
    st.image("我的网络根据地/术式反转赫4.jpg")
    st.image("我的网络根据地/术式反转赫5.jpg")
    st.image("我的网络根据地/术式反转赫6.jpg")
    st.image("我的网络根据地/术式反转赫7.jpg")
    st.image("我的网络根据地/术式反转赫8.jpg")
    st.image("我的网络根据地/术式反转赫9.jpg")
    st.image("我的网络根据地/术式反转赫10.jpg")
    st.image("我的网络根据地/术式反转赫11.jpg")
    st.image("我的网络根据地/术式反转赫12.jpg")
    st.image("我的网络根据地/术式反转赫13.jpg")
    st.image("我的网络根据地/术式反转赫14.jpg")
    st.image("我的网络根据地/术式反转赫15.jpg")
    st.image("我的网络根据地/术式反转赫16.jpg")
    st.image("我的网络根据地/术式反转赫17.jpg")
    st.image("我的网络根据地/术式反转赫18.jpg")
    st.image("我的网络根据地/术式反转赫19.jpg")
    st.image("我的网络根据地/术式反转赫20.jpg")
    st.image("我的网络根据地/术式反转赫21.jpg")
    st.image("我的网络根据地/术式反转赫22.jpg")
    st.image("我的网络根据地/术式反转赫23.jpg")
    st.image("我的网络根据地/术式反转赫24.jpg")
    st.image("我的网络根据地/术式反转赫25.jpg")
    st.image("我的网络根据地/术式反转赫26.jpg")
    st.image("我的网络根据地/术式反转赫27.jpg")
    st.image("我的网络根据地/术式反转赫28.jpg")
    st.image("我的网络根据地/术式反转赫29.jpg")
    st.image("我的网络根据地/术式反转赫30.jpg")
    st.image("我的网络根据地/术式反转赫31.jpg")
    st.image("我的网络根据地/术式反转赫32.jpg")
    st.image("我的网络根据地/术式反转赫33.jpg")
    st.image("我的网络根据地/术式反转赫34.jpg")
    st.image("我的网络根据地/术式反转赫35.jpg")
    st.image("我的网络根据地/术式反转赫36.jpg")
    st.image("我的网络根据地/术式反转赫37.jpg")
    st.write("-------------------------------------------------")
    st.write(":pink[波奇酱]")
    st.image("我的网络根据地/5XF686~Y[76{U`[TPYC%FCW_tmb.jpg")
    st.image("我的网络根据地/([BS4PJ913~7$$X(9S]YN}Q_tmb.jpg")
    st.image("我的网络根据地/G5{ET~P0XMW~$OKVA]XU9_D_tmb.jpg")
    st.image("我的网络根据地/DJ@([3P@UF42MEV%F%GB[6W_tmb.jpg")
def page2():
    '''图片处理工具'''
    pass
def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass
def page5():
    '''音频'''
    st.write("-------------------------------------------------")
    st.write("REPUBLIC OF GAMERS")
    st.image("我的网络根据地/ROG.png")
    with open ("我的网络根据地/ROG开机音效.MP3","rb") as f:
       a = f.read()
    st.audio(a, format="audio/mp3 ",start_time=0)
    with open ("我的网络根据地/for ya伴奏.MP3","rb") as f:
       b = f.read()
    st.audio(b, format="audio/mp3 ",start_time=0)
    with open ("我的网络根据地/原神玩家的诞生.MP3","rb") as f:
       c = f.read()
    st.audio(c, format="audio/mp3 ",start_time=0)
    
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