import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from pydub import AudioSegment as AS

page=st.sidebar.radio('我的首页',['Phigros曲绘','数学','植物大战僵尸PE阵型','图片/音频处理'])

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
    st.write(':sunglasses:图片处理:sunglasses:')
    file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    st.write(file)
    if file:
        fname=file.name
        ftype=file.type
        fsize=file.size
        img=Image.open(file)
        t1,t2,t3,t4,t5=st.tabs(['原图','改色1','改色2','改色3','字符画'])
        with t1:
            st.image(img)
        with t2:
            st.image(imgchange(img,0,2,1))
        with t3:
            st.image(imgchange(img,1,2,0))
        with t4:
            st.image(imgchange(img,1,0,2))
        with t5:
            st.image(wordpic(img))
    file=st.file_uploader('上传音频',type=['wav','mp3','flac'])
    
    # if file:
    #     fname=file.name
    #     ftype=file.type
    #     fsize=file.size
    #     sound=AS.from_file(fname, format=ftype)
    #     t1,t2,t3,t4=st.tabs(['原曲','二倍速','0.5倍速','倒放'])
    #     with t1:
    #         st.audio(sound,format=ftype,start_time=0)
    #     with t2:
    #         st.audio(set_speed(sound,2),format=ftype,start_time=0)
    #     with t3:
    #         st.audio(set_speed(sound,0.5),format=ftype,start_time=0)
    #     with t4:
    #         st.audio(sound.reverse(),format=ftype,start_time=0)
    

def imgchange(img,rc,gc,bc):
    w,h=img.size
    imgarray=img.load()
    for x in range(w):
        for y in range(h):
            r=imgarray[x,y][rc]
            g=imgarray[x,y][gc]
            b=imgarray[x,y][bc]
            imgarray[x,y]=(r,g,b)
    return img

def set_speed(sound,n):
    sound1 = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * n)
    })
    sound1.set_frame_rate(sound.frame_rate)
    return sound1

def wordpic(img1):
    img=img1.convert('L')
    img = img.resize((int(img.width/8), int(img.height/8)))
    ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
    new_img = Image.new('RGB', size=img1.size, color=(255, 255, 255))
    for y in range(img.height):
        for x in range(img.width):
            pos = (x, y)
            gray = img.getpixel(pos)
            index = int(gray/256*70)
            draw = ImageDraw.Draw(new_img)
            draw.text((x*8,y*8), ASCII_HIGH[index], fill=(0,0,0), font=ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 9))
    return new_img

if page=='Phigros曲绘':
    page1()
elif page=='数学':
    page2()
elif page=='植物大战僵尸PE阵型':
    page3()
elif page=='图片/音频处理':
    page4()
