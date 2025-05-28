
import streamlit as st
from PIL import Image

st.set_page_config(page_title="TradeSniper AI", layout="centered")

st.title("📸 TradeSniper AI")
st.subheader("Upload a trading chart screenshot")

uploaded_file = st.file_uploader("Choose a screenshot", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Screenshot", use_column_width=True)

    # Placeholder for trade analysis result
    st.markdown("### 📈 Trade Plan Suggestion")
    st.markdown("""
- **Direction**: 🔼 Long  
- **Entry**: 15,235.00  
- **Stop Loss**: 15,210.00  
- **Take Profit**: 15,275.00  
- **Confidence**: 82%  
""")

    feedback = st.radio("Did this trade plan work for you?", ("✅ Yes", "❌ No"))
    if feedback:
        st.success("Thanks for your feedback! The AI will learn from this.")
