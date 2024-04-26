import numpy as np
import pandas as pd
import streamlit as st
from datetime import time, datetime

if __name__ == '__main__':
    st.header('Streamlitのテストページ', divider='blue')
    page = st.sidebar.selectbox('ページを選択', ['page1','page2','page3','page4','page5'], index=0)

    if page == 'page1':
        st.title('ページ1')
        st.write('Streamlitのテストページ1です。')

        st.subheader('Slider')
        age = st.slider('How old are you?', 0,130,25)
        st.write("I'm ", age, 'years old')

    elif page == 'page2':
        st.title('ページ2')
        st.write('Streamlitのテストページ2です。')

        st.subheader('Range slider')

        values = st.slider('Select a range of values',0.0,100.0,(25.0,75.0))
        st.write('Values:', values)

        appointment = st.slider("Schedule your appointment:",
                                value=(time(11,30), time(12,45)))
        st.write("You're scheduled for:", appointment)

    elif page == 'page3':
        st.write('Streamlitのテストページ3です。')

        st.write('Datetime slider')
        start_time = st.slider("when do you start?", value=datetime(2020,1,1,9,30),format="YYYY/MM/DD - hh:mm")
        st.write("Start time:", start_time)

    elif page == 'page4':
        st.title('ページ4')
        st.write('Streamlitのテストページ4です。')

        st.header('Line Chart')

        chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])

        st.line_chart(chart_data)

    elif page == 'page5':
        st.header('select box')

        option = st.selectbox('What is your favorite color?',('Red','Blue','Yellow'))

        st.write('Your favorite color is ', option)

        st.header('multi select')

        options = st.multiselect('What are your favorite colors', ['Green','Yellow','Red','Blue'],['Yellow', 'Red'])

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