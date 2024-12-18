import streamlit as st
import pandas as pd
import requests
from groq import Groq
import time
import logging


class CSVUploaderApp:
    def __init__(self):
        self.df = None
        self.primary_column = None  # Store selected column here
        self.user_input = None
        self.extract_type = None  # Store the type of extraction (e.g., 'email' etc..)
        logging.basicConfig(
            filename="app_debug.log",
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def upload_csv(self):
        """Handles the file upload and displays the CSV content."""
        st.header("1. Upload Your CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file:
            self.df = pd.read_csv(uploaded_file)
            st.subheader("CSV File Contents:")
            st.dataframe(self.df)
            return self.df
        else:
            st.info("Please upload a CSV file to view its contents.")

    def select_column(self):
        """Displays a column selection dropdown after uploading the CSV."""
        if self.df is not None:
            st.header("2. Select the Column")
            self.primary_column = st.selectbox("Select the column that you need:", self.df.columns)
            return self.primary_column
        return None

    def input_text(self):
        """Displays a text input box for additional user input."""
        if self.primary_column is None:
            st.warning("Please select the column first.")
            return []
        
        st.header("3. Additional Input")
        st.write("Enter a query template with {company} as a placeholder for your data.")
        user_input = st.text_input("Enter your custom query template:")
        if user_input:
            st.write("You entered:", user_input)
            queries = [user_input.format(company=company) for company in self.df[self.primary_column]]
            return queries
        return []

    def input_extraction_type(self):
        """Asks the user what type of data to extract (e.g., email)."""
        st.header("4. Select Data to Extract")
        self.extract_type = st.selectbox("What type of data would you like to extract?", ["email", "phone number", "address", "custom"])

    def scrapWeb(self, queries):
        """Scrapes the web using SerpAPI."""
        serp_api_key = " ENTER_YOUR_API_KEY"
        if not serp_api_key:
            st.error("SerpAPI key is missing! Set it as an environment variable.")
            return []

        all_results = []
        for query in queries:
            params = {"engine": "google", "q": query, "api_key": serp_api_key}
            url = "https://serpapi.com/search"
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()

                # Log the response to debug issues
                res = response.json()
                logging.debug(f"Response for query '{query}': {res}")

                # Extract results safely
                results = res.get("organic_results", [])  # "organic_results" is the key for search results
                all_results.append(results)

                # Add a delay to avoid API rate limits
                time.sleep(2)

            except requests.exceptions.RequestException as e:
                logging.error(f"An error occurred for query '{query}': {e}")
                st.error(f"An error occurred: {e}")
                all_results.append([])

        return all_results

    def getRes(self, snippet):
        """Generates a response using the Groq API."""
        groq_api_key = " ENTER_YOUR_API_KEY "
        if not groq_api_key:
            st.error("Groq API key is missing! Set it as an environment variable.")
            return None

        client = Groq(api_key=groq_api_key)
        prompt = f"Extract the {self.extract_type} from this text:\n\n{snippet}\n\n{self.extract_type.capitalize()}:"
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"An error occurred during {self.extract_type} extraction: {e}")
            st.error(f"An error occurred during {self.extract_type} extraction: {e}")
            return None

    def run(self):
        """Runs the entire application."""
        df = self.upload_csv()
        if df is not None:
            # Step 1: Select column
            self.select_column()  # This will update the primary_column instance variable
            if self.primary_column:
                queries = self.input_text()
                if queries:
                    # Step 2: Ask for extraction type
                    self.input_extraction_type()

                    # Step 3: Scrap data
                    web_results = self.scrapWeb(queries)
                    extracted_data = []
                    source_urls = []
                    for results in web_results:
                        # Initialize links as an empty list in case there are no valid results
                        links = []
                        # Extract the first snippet safely
                        if results and isinstance(results, list):
                            snippet = results[0].get("snippet") if results[0].get("snippet") else None
                            links = [result['link'] if result else None for result in results]  # Extract links
                        else:
                            snippet = None

                        if snippet:
                            extracted_info = self.getRes(snippet)
                            extracted_data.append(extracted_info)
                        else:
                            extracted_data.append(None)

                        source_urls.append(links)  # Append the links (even if empty)

                    df[self.extract_type.capitalize()] = extracted_data
                    df['Source URL'] = source_urls

                    st.subheader(f"Updated CSV File Contents with {self.extract_type.capitalize()}s:")
                    st.dataframe(df)
                    # Allow the user to download the updated CSV
                    csv = df.to_csv(index=False)
                    st.download_button("Download Updated CSV", csv, "updated_file.csv", "text/csv")


if __name__ == "__main__":
    app = CSVUploaderApp()
    app.run()
