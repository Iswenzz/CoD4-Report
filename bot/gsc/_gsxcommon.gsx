WriteToFile(path, string)
{
	checkQueue();

	file = FS_FOpen(path, "append");
	level.openFiles++;
	FS_WriteLine(file, string);

	FS_FClose(file);
	level.openFiles--;
	return true;
}

readAll(a)
{
	checkQueue();
	file = FS_FOpen(a, "read");
	level.openFiles++;

	array = [];
	while (true)
	{
		line = FS_ReadLine(file);
		if (isDefined(line))
			array[array.size] = line;
		else
			break;
	}
	FS_FClose(file);
	level.openFiles--;
	return array;
}

deleteFile(a)
{
	FS_Remove(a);
}

checkQueue()
{
	while (level.openFiles > 8)
		wait .05;
}

checkfile(a)
{
	return FS_TestFile(a);
}
