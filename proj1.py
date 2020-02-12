# File:        proj1.py                                                     
# Author:      Barnes Williams                                                  
# Date:        02/09/2020                                                                                                              
# E-mail:      wi3@umbc.edu                                                    
# Description: The objective of this assignment is to compare two approaches to tokenize 
#              and downcase all words in a collection of HTML documents.

import os
import html2text
#import re
import time
import matplotlib.pyplot as plt
import numpy as np
import sys

def main():

	#setting up html2text
	h = html2text.HTML2Text()
	h.ignore_links = True
	h.ignore_images = True

	#paths to access html files and write to output text files
	path = "/Users/ni/Desktop/CMSC476/files"
	path1 ="/Users/ni/Desktop/CMSC476/outputs/output"


	start = time.time()
	time_plot = []
	numFiles = 1

	#gets each file in the directory of html files
	files = os.listdir(path)

	#Keeps track of all tokens from every document used for the frequencies
	allTokens = list()

	#Loops through list of files, opens file, changes the html to text
	#generates single tokens/words and writes it to new file called
	#output with the file number it is
	#fileNumber = 1;
	for file in sorted(files):
	    fileName = os.path.join(path,file)
	    htmlFile = open(fileName, 'r')
	    try:
	    	formatedHtml = htmlFile.read().lower()
	    	newText = h.handle(formatedHtml)
	    	textTokens = newText
	    	allTokens.append(textTokens)
	    	htmlFile.close()
	    	output = open(path1+str(numFiles)+'.txt', 'w')
	    	output.write(str(textTokens))
	    	output.close()
	    	numFiles = numFiles+1
	    	timeAmount = time.time()
	    	time_plot.append(round(timeAmount - start, 2))
	    	#print(fileName)
	    except:
	    	print("ERRORRRRRRRRRRRRRRRRRRR")
	#print(allTokens)

	#takes the text and adds quotations on the words
	#print(allTokens)
	tmpTokens = "".join(allTokens)

	#for k in tmpTokens.split():
	#	final = re.sub(r"[^a-zA-Z0-9]+", ' ',k)

	#create dictionary and  order the tokens key value pair by frequency
	tokenCounts = {}

	#splits the text
	finalTokens = tmpTokens.split()
	#print(finalTokens)


	#keeps track of how many times a token is counted
	for word in finalTokens:
		if(word in tokenCounts):
			tokenCounts[word] = tokenCounts[word]+1
		else:
			tokenCounts[word] = 1


	#Creates a frequency file based on frequency by fequency(value of key value pair)
	frequencyFile = open(path1+"frequencyfile.txt", 'w')
	for key, value in sorted(tokenCounts.items(), key= lambda x:x[1]):#, reverse=True):
		frequencyFile.write("\n")
		frequencyFile.write(str(key))
		frequencyFile.write("\t"+" : ")
		frequencyFile.write(str(value))
	frequencyFile.close()


	#Creates a frequency file based on tokens by token(key of key value pair)
	tokenFile = open(path1+"tokenfile.txt", 'w')
	for key in sorted(tokenCounts.keys()):
		tokenFile.write("\n")
		tokenFile.write(str(key))
		tokenFile.write("\t"+" : ")
		tokenFile.write(str(tokenCounts[key]))
	tokenFile.close()

	#Creats the graph of number of documents processed vs time
	file_plot = [num for num in range(1, numFiles)]
	fig = plt.figure()
	plt.plot(time_plot, file_plot)
	plt.title('Rate of Document Processing of Inverted Index')
	plt.ylabel("Number of Documents")
	plt.xlabel("Time(seconds)")
	plt.savefig("Program_Process_Time.png")
	plt.show()

main()
