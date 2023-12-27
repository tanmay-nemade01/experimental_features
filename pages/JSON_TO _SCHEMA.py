import streamlit as st
import json

st.title("JSON Data Extractor")

uploaded_file = st.file_uploader("Upload a JSON file")

if uploaded_file is not None:
  try:
    data = json.load(uploaded_file)
    st.write(data)  # Display the entire JSON data

    name_list = []
    type_list = []
    # Optional: Extract specific data for presentation
    for field in data["fields"]:
      name_list.append(field["name"])
      type_list.append(field["type"])

    name_list
    type_list

  except json.JSONDecodeError as e:
    st.error("Invalid JSON file. Please upload a valid JSON file.")
