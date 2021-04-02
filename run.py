import requests
import tweepy
import string

class Bot:
    def __init__(self):
        self.twitter_oauth = ['twitter token','twitter token'] # twitter login info
        self.twitter_token = ['twitter token', 'twitter token'] # twitter login info
        self.url = ' open weather map url ' # openweathermap.org url

    def weatherUpdate(self):
        auth = tweepy.OAuthHandler(self.twitter_oauth[0], self.twitter_oauth[1]) # twitter login info
        auth.set_access_token(self.twitter_token[0], self.twitter_token[1]) # twitter login info
        api = tweepy.API(auth)
        r = requests.get(self.url)
        json_data = r.json()
        desc = json_data['weather'][0]['description']
        temp = json_data['main']['temp']
        feels_like = json_data['main']['feels_like']
        wind_speed = round(json_data['wind']['speed'] * 2.237, 1)
        fTemp = lambda x: round((x - 273.15) * 9/5 + 32)
        user = api.me()
        post_number = user.statuses_count + 1
        manchester_weather = f'Weather in Manchester TN\n\nSky: {string.capwords(desc)}\nTemp: {fTemp(temp)}°F\nFeels Like: {fTemp(feels_like)}°F\nWind Speed: {wind_speed}mph\n\nI am a bot this was posted automatically\n#{post_number}'
        api.update_status(manchester_weather)

if __name__ == '__main__':
    bot = Bot()
    bot.weatherUpdate()
