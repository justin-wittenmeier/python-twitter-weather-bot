import requests
import tweepy

auth = tweepy.OAuthHandler('twitter token','twitter token') # twitter login info
auth.set_access_token('twitter token', 'twitter token') # twitter login info
api = tweepy.API(auth)

r = requests.get('open weather map url') # openweathermap.org api

# data from open weather map
json_data = r.json()

# descrption of weather
desc = json_data['weather'][0]['description']

# real temp
temp = json_data['main']['temp']

# feels like temp
feels_like = json_data['main']['feels_like']

# translate wind speed to mph
wind_speed = round(json_data['wind']['speed'] * 2.237, 1)

# func that find the F temp from K
fTemp = lambda x: round((x - 273.15) * 9/5 + 32)

# get number of post from profile to prevent duplicate posts
user = api.me()
post_number = user.statuses_count + 1

manchester_weather = f'Current Weather in Manchester TN\n\nSky: {desc}\nTemp: {fTemp(temp)}°F\nFeels Like: {fTemp(feels_like)}°F\nWind Speed: {wind_speed}mph\n\nI am a bot this was posted automatically #: {post_number}'

api.update_status(manchester_weather)
