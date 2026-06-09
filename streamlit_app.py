import streamlit as st

st.set_page_config(page_title="게임 사양 가이드", page_icon="🎮", layout="centered")

# 깔끔하게 정리한 6개 게임 데이터
game_specs = {
    "리그 오브 레전드": {
        "min": {"CPU": "Intel i3-530", "RAM": "2GB", "GPU": "GT 9600", "Storage": "16GB HDD"},
        "rec": {"CPU": "Intel i5-3300", "RAM": "4GB", "GPU": "GTX 560", "Storage": "16GB SSD"}
    },
    "발로란트": {
        "min": {"CPU": "Core 2 Duo", "RAM": "4GB", "GPU": "Intel HD 4000", "Storage": "30GB HDD"},
        "rec": {"CPU": "Intel i3-4150", "RAM": "4GB", "GPU": "GT 730", "Storage": "30GB SSD"}
    },
    "FC 온라인": {
        "min": {"CPU": "Intel i3-2100", "RAM": "8GB", "GPU": "GTX 460", "Storage": "50GB HDD"},
        "rec": {"CPU": "Intel i5-3550", "RAM": "8GB", "GPU": "GTX 670", "Storage": "50GB SSD"}
    },
    "로스트아크": {
        "min": {"CPU": "Intel i3", "RAM": "8GB", "GPU": "GTX 460", "Storage": "50GB HDD"},
        "rec": {"CPU": "Intel i5", "RAM": "16GB", "GPU": "RTX 2060", "Storage": "50GB SSD"}
    },
    "오버워치 2": {
        "min": {"CPU": "Intel i3", "RAM": "6GB", "GPU": "GTX 600", "Storage": "50GB HDD"},
        "rec": {"CPU": "Intel i7", "RAM": "8GB", "GPU": "GTX 1060", "Storage": "50GB SSD"}
    },
    "배틀그라운드": {
        "min": {"CPU": "Intel i5-4430", "RAM": "8GB", "GPU": "GTX 960", "Storage": "40GB HDD"},
        "rec": {"CPU": "Intel i5-6600K", "RAM": "16GB", "GPU": "GTX 1060", "Storage": "40GB SSD"}
    }
}

st.title("🎮 게임별 컴퓨터 사양 가이드")
st.write("인기 게임 6종의 최소 및 권장 사양을 확인할 수 있습니다.")
st.markdown("---")

# 게임 선택 드롭다운
selected_game = st.selectbox("사양을 확인할 게임을 선택하세요 👇", list(game_specs.keys()))
spec = game_specs[selected_game]

st.subheader(f"🔍 {selected_game} 요구 사양")

# 최소 / 권장 사양 탭
tab1, tab2 = st.tabs(["📉 최소 사양", "📈 권장 사양"])

with tab1:
    st.table({"하드웨어 부품": list(spec["min"].keys()), "요구 조건": list(spec["min"].values())})

with tab2:
    st.table({"하드웨어 부품": list(spec["rec"].keys()), "요구 조건": list(spec["rec"].values())})

st.markdown("---")
st.info("💡 팁: 원활한 플레이와 빠른 로딩을 위해 게임은 HDD보다 SSD에 설치하는 것이 좋습니다.")