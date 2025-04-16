import streamlit as st
import pandas as pd
import numpy as np

brands = pd.read_csv('brands.csv')



st.title('NO THANKS')
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
            border-radius: 16px;
            }

            .details h3{
                color: green;
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
            html1 = "<div class='details' style='width:100%; margin-top:20px; border:3px solid grey; padding:10px;'>"
            

            for _, row in result.iterrows():
                html1 += f"<h4>{row['name']}</h4>"
                html1 += f'<h3>Logo</h3>'
                html1 += f'<img src="{row["logo_url"]}" width="80" style="margin-bottom:10px;"><br>'
                html1 += f'<br>'
                html1 += f'<h3>Reason</h3>'
                html1 += f'<p>{row["description"]}</p>'
                html1 += f'<br>'
                html1 += f'<h4 style="color: red">{row["status"]}</h4><hr>'

            
            html1 += "</div>"

            st.markdown(html1, unsafe_allow_html=True)

        else:
            st.markdown(f"<div style='width:100%; margin-top:20px; border:3px solid red; padding:10px;'>Please use search: Some brands may not show up unless you include spaces in the name. For example, try '5 Gum' instead of '5gum.</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a search term or select from dropdown.")