import discord
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "imperial"}  
    r = requests.get(url, params=params, timeout=10)

    if r.status_code == 401:
        return "🔑 OpenWeather says the API key is invalid. Double-check it in your `.env`."
    if r.status_code == 404:
        return "🏙️ City not found. Try `City, CountryCode` (e.g., `Paris, FR`)."
    if r.status_code != 200:
        return f"🌐 Weather API error (status {r.status_code})."

    d = r.json()
    name    = d.get("name", "Unknown")
    country = d.get("sys", {}).get("country", "")
    w       = (d.get("weather") or [{}])[0]
    desc    = (w.get("description") or "").title()
    main    = d.get("main", {})
    wind    = d.get("wind", {})

    temp  = main.get("temp", "N/A")
    feels = main.get("feels_like", "N/A")
    hum   = main.get("humidity", "N/A")
    ws    = wind.get("speed", "N/A")

    title = f"{name}, {country}" if country else name
    return (
        f"**{title}**\n"
        f"• {desc}\n"
        f"• Temp: {temp}°F (feels like {feels}°F)\n"
        f"• Humidity: {hum}%\n"
        f"• Wind: {ws} m/s"
    )

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$weather'):
            parts = message.content.split(maxsplit=1)
            if len(parts) == 1:
                await message.channel.send("Usage: `$weather <city>`")
                return
            city = parts[1]
            await message.channel.send(get_weather(city))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
