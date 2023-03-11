# my-first-streamlit-app
import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('tham số a')
b = st.number_input('tham số b')
if st.button('Gỉai'):
  if a == 0:
    if b == 0:
      st.write('vô số nghiệm')
    if b != 0:
      st.write('vô nghiệm')
  if a != 0:
    st.write('Phương trình có nghiệm là', -b/a)
!streamlit run app.py & npx localtunnel --port 8501
