# ai_agent_

## Project Overview
The AI AGENT application allows users to upload a CSV file, input a custom query template with placeholders, and scrape the web using SerpAPI to extract relevant information. It then uses the Groq API to extract information from the scraped data and appends the results back to the original CSV file.

### Key Features:
- **Upload CSV**: Upload a CSV file.
- **Select Column**: Choose the column to query.
- **Input Custom Query**: Enter a query template to dynamically generate search queries.
-  **Input extraction type**:  Asks the user what type of data they want to extract (e.g., email, phone number, address,etc..).
- **Web Scraping**: Use SerpAPI to scrape search results for each query.
- **Download Updated CSV**: Download the original CSV with extracted information and source URLs.

## Setup Instructions

Follow these steps to set up and run the application:

### 1. Clone the repository:

git clone https://github.com/abrav970/ai_agent_.git
cd ai_agent

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

1. **Upload a CSV file**: The first step is to upload a CSV file. The app will display the content of the CSV file for you to review.
   
2. **Select Column**: Choose the column . The application will generate queries using these names.

3. **Enter Query Template**: In the text input box, enter a query template. Use `{company}` as a placeholder. For example:
"Find contact details for {company}"

4.**Input extraction type**: Asks the user what type of data they want to extract (e.g., email, phone number, address). 

5. **Scrape the Web**: The application will send requests to SerpAPI to search for each query and retrieve the results. It will then use the Groq API to extract information from the search snippets.

6. **Download the Updated CSV**: After the emails and source URLs have been extracted, the updated CSV file will be displayed, and you can download it by clicking the "Download Updated CSV" button.


**link to the video https://drive.google.com/file/d/17nah8QykdPa5nM5epQkPmN9ruHXcYLHg/view?usp=drive_link
