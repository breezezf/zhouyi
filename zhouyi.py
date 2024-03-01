'''主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('首页', ['推荐', '舞蹈图片处理', '查询', '交流区'])

def page_1():
    '''推荐'''
    with open('编程猫的梦想.mp3', 'rb') as f:
        mymp3 = f.read()
    st.balloons()
    tab1, tab2, tab3, tab4 = st.tabs(['古典舞', '街舞', '民族舞', '明星舞蹈'])
    with tab1:
        st.write('舞者：程潇')
        st.image('1.jpg')
        st.video('舞蹈1.mp4')
    with tab2:
        st.write('舞者：程潇')
        st.image('2.jpg')
        st.video('舞蹈2.mp4')
    with tab3:
        st.write('舞者：程潇')
        st.image('3.jpeg')
        st.video('舞蹈3.mp4')
    with tab4:
        st.write('舞者：程潇')
        st.image('4.jpg')
        st.video('舞蹈4.mp4')
    st.write('网页推荐')
    st.write('除了本主站之外，我还将关于北京舞蹈学院考级七级及以上的考级视频分享在了其他网站中')
    st.write('小提示：考完十三级就可以考教师资格证啦')
    go = st.selectbox('选择想要查看的网页', ['七级', '八级', '九级', '十级', '十一级', '十二级','十三级'])   
    st.link_button('七级', 'https://list.youku.com/albumlist/show/id_51495106.html?ascending=1')
    st.link_button('八级', 'https://www.bilibili.com/video/BV14t41117sw?p=20')
    st.link_button('九级', 'https://www.bilibili.com/video/av36311915/')
    st.link_button('十级', 'https://www.bilibili.com/video/BV14t41117Rs/?spm_id_from=333.337.search-card.all.click')
    st.link_button('十一级', 'https://www.bilibili.com/video/BV1vj411f7x9?p=2')
    st.link_button('十二级', 'https://www.bilibili.com/video/BV1vj411f78J?p=8')
    st.link_button('十三级', 'https://www.bilibili.com/video/BV14t41117sX/?spm_id_from=333.337.search-card.all.click')
    if go == '七级考级视频':
        st.link_button('跳转到'+go, st.link_button('七级', 'https://list.youku.com/albumlist/show/id_51495106.html?ascending=1'))
    elif go == '八级考级视频':
        st.link_button('跳转到'+go, st.link_button('八级', 'https://www.bilibili.com/video/BV14t41117sw?p=20'))
    elif go == '九级考级视频':
        st.link_button('跳转到'+go, st.link_button('九级', 'https://www.bilibili.com/video/av36311915/'))
    elif go == '十级考级视频':
        st.link_button('跳转到'+go, st.link_button('十级', 'https://www.bilibili.com/video/BV14t41117Rs/?spm_id_from=333.337.search-card.all.click'))
    elif go == '十一级考级视频':
        st.link_button('跳转到'+go, st.link_button('十一级', 'https://www.bilibili.com/video/BV1vj411f7x9?p=2'))
    elif go == '十二级考级视频':
        st.link_button('跳转到'+go, st.link_button('十二级', 'https://www.bilibili.com/video/BV1vj411f78J?p=8'))
    elif go == '十三级考级视频':
        st.link_button('跳转到'+go, st.link_button('十三级', 'https://www.bilibili.com/video/BV14t41117sX/?spm_id_from=333.337.search-card.all.click'))
    
    
def page_2(): 
    '''舞蹈图片处理'''
    st.write('''舞蹈演出图片处理''')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img =  Image.open(uploaded_file)
        
        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        
        
def page_3(): 
    '''查询'''
    st.write('翻译')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的名称')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8')as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])

def page_4():
    '''交流区'''
    st.write('留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '舞者一':
            with st.chat_message('✨'):
                st.write(i[1], ':', i[2])
        elif i[1] == '舞者二':
            with st.chat_message('✨'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是.....', ['舞者一', '舞者二'])
    new_messages = st.text_input('想说的话...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_messages])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

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

if page == '推荐':
    page_1()
elif page == '舞蹈图片处理':
    page_2()
elif page == '查询':
    page_3()
elif page == '交流区':
    page_4()