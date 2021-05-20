import streamlit as st

import streamlit.components.v1 as components  
# Import Streamlit

# Render the h1 block, contained in a frame of size 200x200.
#components.html("<html><body><h1>Hello, World</h1></body></html>", width=200, height=200)

# Import the wrapper function from your package
from streamlit_custom_slider import st_custom_slider
st.title("Testing Streamlit custom components")
st_custom_slider()
st.markdown("Streamlit Markdown")
