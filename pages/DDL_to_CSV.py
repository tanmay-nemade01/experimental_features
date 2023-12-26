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

csv_content = ""
csv_writer = csv.writer(st.empty())  # Create a temporary CSV writer object
csv_writer.writerow(["Column Name", "Column Type"])
for name, type in zip(column_names, column_types):
    csv_writer.writerow([name, type])

# Get the CSV content as a string
csv_content = csv_writer.out.getvalue().decode("utf-8")

# Offer the download button
if st.button("Download CSV"):
    st.download_button(
        label="Download Separated Lists",
        data=csv_content,
        file_name="separated_lists.csv",
        mime="text/csv",
    )
