import streamlit as st

def input_number():
    number = st.number_input('数字を入力してください', min_value=1, value=1)
    return number