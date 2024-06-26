import streamlit as st
import pandas as pd
import altair as alt

def plot_linechart(sequence):
    # DataFrameを作成して横軸と縦軸のラベルを設定
    df = pd.DataFrame({'値': sequence, 'ステップ数': range(len(sequence))})
    # Altairで折れ線グラフを作成
    chart = alt.Chart(df).mark_line(point={'size': 100, 'filled': True, "color": "deepskyblue"},color='deepskyblue').encode(
        x='ステップ数',
        y='値',
        tooltip=[
        alt.Tooltip('ステップ数', title='ステップ数', format='.0f'),  # ツールチップのフォーマットを指定
        alt.Tooltip('値', title='値', format='.0f')  # ツールチップのフォーマットを指定
        ]
    ).properties(
        width=600,
        height=400
    ).configure_line(
        strokeWidth=2  # 折れ線の太さを設定
    ).configure_mark(
        fontSize=14  # マーカーのフォントサイズを設定
    ).configure_axis(
        labelFontSize=14  # 軸ラベルのフォントサイズを設定
    )
    # Streamlitで表示
    st.altair_chart(chart, use_container_width=True)