import streamlit as st

#  PAGE CONFIG
st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)


# Header

st.markdown("<h1 style='text-align:center;'>🧮 Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>All-in-One Math & Finance Calculator</p>",
    unsafe_allow_html=True
)

st.divider()

# TABS 
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "➕ Basic Math",
    "📊 Percentage",
    "💰 Simple Interest",
    "📈 Compound Interest",
    "🏦 EMI"
])

#  BASIC MATH  MY LOVE
with tab1:
    st.subheader("Basic Arithmetic")

    num1 = st.number_input("First number", value=0.0, key="bm_num1")
    num2 = st.number_input("Second number", value=0.0, key="bm_num2")

    operation = st.selectbox(
        "Operation",
        ["Add", "Subtract", "Multiply", "Divide"],
        key="bm_op"
    )

    if st.button("Calculate", key="bm_calc"):
        if operation == "Add":
            st.success(num1 + num2)
        elif operation == "Subtract":
            st.success(num1 - num2)
        elif operation == "Multiply":
            st.success(num1 * num2)
        elif operation == "Divide":
            if num2 == 0:
                st.error("Cannot divide by zero")
            else:
                st.success(num1 / num2)

#  PERCENTAGE
with tab2:
    st.subheader("Percentage Calculator")

    value = st.number_input("Value", value=0.0, key="pct_value")
    percent = st.number_input("Percentage (%)", value=0.0, key="pct_percent")

    if st.button("Calculate Percentage", key="pct_calc"):
        st.success((value * percent) / 100)

# SIMPLE INTEREST 
with tab3:
    st.subheader("Simple Interest")

    p = st.number_input("Principal Amount", value=0.0, key="si_p")
    r = st.number_input("Rate (%)", value=0.0, key="si_r")
    t = st.number_input("Time (years)", value=0.0, key="si_t")

    if st.button("Calculate SI", key="si_calc"):
        si = (p * r * t) / 100
        st.success(f"Interest: {si}")
        st.info(f"Total Amount: {p + si}")

#COMPOUND INTEREST 
with tab4:
    st.subheader("Compound Interest")

    p = st.number_input("Principal", value=0.0, key="ci_p")
    r = st.number_input("Rate (%)", value=0.0, key="ci_r")
    t = st.number_input("Time (years)", value=0.0, key="ci_t")
    n = st.selectbox(
        "Compounding per year",
        [1, 2, 4, 12],
        key="ci_n"
    )

    if st.button("Calculate CI", key="ci_calc"):
        amount = p * (1 + (r / (100 * n))) ** (n * t)
        st.success(f"Interest: {amount - p:.2f}")
        st.info(f"Final Amount: {amount:.2f}")

# EMI I HATE THIS!!!!
with tab5:
    st.subheader("EMI Calculator")

    loan = st.number_input("Loan Amount", value=0.0, key="emi_loan")
    rate = st.number_input("Annual Interest Rate (%)", value=0.0, key="emi_rate")
    months = st.number_input("Tenure (months)", value=1, key="emi_months")

    if st.button("Calculate EMI", key="emi_calc"):
        monthly_rate = rate / (12 * 100)
        emi = loan * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
        st.success(f"Monthly EMI: {emi:.2f}")

st.sidebar.header("⚙ Settings")
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])

# Footer
st.divider()
st.markdown(
    "<p style='text-align:center;font-size:14px;'>"
    "Built with ❤️ by <strong>P Vaishnavi</strong>"
    "</p>",
    unsafe_allow_html=True
)

