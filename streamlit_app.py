import streamlit as st
import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
# Show title and description.
st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
    "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)

# Replace with your API endpoint URL
API_URL = "https://yourapi.com/your-endpoint"

def fetch_data_from_api():
    """Fetches data from the API and returns it as a pandas DataFrame."""
    try:
        # Send a GET request to the API
        response = requests.get(API_URL)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Assuming the API returns a list of records
            # You can modify this part depending on the structure of your API response
            df = pd.DataFrame(data, columns=["report_date", "installs_volume"])
            return df
        else:
            st.error(f"Error fetching data from API. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error fetching data from API: {e}")
        return None

def plot_data(df):
    """Plots the data using matplotlib."""
    st.subheader('Installs Volume Over Time')

    # Plotting with matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df['report_date'], df['installs_volume'], marker='o', linestyle='-', color='b')
    plt.xlabel('Report Date')
    plt.ylabel('Installs Volume')
    plt.title('Installs Volume Over the Last 3 Months')
    plt.xticks(rotation=45)
    plt.grid(True)

    # Show plot in the Streamlit app
    st.pyplot(plt)

def main():
    """Main function to run the Streamlit app."""
    st.title('Data Visualization from API')

    # Fetch data from the API
    df = fetch_data_from_api()

    if df is not None:
        # Display the fetched data
        st.write("Fetched Data:", df)

        # Plot the data
        plot_data(df)
    else:
        st.error("Failed to fetch data from the API.")

if __name__ == "__main__":
    main()
