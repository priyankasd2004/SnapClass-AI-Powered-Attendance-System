import streamlit as st 
from pathlib import Path
import base64
from pathlib import Path


def header_home():
    
    logo_path = Path(__file__).parent.parent / "static" / "logo.png"
    st.image(logo_path, width=100)

    st.markdown(f"""
    <div style='display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px ; margin-top:10px'>
    <h1 style='text-align:center; color:#E0E3FF'>Snap <br> Class</h1>
    </div>
    
      

      """,unsafe_allow_html=True
    )




def header_dashboard():

    logo_path = Path(__file__).parent.parent / "static" / "logo.png"
    
    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center; gap:10px">
    <img src="data:image/png;base64,{base64.b64encode(logo_path.read_bytes()).decode()}"style="width:85px; height:auto;">
    <h2 style='text-align:left; color:#5865F2'>SNAP<br/>CLASS</h1>
    </div>   
                
                """, unsafe_allow_html=True)