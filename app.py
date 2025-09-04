from src.addition import add
from src.substration import mainus
from src.divison import divide
from src.multiplication import multiply
import streamlit as st

st.title("Calculator")

a = st.number_input("Enter the First Number : ", value=0)
b = st.number_input("Enter the Second Number : ", value=0)

option = st.selectbox(
    "Enter the Mathematical Operation you want to perform",
    ("Addition", "Substraction","multiplication","divison"),
    )

if st.button("Calculate"):
    if option == "Addition":
        result = add(a, b)
    if option == "Substraction":
        result = mainus(a, b)
    if option == "divison":
         result = divide(a, b)
    if option == "multiplication":
        result = multiply(a, b)
        
    st.write(f"Result : {result}")