# 🍽️🌟 부천 핫플 맛집·카페 MAP (교육용 예시) 🌟🍰
# 실행 :  streamlit run bucheon_food_map.py
# 필요 패키지 : streamlit, pandas
# -------------------------------------------------
import streamlit as st
import pandas as pd

# ✅ 페이지 설정 (반드시 가장 먼저!)
st.set_page_config(page_title="부천 핫플 MAP", page_icon="🍽️", layout="wide")

# 🎨 배경 및 기본 스타일 ------------------------------------------------------
st.markdown(
    """
    <style>
    body {background:linear-gradient(135deg,#ffe259 0%,#ffa751 100%);}
    .block-container {padding-top:1.5rem;}
    h1, h2, h3, h4 {color:#ffffff; text-shadow:1px 1px 3px rgba(0,0,0,0.3);}
    </style>
    """,
    unsafe_allow_html=True,
)

# 📝 데이터 (실제 영업 중이며 24-25년 SNS/BLOG 화제 매장) -------------------
DATA = [
    # name, category, address, lat, lon
    ("코르드블랭크", "브런치 카페 🥞", "경기도 부천시 오정구 까치로6번길 17-12",
     37.507313, 126.809723),  # :contentReference[oaicite:0]{index=0}
    ("앤드", "티 전문 카페 🍵", "경기도 부천시 오정구 까치로6번길 40",
     37.507410, 126.808624),   # 인근 7-40 좌표 사용 (까치울 카페거리) :contentReference[oaicite:1]{index=1}
    ("숲숲", "플랜트 카페 🌿", "경기도 부천시 오정구 까치로6번길 36",
     37.506759, 126.810326),   # :contentReference[oaicite:2]{index=2}
    ("리틀 시칠리", "가성비 파스타 🍝", "경기도 부천시 원미구 길주로 80",
     37.504994, 126.752435),   # :contentReference[oaicite:3]{index=3}
    ("뽁식당 부천점", "로제·리조또 🍲", "경기도 부천시 원미구 석천로177번길 36",
     37.503636, 126.761052),   # :contentReference[oaicite:4]{index=4}
    ("명가 진흙구이", "오리·백숙 🦆", "경기도 부천시 오정구 소사로 599",
     37.511505, 126.798433),   # :contentReference[oaicite:5]{index=5}
]

df = pd.DataFrame(DATA, columns=["name", "category", "address", "lat", "lon"])

# 🏷️ 헤더 -------------------------------------------------------------------
st.title("🎉 부천 요즘 🔥핫🔥 한 맛집 & 카페 지도")
st.caption("※ 본 페이지는 **교육 목적**으로 제작되었으며, 방문 전 영업시간·휴무일을 꼭 확인하세요!")

# 🗺️ 지도 (Streamlit 기본 지도 사용) ----------------------------------------
st.map(df, latitude="lat", longitude="lon", zoom=12)

# 📋 상세 정보 --------------------------------------------------------------
st.markdown("---")
st.subheader("📌 매장 리스트")

for _, row in df.iterrows():
    with st.expander(f"{row['name']} — {row['category']}"):
        st.write(f"**주소** : {row['address']}")
        st.write(f"🛰️ 위·경도 : {row['lat']:.6f}, {row['lon']:.6f}")
        kakao_link = f"https://map.kakao.com/?q={row['address']}"
        st.markdown(f"[🗺️ 카카오지도에서 길찾기]({kakao_link})", unsafe_allow_html=True)

st.success("🍴 부천 미식 투어를 즐겨 보세요! ✨")
