import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Select an option',
    ('Medal Taly', 'Overal Analysis', 'Country-wise Analysis', 'Athlete wise Analysi')
)