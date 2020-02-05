from bot.reportbot import ReportBOT
import os

if (__name__ == "__main__"):
    if os.path.exists("token"):
        with open("token", "r") as f:
            client = ReportBOT()
            client.run(f.read())
