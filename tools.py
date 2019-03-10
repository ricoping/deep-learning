import re, mecabing
import numpy as np
def cleaner(text):
	text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
	text=re.sub('RT', "", text)
	text=re.sub('お気に入り', "", text)
	text=re.sub('まとめ', "", text)
	text=re.sub(r'[!-~]', "", text)
	text=re.sub(r'[︰-＠]', "", text)
	text=re.sub('\n', " ", text)
	text=text.replace("■","")
	text=text.replace("】","")
	text=text.replace("【","")
	return text

def getData(genres, genre, files, fields):
	x_data=[]; t_data=[]; meta=[]
	for file in files:
		try:
			row=[]
			d={}
			f=open(genre+file); text=f.read(); f.close()
			text=cleaner(text)

			data = sorted(mecabing.mecab2obj(text[:3000]), key=lambda x: x["word"])
			for field in fields:
				target=[x for x in filter(lambda d: d["word"] == field, data)]
				if len(target) > 0:
					row.append(target[0]["count"])
				else:
					row.append(0)

			t_data.append(genres.index(genre))
			x_data.append(row)

			d["text"]=text[:500]
			d["genre"]=genre
			d["path"]=genre+file

			meta.append(d)
		except:
			continue
	return [x_data, t_data, meta]

def oneHotify(t_data):
	one_hot_list=[]
	for d in t_data:
		ini = np.zeros(4, dtype=int)
		ini[d] = 1
		one_hot_list.append(ini)
	one_hot=np.array(one_hot_list)
	return one_hot