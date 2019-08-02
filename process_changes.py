#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:31:14 2017

@author: muditkapoor
"""

def read_file(any_file):

    data = [line.strip() for line in open(any_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            
            details = data[index + 1].split('|')
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'time': details[2].strip().split(' ')[1],
                'number_of_lines': details[3].strip().split(' ')[0]
            }
           
            commits.append(commit)
           
            index = data.index(sep, index + 1)
        except IndexError:
            index = len(data) #break
    return commits

def save_commits (commits, any_file):
    my_file=open(any_file, 'w')
    my_file.write("revision,author,date,time,number_of_lines\n")
    for commit in commits:
        my_file.write(commit['revision']+','+ commit ['author']+
                      ','+ commit['date']+',' + commit['time']+','+ commit['number_of_lines'] + '\n')
    my_file.close()


if __name__ == '__main__':

    import os
    os.chdir('/Users/muditkapoor/Desktop/Big Data')
    os.getcwd()

 
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    print len(data)
    commits = get_commits(data)
    print len(commits)
    print commits[0]
    print commits[0]['author']
    save_commits(commits, 'changes.csv')
    

    