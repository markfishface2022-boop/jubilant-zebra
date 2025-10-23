import streamlit as st
import pandas as pd
import openpyxl

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Excel Data Viewer",
    page_icon="📊",
    layout="wide"
)

# --- 2. Title and Description ---
st.title("Local Excel File Viewer 📊")
st.write("Upload an Excel file from your computer to view its data below.")

# --- 3. File Uploader Widget ---
# We create a file uploader widget that accepts .xlsx files.
# 'uploaded_file' will be 'None' until a file is uploaded.
uploaded_file = st.file_uploader(
    "Choose your Excel file", 
    type="xlsx",
    help="Upload an Excel file (.xlsx) to see its contents."
)

# --- 4. Logic to Process the File ---
# We only proceed if the user has uploaded a file.
if uploaded_file is not None:
    
    st.success("File uploaded successfully!")
    st.markdown("---") # Adds a horizontal line

    # We use a try-except block to handle potential errors,
    # like uploading a corrupt file or a non-Excel file.
    try:
        # --- 5. Read the Excel File ---
        # We pass the uploaded file object directly to pandas.
        # Pandas is smart enough to read it without saving it to disk.
        df = pd.read_excel(uploaded_file)

        # --- 6. Display the Data ---
        st.subheader("Here is the data from your file:")
        
        # st.dataframe() provides an interactive table (sortable, etc.)
        st.dataframe(df)

    except Exception as e:
        # If pandas fails to read the file, show an error.
        st.error(f"Error: Unable to read the file. Please ensure it's a valid Excel file. Details: {e}")

else:
    # This message is shown by default when no file is uploaded.
    st.info("Please upload an Excel file to get started.")