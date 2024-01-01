from .bot_base import BotBase


def main():
    bot = BotBase()

    @bot.command(name="info")
    async def info(message):
        await message.channel.send("Response incoming!")

    return bot
