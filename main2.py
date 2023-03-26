
import streamlit as st
import requests

# Set up the API endpoint and headers
url = "https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp"
headers = {
    "X-RapidAPI-Key": "f02657f1d1msh39dc9ff97e04a4cp15c205jsn148e53c9e760",
    "X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
}

# Create a Streamlit app with input fields for the phone number and country
st.title("Phone Number Validation App")
phone_number = st.text_input("Enter a phone number:")
country = st.text_input("Enter the country code (e.g. US, GB, FR):")

# When the user clicks the "Validate" button, send a GET request to the API
if st.button("Validate"):
    # Set up the query parameters for the API request
    querystring = {"number": phone_number, "country": country}

    # Send the GET request to the API
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Parse the response and display the results in a visual format
    result = response.json()
    st.write(f"**Phone Number:** {result['phoneNumberEntered']}")
    st.write(f"**Country:** {result['location']}")
    st.write(f"**Carrier:** {result['carrier']}")
    st.write(f"**Valid:** {result['isValidNumber']}")





