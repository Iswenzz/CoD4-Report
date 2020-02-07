from bot import ReportBOT, ReportCommands
import os

def main():
    """
    Entry point of the program.
    """
    if os.path.exists("token"):
        with open("token", "r") as f:
            client = ReportBOT(command_prefix=";")
            client.add_cog(ReportCommands())
            client.run(f.read())


if (__name__ == "__main__"):
    main()
