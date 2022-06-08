import hikari
import lightbulb
from lightbulb import commands
import asyncio
import aiohttp

# The options the command will have. This creates a required member
# option. Validation is handled for you -- Discord won't let you
# send the command unless it's a valid member.
@lightbulb.option("target", "The member you wish to hug.", hikari.Member)
# Convert the function into a command
@lightbulb.command("hug", "hug someone in the server!")
# Define the types of command that this function will implement
@lightbulb.implements(commands.SlashCommand)
async def hug(ctx: lightbulb.context.Context,) -> None:
    target_ = ctx.options.target
    # Convert the option into a Member object if lightbulb couldn't resolve it automatically
    target = (
        target_
        if isinstance(target_, hikari.Member)
        else ctx.get_guild().get_member(target_)
    )
    if not target:
        await ctx.respond("That user is not in the server.")
        return

    embed = hikari.Embed(title=" ", description="An example hikari embed")
    embed.add_field("Field name", "Field content (value)")
    embed.set_thumbnail("https://some-random-api.ml/animu/hug")
    embed.set_footer("This is the footer")


    await ctx.respond(embed)



















def load(bot: lightbulb.BotApp):
    bot.command(hug)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("hug"))
