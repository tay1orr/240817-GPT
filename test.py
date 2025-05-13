# 🍽️✨ 부천 핫플 맛집·카페 MAP (클릭하면 지도 이동!) ✨🍰
# 실행: streamlit run bucheon_food_map.py
# 필요: pip install streamlit pydeck pandas
import streamlit as st
import pandas as pd
import pydeck as pdk

# ──────────────────── 1. 페이지 설정 ──────────────────── #
st.set_page_config(page_title="부천 핫플 MAP", page_icon="🍽️", layout="wide")

# ──────────────────── 2. 데이터 ───────────────────────── #
PLACES = [
    # name, category, address, lat, lon
    ("코르드블랭크", "브런치 카페 🥞", "경기도 부천시 오정구 까치로6번길 17-12", 37.507313, 126.809723),
    ("앤드", "티 전문 카페 🍵",       "경기도 부천시 오정구 까치로6번길 40",    37.507410, 126.808624),
    ("숲숲", "플랜트 카페 🌿",        "경기도 부천시 오정구 까치로6번길 36",    37.506759, 126.810326),
    ("리틀 시칠리", "가성비 파스타 🍝", "경기도 부천시 원미구 길주로 80",         37.504994, 126.752435),
    ("뽁식당 부천점", "로제·리조또 🍲", "경기도 부천시 원미구 석천로177번길 36",  37.503636, 126.761052),
    ("명가 진흙구이", "오리·백숙 🦆",   "경기도 부천시 오정구 소사로 599",        37.511505, 126.798433),
]
df = pd.DataFrame(PLACES, columns=["name", "category", "address", "lat", "lon"])

# ──────────────────── 3. 사이드바(매장 선택) ───────────── #
st.sidebar.header("📍 매장을 선택하면 지도가 이동해요!")
choice = st.sidebar.radio(
    label="🍴 부천 핫플 리스트",
    options=df["name"],
    format_func=lambda x: f"{x} ({df.loc[df['name']==x,'category'].values[0]})",
)

# 선택한 매장의 좌표
row = df[df["name"] == choice].iloc[0]
sel_lat, sel_lon = row["lat"], row["lon"]

# ──────────────────── 4. 지도 그리기 ─────────────────── #
# 선택 매장은 크고 연둣빛, 나머지는 분홍빛 표시
layer_all = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position="[lon, lat]",
    get_radius=120,
    get_fill_color="[255,0,127,160]",
    pickable=True,
)

layer_selected = pdk.Layer(
    "ScatterplotLayer",
    pd.DataFrame([row]),
    get_position="[lon, lat]",
    get_radius=250,
    get_fill_color="[0,255,127,200]",
)

view_state = pdk.ViewState(latitude=sel_lat, longitude=sel_lon, zoom=14, pitch=45)

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/streets-v12",
        initial_view_state=view_state,
        layers=[layer_all, layer_selected],
        tooltip={"text": "{name}\n{category}\n{address}"},
    )
)

# ──────────────────── 5. 상세 정보 ───────────────────── #
st.markdown("## 📌 선택한 매장 정보")
st.write(f"**{row['name']} — {row['category']}**")
st.write(f"🏠 주소: {row['address']}")
st.write(f"🛰️ 위·경도: {sel_lat:.6f}, {sel_lon:.6f}")
st.markdown(
    f"[🗺️ 카카오지도 길찾기](https://map.kakao.com/?q={row['address']})",
    unsafe_allow_html=True,
)

st.caption("※ 본 앱은 **교육 목적** 예시입니다. 방문 전 영업시간·휴무일을 확인하세요!")
