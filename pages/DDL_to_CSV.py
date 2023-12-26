import streamlit as st
import csv

ddl = st.text_input("Enter the DDL")
ddl_list = ddl.split(', ')
for i in ddl_list:
  i.replace(' ','')
ddl_list
