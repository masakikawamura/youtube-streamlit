import streamlit as st
import time

st.title("streamit 超入門")
st.write("プログレスバーの表示")

"start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Interation{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!!"


left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ内容を書く1")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ内容を書く2")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ内容を書く3")

# text = st.text_input("あなたの趣味を教えてください")

# condition = st.slider("今のあなたの調子は？", 0, 100, 50)

# "あなたの趣味は：", text
# "コンディディション", condition



# セレクトボックス
# option = st.selectbox(
#     "あなたが好きな数字を教えてください",
#     list(range(1, 11))
# )

# "あなたの好きな数字は", option ,"です。"

#画像に関して（チェックボックス入れたら見れる制御あり)
# if st.checkbox("show image"):
#     img = Image.open("onepiece001.png")
#     st.image(img, caption="onepiece1000", use_column_width= True)

# 表の書き方
# df = pd.DataFrame({
#     "1列目": [1, 2, 3, 4],
#     "2列目": [10, 20, 30, 40],
# })

# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# マップの書き方
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )

# st.map(df)