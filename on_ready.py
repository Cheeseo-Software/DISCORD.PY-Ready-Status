@bot.event
async def on_ready():
    # You can edit certain things here such as the name ("GTAV", "My Stream", "Spotify", "Netflix")

    # Setting `Playing ` status
    await bot.change_presence(activity=discord.Game(name="GTAV"))

    # Setting `Streaming ` status
    await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

    # Setting `Listening ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))

    # Setting `Watching ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))

    print("Bot is now online!")