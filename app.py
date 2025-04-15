import streamlit as st
import pandas as pd
import numpy as np

brands = pd.read_csv('brands.csv')



st.title('No Thanks')
st.subheader('Search or Select from dropdown a brand/Company')

dropdown = st.selectbox('All Brands',options=[""] + brands['id'])
search = st.text_input('Search a brand/Company')





st.markdown(
        """
        <style>
            .details{
            width: 100%;
            margin-top: 20px;
            border: 3px solid red;
            background-color: Scarlet;
            padding: 10px;
            }
        </style>

        
        """,
        unsafe_allow_html=True
    )

if st.button("Search"):
    # Use text input if provided, otherwise use dropdown
    user_input = search.strip() if search.strip() else dropdown.strip()

    if user_input:
        st.write("You searched for:", user_input)

        result = brands[brands['name'].str.strip().str.contains(user_input, case=False, na=False)]

        if not result.empty:
            html = "<div class='details' style='width:100%; margin-top:20px; border:3px solid grey; padding:10px;'>"

            for _, row in result.iterrows():
                html += f"<h4>{row['name']}</h4>"
                html += f'<img src="{row["logo_url"]}" width="80" style="margin-bottom:10px;"><br>'
                html += f'<p>{row["description"]}</p>'
                html += f'<h4 style="color: red">{row["status"]}</h4><hr>'

            html += "</div>"

            st.markdown(html, unsafe_allow_html=True)

        else:
            st.markdown("<div style='width:100%; margin-top:20px; border:3px solid red; padding:10px;'>❌ No matching results found.</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a search term or select from dropdown.")