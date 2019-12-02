import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")

args = parser.parse_args()
fileName = args.file

with open(fileName) as f:
	contents = f.read()
	splitContents = contents.split("\r\n\r\n")
	newContents = splitContents[1]
	g = open(fileName+"_clean.json", "w")
	g.write(newContents)
