import streamlit as st

page = st.sidebar.radio("首页",["模组分享","汉化作品","打赏区","交流群","留言区"])

# 1-1
def page1():
    with open("screamingwall.mp3","rb") as f:
        bgm = f.read()
    st.audio(bgm, format = "mp3", start_time = 0)
    st.write(":green[Las Monjas]")
    st.write(":red[The Other Roles]")
    st.write(":orange[Town Of Us]")

#1-2
def page2():
    pass

#1-3
def page3():
    pass

#1-4
def page4():
    st.write(":orange[QQ交流1群]")

#1-5
def page5():
    pass

if page == "模组分享":
    page1()
elif page == "汉化作品":
    page2()
elif page == "打赏区":
    page3()
elif page == "交流群":
    page4()
elif page == "留言区":
    st.write(":orange[有建议或者反馈请在下方留言]")
