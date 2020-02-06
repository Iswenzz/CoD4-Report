from bot.reportbot import ReportBOT
from bot.commands import ReportCommands
import os

def main():
    if os.path.exists("token"):
        with open("token", "r") as f:
            client = ReportBOT(command_prefix=";")
            client.add_cog(ReportCommands())
            client.run(f.read())


if (__name__ == "__main__"):
    main()
