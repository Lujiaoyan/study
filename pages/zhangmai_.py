import streamlit as st

page=st.sidebar.radio('我的首页',['Phigros曲绘','数学','植物大战僵尸PE阵型'])

def page1():
    with open('aapa.mp3','rb') as f:
        music=f.read()
    st.audio(music,format='audio/mp3',start_time=0)
    st.write("Rrhar'il")
    st.image("Rrhar'il.jpg")
    st.write("concvssion")
    st.image("concvssion.png")
    st.write("Aleph-0")
    st.image("Aleph-0.png")

def page2():
    st.write("诱导公式")
    st.image("ydgs.jpg")
    st.write("和差角公式")
    st.image("hcjgs.jpg")
    st.write("二倍角公式")
    st.image("ebjgs.jpg")

def page3():
    st.write("经典八炮 节奏：ch6(PP丨I-PP丨PP丨I-PP)")
    st.image("jd8.png")
    st.write("传统四炮")
    st.image("ct4.png")
    st.write("石英钟无炮")
    st.image("syz.png")
    st.write("机械钟无炮")
    st.image("jxz.png")

def page4():
    #留言区
    pass

if page=='Phigros曲绘':
    page1()
elif page=='数学':
    page2()
elif page=='植物大战僵尸PE阵型':
    page3()
# elif page=='我的留言区':
#     page4()