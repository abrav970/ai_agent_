# ai_agent_

## Project Overview
The AI AGENT application allows users to upload a CSV file containing company names, input a custom query template with placeholders, and scrape the web using SerpAPI to extract relevant information. It then uses the Groq API to extract email addresses from the scraped data and appends the results back to the original CSV file.

### Key Features:
- **Upload CSV**: Upload a CSV file containing company names.
- **Select Column**: Choose the column with company names to query.
- **Input Custom Query**: Enter a query template to dynamically generate search queries.
- **Web Scraping**: Use SerpAPI to scrape search results for each query.
- **Email Extraction**: Extract emails from the snippets using the Groq API.
- **Download Updated CSV**: Download the original CSV with extracted emails and source URLs.

## Setup Instructions

Follow these steps to set up and run the application:

### 1. Clone the repository:

git clone https://github.com/your-username/csv-web-scraper.git
cd csv-web-scraper

### 2. Install dependencies::
pip install -r requirements.txt

### 3. Set up API keys:

You will need API keys for the following services:

SerpAPI: Sign up for SerpAPI and get your API key.
Groq: Sign up for Groq and get your API key.
Set up the API keys either by:

Adding them to your environment variables, or
Directly inputting the keys into the code (though environment variables are recommended for security).

### 4. Run the application:

streamlit run app.py


## Usage Guide

1. **Upload a CSV file**: The first step is to upload a CSV file containing company names. The app will display the content of the CSV file for you to review.
   
2. **Select Column with Company Names**: Choose the column that contains the company names. The application will generate queries using these names.

3. **Enter Query Template**: In the text input box, enter a query template. Use `{company}` as a placeholder for the company names. For example:
"Find contact details for {company}"

4. **Scrape the Web**: The application will send requests to SerpAPI to search for each query and retrieve the results. It will then use the Groq API to extract email addresses from the search snippets.

5. **Download the Updated CSV**: After the emails and source URLs have been extracted, the updated CSV file will be displayed, and you can download it by clicking the "Download Updated CSV" button.
