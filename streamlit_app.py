import streamlit as st

st.set_page_config(page_title="Fridge to Feast")

st.title("Fridge to Feast 🍳")
st.write("AI-powered recipe ideas based on what’s in your fridge.")

ingredients = st.text_input("Enter ingredients (comma separated):")

if ingredients:
st.subheader("You entered:")
st.write(ingredients)
