from bot.reportbot import ReportBOT

if (__name__ == "__main__"):
    with open("token", "r") as f:
        client = ReportBOT()
        client.run(f.read())
