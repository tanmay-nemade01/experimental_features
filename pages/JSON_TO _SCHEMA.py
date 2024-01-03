import streamlit as st
import json
import pandas as pd
import csv
import io


st.title("JSON Data Extractor")

uploaded_file = st.file_uploader("Upload a JSON file")

if uploaded_file is not None:
  try:
    data = json.load(uploaded_file)

    name_list = []
    type_list = []
    # Optional: Extract specific data for presentation
    for field in data["fields"]:
      name_list.append(field["name"])
      type_list.append(field["type"])

    data = {
      "COLUMN_NAME" : name_list,
      "TYPE" : type_list
    }
    
    df = pd.DataFrame(data)

    st.dataframe(df)
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)  # Create a CSV writer on the buffer
    
    # Write the CSV content to the buffer
    csv_writer.writerow(["COLUMN_NAME", "TYPE"])
    for name, type in zip(name_list, type_list):
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

  except json.JSONDecodeError as e:
    st.error("Invalid JSON file. Please upload a valid JSON file.")
