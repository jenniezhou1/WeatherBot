<h1>WeatherBot – Discord Weather Responder</h1>

<h2>Description</h2>
WeatherBot is a Python Discord bot that listens for the command <code>$weather &lt;city&gt;</code> (e.g., <code>$weather Los Angeles</code>) and replies with current conditions fetched from the OpenWeather API. It uses <code>discord.py</code> to read messages and send replies, <code>requests</code> to call the weather API, and <code>python-dotenv</code> to keep API keys out of source control.
<br />

<h2>Languages and Utilities Used</h2>

- <b>Python 3.10+</b>
- <b>discord.py (2.x)</b>
- <b>requests</b>
- <b>python-dotenv</b> (loads tokens from <code>.env</code>)
- <b>OpenWeather API</b> (<code>https://openweathermap.org/api</code>)

<h2>Environments Used</h2>

- <b>macOS</b> 

<h2>Program walk-through </h2>

<b>1) Open the project folder</b>
<br />
Open a terminal in the repository folder containing the bot:
<pre><code>cd weatherbot
</code></pre>

<b>2) Create <code>.env</code> with tokens</b>
<br />
Create a file named <code>.env</code> in the same folder as your bot file (e.g., <code>bot2.py</code>):
<pre><code>DISCORD_TOKEN=your_discord_bot_token_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
</code></pre>

<b>3) Install dependencies</b>
<pre><code>python3 -m pip install -U discord.py requests python-dotenv
</code></pre>

<b>4) (One-time) Invite the bot to your server</b>
<br />
In the Discord Developer Portal, use OAuth2 → URL Generator with scope <code>bot</code> and permission <code>Send Messages</code>, then add the bot to your server. Ensure <b>Message Content Intent</b> is enabled under Bot → Privileged Gateway Intents.

<b>5) Run the bot</b>
<pre><code>python3 bot2.py
</code></pre>
Expected terminal output:
<pre><code>Logged on as WeatherBot#xxxx!
</code></pre>

<b>6) Use in Discord</b>
<pre><code>$weather Los Angeles
</code></pre>
The bot replies with a formatted summary, e.g.:
<pre><code>Los Angeles, US
• Overcast Clouds
• Temp: 68.0°F (feels like 67.1°F)
• Humidity: 85%
• Wind: 4.1 mph
</code></pre>

<h2>Notes / Troubleshooting</h2>

- <b>Key not working (401):</b> OpenWeather keys can take a few minutes to activate. Verify the exact value in <code>.env</code> and restart the bot.  
- <b>City not found (404):</b> Try <code>City, CountryCode</code> (e.g., <code>Paris, FR</code>).  
- <b>No response to commands:</b> Confirm the bot is online, has Read/Send permissions, and <b>Message Content Intent</b> is enabled.  
- <b>Multiple replies:</b> Only run one process. Stop extra terminals with <code>Ctrl+C</code>.  
- <b>Keep secrets safe:</b> Do not commit <code>.env</code>; add it to <code>.gitignore</code>.  
- <b>macOS SSL error (system Python):</b>
<pre><code>/Applications/Python\ 3.10/Install\ Certificates.command
</code></pre>
