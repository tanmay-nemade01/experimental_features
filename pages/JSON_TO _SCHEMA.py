import streamlit as st
import json
import pandas as pd

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

  except json.JSONDecodeError as e:
    st.error("Invalid JSON file. Please upload a valid JSON file.")
