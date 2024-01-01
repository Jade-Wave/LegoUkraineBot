from discord import Intents, File
from discord.ext import commands


class BotBase(commands.Bot):

    def __init__(self):
        super(BotBase, self).__init__(intents=Intents.all(), command_prefix="!")
        self.application_token = "MTE5MTQ0ODAzMDMzMTgwMTY4MA.GrgzFR.93IvOob_1FtNhHLnJQN3-IjnOuq_aJiEf65UsQ"

