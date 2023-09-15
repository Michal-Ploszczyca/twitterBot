# Twitter Weather Bot

Welcome to my first project - a Twitter Weather Bot! 🌤️

This bot automates the process of fetching current weather data from `pogoda.interia.pl`, processes the extracted details, and then tweets the information through a Twitter account. 

## 🚀 Features

1. **Twitter Login Automation**: 
   - It navigates to the Twitter login page, inputs the user credentials, and logs into the Twitter account.
   
2. **Weather Data Extraction**:
   - This bot uses the power of BeautifulSoup to scrape weather details from `pogoda.interia.pl`.
   
3. **Tweeting Weather Details**:
   - After data extraction, it automates the process of creating a new tweet containing weather information for multiple cities and then posts it.

## 💼 Tech Stack

- **Selenium**: For web automation (especially the Twitter interactions).
- **BeautifulSoup**: For parsing and extracting data from `pogoda.interia.pl`.
- **Requests**: To fetch the web page for scraping.

## 📝 Instructions

- Ensure you have the required Python packages installed, including `selenium`, `beautifulsoup4`, and `requests`.
- Make sure to input your Twitter credentials in the appropriate placeholders within the script.
- Simply run the script and watch the bot in action!

## ⚠️ Note

Please be cautious while automating any process on platforms like Twitter. Abusive or too frequent requests might get your account restricted or banned. Use this bot responsibly and understand the terms of service of the platform.
