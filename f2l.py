#!/usr/bin/env/python3

#http://stackoverflow.com/a/15233739

def f2l(file):
	"""Take each line of a file, strip it, and append to a list"""
	list = [line.strip() for line in open(file)]
	return list