from langchain_community.llms import Ollama
import streamlit as st

# 初始化 LLM
llm = Ollama(model="llama3")

# 初始化對話記錄

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 標題
st.title("Chatbot using llama3 with Memory")

# 用戶輸入區
prompt = st.text_area("Enter your prompt:")

# 按鈕處理邏輯
if st.button("Generate"):
    if prompt:
        # 將用戶的輸入加入對話記錄
        st.session_state.chat_history.append(f"User: {prompt}")
        # 拼接所有的對話記錄作為上下文
        conversation = "\n".join(st.session_state.chat_history)
        
        
        with st.spinner("Generating response..."):
            # 調用模型生成回應
            response = ""
            for chunk in llm.stream(conversation, stop=['<|eot_id|>']):
                response += chunk  # 将生成器返回的每个分块拼接成完整的响应
            # 將模型回應加入對話記錄
            st.session_state.chat_history.append(f"Bot: {response}")
            # 顯示模型的回應
            st.write(response)

# 顯示對話記錄
st.markdown("### Conversation History:")
st.write("\n".join(st.session_state.chat_history))
###111111
