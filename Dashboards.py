import streamlit as st

# Title of the Streamlit app
st.title("Air Quality Index (2018 - 2022)")

# Power BI report embed URL (replace with your Power BI embed link)
embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMjgyMmM3M2EtMzI4Zi00N2M3LTkzMjgtOGMyOWQ2N2NmNmI2IiwidCI6ImJmN2I4YjZlLWQwOWQtNGU2ZS05NGIwLTY1MWE3NDAwNzA0NyJ9"

# Add a description or context (optional)
st.markdown("""
This is an Air Quality Index Dashboard.
You can interact with the live Power BI report below.
""")

# Embed the Power BI dashboard using an iframe
st.components.v1.iframe(embed_url, width=1000, height=800)
