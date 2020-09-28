#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	return 0

def get_word_length_histogram(text):
	histogram = [0]
	for word in text.split():
		length = get_num_letters(word)
		if length >= len(histogram):
			histogram += [0]* (length - len(histogram) + 1)
		histogram[length] += int(length != 0)
	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"

	alignment = len(str(len(histogram) -1))
	#result = ""
	#for i, elem in enumerate(histogram[1:]):
	#	if i == 0:
	#		continue
	#	result += f"{i : >{alignment}} {ROW_CHAR * elem}" + "\n"


	return "\n".join([f"{i : >{alignment}} {ROW_CHAR * elem}" for i, elem in enumerate(histogram) if i !=0])

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	height = max(histogram)	
	for i in range(height -1, -1, -1):
		for j, elem in enumerate(histogram):
			if j == 0:
				continue	
			if elem >= i+1:
				result += BLOCK_CHAR
			else :
				result += " "
		result += "\n"
	result += LINE_CHAR * len(histogram)
	return result

	# for elem in histogram[1:]:
		# result += (BLOCK_CHAR  if  elem >= i +1 else " ") if j != 0 else " "
	# result += "\n"


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
