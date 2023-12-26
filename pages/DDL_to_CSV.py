import streamlit as st
import csv

ddl = st.text_input("Enter the DDL")
ddl_list = ddl.split(', ')
for i in range(len(ddl_list)):
  ddl_list[i] = ddl_list[i].lstrip()
ddl_list
