
import pandas as pd
import streamlit as st

st.title('小小的展示系統')
st.subheader('台電你還好嗎？')

# read data
data = pd.read_csv(
    './Dataset/台灣電力公司_過去電力供需資訊_20210514.csv')
data['日期'] = pd.to_datetime(
    data['日期'], 
    format='%Y%m%d').dt.date
data.set_index('日期', inplace=True)

# show data
st.markdown('---')
st.write(data)

# plot
st.markdown('---')
st.line_chart(data[['工業用電(百萬度)', '民生用電(百萬度)']])

# prediction
do_btn = st.button('預測！')
if do_btn:
    # do something...
    st.write('## 嘿嘿不告訴你 (>.^)')
