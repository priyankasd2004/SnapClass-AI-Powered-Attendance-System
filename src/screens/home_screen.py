import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_home
from pathlib import Path



def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    student_path = Path(__file__).parent.parent / "static" / "student.png"
    teacher_path = Path(__file__).parent.parent / "static" / "teacher.png"


    col1,col2 = st.columns(2,gap="large")

    with col1:
        st.markdown(
        "<h3 style='text-align:center; font-family:'Outfit',sans-serif;'>I am Student</h3>",
        unsafe_allow_html=True
        )
        st.image(student_path, width=200)
        if st.button('Teacher Portal', type="primary" , icon=':material/arrow_outward:', icon_position="right"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()


    with col2:
        st.markdown(
        "<h3 style='text-align:center; font-family:'Outfit',sans-serif;'>I am Teacher</h3>",
        unsafe_allow_html=True
        )
        st.image(teacher_path, width=200)
        if st.button('Student Portal', type="primary" , icon=':material/arrow_outward:',icon_position="right"):
            st.session_state['login_type'] = 'student'
            st.rerun()

    footer_home()
    
