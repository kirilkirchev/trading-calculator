import streamlit as st

st.set_page_config(page_title="Position Sizer", page_icon="📈")

st.title("🛡️ Risk Management Calculator")
st.write("Calculate exactly how many shares to buy to keep your risk under control.")

# Inputs from the user
col1, col2 = st.columns(2)

with col1:
    account_size = st.number_input("Account Balance ($)", min_value=0.0, value=10000.0, step=100.0)
    # This is the variable risk % you asked for
    risk_percent = st.slider("Risk per Trade (%)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

with col2:
    entry_price = st.number_input("Entry Price ($)", min_value=0.01, value=150.0)
    stop_loss = st.number_input("Stop Loss Price ($)", min_value=0.0, value=145.0)

# The Math Logic
risk_amount = account_size * (risk_percent / 100)
risk_per_share = entry_price - stop_loss

if risk_per_share > 0:
    position_size = risk_amount / risk_per_share
    total_cost = position_size * entry_price
    
    st.divider()
    
    # Results Display
    st.subheader("Your Trade Plan:")
    res_col1, res_col2 = st.columns(2)
    res_col1.metric("Shares to Buy", f"{int(position_size)}")
    res_col2.metric("Total Risk ($)", f"${risk_amount:,.2f}")
    
    st.info(f"💡 Buying {int(position_size)} shares will cost **${total_cost:,.2f}**. If the price hits ${stop_loss}, you will lose exactly **${risk_amount:,.2f}**.")
else:
    st.error("Stop loss must be lower than entry price for a 'Long' trade.")
