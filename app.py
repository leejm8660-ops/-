import random
import streamlit as st

YORUSHIKA_SONGS = [
    {"title": "말해줘. (言って。)", "album": "여름풀이 방해를 해 (夏草が邪魔をする)", "link": "https://www.youtube.com/watch?v=F64yFFnZfkI"},
    {"title": "구름과 유령 (雲と幽霊)", "album": "여름풀이 방해를 해 (夏草が邪魔をする)", "link": "https://www.youtube.com/watch?v=130N_Rsk4qM"},
    {"title": "히치콕 (ヒッチコック)", "album": "패배자에게 앵콜은 필요없어 (負け犬にアンコールはいらない)", "link": "https://www.youtube.com/watch?v=t7MBzHJgPjU"},
    {"title": "그저 네게 맑아라 (ただ君に晴れ)", "album": "패배자에게 앵콜은 필요없어 (負け犬にアンコールはいらない)", "link": "https://www.youtube.com/watch?v=-VKIqrvVOpo"},
    {"title": "준투명 비가 (準透明哀歌)", "album": "패배자에게 앵콜은 필요없어 (負け犬にアンコールはいらない)", "link": "https://www.youtube.com/watch?v=9L9A2Rst8fE"},
    {"title": "그래서 나는 음악을 그만두었다 (だから僕は音楽を辞めた)", "album": "그래서 나는 음악을 그만두었다 (だから僕は音楽を辞めた)", "link": "https://www.youtube.com/watch?v=KTZ-y85Erus"},
    {"title": "아이니죠 / 청람 (藍二乗)", "album": "그래서 나는 음악을 그만두었다 (だから僕は音楽を辞めた)", "link": "https://www.youtube.com/watch?v=4MoRLTAJY_o"},
    {"title": "비와 카푸치노 (雨とカプチーノ)", "album": "엘마 (エルマ)", "link": "https://www.youtube.com/watch?v=PWbRleMGagU"},
    {"title": "노틸러스 (ノーチラス)", "album": "엘마 (エルマ)", "link": "https://www.youtube.com/watch?v=j83OVv6xWyo"},
    {"title": "꽃에 망령 (花に亡霊)", "album": "도작 (盗作)", "link": "https://www.youtube.com/watch?v=SW1FlutagE8"},
    {"title": "봄도둑 (春泥棒)", "album": "도작 (盗作)", "link": "https://www.youtube.com/watch?v=Sw1FlutagE8"},
    {"title": "사상범 (思想犯)", "album": "도작 (盗作)", "link": "https://www.youtube.com/watch?v=ENcnYh79dUY"},
    {"title": "좌우맹 (左右盲)", "album": "환등 (幻燈)", "link": "https://www.youtube.com/watch?v=4d0kG4m2J6U"},
    {"title": "사양 (斜陽)", "album": "사양 (斜陽)", "link": "https://www.youtube.com/watch?v=3aRz80x2p8Q"},
    {"title": "달에 붙잡힌 야수 (月に吠える)", "album": "환등 (幻燈)", "link": "https://www.youtube.com/watch?v=dFbe2k1C7oU"},
    {"title": "알고르 (アルジャーノン)", "album": "알저넌 (アルジャーノン)", "link": "https://www.youtube.com/watch?v=Le1Lq_b8nUQ"}
]

st.set_page_config(page_title="요루시카 노래 추천기", page_icon="🎧")

st.title("🎧 요루시카 노래 추천기")
st.write("버튼을 누르면 대표 곡 중에서 무작위로 1곡을 추천해 드립니다.")
st.divider()

if st.button("🎲 오늘 들을 요루시카 노래 뽑기", use_container_width=True):
    total_count = len(YORUSHIKA_SONGS)
    random_idx = random.randint(0, total_count - 1)
    song = YORUSHIKA_SONGS[random_idx]
    
    st.success("오늘의 추천 곡이 도착했습니다!")
    st.subheader(f"🎵 {song['title']}")
    st.write(f"💿 **수록 앨범:** {song['album']}")
    st.link_button("▶️ YouTube에서 감상하기", song['link'])
