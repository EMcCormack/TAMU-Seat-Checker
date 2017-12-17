#!/usr/bin/env/python3

# http://stackoverflow.com/a/15233739


def file_to_list(file):
    """Take each line of a file, strip it, and append to a list"""
    return [line.strip() for line in open(file)]
