import streamlit as st
import csv
import io
import pandas as pd

ddl = st.text_input("Enter the DDL")
if ddl is not None:
  try:
    ddl_list = ddl.split(', ') 
    for i in range(len(ddl_list)):
      ddl_list[i] = ddl_list[i].lstrip()
    
    column_names = []
    column_types = []
    
    for element in ddl_list:
      name, type = element.split(" ")
      column_names.append(name)
      column_types.append(type)
    
    for i in range(len(column_types)):
        if column_types[i] == 'VARCHAR(16777216)':
            column_types[i] = 'STRING'
        if column_types[i] == 'TIMESTAMP_NTZ':
            column_types[i] = 'TIMESTAMP'
    
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
        label="Download",
        data=csv_content,
        file_name="separated_lists.csv",
        mime="text/csv",
    )
  except:
    st.info('Please Enter a valid DDL')
