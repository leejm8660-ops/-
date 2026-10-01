import random
import streamlit as st
import urllib.parse

st.set_page_config(page_title="요루시카 노래 추천기", page_icon="🎧")

st.title("🎧 요루시카 노래 추천기")
st.write("버튼을 누르면 요루시카의 전체 곡 목록 중에서 무작위로 1곡을 추천해 드립니다.")
st.divider()

# 요루시카 Discography 전체 트랙 목록
YORUSHIKA_SONGS = [
    # 夏草が邪魔をする (여름풀이 방해를 해)
    {"title": "夏草が邪魔をする (여름풀이 방해를 해)", "album": "夏草が邪魔をする"},
    {"title": "カトレア (카틀레야)", "album": "夏草が邪魔をする"},
    {"title": "言っ。 (말해줘.)", "album": "夏草が邪魔をする"},
    {"title": "あの夏に咲け (그 여름에 피어라)", "album": "夏草が邪魔をする"},
    {"title": "飛行 (비행)", "album": "夏草が邪魔をする"},
    {"title": "靴のの花火 (신발의 불꽃)", "album": "夏草が邪魔をする"},
    {"title": "雲と幽霊 (구름과 유령)", "album": "夏草が邪魔をする"},

    # 負け犬にアンコールはいらない (패배자에게 앵콜은 필요없어)
    {"title": "前世 (전세)", "album": "負け犬にアンコールはいらない"},
    {"title": "負け犬にアンコールはいらない (패배자에게 앵콜은 필요없어)", "album": "負け犬にアンコールはいらない"},
    {"title": "ヒッチコック (히치콕)", "album": "負け犬にアンコールはいらない"},
    {"title": "落下 (낙하)", "album": "負け犬にアンコールはいらない"},
    {"title": "準透明哀歌 (준투명비가)", "album": "負け犬にアンコールはいらない"},
    {"title": "ただ君に晴れ (그저 네게 맑아라)", "album": "負け犬にアンコールはいらない"},
    {"title": "B-Side (B면)", "album": "負け犬にアンコールはいらない"},
    {"title": "思想犯 (사상범)", "album": "負け犬にアンコールはいらない"},
    {"title": "冬眠 (동면)", "album": "負け犬にアンコールはいらない"},

    # だから僕は音楽を辞めた (그래서 나는 음악을 그만두었다)
    {"title": "8/31", "album": "だから僕は音楽を辞めた"},
    {"title": "藍二乗 (청람 / 아이니죠)", "album": "だから僕は音楽を辞めた"},
    {"title": "八月、某、月明かり (8월, 어느 날, 달빛)", "album": "だから僕は音楽を辞めた"},
    {"title": "詩書きと男 (시인과 남자)", "album": "だから僕は音楽を辞めた"},
    {"title": "夕凪、某、花惑い (해질녘, 어느 날, 꽃에 홀림)", "album": "だから僕は音楽を辞めた"},
    {"title": "踊ろうぜ (춤추자)", "album": "だから僕は音楽を辞めた"},
    {"title": "パレード (퍼레이드)", "album": "だから僕は音楽を辞めた"},
    {"title": "エルマ (엘마)", "album": "だから僕は音楽を辞めた"},
    {"title": "だから僕は音楽を辞めた (그래서 나는 음악을 그만두었다)", "album": "だから僕は音楽を辞めた"},

    # エルマ (엘마)
    {"title": "車窓 (차창)", "album": "エルマ"},
    {"title": "憂一乗 (우일승)", "album": "エルマ"},
    {"title": "夕畳 (저녁 다다미)", "album": "エルマ"},
    {"title": "雨とカプチーノ (비와 카푸치노)", "album": "エルマ"},
    {"title": "湖の街 (호수의 거리)", "album": "エルマ"},
    {"title": "神様のダンス (신들의 춤)", "album": "エルマ"},
    {"title": "雨晴れ (비 갠 뒤)", "album": "エルマ"},
    {"title": "歩く (걷다)", "album": "エルマ"},
    {"title": "心に穴が空いた (마음에 구멍이 뚫렸다)", "album": "エルマ"},
    {"title": "ノーチラス (노틸러스)", "album": "エルマ"},

    # 盗作 (도작)
    {"title": "盗作 (도작)", "album": "盗作"},
    {"title": "思想犯 (사상범)", "album": "盗作"},
    {"title": "昼鳶 (낮개구리)", "album": "盗作"},
    {"title": "春ひさぎ (매춘)", "album": "盗作"},
    {"title": "月光 (월광)", "album": "盗作"},
    {"title": "花に亡霊 (꽃에 망령)", "album": "盗作"},
    {"title": "爆弾魔 (폭탄마)", "album": "盗作"},
    {"title": "レプリカント (복제인간)", "album": "盗作"},
    {"title": "逃亡 (도망)", "album": "盗作"},
    {"title": "夜行 (야행)", "album": "盗作"},
    {"title": "花人局 (꽃사기)", "album": "盗作"},

    # 幻燈 (환등) 및 싱글
    {"title": "又三郎 (마타사부로)", "album": "幻燈"},
    {"title": "老人と海 (노인과 바다)", "album": "幻燈"},
    {"title": "月に吠える (달에 짖다)", "album": "幻燈"},
    {"title": "ブレーメン (브레멘)", "album": "幻燈"},
    {"title": "左右盲 (좌우맹)", "album": "幻燈"},
    {"title": "チノカテ (치노카테)", "album": "幻燈"},
    {"title": "アルジャーノン (알저넌)", "album": "アルジャーノン"},
    {"title": "斜陽 (사양)", "album": "斜陽"},
    {"title": "都落ち (Capital Departure)", "album": "都落ち"},
    {"title": "晴る (봄 / Haru)", "album": "晴る"},
    {"title": "ルバート (Rubato)", "album": "ルバート"}
]

if st.button("🎲 오늘 들을 요루시카 노래 뽑기", use_container_width=True):
    song = random.choice(YORUSHIKA_SONGS)
    
    st.success("오늘의 추천 곡이 도착했습니다!")
    st.subheader(f"🎵 {song['title']}")
    st.write(f"💿 **수록 앨범:** {song['album']}")
    
    # 스포티파이 검색 URL (일본어/한국어 제목 검색 최적화)
    spotify_query = urllib.parse.quote(f"Yorushika {song['title'].split(' (')[0]}")
    spotify_url = f"https://open.spotify.com/search/{spotify_query}"
    
    st.link_button("🟢 Spotify에서 검색 및 감상하기", spotify_url)
