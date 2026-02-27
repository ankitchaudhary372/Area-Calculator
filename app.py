import streamlit as st
st.title("Area Calculator")
st.header("Please enter Length and Breath Respectiviy")
length = st.number_input("Input Lenght : ")
breath = st.number_input("Input Breath : ")

a= length*breath

st.write("Area of Given Values is -- ",a, size =20)

st.markdown(
    f"""
    <div style='
        font-size:22px;
        color:#2E86C1;
        font-weight:600;
        text-align:center;
    '>
        Area of Given Values is — {a}
    </div>
    """,
    unsafe_allow_html=True
)
    