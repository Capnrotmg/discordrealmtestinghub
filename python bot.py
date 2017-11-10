import pip

def install(package):
	pip.main(['install', package]);

#install("requests");
#install("discord.py");
import os;
import discord;
import asyncio;
import requests;
import urllib.request;
import subprocess;
from ExtractFile import extract;
import zipfile;
#=================Functions===============================


def getVersion():
	r = requests.get("http://realmtesting2.appspot.com/version.txt", headers={'User-Agent': 'Mozilla/5.0'});
	print(r.content.decode("utf-8"));
	return r.content.decode("utf-8");

def downloadFile(version):
	print("Downloading file");
	currentPath = os.getcwd();
	fullfilename = os.path.join(currentPath ,  version + ".swf");
	url = "http://realmtesting2.appspot.com/AssembleeGameClient" + version + ".swf";
	urllib.request.urlretrieve (url, fullfilename);
	return fullfilename;

# def extractFile(version):
# 	swfExtractPath = os.path.dirname(os.path.abspath(__file__))+"\SWFTools\\";
# 	outdir = os.path.dirname(os.path.abspath(__file__)) + "\\" + version;
# 	extract(swfExtractPath, os.path.dirname(os.path.abspath(__file__)) + "\\" + version + ".swf", outdir);

# def makeZipFile(version):
# 	zf = zipfile.ZipFile(version+".zip", "w");
# 	for dirname, subdirs, files in os.walk(os.path.dirname(os.path.abspath(__file__)) + "\\" + version):
# 		zf.write(dirname)
# 		for filename in files:
# 			zf.write(os.path.join(dirname, filename))
# 	zf.close()

#==================Main=======================================

client = discord.Client();
currentVersion = "";
channelId = "371707295865896965";

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
       await client.send_message(client.get_channel(channelId), 'Testing');
    if message.content.startswith('!update'):
    	await doOnCommand();

async def doOnCommand():
	global currentVersion;
	version =getVersion();
	if (version != currentVersion):
		await client.send_message(client.get_channel(channelId), 'New version detected, please wait while I process the file');
		currentVersion =version;
		downloadFile(currentVersion);
	await client.send_file(client.get_channel(channelId), os.path.dirname(os.path.abspath(__file__)) + "\\" + version + ".swf");
	await client.change_presence(game=discord.Game(name='Acquiring latest testing patch, please wait...'))
	print("Done");


client.run('MzcxNzA3OTIwMTIxMDY5NTY5.DM5oNw.rKGn-Cp8ZqtwdmvpSCCtoe_n9Tk');
