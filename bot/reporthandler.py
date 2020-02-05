from watchdog.events import FileSystemEventHandler
from discord import Embed

import asyncio

class ReportHandler(FileSystemEventHandler):
    def __init__(self, client):
        self.client = client
        self.mapReports = []
        self.playerReports = []


    def on_modified(self, event):
        if not event.is_directory:
            if "report_map.txt" in event.src_path:
                asyncio.run_coroutine_threadsafe(self.processMapReport(event.src_path), self.client.loop)
            elif "report_player.txt" in event.src_path:
                asyncio.run_coroutine_threadsafe(self.processPlayerReport(event.src_path), self.client.loop)


    async def processMapReport(self, filepath):
        with open(filepath, "r") as f:
            tkn = f.readlines()[-1].split(" ")
            if len(tkn) != 7:
                return
            mapname = tkn[0]
            name = tkn[2]
            selfguid = tkn[4]
            reason = tkn[6]
    
        res = "```yaml\nmap: %s\nauthor: [%s]%s\nreason: %s\n```" % (mapname, selfguid, name, reason)
        if not len(self.mapReports) or self.mapReports[-1] != res:
            self.mapReports.append(res)
            print(res)
            embed = Embed(title="Map Report", description=res, color=0xFF006F)
            channel = self.client.get_channel(674694399598526471)
            await channel.send(embed=embed)


    async def processPlayerReport(self, filepath):
        with open(filepath, "r") as f:
            tkn = f.readlines()[-1].split(" ")
            if len(tkn) != 9:
                return
            name = tkn[0]
            selfguid = tkn[2]
            who = tkn[4]
            whoguid = tkn[6]
            reason = tkn[8]

        res = "```yaml\nauthor: [%s]%s\nreported: [%s]%s\nreason: %s\n```" % (selfguid, name, whoguid, who, reason)
        if not len(self.playerReports) or self.playerReports[-1] != res:
            self.playerReports.append(res)
            print(res)
            embed = Embed(title="Player Report", description=res, color=0xA416F8)
            channel = self.client.get_channel(674694399598526471)
            await channel.send(embed=embed)
