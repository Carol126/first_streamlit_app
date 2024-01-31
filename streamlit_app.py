import streamlit

streamlit.title("My parents new healthy diner")

streamlit.header("Breakfast menu")
streamlit.text("Omega 3 & Blueberry oatmeal")

streamlit.text("Kale, Spinach & ROcket Smoothie")

streamlit.text("Hard-boiled free-range egg")
streamlit.header("Build your own fuit smoothie!")


import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
## put a pick list
streamlit.multiselect("pick some fuits:", list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)



