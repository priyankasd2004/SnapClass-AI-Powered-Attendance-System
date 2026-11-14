import streamlit as st

from supabase import create_client, Client

supabase: Client = create_client(
    st.secrets["SUPBASE_URL"],
    st.secrets["SUPBASE_KEY"]
)
