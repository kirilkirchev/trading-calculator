import streamlit as st

st.set_page_config(page_title="Position Sizer", page_icon="💶")

st.title("🛡️ Trader's Risk Calculator")
st.write("Determine your position size by defining your entry and exit points.")

# 1. Inputs Section
account_size = st.number_input("Account Balance (€)", min_value=0.0, value=10000.0, step=100.0)
risk_percent = st.slider("Risk per Trade (%)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

st.divider()

col1, col2 = st.columns(2)
with col1:
    entry_price = st.number_input("Entry Price (€)", min_value=0.01, value=100.0)
with col2:
    stop_loss = st.number_input("Stop Loss Price (€)", min_value=0.0, value=95.0)

# 2. View Toggle
view_mode = st.radio("Show result as:", ["Shares to Buy", "Total EUR Investment Amount"])

# 3. Calculate Button
if st.button("🚀 Calculate Position Size"):
    
    # Logic: Risk Amount (e.g., 1% of 10k = 100€)
    total_eur_to_risk = account_size * (risk_percent / 100)
    
    # Logic: Risk per share (e.g., Entry 100 - Stop 95 = 5€ risk per share)
    risk_per_share = entry_price - stop_loss
    
    if risk_per_share > 0:
        shares_to_buy = total_eur_to_risk / risk_per_share
        total_investment_value = shares_to_buy * entry_price
        
        st.divider()
        
        # 4. Results Display
        if view_mode == "Shares to Buy":
            st.header(f"Buy: {int(shares_to_buy)} Shares")
            st.info(f"If the price hits your Stop Loss (€{stop_loss}), you will lose €{total_eur_to_risk:,.2f} ({risk_percent}%).")
        else:
            st.header(f"Total Value: €{total_investment_value:,.2f}")
            st.info(f"This is the total cost to open this position (Buying {int(shares_to_buy)} shares).")
            
    elif risk_per_share == 0:
        st.error("Entry Price and Stop Loss cannot be the same.")
    else:
        st.error("Stop Loss must be lower than the Entry Price for a long position.")
