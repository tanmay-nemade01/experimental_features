import streamlit as st
import csv

ddl = st.text_input("Enter the DDL")
ddl_list = ddl.split(', ')
ddl_list
