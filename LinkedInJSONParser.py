import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")

args = parser.parse_args()
inputFile = args.file

with open(inputFile) as f:
	jsonData = json.load(f)

for x in range(0,len(jsonData['data']['elements'][0]['elements'])):
	fullName = jsonData['data']['elements'][0]['elements'][x]['title']['text']
	if (fullName == 'LinkedIn Member' or fullName == ''):
		continue
	else:
		print(jsonData['data']['elements'][0]['elements'][x]['title']['text']+":"+jsonData['data']['elements'][0]['elements'][x]['headline']['text'])+":"+jsonData['data']['elements'][0]['elements'][x]['subline']['text']
