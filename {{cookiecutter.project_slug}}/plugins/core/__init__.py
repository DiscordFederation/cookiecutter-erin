from core.error import CommandError
from core.navigation import Help
from core.startup import Login

plugin_data = {
    "name": "Core Plugins"
}


def setup(bot):
    bot.add_cog(CommandError(bot))
    bot.add_cog(Help(bot))
    bot.add_cog(Login(bot))
