import streamlit as st

st.set_page_config(page_title="Position Sizer", page_icon="💶")

st.title("🛡️ Trader's Risk Calculator")
st.write("Calculate your position size based on your risk tolerance.")

# 1. Inputs Section
account_size = st.number_input("Account Balance (€)", min_value=0.0, value=10000.0, step=100.0)
risk_percent = st.slider("Risk per Trade (%)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
entry_price = st.number_input("Entry Price (€)", min_value=0.01, value=100.0)
risk_per_share = st.number_input("Amount to Risk per Share (€)", min_value=0.01, value=1.0)

# 2. View Toggle (Button-like behavior using a Radio)
view_mode = st.radio("Display Result As:", ["Shares to Buy", "Total EUR Amount"])

# 3. Calculate Button
if st.button("🚀 Calculate Position Size"):
    
    # The Math
    total_eur_to_risk = account_size * (risk_percent / 100)
    
    if risk_per_share > 0:
        shares_to_buy = total_eur_to_risk / risk_per_share
        total_investment_value = shares_to_buy * entry_price
        
        st.divider()
        
        # 4. Display Logic
        if view_mode == "Shares to Buy":
            st.metric("Quantity", f"{int(shares_to_buy)} Shares")
            st.caption(f"Based on risking {risk_percent}% (€{total_eur_to_risk:,.2f}) of your account.")
        else:
            st.metric("Total Position Value", f"€{total_investment_value:,.2f}")
            st.caption(f"This is the total cost of buying {int(shares_to_buy)} shares.")

        st.success(f"Done! If the price drops by €{risk_per_share} per share, you lose exactly €{total_eur_to_risk:,.2f}.")
    else:
        st.error("Risk per share must be greater than 0.")
