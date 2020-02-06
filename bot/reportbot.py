from watchdog.observers import Observer
from pathlib import Path
from bot.reporthandler import ReportHandler
from discord.ext import commands

import os
import sys

class ReportBOT(commands.Bot):
    async def on_ready(self):
        print("Logged in as\n%s\n%s\n------" % (self.user.name, self.user.id))
        dir_path = sys.argv[1] if len(sys.argv) > 1 else str(Path(os.getcwd()) / "bot" / "tests")
        print("[Watchdog]: %s" % dir_path)

        observer = Observer()
        observer.schedule(ReportHandler(self), dir_path, recursive=True)
        observer.start()
