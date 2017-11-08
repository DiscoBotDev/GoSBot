import discord
from discord.ext import commands
import requests as req 

bot = commands.Bot(command_prefix='Gos!', description='Real Life TB simulator')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.user)
    print('------')

@bot.command()
#GOS Command List
async def Help():
    await bot.say("Here are my commands: Gos!Players, Gos!NoPlayers, Gos!PlayerRoom, Gos!GamesRoom, Gos!Games")

@bot.command()
#Players online
async def Players():
	myrgard = req.get('http://metaserver.gateofstorms.net:8080/status.json')
	myr = myrgard.json()

	playersingame = [];

	rooms = myr['rooms']

	for room in rooms:
		players = room['players']

		for player in players:
			playersingame.append(player['nick_name'])

	count = len(playersingame)
	playerspeak = f"Here are the number of players on Gate of Storms: {count}"
	await bot.say(playerspeak)

	for play in playersingame:
		await bot.say(play)


@bot.command()
#Players total
async def NoPlayers():
	myrgard = req.get('http://metaserver.gateofstorms.net:8080/status.json')
	myr = myrgard.json()

	playersingame = [];

	rooms = myr['rooms']

	for room in rooms:
		players = room['players']
		print(players)
		for player in players:
			playersingame.append(player['nick_name'])

	count = len(playersingame)
	playerspeak = f"Here are the number of players on Gate of Storms: {count}"
	await bot.say(playerspeak)

@bot.command()
#Players in each Room.
async def PlayerRoom():
	myrgard = req.get('http://metaserver.gateofstorms.net:8080/status.json')
	myr = myrgard.json()

	rooms = myr['rooms']

	for room in rooms:
		name = room['name']
		playersinroom = []
		for player in room['players']:
			playersinroom.append(player['nick_name'])
		count = len(playersinroom)
		roomspeak = f"In Room: {name} there are {count} number of players"
		await bot.say(roomspeak)
		for play in playersinroom:
			await bot.say(play)
		
@bot.command()
#Games in each Room.
async def GamesRoom():
	myrgard = req.get('http://metaserver.gateofstorms.net:8080/status.json')
	myr = myrgard.json()

	rooms = myr['rooms']

	for room in rooms:
		name = room['name']
		games = []
		maps = []
		players = []
		timeplayed = []
		for game in room['games']:
			games.append(game['name'])
			maps.append(game['map_name'])
			players.append(game['players'])
			timeplayed.append(int(game['elapsed_seconds']))
		gamesinroom = f"Here are the games played in: {name}"
		await bot.say(gamesinroom)
		for i in range(0, len(games)):
			namegame = games[i]
			mapgame = maps[i]
			playersgame = players[i]
			timepl = round(timeplayed[i] / 60)
			play = f"The game {namegame} is being played on {mapgame}. It has {playersgame} players and has gone on for {timepl} minutes."
			await bot.say(play)

@bot.command()
#Games total.
async def Games():
	myrgard = req.get('http://metaserver.gateofstorms.net:8080/status.json')
	myr = myrgard.json()

	rooms = myr['rooms']

	games = []
	maps = []
	players = []
	timeplayed = []

	for room in rooms:

		for game in room['games']:
			games.append(game['name'])
			maps.append(game['map_name'])
			players.append(game['players'])
			timeplayed.append(int(game['elapsed_seconds']))
	
	count = len(games)
	countinroom = f"Here are the total number of games played on GoS: {count}"
	await bot.say(countinroom)
	for i in range(0, len(games)):
			namegame = games[i]
			mapgame = maps[i]
			playersgame = players[i]
			timepl = round(timeplayed[i] / 60)
			play = f"The game {namegame} is being played on {mapgame}. It has {playersgame} players and has gone on for {timepl} minutes."
			await bot.say(play)

bot.run(#Insert Token Here)

