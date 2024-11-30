# Copyright (c) 2023 yuky_az
# MIT License https://opensource.org/license/mit/

import streamlit as st
import openai

# 外部ファイルからAPI keyを保存
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = "あなたは優秀なアシスタントAIです。なんでも質問に答えてください。"

# メッセージのやりとりを保存する
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
        ]

# OpenAI API との通信部分
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""


# UI 部分の実装
st.title("アシスタントAIボットテスト")
st.image("title_image.jpg")
st.write("こんにちは！何でも質問してください")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "?"
        if message["role"]=="assistant":
            speaker="?"

        st.write(speaker + ": " + message["content"])