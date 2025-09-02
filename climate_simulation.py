# streamlit 라이브러리 설치 필요
# pip install streamlit matplotlib numpy

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="지구 기후 시뮬레이션", layout="wide")

st.title("🌍 지구 기후 시뮬레이션")

# Sidebar 버튼
st.sidebar.header("시뮬레이션 선택")
elnino = st.sidebar.button("엘니뇨")
lanina = st.sidebar.button("라니냐")
glacier = st.sidebar.button("빙하 녹음")
greenhouse = st.sidebar.button("온실 효과 강화")
typhoon = st.sidebar.button("태풍")
rain = st.sidebar.button("강수량")
heatwave = st.sidebar.button("폭염")

# 지구 시각화 기본 설정
earth_temp = 15  # 평균 지구 기온
sea_level = 0    # 해수면 기준
cloud_density = 0.5  # 구름 밀도 (0~1)

# 버튼 이벤트에 따른 상태 변경
if elnino:
    st.subheader("🌡 엘니뇨 시뮬레이션")
    earth_temp += 2
    cloud_density += 0.2
    st.write("태평양 적도 해수 온도가 상승하여 남미 지역 강수량 증가, 아시아 지역 가뭄 발생")

if lanina:
    st.subheader("🌊 라니냐 시뮬레이션")
    earth_temp -= 1
    cloud_density -= 0.1
    st.write("태평양 해수 온도가 낮아져 전 세계 날씨 패턴 변화")

if glacier:
    st.subheader("🧊 빙하 녹음 시뮬레이션")
    sea_level += 1  # 간단히 1단위 상승
    st.write("빙하 용해로 해수면 상승, 해안 지역 홍수 가능성")

if greenhouse:
    st.subheader("🔥 온실 효과 강화 시뮬레이션")
    earth_temp += 3
    cloud_density += 0.3
    st.write("대기 온도 상승으로 구름 형태 변화 및 극한 기상 증가 가능")

if typhoon:
    st.subheader("🌀 태풍 시뮬레이션")
    st.write("따뜻한 해수에서 발생한 저기압으로 강력한 바람과 폭우 발생")

if rain:
    st.subheader("☔ 강수량 시뮬레이션")
    st.write("대기와 해수의 상호작용으로 강수량 변화 관찰")

if heatwave:
    st.subheader("🌞 폭염 시뮬레이션")
    st.write("온실효과로 인한 극한 고온 발생 가능")

# 지구 시각화 (간단한 원형 이미지 + 온도, 구름 밀도 표시)
fig, ax = plt.subplots(figsize=(6,6))
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

ax.fill(x, y, color='deepskyblue')  # 바다
ax.fill(0.7*x, 0.7*y, color='forestgreen')  # 대륙

# 구름 표현
cloud_x = np.random.uniform(-1,1, int(cloud_density*50))
cloud_y = np.random.uniform(-1,1, int(cloud_density*50))
ax.scatter(cloud_x, cloud_y, color='white', alpha=0.6, s=100, label='구름')

ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# 해수면 상승 표시
st.write(f"🌊 해수면 상승: {sea_level} 단위")
st.write(f"🌡 평균 지구 온도: {earth_temp} ℃")
st.write(f"☁ 구름 밀도: {cloud_density:.2f}")
