import streamlit as st
import mymodel as m
st.sidebar.write("""# Weather Model
This app is fitting different regression models to perform weather forecasting. 
""")
k = st.slider("range",0,40,30)
st.write(m.run(k))