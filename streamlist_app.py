import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError
import requests

streamlit.title("My Parents New HEalthy Dinner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, spinach and Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')

streamlit.header('Build your own friut smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick from fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit advice')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
streamlit.header('Fruityvice Fruit advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_funciton = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_funciton)


except URLError as e:
  streamlit.error()
      

#

    
#streamlit.text(fruityvice_response)


streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like add?')
streamlit.write('thanks for adding',add_my_fruit)                                 

def insert_row_sf(fruit):
    with my_cnx.cursor() as my_cur_i:
        my_cur_i.execute("insert into fruit_load_list values (' " + ???? + "')")
        #my_cur_i.execute("insert into pc_rivery_db.public.fruit_load_list values('" + ???? + "')")
        return 'Thanks for addding' + fruit
