## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import html
import os
import requests
from twilio.rest import Client

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
STOCK_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}


def trend_indicator(num):
    """Determines whether number is positive or negative and assigns corresponding emoji"""
    if num > 0:
        return f"🔺{round(num, 2)}%"
    else:
        return f"🔻{round(num, 2)}%"


response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
trading_days = [key for key in data.keys()]
yesterday_close = float(data[trading_days[0]]['4. close'])
two_days_ago_close = float(data[trading_days[1]]['4. close'])

news_url = ('https://newsapi.org/v2/everything?'
            f'q={COMPANY_NAME}&'
            'from=2022-05-04&'
            'sortBy=relevancy&'
            'language=en&'
            f'apiKey={NEWS_API_KEY}')

news_response = requests.get(news_url)
news_articles = news_response.json()['articles'][:3]

percent_diff = (yesterday_close - two_days_ago_close) / two_days_ago_close * 100
if abs(percent_diff) >= 5:
    for news_index in range(3):
        message = client.messages.create(
            body=f"""
{STOCK}: {trend_indicator(percent_diff)}
Headline: {html.unescape(news_articles[news_index]['title'])}
Brief: {html.unescape(news_articles[news_index]['description'])}
Link: {html.unescape(news_articles[news_index]['url'])}
""",
            from_=os.environ.get('TWILIO_PHONE'),
            to=os.environ.get('MY_PHONE')
        )
        print(message.status)
else:
    print(percent_diff)
