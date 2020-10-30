# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:11:56 2020

@author: Mariie
"""

import json
Conocimiento = False
a = 0
palabras = ["Que","Video","Chale","Top","Ni","pedo","¡","!",":","vayan","pedo","wey","Historia","juegos","Nuevo"]

with open("tweets.json","r") as read_file:
	data = json.load(read_file)
	Conocimiento = data['Tweets']

def Mat(matriz):
	print()
	a = 0
	data = {}
	data["Probabilidades"] = []
	while a < len(matriz):
		data["Probabilidades"].append([matriz[a][0],matriz[a][4]])
		a = a + 1
	with open('tweets.json', 'w') as file:
		json.dump(data, file, indent=1)
	with open("tweets.json","r") as read_file:
		data = json.load(read_file)
		tweet = data["Probabilidades"]
	return(tweet)

def buscar(tweet,palabras):
	i=0
	j=[]
	k=[]
	while i<len(tweet):
		a=0
		while a<len(tweet[i]):
			if not tweet[i][a] in palabras:
				b=tweet[i][a]
				j=j+[b]
			a=a+1
		i=i+1
	i=0
    
	while i<len(j):
		if not j[i] in k:
			k=k+[j[i]]
		i=i+1 
	return Mat(j,k, len(tweet))

def split(tweets,palabras,x = []):
	a=0
	while a<len(tweets):
		tweet=tweets[a]
		Stream=tweet['Stream']
		texto=tweet['texto']
		if Stream==True:
			texto=texto.split()
			x=x+[texto]
		a=a+1
	return buscar(x,palabras)