###################################import###############################
import streamlit as st 
from main import get_exchange_rate, convert_currency
import currencies

# Get the list of currencies from the currencies library
currencies_list = list(currencies.MONEY_FORMATS.keys())
currencies_list.append("IRR")

##############################streamlit_app#############################
st.markdown("<h1 style='text-align: center; color:#f58d05;'>Currency Converter</h1>", unsafe_allow_html=True)
st.image("./images/image01.png")
st.markdown("""
This tool allows you to instantly convert amounts between different currencies 🌍.
Enter the amount and choose the currencies to see the result.
""")

# Input number for amount to convert
col1, col2, col3 = st.columns(3)
amount = col1.number_input("Amount", min_value=0.00, value=1.00, step=0.5)

# Select boxes for choosing currencies
base_currency = col2.selectbox("From", options=currencies_list, index=currencies_list.index("USD"))
target_currency = col3.selectbox("To", options=currencies_list, index=currencies_list.index("IRR"))

# Perform conversion without a button for instant execution
if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        col1, col2, col3 = st.columns(3)

        col1.metric( label="Base Currency", value=f"{amount} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color:#f58d05;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f}")
    else:
        st.error(f"❌Error: Unable to fetch the exchange rate. Please try again.")


st.markdown("---")
st.markdown("### 📙 About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")

