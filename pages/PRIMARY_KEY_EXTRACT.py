import streamlit as st
import csv
import io
import pandas as pd

ddl = st.text_input("Enter the DDL")
if ddl is not None:
  ddl_list = ddl.split(', ')
  for i in range(len(ddl_list)):
    ddl_list[i] = ddl_list[i].lstrip()
    ddl_list[i] = ddl_list[i].replace('"','')
  column_names = []
  column_types = []
  
  for element in ddl_list:
    if "NOT NULL" in element:
      ddl, enable = element.split(" NOT NULL ")
      name, type = ddl.split(" ",1)
      column_names.append(name)
      column_types.append(type)

  column_names
  column_types
  str1 = ''
  for i in column_names:
    str1 = str1 + i + ','
  str1[:-1]

st.image('https://github.com/tanmay-nemade01/experimental_features/blob/main/screenshots/CDP%20DDL%20Screenshot.png?raw=true')
