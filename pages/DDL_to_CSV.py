import streamlit as st
import csv

ddl = st.text_input("Enter the DDL")
ddl_list = ddl.split(', ')
for i in range(len(ddl_list)):
  ddl_list[i] = ddl_list[i].lstrip()

column_names = []
column_types = []

for element in ddl_list:
  name, type = element.split(" ")
  column_names.append(name)
  column_types.append(type)

ddl_list
column_names
column_types
