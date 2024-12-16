import streamlit as st

# Set up a basic login system
def login_page():
    st.title("🔐 AQI Dashboard Sign In")
    st.write("Please log in to access the Power BI Dashboard.")
    
    # Input fields for login
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    # Authentication credentials (for demonstration purposes only)
    valid_username = "RishavAQI"
    valid_password = "AQI@123"

    # Login button
    if st.button("Sign In"):
        if username == valid_username and password == valid_password:
            st.session_state["authenticated"] = True
            st.success("Login successful! Redirecting...")
        else:
            st.error("Invalid username or password. Please try again.")

# Power BI Dashboard Page
def dashboard_page():
    st.title("📊 AQI Dasboard (2018 - 22)")
    st.write("Welcome to Air Quality Index Dashboard!")

    # Power BI Embed URL
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMjgyMmM3M2EtMzI4Zi00N2M3LTkzMjgtOGMyOWQ2N2NmNmI2IiwidCI6ImJmN2I4YjZlLWQwOWQtNGU2ZS05NGIwLTY1MWE3NDAwNzA0NyJ9"

    # Embed Power BI Dashboard using iframe
    st.markdown(
        f"""
        <iframe 
            src="{power_bi_url}" 
            width="1000" 
            height="800" 
            frameborder="0" 
            allowfullscreen="true">
        </iframe>
        """,
        unsafe_allow_html=True
    )

    # Sign-out button
    if st.button("Sign Out"):
        st.session_state["authenticated"] = False
        st.experimental_rerun()

# Main App Logic
def main():
    # Initialize session state for authentication
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # Display appropriate page based on authentication state
    if st.session_state["authenticated"]:
        dashboard_page()
    else:
        login_page()

# Run the Streamlit App
if __name__ == "__main__":
    main()
