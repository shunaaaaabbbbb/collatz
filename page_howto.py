import streamlit as st

def page_howto():


    st.title("このサイトの使い方")
    st.subheader("数字を入力してください。")
    st.image("image/input.png")
    st.title("\u2193")
    st.subheader("「計算実行」ボタンを押してください。")
    st.image("image/button.png")
    st.title("\u2193")
    st.subheader("計算過程を出力してくれます。")
    st.image("image/result.png")
    st.title("\u2193")
    st.subheader("カーソルを合わせたらステップ数と計算して得らえた値を表示してくれます。")
    st.image("image/tooltip.png")

