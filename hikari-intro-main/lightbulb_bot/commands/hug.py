import hikari
import lightbulb
from lightbulb import commands


# The options the command will have. This creates a required member
# option. Validation is handled for you -- Discord won't let you
# send the command unless it's a valid member.
@lightbulb.option("target", "The member you wish to hug.", hikari.Member)
# Convert the function into a command
@lightbulb.command("hug", "hug someone in the server!")
# Define the types of command that this function will implement
@lightbulb.implements(commands.SlashCommand)
async def hug(ctx: lightbulb.context.Context) -> None:
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

    embed = (hikari.Embed(
            title="Hugged" 'ctx',
    ))




















def load(bot: lightbulb.BotApp):
    bot.command(hug)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("hug"))
