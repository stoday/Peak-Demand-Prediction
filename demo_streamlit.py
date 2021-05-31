
# 
import pandas as pd
import streamlit as st

from pmdarima import auto_arima, model_selection

from sklearn.linear_model import LinearRegression

st.title('小小的展示系統')
st.subheader('台電你還好嗎？')

# read data
data = pd.read_csv('./Dataset/台灣電力公司_過去電力供需資訊_20210514.csv')
data['日期'] = pd.to_datetime(data['日期'], format='%Y%m%d').dt.date
data.set_index('日期', inplace=True)

# show data
st.markdown('---')
st.write(data)

# plot
st.markdown('---')
st.line_chart(data[['工業用電(百萬度)', '民生用電(百萬度)']])

st.button('aa')

# predict
st.text(data.shape)
# model = LinearRegression()
train, test = model_selection.train_test_split(data['民生用電(百萬度)'], train_size=400)
model = auto_arima(
    train, 
    error_action='ignore', 
    trace=True,
    suppress_warnings=True, 
    maxiter=10,
    seasonal=False,
    m=12)

# predicted = model.predict(n_periods=test.shape[0])
predicted = model.predict(n_periods=425-400)

st.markdown('---')
predicted_df = pd.DataFrame(data={'預測': predicted}, index=test.index)
predicted_df = pd.concat([predicted_df, test], axis=1)
st.write(predicted_df)
st.line_chart(predicted_df)
