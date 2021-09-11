import streamlit as st


def app():
    # Setting up the Title
    st.title("Welcome :wave:")
    st.write(f"""
        ### Made with ❤️ by [**FitCommunity.Ai**](https://za.linkedin.com/in/yattishramhorry)
        """)
    intro = f"""
    ---
    ### **🎈 Getting Started**
    - Thank you for being a part of this Open-Source **GPT-3 Sandbox** 🙌
    - To get started, 1. go to **GPT-3 Sandbox** on the left sidebar-> 2. Paste your **OpenAI API key**

    ### **👾 FitCommunity.Ai Health Bot**
    - Our bodies need nutrients and vitamins to help the body and brain function and grow.
    - To help your body get these nutrients and vitamins, you need to eat a well-balanced diet. 
    - FitCommunity.Ai is an interactive AI Chatbot that provides an individual with a few healthy meal choices
    - Powered by: Nextgrid & GPT-3
    """

    #st.header("🧠 Powered by FitCommunity.Ai") 🎈 🐾 🏆

    st.write(intro)
    
    st.write(f"""
        ###  🐾 **About the Sandbox**
        - This is an open-source 🔧 and it is alive thanks to the awesome GPT-3 community. If you'd like to contribute, please check [Collaboration Guidelines](https://github.com/Shubhamsaboo/kairos_gpt3/blob/master/CONTRIBUTE.md)
        - If you are curious about what _exactly_ went behind this sandbox, check out the [source code](https://github.com/Shubhamsaboo/kairos_gpt3)
        - We are still working on it and we'd ❤️ to hear from you! If you have ideas on how to improve the Sandbox, let us know [here](sandra@kairosdatalabs.com)
        """)

    st.write(f"""
            ---
            ### 🔗 **Connect With Us**
            - We are [Yattish](https://za.linkedin.com/in/yattishramhorry/) and [Sumit Kumar Gupta](https://za.linkedin.com/in/yattishramhorry/), co-founders of [FitCommunity.Ai](https://www.linkedin.com/company/kairos-data-labs) 
            - We are super excited to have you here. Our mission is to make the [GPT-3 Sandbox](https://github.com/Shubhamsaboo/kairos_gpt3) accessible and usable to everyone who wants to build applications with OpenAI's GPT-3 ❤️ 
            - Come by 🤗 [the forum](https://github.com/Shubhamsaboo/kairos_gpt3) if you'd like to ask questions, post an awesome app, or just say Hi!
        """)