import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.anthropic import Claude

st.title("Claude Search")
st.caption("Search using claude AI")

anthropic_api=st.text_input("Claude API Key", type="password")

if anthropic_api:
    assistant=Assistant(
        llm=Claude(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1024,
            temperature=0.9,
            api_key=anthropic_api
        ),
        tools=[DuckDuckGo()],show_tool_calls=True
    )
    
    query=st.text_input("Enter Search query", type="default")
    
    if query:
        response=assistant.run(query, stream=False)
        st.write(response)