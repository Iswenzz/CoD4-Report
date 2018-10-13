import time
from datetime import datetime
import os
import re
import discord
import asyncio

client = discord.Client()

def reportMap(file):

        split_string = [0] * 5
        global last_time_info_map

        try:
                if last_time_info_map is not None:
                                
                        get_time = time.ctime(os.path.getmtime(file))
                        datetime_object = datetime.strptime(get_time, '%a %b %d %H:%M:%S %Y')
                        time_info = datetime_object.strftime("%H %M %S")

                        if last_time_info_map == time_info:
                                return 'null'
                        else:
                                last_time_info_map = time_info
                                with open(file, 'r') as f:
                                        
                                        lines = f.read().splitlines()
                                        last_line = lines[-1]
                                        split_string[0] = re.split(' (?=name: )', last_line)
                                        split_string[1] = re.split(' (?=selfguid: )', split_string[0][1])
                                        split_string[2] = re.split(' (?=arg: )', split_string[1][1])
                                        return '```elixir\nmap: ' + split_string[0][0] + '\n' + split_string[1][0] + ' [' + split_string[2][0] + ']\n' + split_string[2][1] + '\n```'
                                        
        except NameError:
                        
                get_time = time.ctime(os.path.getmtime(file))
                datetime_object = datetime.strptime(get_time, '%a %b %d %H:%M:%S %Y')
                time_info = datetime_object.strftime("%H %M %S")
                last_time_info_map = time_info

                with open(file, 'r') as f:
                                
                        lines = f.read().splitlines()
                        last_line = lines[-1]
                        split_string[0] = re.split(' (?=name: )', last_line)
                        split_string[1] = re.split(' (?=selfguid: )', split_string[0][1])
                        split_string[2] = re.split(' (?=arg: )', split_string[1][1])
                        return '```elixir\nmap: ' + split_string[0][0] + '\n' + split_string[1][0] + ' [' + split_string[2][0] + ']\n' + split_string[2][1] + '\n```'

def reportPlayer(file):

        split_string = [0] * 5
        global last_time_info_player

        try:
                if last_time_info_player is not None:
                                
                        get_time = time.ctime(os.path.getmtime(file))
                        datetime_object = datetime.strptime(get_time, '%a %b %d %H:%M:%S %Y')
                        time_info = datetime_object.strftime("%H %M %S")

                        if last_time_info_player == time_info:
                                return 'null'
                        else:
                                last_time_info_player = time_info
                                with open(file, 'r') as f:
                                        
                                        lines = f.read().splitlines()
                                        last_line = lines[-1]
                                        split_string[0] = re.split(' (?=selfguid: )', last_line)
                                        split_string[1] = re.split(' (?=who: )', split_string[0][1])
                                        split_string[2] = re.split(' (?=whoguid: )', split_string[1][1])
                                        split_string[3] = re.split(' (?=arg: )', split_string[2][1])
                                        return '```elixir\nname: ' + split_string[0][0] + ' [' + split_string[1][0] + ']\n' + split_string[2][0] + ' [' + split_string[3][0] + ']\n' + split_string[3][1] + '\n```'
                                        
        except NameError:
                        
                get_time = time.ctime(os.path.getmtime(file))
                datetime_object = datetime.strptime(get_time, '%a %b %d %H:%M:%S %Y')
                time_info = datetime_object.strftime("%H %M %S")
                last_time_info_player = time_info

                with open(file, 'r') as f:
                                
                        lines = f.read().splitlines()
                        last_line = lines[-1]
                        split_string[0] = re.split(' (?=selfguid: )', last_line)
                        split_string[1] = re.split(' (?=who: )', split_string[0][1])
                        split_string[2] = re.split(' (?=whoguid: )', split_string[1][1])
                        split_string[3] = re.split(' (?=arg: )', split_string[2][1])
                        return '```elixir\nname: ' + split_string[0][0] + ' [' + split_string[1][0] + ']\n' + split_string[2][0] + ' [' + split_string[3][0] + ']\n' + split_string[3][1] + '\n```'

@client.event
async def on_ready():
        
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        
        while True:
                
                rep_map = reportMap('./report_map.txt')
                rep_player = reportPlayer('./report_player.txt')
                
                if rep_map != 'null':
                        await client.send_message(client.get_channel('400675751738867733'), rep_map)
                        print(rep_map)
                if rep_player != 'null':
                        await client.send_message(client.get_channel('406484699414921216'), rep_player)
                        print(rep_player)
                        
                await asyncio.sleep(5)

client.run('TOKEN HERE')
