from os import wait

import numpy as np
import pandas as pd
import streamlit as st
import datetime
from time import sleep
from time import time


@st.cache_data
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e'])
    return df


def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df


if __name__ == '__main__':
    st.header('Streamlitのテストページ', divider='blue')
    page = st.sidebar.selectbox('ページを選択',
                                ['page1', 'page2', 'page3', 'page4', 'page5', 'page6', 'page7', 'page8', 'page9',
                                 'page10', 'page11', 'page12'], index=0)

    if page == 'page1':
        st.title('ページ1')
        st.write('Streamlitのテストページ1です。')

        st.subheader('Slider')
        age = st.slider('How old are you?', 0, 130, 25)
        st.write("I'm ", age, 'years old')

    elif page == 'page2':
        st.title('ページ2')
        st.write('Streamlitのテストページ2です。')

        st.subheader('Range slider')

        values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
        st.write('Values:', values)

        appointment = st.slider("Schedule your appointment:",
                                value=(time(11, 30), time(12, 45)))
        st.write("You're scheduled for:", appointment)

    elif page == 'page3':
        st.write('Streamlitのテストページ3です。')

        st.write('Datetime slider')
        start_time = st.slider("when do you start?", value=datetime(2020, 1, 1, 9, 30), format="YYYY/MM/DD - hh:mm")
        st.write("Start time:", start_time)

    elif page == 'page4':
        st.title('ページ4')
        st.write('Streamlitのテストページ4です。')

        st.header('Line Chart')

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

    elif page == 'page5':
        st.header('select box')

        option = st.selectbox('What is your favorite color?', ('Red', 'Blue', 'Yellow'))

        st.write('Your favorite color is ', option)

        st.header('multi select')

        options = st.multiselect('What are your favorite colors', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])

        st.write('Your selected:', options)

        st.header('check box')

        st.write('What would you like to order?')

        icecream = st.checkbox('Ice cream')
        coffee = st.checkbox('Coffee')
        cola = st.checkbox('Cola')

        if icecream:
            st.write("Great! Here's some more ??")

        if coffee:
            st.write("Okay, here's some coffee ?")

        if cola:
            st.write("Here you go ??")

    elif page == 'page6':
        st.title('file uploader')

        st.subheader('Input CSV')

        uploaded_file = st.file_uploader("Choose a file")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.subheader('DataFrame')
            df
            st.subheader('Descriptive Statistics')
            df.describe()
        else:
            st.info('??? Upload a CSV file')

    elif page == 'page7':
        st.title('How to layout your Streamlit app')

        with st.expander('About this app'):
            st.write('This app shows the various ways on how you can layout your Streamlit app.')
            st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

        st.sidebar.header('Sidebar Input')
        user_name = st.sidebar.text_input('What is your name?')
        user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
        user_food = st.sidebar.selectbox('What is your favorite food?',
                                         ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

        st.header('Output')

        col1, col2, col3 = st.columns(3)

        with col1:
            if user_name != '':
                st.write(f'?? Hello {user_name}!')
            else:
                st.write('??  Please enter your **name**!')

        with col2:
            if user_emoji != '':
                st.write(f'{user_emoji} is your favorite **emoji**!')
            else:
                st.write('?? Please choose an **emoji**!')

        with col3:
            if user_food != '':
                st.write(f'?? **{user_food}** is your favorite **food**!')
            else:
                st.write('?? Please choose your favorite **food**!')

    elif page == 'page8':
        st.title('st.progress')

        with st.expander('About this app'):
            st.write(
                'You can now display the progress of your calculations in a Streamlit app with the `st.progress` '
                'command.')

        my_bar = st.progress(0)

        for percent_complete in range(100):
            sleep(0.05)
            my_bar.progress(percent_complete + 1)

        st.balloons()

    elif page == 'page9':
        st.title('st.form')

        # with表記の使用例
        # ※「完全な」は「Full」の訳だと思いますが訳さなくても伝わると思います。
        st.header('1. Example of using `with` notation')
        st.subheader('Coffee machine')

        with st.form('my_form'):
            st.subheader('**Order your coffee**')

            # 入力ウィジェット
            coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
            coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
            brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
            serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
            milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
            owncup_val = st.checkbox('Bring own cup')

            # すべてのフォームには送信ボタンが必要です
            submitted = st.form_submit_button('Submit')

        if submitted:
            st.markdown(f'''
                ? You have ordered:
                - Coffee bean: `{coffee_bean_val}`
                - Coffee roast: `{coffee_roast_val}`
                - Brewing: `{brewing_val}`
                - Serving type: `{serving_type_val}`
                - Milk: `{milk_val}`
                - Bring own cup: `{owncup_val}`
                ''')
        else:
            st.write('?? Place your order!')

        # オブジェクト表記を使用した短い例
        st.header('2. Example of object notation')

        form = st.form('my_form_2')
        selected_val = form.slider('Select a value')
        form.form_submit_button('Submit')

        st.write('Selected value: ', selected_val)

    elif page == 'page10':
        st.title('st.cache')

        # キャッシュを使用する
        a0 = time()
        st.subheader('Using st.cache')

        st.write(load_data_a())
        a1 = time()
        st.info(a1 - a0)

        # キャッシュを使用しない
        b0 = time()
        st.subheader('Not using st.cache')

        st.write(load_data_b())
        b1 = time()
        st.info(b1 - b0)

    elif page == 'page11':
        st.title('st.session_state')


        def lbs_to_kg():
            st.session_state.kg = st.session_state.lbs / 2.2046


        def kg_to_lbs():
            st.session_state.lbs = st.session_state.kg * 2.2046


        st.header('Input')
        col1, spacer, col2 = st.columns([2, 1, 2])
        with col1:
            pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)
        with col2:
            kilogram = st.number_input("Kilograms:", key="kg", on_change=kg_to_lbs)

        st.header('Output')
        st.write("st.session_state object:", st.session_state)

    elif page == 'page12':
        st.title('??? yt-img-app')
        st.header('YouTube Thumbnail Image Extractor App')

        with st.expander('About this app'):
            st.write('This app retrieves the thumbnail image from a YouTube video.')

        # 画像設定
        st.sidebar.header('Settings')
        img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
        selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
        img_quality = img_dict[selected_img_quality]

        yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')


        def get_ytid(input_url):
            if 'youtu.be' in input_url:
                ytid = input_url.split('/')[-1]
            if 'youtube.com' in input_url:
                ytid = input_url.split('=')[-1]
            return ytid


        # YouTubeのサムネイル画像を表示します
        if yt_url != '':
            ytid = get_ytid(yt_url)  # yt or yt_url

            yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
            st.image(yt_img)
            st.write('YouTube video thumbnail image URL: ', yt_img)
        else:
            st.write('?? Enter URL to continue ...')
