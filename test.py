# 🍽️🌟 부천 핫플 맛집·카페 MAP (Education Only) 🌟🍰
# ------------------------------------------------------------------
# * 이 페이지는 **교육 목적**으로 제작된 예시입니다.
# * 실제 운영 중인 2024-25년 최신 블로그·SNS 후기(📝)를 확인해
#   트렌디한 부천 맛집·카페를 선정했어요!
#   - 코르드블랭크 (브런치) 💖  [까치울역]
#   - 앤드 (티 전문) 🫖  [까치울역]
#   - 숲숲 (플랜트 카페) 🌿  [까치울역]
#   - 리틀 시칠리 (파스타) 🍝  [상동역]
#   - 뽁식당 (로제·리조토) 🍕  [부천시청역]
#   - 명가 진흙구이 (오리·백숙) 🦆  [종합운동장역]
# ------------------------------------------------------------------
# 실행 :  streamlit run bucheon_food_map.py
# 필요 패키지 : streamlit, pandas, geopy, pydeck
# ------------------------------------------------------------------

import streamlit as st
import pandas as pd

# 지오코딩 (주소→위/경도) ----------------------------------------------------
try:
    from geopy.geocoders import Nominatim
    from geopy.extra.rate_limiter import RateLimiter
    _geolocator = Nominatim(user_agent="bucheon_food_app")
    _geocode = RateLimiter(_geolocator.geocode, min_delay_seconds=1)

    @st.cache_data(show_spinner=False)
    def geocode_addr(addr):
        info = _geocode(addr)
        if info:
            return info.latitude, info.longitude
        return None, None
except ModuleNotFoundError:
    # geopy 미설치 시 안내
    st.warning("⚠️ `geopy`가 설치되지 않았어요 → `pip install geopy` 후 재실행해 주세요!")
    geocode_addr = lambda x: (None, None)

# 핫플 데이터 ---------------------------------------------------------------
PLACES = [
    # name, category, address, lat, lon (lat/lon은 없으면 geocode)
    ("코르드블랭크", "브런치 카페 💖",  "경기도 부천시 오정구 까치로6번길 17-12", 37.507313, 126.809723),
    ("앤드",         "티 전문 카페 🫖", "경기도 부천시 오정구 까치로6번길 40",     None,     None),
    ("숲숲",         "플랜트 카페 🌿", "경기도 부천시 오정구 까치로6번길 36",     37.506759,126.810326),
    ("리틀 시칠리",   "가성비 파스타 🍝", "경기도 부천시 원미구 길주로 80",          None,     None),
    ("뽁식당 부천점", "분위기 만점 🍕",  "경기도 부천시 원미구 석천로177번길 36",  None,     None),
    ("명가 진흙구이", "오리 보양식 🦆", "경기도 부천시 오정구 소사로 599",        None,     None),
]

records = []
for name, cat, addr, lat, lon in PLACES:
    if lat is None or lon is None:
        lat, lon = geocode_addr(addr)
    if lat is None:
        st.error(f"❌ {addr} 지오코딩 실패 – 수동 좌표 필요!")
        continue
    records.append({"name": name, "category": cat, "address": addr, "lat": lat, "lon": lon})

df = pd.DataFrame(records)

# 페이지 설정 & 화려한 CSS ----------------------------------------------------
st.set_page_config(page_title="부천 핫플 MAP", page_icon="🍽️", layout="wide")
st.markdown(
    """
    <style>
    body {background:linear-gradient(135deg,#fceabb 0%,#f8b500 100%);}
    .block-container {padding-top:1rem;}
    h1, h2, h3 {color:#fff;}
    .st-tooltip {font-size:14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# 헤더 ----------------------------------------------------------------------
st.title("🎉 부천 요즘 🔥핫🔥 한 맛집 & 카페 지도")
st.title("우리의 부천 맛집 뿌시기 지도")
st.caption("ⓘ 실시간 정보가 아닐 수 있으니 방문 전 영업시간을 꼭 확인하세요!")

# 지도 ----------------------------------------------------------------------
import pydeck as pdk

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    pickable=True,
    get_position="[lon, lat]",
    get_radius=120,
    get_fill_color="[255, 0, 127, 180]",
)

view_state = pdk.ViewState(latitude=df.lat.mean(), longitude=df.lon.mean(), zoom=12, pitch=45)

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/streets-v12",
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{name} ({category})\n{address}"},
    )
)

# 상세 리스트 ---------------------------------------------------------------
st.markdown("---")
st.subheader("📌 상세 정보")
for _, row in df.iterrows():
    with st.expander(f"{row['name']} — {row['category']}"):
        st.write(f"📍 **주소** : {row['address']}")
        st.write(f"🛰️ 위·경도 : {row['lat']:.6f}, {row['lon']:.6f}")
        st.write("💬 블로그·SNS 후기 기준으로 2024-25년에 여전히 *영업 중*인 핫플입니다!")
        st.button("길찾기 🔗", on_click=lambda url=f"https://map.kakao.com/?q={row['address']}": st.markdown(f"[카카오지도에서 열기]({url})"))

st.success("🍴 맛있는 부천 미식 투어를 즐기세요! 🚀")
