import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")

args = parser.parse_args()
inputFile = args.file

with open(inputFile) as f:
	jsonData = json.load(f)

if (len(jsonData['included']) > 1):
	for x in range(10,20):
		fullName = jsonData['included'][x]['title']['text']
		if (fullName == 'LinkedIn Member' or fullName == ''):
			continue
		else:
			print(jsonData['included'][x]['title']['text']+":"+jsonData['included'][x]['primarySubtitle']['text'])+":"+jsonData['included'][x]['secondarySubtitle']['text']
else:
	for x in range(10,len(jsonData['data']['elements'])):
		fullName = jsonData['data']['elements'][x]['title']['text']
		if (fullName == 'LinkedIn Member' or fullName == ''):
			continue
		else:
			print(jsonData['data']['elements'][x]['title']['text']+":"+jsonData['data']['elements'][x]['primarySubtitle']['text'])+":"+jsonData['data']['elements'][x]['secondarySubtitle']['text']
