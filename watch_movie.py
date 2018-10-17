import time

with open("script.txt") as script:
	script = script.read().split("\n")
	for line in script:
		print line
		time.sleep(.3)
