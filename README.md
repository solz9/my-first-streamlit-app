# my-first-streamlit-app
pip install streamlit
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('tham số a')
b = st.number_input('tham số b')
if st.button('Gỉai'):
  if a == 0:
    if b == 0:
      print('vô số nghiệm')
    if b != 0:
      print('vô nghiệm')
  if a != 0:
    print('Phương trình có nghiệm là', -b/a)
!streamlit run app.py & npx localtunnel --port 8501
