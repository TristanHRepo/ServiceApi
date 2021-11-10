from flask import Flask
import requests
import json
import os


app = Flask(__name__)


@app.route('/')
def root():

    news_data = requests.get("http://site.api.espn.com/apis/site/v2/sports/football/nfl/news")

    send_data = {}

    for count in range(5):
        description = news_data.json()['articles'][count]['description']
        link = news_data.json()['articles'][count]['links']['web']['href']
        send_data[count + 1] = {'link': link, 'description': description}

    return json.dumps(send_data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7777))
    app.run(port=port, debug=True)