import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.image("brand.png", width=200)

st.tittle("Products Management")

# Function to show detailed errors
def show_response_message(response):
    if response.status_code == 200:
        st.succes("Successfully done!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                # If the error comes from a list, bring each message of error
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Error: {errors}")
                else:
                    # Otherwise show the error.
                    st.erroe(f"Error: {data["detail"]}")
        except ValueError:
            st.error("Unknown error")

# Adding products
with st.expander("Add a new Product"):
    with st.form("new_product"):
        name = st.text_input(" Product name")
        description = st.text_area("Product description")
        price = st.number_input("Price", min_value=0.01, format="%f")
        category = st.selectbox(
            "Category",
            ["Type1", "Type2", "Type3", "Type4", "Type5"]
        )
        email = st.text_input("Email")
        submit_button = st.form_submit_button("Add Product")

        if submit_button:
            response = requests.post(
                "http://backend:8000/products/",
                json={
                    "name": name,
                    "description": description,
                    "price": price,
                    "category": category,
                    "email": email
                }
            )
            show_response_message(response)
# Show Products
with st.expander("Show Products"):
    if st.button("Show all Products"):
        response = requests.get("http://backend:8000/products/")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "email",
                    "created_at"
                ]
            ]

            # Show dataframe wothout index
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Delete product
with st.expander("delete the product"):
    delete_id = st.number_input("Product ID to delete", min_value=1, format="%d")
    if st.button("Delete the Product"):
        response = requests.delete(f"http://backend:8000/products/{delete_id}")
        show_response_message(response)

# Update product
with st.expander("Update the product"):
    with st.form("update_product"):
        update_id = st.number_input("Product ID", min_value=1, format="%d")
        new_name = st.text_input("New product name")
        new_description = st.text_area("New product description")
        new_price = st.number_input(
            "New Price",
            min_value=0.01,
            format="%f"
        )
        new_category = st.selectbox(
            "New Category",
            ["Type1", "Type2", "Type3", "Type4", "Type5"]
        )
        new_email = st.text_input("New email")

        update_button = st.form_submit_button("Update Products")

        if update_button:
            update_data = {}
            if new_name:
                update_data["name"] = new_name
            if new_description:
                update_data["description"] = new_description
            if new_price > 0:
                update_data["price"] = new_price
            if new_email:
                update_data["email"] = new_email
            if new_category:
                update_data["category"] = new_category

            if update_data:
                response = requests.put(
                    f"http://backend:8000/products/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("Empty information to update")