#include src\_gsxcommon;

commands(a, arg) // add this to a command callback.
{
	players = getEntArray( "player", "classname" );

	switch(a)
	{	
		case "reportplayer":
			wait 0.05;

			if(!isDefined(arg) || arg == "")
			{
				self iprintlnbold("!reportplayer <playerName> <reason>");
				break;
			}

			tkn = StrTok(arg," ");

			if(tkn.size < 2)
			{
				self iprintlnbold("!reportplayer <playerName> <reason>");
				break;
			}

			id = getPlayerByName(tkn[0]);

			if(!isDefined(tkn[1]) || tkn[1] == "")
			{
				self iprintlnbold("!reportplayer <playerName> <reason>");
				break;
			}

			if(id.size > 1 || id.size == 0)
			{
				self IPrintLnBold("Could not find player");
				break;
			}

			string = "";

			for(i=1;i<tkn.size;i++)
				string += tkn[i]+" ";

			if( isDefined( players[id[0]] ) )
				self recordReportPlayer( string, players[id[0]] );

			break;
			
		case "reportmap":
			wait 0.05;
			
			if(!isDefined(arg) || arg == "")
			{
				self iprintlnbold("!reportplayer <reason>");
				break;
			}
			
			tkn = StrTok(arg," ");
			
			if(tkn.size < 1)
			{
				self iprintlnbold("!reportplayer <reason>"); 
				break;
			}

			string = "";

			for(i=0;i<tkn.size;i++)
				string += tkn[i]+" ";

			self recordReportMap(string);

			break;

		default:
			break;
	}
}

getPlayerByNum( pNum ) 
{
	players = getEntArray( "player", "classname" );
	x = [];

	for (i = 0; i < players.size; i++)
	{
		if (players[i] getEntityNumber() == int(pNum)) 
			x[x.size] = i;
	}

	return x;
}

getPlayerByName( nickname ) 
{
	players = getEntArray( "player", "classname" );
	x = [];

	for (i = 0; i < players.size; i++)
	{
		if (isSubStr(toLower(players[i].name), toLower(nickname) )) 
			x[x.size] = i;
	}

	return x;
}

recordReportMap(argument)
{
	self.guid = getSubStr(self getGuid(), 24, 32);
	line = "";

	if(isDefined(argument))
		line += level.mapName + " name: " + self.name + " selfguid: " + self.guid + " arg: " + argument;
	else
		return;
	
	path = "./server_data/report_map.txt";
	file_exists = checkfile(path);
	
	if(!file_exists)
	{
		checkQueue();
		new = FS_Fopen(path, "write");
		FS_FClose(new);
	}

	WriteToFile(path, line);
}

recordReportPlayer(argument, player)
{
	self.guid = getSubStr(self getGuid(), 24, 32);
	line = "";

	if(isDefined(argument))
		line += self.name + " selfguid: " + self.guid + " who: " + player.name + " whoguid: " + player.guid + " arg: " + argument;
	else
		return;
	
	path = "./server_data/report_player.txt";
	file_exists = checkfile(path);

	if(!file_exists)
	{
		checkQueue();
		new = FS_Fopen(path, "write");
		FS_FClose(new);
	}

	WriteToFile(path, line);
}