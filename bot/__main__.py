from bot.reportbot import ReportBOT
import os

def main():
    if os.path.exists("token"):
        with open("token", "r") as f:
            client = ReportBOT()
            client.run(f.read())


if (__name__ == "__main__"):
    main()
