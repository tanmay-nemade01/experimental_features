import streamlit as st
import csv
import io
import pandas as pd

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

column_types.replace('VARCHAR(16777216)','STRING')

data = {
  "COLUMN_NAME" : column_names,
  "TYPE" : column_types
}

df = pd.DataFrame(data)

st.dataframe(df)

csv_buffer = io.StringIO()
csv_writer = csv.writer(csv_buffer)  # Create a CSV writer on the buffer

# Write the CSV content to the buffer
csv_writer.writerow(["COLUMN_NAME", "TYPE"])
for name, type in zip(column_names, column_types):
    csv_writer.writerow([name, type])

# Get the CSV content as a string
csv_content = csv_buffer.getvalue()

# Offer the download button
# if st.button("Download CSV"):
#     st.download_button(
#         label="Download DDL Excel",
#         data=csv_content,
#         file_name="separated_lists.csv",
#         mime="text/csv",
#     )
st.download_button(
    label="Download DDL Excel",
    data=csv_content,
    file_name="separated_lists.csv",
    mime="text/csv",
)
