import streamlit
import pandas

streamlit.title("My Parents New HEalthy Dinner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, spinach and Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')

streamlit.header('Build your own friut smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick from fruits",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
