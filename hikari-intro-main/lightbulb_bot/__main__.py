import os

import hikari
import lightbulb
import lightbulb_bot
import aiohttp

def create_bot() -> lightbulb.BotApp:
    # Load the token from a secrets file you'll need to create yourself.
    with open("./secrets/token.py") as f:
        token = f.read().strip()

    # Create the main bot instance with all intents.
    bot = lightbulb.BotApp(
        token=token,
        prefix="!",
        intents=hikari.Intents.ALL,
        default_enabled_guilds=lightbulb_bot.GUILD_ID,
    )

    @bot.listen()
    async def on_starting(event: hikari.StartingEvent) -> None:
        bot.d.aio_session = aiohttp.ClientSession()

    @bot.listen()
    async def on_stopping(event: hikari.StoppingEvent) -> None:
        await bot.d.aio_session.close()

    # Load all extensions.
    bot.load_extensions_from("./commands")

    return bot


if __name__ == "__main__":
    if os.name != "nt":
        # uvloop is only available on UNIX systems, but instead of
        # coding for the OS, we include this if statement to make life
        # easier.
        import uvloop

        uvloop.install()

    # Create and run the bot.
    create_bot().run()
