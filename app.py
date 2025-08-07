import streamlit as st
import streamlit.components.v1 as components

# 제목
st.title("🗺️ 2023년 분리배출량 지도")

# HTML 파일 불러오기
with open("recycle_map_2023.html", "r", encoding="utf-8") as f:
    map_html = f.read()

# 지도를 웹에 출력
components.html(map_html, height=600)
