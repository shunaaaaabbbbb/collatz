import streamlit as st

from collatz import collatz
from input import input_number
from plot import plot_linechart
from explanation import explanation



def page_main():
    st.title("このサイトはコラッツの問題（コラッツ予想）の計算ができるwebアプリです。")
    st.write("")
    st.subheader("数字を入力すれば、計算過程を表示してくれます。")


    ## データの入力
    n = input_number()
    if st.button('計算実行'):
        sequence = collatz(n)
        st.subheader("計算過程：")
        st.markdown(f"{' → '.join(map(str, sequence))}")
        plot_linechart(sequence)
    
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
            
    styled_html = explanation()
    st.markdown(styled_html, unsafe_allow_html=True)  # StreamlitでHTMLコードを表示
     







