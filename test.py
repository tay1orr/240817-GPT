# 🍽️🌟 부천 핫플 맛집·카페 MAP  (EDUCATIONAL DEMO) 🌟🍰
# ------------------------------------------------------------------
# * 실제 영업 중(2024~2025 후기 기준)인 부천 맛집·카페만 선정했습니다.
# * 학습·시연용 예시 코드이며 정보 정확도는 직접 확인 후 이용하세요!
# * 실행:  streamlit run bucheon_food_map.py
# * 필요:  streamlit, pandas, pydeck   (pip install streamlit pandas pydeck)
# ------------------------------------------------------------------

import streamlit as st
import pandas as pd
import pydeck as pdk

# ------ 반드시 첫 번째 Streamlit 명령! --------------------------------------
st.set_page_config(page_title="부천 핫플 MAP", page_icon="🍽️", layout="wide")
# ---------------------------------------------------------------------------

# 🌈 화려한 배경 CSS --------------------------------------------------------
st.markdown(
    """
    <style>
    body {background:linear-gradient(135deg,#fceabb 0%,#f8b500 100%);}
    h1,h2,h3 {color:#fff;}
    .block-container {padding-top:1.2rem;}
    .stButton>button {border-radius:8px;font-weight:600;
        box-shadow:0 4px 14px rgba(0,0,0,0.25);transition:.3s;}
    .stButton>button:hover {transform:translateY(-3px);}
    </style>
    """,
    unsafe_allow_html=True,
)

# 🎉 헤더 -------------------------------------------------------------------
st.title("🎉 부천 요즘 🔥핫🔥 한 맛집 & 카페 지도")
st.caption("※ 교육용 데모 · 방문 전 영업 시간/휴무를 꼭 확인해주세요!")

# 📍 맛집·카페 데이터 (좌표는 실제 위치 기준) -------------------------------
PLACES = [
    # name, category, address, lat, lon
    ("코르드블랭크",  "브런치 카페 💖",   "경기 부천시 오정구 까치로6번길 17-12",
     37.507313, 126.809723),
    ("앤드",          "티 전문 카페 🫖",  "경기 부천시 오정구 까치로6번길 40",
     37.507135, 126.810100),
    ("숲숲",          "플랜트 카페 🌿",   "경기 부천시 오정구 까치로6번길 36",
     37.506760, 126.810326),
    ("리틀 시칠리",    "가성비 파스타 🍝", "경기 부천시 원미구 길주로 80",
     37.505818, 126.753162),
    ("뽁식당 부천점",  "분위기 만점 🍕",  "경기 부천시 원미구 석천로177번길 36",
     37.504900, 126.765500),
    ("명가 진흙구이",  "오리 보양식 🦆",  "경기 부천시 오정구 소사로 599",
     37.505381, 126.797350),
]

df = pd.DataFrame(
    PLACES, columns=["name", "category", "address", "lat", "lon"]
)

# 🗺️ PyDeck 지도 ------------------------------------------------------------
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[lon, lat]",
    get_radius=120,
    get_fill_color="[255, 0, 127, 180]",
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=float(df.lat.mean()),
    longitude=float(df.lon.mean()),
    zoom=12,
    pitch=45,
)

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/streets-v12",
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{name} ({category})\n{address}"},
    )
)

# 📋 상세 리스트 -------------------------------------------------------------
st.markdown("---")
st.subheader("📌 상세 정보")

for _, row in df.iterrows():
    with st.expander(f"{row['name']} — {row['category']}"):
        st.write(f"📍 **주소** : {row['address']}")
        st.write(f"🛰️ **좌표** : {row['lat']:.6f}, {row['lon']:.6f}")
        kakao_link = f"https://map.kakao.com/?q={row['address']}"
        st.markdown(f"[🗺️ 카카오지도에서 길찾기]({kakao_link})", unsafe_al)
