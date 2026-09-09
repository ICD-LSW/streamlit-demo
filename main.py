import streamlit as st

st.set_page_config(page_title="전기 계산기", layout="centered")

st.title("전류 및 소비전력 계산")
st.write("전압과 저항을 입력하면 계산 결과를 표시합니다.")

with st.form("calculator"):
    voltage = st.number_input(
        "인가 전압 [V]",
        value=24.0,
        step=1.0,
    )

    resistance = st.number_input(
        "저항 [Ω]",
        min_value=0.1,
        value=1000.0,
        step=100.0,
    )

    submitted = st.form_submit_button("계산")

if submitted:
    current = voltage / resistance
    power = voltage ** 2 / resistance

    col1, col2 = st.columns(2)
    col1.metric("전류", f"{current * 1000:.2f} mA")
    col2.metric("소비전력", f"{power:.3f} W")