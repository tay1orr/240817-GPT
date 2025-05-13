# 📚✨ MBTI 분야·직업 추천 웹앱 (Educational Purpose Only) ✨📚
# ----------------------------------------------------------
# 이 앱은 교육 목적으로 제작되었습니다. 재미와 학습용으로만 사용해 주세요!
# Streamlit으로 실행:  `streamlit run mbti_app.py`
# ----------------------------------------------------------

import streamlit as st

# ------------------ 페이지 설정 ------------------ #
st.set_page_config(
    page_title="MBTI 전공·직업 추천 🌈",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------ 맞춤형 CSS ------------------ #
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffcc70 0%, #ff8177 100%);
        color: #ffffff;
        font-family: 'NanumSquare', sans-serif;
    }
    .stButton > button {
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
        transition: 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------ 타이틀 ------------------ #
st.title("🔮 MBTI로 알아보는 전공 & 커리어 추천 🎓💼")
st.caption("**이 사이트는 교육 목적(Educational purpose)으로 제작되었습니다.** 🏫")

st.markdown("### 🌟 당신에게 딱 맞는 진로를 찾아볼까요?")

# ------------------ MBTI 데이터 ------------------ #
MBTI_RECOMMENDATIONS = {
    "INTJ": {
        "majors": ["컴퓨터공학 💻", "데이터사이언스 📊", "전기·전자공학 ⚡️", "산업공학 🏗️"],
        "jobs": ["AI 연구원 🤖", "데이터 사이언티스트 📈", "시스템 엔지니어 🛠️"],
    },
    "INTP": {
        "majors": ["물리학 🔬", "수학 📐", "컴퓨터공학 💻"],
        "jobs": ["연구개발 엔지니어 ⚙️", "빅데이터 분석가 📊", "기술 컨설턴트 🧩"],
    },
    "ENTJ": {
        "majors": ["경영학 🏢", "경제학 💹", "법학 ⚖️"],
        "jobs": ["전략 컨설턴트 🗺️", "프로덕트 매니저 📦", "창업가 🚀"],
    },
    "ENTP": {
        "majors": ["산업디자인 🎨", "마케팅 📢", "미디어커뮤니케이션 📺"],
        "jobs": ["스타트업 창업가 🚀", "크리에이티브 디렉터 🎬", "상품기획자 🧠"],
    },
    "INFJ": {
        "majors": ["심리학 🧠", "교육학 🍎", "사회복지학 🤝"],
        "jobs": ["상담사 💬", "콘텐츠 작가 ✍️", "사회복지사 🫶"],
    },
    "INFP": {
        "majors": ["문예창작학 📚", "시각디자인 🎨", "언론정보학 📰"],
        "jobs": ["작가 ✍️", "UX/UI 디자이너 🖌️", "콘텐츠 크리에이터 🎥"],
    },
    "ENFJ": {
        "majors": ["교육학 🍎", "커뮤니케이션학 📡", "국제관계학 🌍"],
        "jobs": ["교육컨설턴트 🎓", "홍보·PR 전문가 📣", "비영리단체 활동가 🌱"],
    },
    "ENFP": {
        "majors": ["광고홍보학 📺", "문화예술경영 🎭", "관광학 ✈️"],
        "jobs": ["브랜드 매니저 🪄", "이벤트 플래너 🎉", "여행 콘텐츠 제작자 🌏"],
    },
    "ISTJ": {
        "majors": ["회계학 🧾", "행정학 🏛️", "법학 ⚖️"],
        "jobs": ["공무원 🏢", "회계사 🧮", "품질관리 전문가 ✅"],
    },
    "ISFJ": {
        "majors": ["간호학 🩺", "아동학 🧸", "도서관학 📚"],
        "jobs": ["간호사 🏥", "보건교사 🏫", "사서 📖"],
    },
    "ESTJ": {
        "majors": ["경영학 🏢", "토목공학 🛤️", "군사학 🪖"],
        "jobs": ["프로젝트 매니저 📋", "군장교 🎖️", "생산 관리자 🏭"],
    },
    "ESFJ": {
        "majors": ["호텔관광학 🏨", "식품영양학 🥗", "교육학 🍎"],
        "jobs": ["호텔리어 🛎️", "영양사 🍱", "학교 행정가 📑"],
    },
    "ISTP": {
        "majors": ["기계공학 🛠️", "항공우주공학 🚀", "해양학 🌊"],
        "jobs": ["항공整備사 ✈️", "게임 개발자 🎮", "스포츠 트레이너 🏋️‍♂️"],
    },
    "ISFP": {
        "majors": ["미술학 🎨", "패션디자인 👗", "조경학 🌳"],
        "jobs": ["그래픽 디자이너 🖍️", "플로리스트 💐", "포토그래퍼 📷"],
    },
    "ESTP": {
        "majors": ["스포츠과학 🏃‍♂️", "국제무역학 🌐", "광고홍보학 📢"],
        "jobs": ["세일즈 매니저 💼", "스포츠 에이전트 ⚽️", "응급구조사 🚑"],
    },
    "ESFP": {
        "majors": ["공연예술학 🎭", "방송연예학 🎤", "이벤트경영학 🎉"],
        "jobs": ["MC / 쇼호스트 🎙️", "배우 🎬", "SNS 인플루언서 📱"],
    },
}

mbti_types = list(MBTI_RECOMMENDATIONS.keys())

# ------------------ 사용자 입력 ------------------ #
st.sidebar.header("🧩 MBTI 선택")
user_mbti = st.sidebar.selectbox("당신의 MBTI를 선택하세요 👇", options=mbti_types, index=mbti_types.index("INTJ"))

# ------------------ 결과 출력 ------------------ #
if user_mbti:
    rec = MBTI_RECOMMENDATIONS.get(user_mbti, {})
    
    st.markdown(f"## 🌈 **{user_mbti}** 유형에게 추천하는 학과 분야")
    for major in rec.get("majors", []):
        st.write(f"🔸 {major}")
    
    st.markdown("---")
    
    st.markdown(f"## 🚀 **{user_mbti}** 유형에게 어울리는 직업")
    for job in rec.get("jobs", []):
        st.write(f"⭐ {job}")
    
    st.success("당신만의 길을 탐험해 보세요! ✨")
    st.balloons()

# ------------------ 추가 요소 ------------------ #
st.markdown(
    """
    ---
    **Tip:** MBTI는 절대적인 기준이 아니므로, 취향과 경험을 종합적으로 고려해 진로를 선택하세요! 🌟
    """
)
