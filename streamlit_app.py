import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="게임별 맞춤 컴퓨터 사양 가이드 PRO",
    page_icon="🎮",
    layout="centered"
)

# 확장된 게임 사양 데이터 (총 10종)
game_specs = {
    "리그 오브 레전드 (League of Legends)": {
        "genre": "MOBA / AOS (저사양)",
        "min": {
            "CPU": "Intel Core i3-530 / AMD A6-3650",
            "RAM": "2 GB",
            "GPU": "NVIDIA GeForce 9600GT / AMD HD 6570",
            "Storage": "16 GB HDD 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel Core i5-3300 / AMD Ryzen 3 1200",
            "RAM": "4 GB",
            "GPU": "NVIDIA GeForce GTX 560 / AMD Radeon HD 6950",
            "Storage": "16 GB SSD 권장",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "발로란트 (Valorant)": {
        "genre": "FPS / 전술 슈팅 (저사양)",
        "min": {
            "CPU": "Intel Core 2 Duo E8400 / AMD Athlon 200GE",
            "RAM": "4 GB",
            "GPU": "Intel HD 4000 / AMD Radeon R5 200",
            "Storage": "30 GB 이상",
            "OS": "Windows 10 (Build 19041+) 64-bit"
        },
        "rec": {
            "CPU": "Intel i3-4150 / AMD Ryzen 3 1200",
            "RAM": "4 GB",
            "GPU": "NVIDIA GeForce GT 730 / AMD Radeon R7 240",
            "Storage": "30 GB SSD 권장",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "FC 온라인 (FC Online)": {
        "genre": "스포츠 / 축구",
        "min": {
            "CPU": "Intel Core i3-2100 / AMD Phenom II X4 965",
            "RAM": "8 GB",
            "GPU": "NVIDIA GeForce GTX 460 / AMD Radeon HD 6870",
            "Storage": "50 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel Core i5-3550 / AMD FX-6350",
            "RAM": "8 GB",
            "GPU": "NVIDIA GeForce GTX 670 / AMD Radeon R9 270X",
            "Storage": "50 GB SSD 권장",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "로스트아크 (Lost Ark)": {
        "genre": "쿼터뷰 MMORPG",
        "min": {
            "CPU": "Intel Core i3 / AMD Ryzen 3",
            "RAM": "8 GB",
            "GPU": "NVIDIA GeForce GTX 460 / AMD Radeon HD 6850",
            "Storage": "50 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel Core i5 / AMD Ryzen 5",
            "RAM": "16 GB",
            "GPU": "NVIDIA RTX 2060 / AMD Radeon RX 5600 XT (1440p 기준)",
            "Storage": "50 GB SSD 필수",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "오버워치 2 (Overwatch 2)": {
        "genre": "팀 기반 하이퍼 슈팅",
        "min": {
            "CPU": "Intel Core i3 / AMD Phenom X3 8650",
            "RAM": "6 GB",
            "GPU": "NVIDIA GeForce GTX 600 series / AMD Radeon HD 7000 series",
            "Storage": "50 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel Core i7 / AMD Ryzen 5",
            "RAM": "8 GB",
            "GPU": "NVIDIA GeForce GTX 1060 / AMD Radeon RX 6400",
            "Storage": "50 GB SSD 권장",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "배틀그라운드 (PUBG)": {
        "genre": "배틀로얄 FPS (중고사양)",
        "min": {
            "CPU": "Intel Core i5-4430 / AMD FX-6300",
            "RAM": "8 GB",
            "GPU": "NVIDIA GeForce GTX 960 2GB / AMD Radeon R7 370 2GB",
            "Storage": "40 GB 이상",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel Core i5-6600K / AMD Ryzen 5 1600",
            "RAM": "16 GB",
            "GPU": "NVIDIA GeForce GTX 1060 3GB / AMD Radeon RX 580 4GB",
            "Storage": "40 GB SSD 권장",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "팰월드 (Palworld)": {
        "genre": "오픈월드 서바이벌 제작 (중고사양)",
        "min": {
            "CPU": "Intel Core i5-3570K 3.4GHz",
            "RAM": "16 GB",
            "GPU": "NVIDIA GeForce GTX 1050 2GB",
            "Storage": "40 GB SSD 필수",
            "OS": "Windows 10 (64-bit)"
        },
        "rec": {
            "CPU": "Intel Core i9-9900K 3.6GHz",
            "RAM": "32 GB",
            "GPU": "NVIDIA GeForce RTX 2070",
            "Storage": "40 GB SSD 필수",
            "OS": "Windows 10 / 11 (64-bit)"
        }
    },
    "사이버펑크 2077 (Cyberpunk 2077)": {
        "genre": "오픈월드 액션 RPG (고사양)",
        "min": {
            "CPU": "Intel Core i7-6700 / AMD Ryzen 5 1600",
            "RAM": "12 GB",
            "GPU": "