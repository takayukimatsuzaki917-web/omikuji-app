import streamlit as st
from datetime import date
from omikuji import draw_omikuji, get_omikuji_results, get_kingen

st.set_page_config(
    page_title="おみくじ",
    page_icon="🎋",
    layout="centered",
)

st.markdown("""
<style>
    /* 全体 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 480px;
    }

    /* タイトル */
    .omikuji-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        color: #8B0000;
        margin-bottom: 0.2rem;
        letter-spacing: 0.15em;
    }

    .omikuji-date {
        text-align: center;
        color: #888;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }

    /* 結果ボックス */
    .result-box {
        text-align: center;
        padding: 2.5rem 1rem;
        border-radius: 18px;
        margin: 1.5rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.18);
        animation: fadeIn 0.6s ease;
    }

    .result-label {
        font-size: 1.1rem;
        margin-bottom: 0.4rem;
        opacity: 0.85;
    }

    .result-text {
        font-size: 4.5rem;
        font-weight: bold;
        margin: 0;
        line-height: 1.1;
    }

    /* 金言ボックス */
    .kingen-box {
        background: #FFFBEA;
        border-left: 5px solid #DAA520;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0 1.5rem 0;
        animation: fadeIn 0.8s ease;
    }

    .kingen-label {
        font-size: 0.85rem;
        color: #888;
        margin-bottom: 0.4rem;
    }

    .kingen-text {
        font-size: 1.25rem;
        font-weight: bold;
        color: #333;
        line-height: 1.6;
    }

    /* フェードインアニメーション */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ボタン */
    div.stButton > button {
        width: 100%;
        height: 3.5rem;
        font-size: 1.3rem;
        font-weight: bold;
        background-color: #8B0000;
        color: white;
        border: none;
        border-radius: 12px;
        letter-spacing: 0.1em;
        transition: background 0.2s;
    }

    div.stButton > button:hover {
        background-color: #A52020;
        color: white;
    }

    /* スマホ対応 */
    @media (max-width: 480px) {
        .result-text   { font-size: 3.5rem; }
        .omikuji-title { font-size: 2.2rem; }
        .kingen-text   { font-size: 1.1rem; }
    }
</style>
""", unsafe_allow_html=True)

RESULT_COLORS = {
    "大吉": {"bg": "#FFD700", "text": "#5C3317"},
    "中吉": {"bg": "#FF8C00", "text": "#FFFFFF"},
    "小吉": {"bg": "#3CB371", "text": "#FFFFFF"},
    "吉":   {"bg": "#1E90FF", "text": "#FFFFFF"},
    "凶":   {"bg": "#696969", "text": "#FFFFFF"},
}


def main():
    st.markdown('<div class="omikuji-title">🎋 おみくじ 🎋</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="omikuji-date">{date.today().strftime("%Y年%m月%d日")}</div>',
        unsafe_allow_html=True,
    )
    st.divider()

    if "result" not in st.session_state:
        st.session_state.result = None
        st.session_state.kingen = None

    if st.session_state.result is None:
        # おみくじを引く前
        st.markdown(
            "<p style='text-align:center; color:#555; font-size:1.05rem;'>"
            "ボタンを押しておみくじを引いてください</p>",
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            if st.button("おみくじを引く", use_container_width=True):
                result = draw_omikuji(get_omikuji_results())
                st.session_state.result = result
                st.session_state.kingen = get_kingen(result)
                st.rerun()
    else:
        # 結果表示
        result = st.session_state.result
        kingen = st.session_state.kingen
        colors = RESULT_COLORS.get(result, {"bg": "#808080", "text": "#FFFFFF"})

        st.markdown(f"""
        <div class="result-box" style="background:{colors['bg']};">
            <p class="result-label" style="color:{colors['text']};">あなたの運勢は</p>
            <p class="result-text"  style="color:{colors['text']};">{result}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="kingen-box">
            <p class="kingen-label">📜 本日の金言</p>
            <p class="kingen-text">「{kingen}」</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            if st.button("もう一度引く", use_container_width=True):
                st.session_state.result = None
                st.session_state.kingen = None
                st.rerun()


if __name__ == "__main__":
    main()
