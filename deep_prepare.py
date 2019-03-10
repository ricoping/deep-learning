#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve,re,random,sys,pprint,os
import mecabing,tools
sys.path.append(os.pardir)
import numpy as np

sh=shelve.open("deep_classify2")

fields=set()
genres=["it-life-hack/", "sports-watch/", "movie-enter/", "dokujo-tsushin/"]

# What kind of word is included as features? 
for genre in genres:
	for file in os.listdir(genre)[:50]:
		try:
			f=open(genre+file); text=f.read(); f.close()
			text=tools.cleaner(text)
			[fields.add(d["word"]) for d in mecabing.mecab2obj(text[:3000]) if not len(d["word"]) < 2]
		except:
			continue

x_data=[]; t_data=[]
for genre in genres:
	data=tools.getData(genres, genre, os.listdir(genre)[:400], fields)
	x_data.extend(data[0])
	t_data.extend(data[1])

x_data_test=[]; t_data_test=[]; meta_test=[]
for genre in genres:
	data=tools.getData(genres, genre, os.listdir(genre)[400:600], fields)
	x_data_test.extend(data[0])
	t_data_test.extend(data[1])
	meta_test.extend(data[2])

sh["fields"]=fields

sh["x_data"]=x_data
sh["t_data"]=t_data

sh["x_data_test"]=x_data_test
sh["t_data_test"]=t_data_test
sh["meta_test"]=meta_test