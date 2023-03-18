# my-first-streamlit-app
import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
st.write('Phương trình có dạng: ax + b = 0', color = 'blue')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a == 0:
    if b == 0:
      st.write('Phương trình có vô số nghiệm')
    if b != 0:
      st.write('Phương trình vô nghiệm')
  if a != 0:
    st.write('Phương trình có nghiệm là', -b/a)

