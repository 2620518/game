import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="게임 사양 가이드",
    page_icon="🎮",
    layout="centered"
)

# 게임 사양 데이터 (오류 방지를 위해 텍스트 간소화)
game_specs = {
    "리그 오브 레전드": {
        "genre": "MOBA / AOS",
        "min": {
            "CPU": "Intel i3-530 / AMD A6-3650",
            "RAM": "2 GB",
            "GPU": "NVIDIA 9600GT / AMD HD 6570",
            "Storage": "16 GB HDD 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i5-3300 / AMD Ryzen 3 1200",
            "RAM": "4 GB",
            "GPU": "NVIDIA GTX 560 / AMD HD 6950",
            "Storage": "16 GB SSD 권장",
            "OS": "Windows 10 / 11"
        }
    },
    "발로란트": {
        "genre": "FPS / 전술 슈팅",
        "min": {
            "CPU": "Intel Core 2 Duo E8400",
            "RAM": "4 GB",
            "GPU": "Intel HD 4000",
            "Storage": "30 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i3-4150 / AMD Ryzen 3",
            "RAM": "4 GB",
            "GPU": "NVIDIA GT 730 / AMD R7 240",
            "Storage": "30 GB SSD 권장",
            "OS": "Windows 10 / 11"
        }
    },
    "FC 온라인": {
        "genre": "스포츠 / 축구",
        "min": {
            "CPU": "Intel i3-2100 / AMD Phenom II",
            "RAM": "8 GB",
            "GPU": "NVIDIA GTX 460 / AMD HD 6870",
            "Storage": "50 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i5-3550 / AMD FX-6350",
            "RAM": "8 GB",
            "GPU": "NVIDIA GTX 670 / AMD R9 270X",
            "Storage": "50 GB SSD 권장",
            "OS": "Windows 10 / 11"
        }
    },
    "로스트아크": {
        "genre": "쿼터뷰 MMORPG",
        "min": {
            "CPU": "Intel i3 / AMD Ryzen 3",
            "RAM": "8 GB",
            "GPU": "NVIDIA GTX 460 / AMD HD 6850",
            "Storage": "50 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i5 / AMD Ryzen 5",
            "RAM": "16 GB",
            "GPU": "NVIDIA RTX 2060 / AMD RX 5600",
            "Storage": "50 GB SSD 필수",
            "OS": "Windows 10 / 11"
        }
    },
    "오버워치 2": {
        "genre": "팀 기반 하이퍼 슈팅",
        "min": {
            "CPU": "Intel i3 / AMD Phenom X3",
            "RAM": "6 GB",
            "GPU": "NVIDIA GTX 600 / AMD HD 7000",
            "Storage": "50 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i7 / AMD Ryzen 5",
            "RAM": "8 GB",
            "GPU": "NVIDIA GTX 1060 / AMD RX 6400",
            "Storage": "50 GB SSD 권장",
            "OS": "Windows 10 / 11"
        }
    },
    "배틀그라운드": {
        "genre": "배틀로얄 FPS",
        "min": {
            "CPU": "Intel i5-4430 / AMD FX-6300",
            "RAM": "8 GB",
            "GPU": "NVIDIA GTX 960 / AMD R7 370",
            "Storage": "40 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i5-6600K / AMD Ryzen 5",
            "RAM": "16 GB",
            "GPU": "NVIDIA GTX 1060 / AMD RX 580",
            "Storage": "40 GB SSD 권장",
            "OS": "Windows 10 / 11"
        }
    },
    "팰월드": {
        "genre": "오픈월드 서바이벌",
        "min": {
            "CPU": "Intel i5-3570K 3.4GHz",
            "RAM": "16 GB",
            "GPU": "NVIDIA GTX 1050 2GB",
            "Storage": "40 GB SSD 필수",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i9-9900K 3.6GHz",
            "RAM": "32 GB",
            "GPU": "NVIDIA RTX 2070",
            "Storage": "40 GB SSD 필수",
            "OS": "Windows 10 / 11"
        }
    },
    "사이버펑크 2077": {
        "genre": "오픈월드 액션 RPG",
        "min": {
            "CPU": "Intel i7-6700 / AMD Ryzen 5",
            "RAM": "12 GB",
            "GPU": "NVIDIA GTX 1060 / AMD RX 580",
            "Storage": "70 GB SSD 필수",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel i7-