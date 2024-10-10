import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday Thạch Thảo", page_icon="🎂")

if "celebrated" not in st.session_state:
    st.session_state.celebrated = False


def celebrate():
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFAF0;
        }
        .title {
            font-size: 50px;
            color: #ff69b4;
            font-weight: bold;
            font-family: 'Comic Sans MS', cursive;
        }
        .subtitle {
            font-size: 30px;
            color: #ff1493;
            font-family: 'Comic Sans MS', cursive;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h1 class="title">🎂Happy Birthday 3T🎉</h1>',
        unsafe_allow_html=True,
    )

    img_paths = [
        "z5917634808627_855868aec4f5527bfd43c71602aef550.jpg",
        "z5917634810726_3276092a14c311245c4e358331f10f37.jpg",
        "z5917635400453_fc6bd584218c27b643311d4a6e34a347.jpg",
    ]

    cols = st.columns(3)
    for i, img in enumerate(img_paths):
        with cols[i]:
            st.image(img, width=250)
            time.sleep(1)

    components.html(
        """
        <iframe width="0" height="0" src="https://www.youtube.com/embed/-DRSruRMZ8o?autoplay=1&loop=1&playlist=-DRSruRMZ8o" 
        frameborder="0" allow="autoplay"></iframe>
        """,
        height=0,
    )
    st.balloons()


if not st.session_state.celebrated:
    st.title("Đoán xem có gì nào 😉")
    if st.button("Click 🖱️!"):
        st.session_state.celebrated = True

if st.session_state.celebrated:
    celebrate()
