import streamlit as st

st.set_page_config(page_title="Auto-Stop Position Sizer", page_icon="💶")

st.title("🛡️ Smart Risk Calculator")
st.write("This tool calculates your Stop Loss and Position Size automatically.")

# 1. Account Settings
account_size = st.number_input("Account Balance (€)", min_value=0.0, value=10000.0, step=100.0)
risk_percent = st.slider("Risk per Trade (%)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

st.divider()

# 2. Trade Settings
col1, col2 = st.columns(2)
with col1:
    entry_price = st.number_input("Entry Price (€)", min_value=0.01, value=100.0)
with col2:
    # This represents the 'wiggle room' or Volatility (ATR)
    volatility = st.number_input("Stock Volatility (€ amount)", min_value=0.01, value=2.0, help="How much does this stock normally move? Your stop loss will be placed this far away.")

view_mode = st.radio("Display Result As:", ["Shares to Buy", "Total EUR Investment"])

# 3. The Calculation
if st.button("🚀 Calculate Trade Plan"):
    
    # Calculate Stop Loss Price automatically
    suggested_stop = entry_price - volatility
    
    # Calculate Risk Amount (e.g., 1% of 10k = 100€)
    total_eur_to_risk = account_size * (risk_percent / 100)
    
    # Risk per share is exactly the volatility
    shares_to_buy = total_eur_to_risk / volatility
    total_investment_value = shares_to_buy * entry_price
    
    st.divider()
    
    # 4. Results Display
    st.subheader(f"📍 Suggested Stop Loss: €{suggested_stop:,.2f}")
    
    if view_mode == "Shares to Buy":
        st.metric("Quantity", f"{int(shares_to_buy)} Shares")
    else:
        st.metric("Total Investment", f"€{total_investment_value:,.2f}")
        
    st.success(f"Strategy: By buying at €{entry_price} and setting a stop at €{suggested_stop}, you are risking exactly €{total_eur_to_risk:,.2f} ({risk_percent}% of your account).")
