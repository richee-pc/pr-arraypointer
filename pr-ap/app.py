import streamlit as st
import os

# 웹 페이지 HTML 파일의 경로 설정
# 이 파이썬 파일과 lesson_page.html 파일이 같은 폴더에 있다고 가정합니다.
# 만약 HTML 파일 이름이 다르다면 아래 이름을 수정해주세요.
WEB_PAGE_FILE_NAME = "index.html"

# HTML 파일의 전체 경로를 구성합니다.
html_file_path = os.path.join(os.path.dirname(__file__), WEB_PAGE_FILE_NAME)

# Streamlit 앱의 제목 설정
st.set_page_config(
    page_title="C 언어 배열과 포인터 수업 📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML 파일이 존재하는지 확인
if not os.path.exists(html_file_path):
    st.error(f"오류: '{WEB_PAGE_FILE_NAME}' 파일을 찾을 수 없습니다.")
    st.markdown(f"'{WEB_PAGE_FILE_NAME}' 파일이 이 파이썬 스크립트와 같은 폴더에 있는지 확인해주세요.")
else:
    # HTML 파일 내용을 읽어옵니다.
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Streamlit에 HTML 내용을 렌더링합니다.
        # unsafe_allow_html=True 를 사용하여 HTML 태그를 직접 렌더링할 수 있도록 허용합니다.
        st.components.v1.html(html_content, height=2000, scrolling=True) # 적절한 높이와 스크롤 설정

    except Exception as e:
        st.error(f"HTML 파일을 읽거나 렌더링하는 중 오류가 발생했습니다: {e}")

# Footer (선택 사항)
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1E90FF; /* Tailwind blue-600 */
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 0.9em;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
    }
    </style>
    <div class="footer">
        <p>&copy; 2025 C 언어 프로그래밍 수업 자료. 여러분의 프로그래밍 여정을 응원합니다! 🎉</p>
    </div>
    """, unsafe_allow_html=True)
