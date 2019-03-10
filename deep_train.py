import shelve,re,random,sys,pprint,os
import mecabing,tools
sys.path.append(os.pardir)
import numpy as np
from multi_layer_net import MultiLayerNet
from trainer import Trainer

sh=shelve.open("deep_classify2")

fields=sh["fields"]

x_data=sh["x_data"]
t_data=sh["t_data"]

x_data_test=sh["x_data_test"]
t_data_test=sh["t_data_test"]
meta_test=sh["meta_test"]


x_train=np.array(x_data)
t_train=np.array(t_data)

x_test=np.array(x_data_test)
t_test=np.array(t_data_test)

print(x_train.shape, t_train.shape)
print(x_test.shape, t_test.shape)

#network = TwoLayerNet(input_size=15143, hidden_size=1700, output_size=4)
network = MultiLayerNet(input_size=10336, hidden_size_list=[100,50], output_size=4)

trainer = Trainer(network, x_train, t_train, x_test, t_test,epochs=100, mini_batch_size=100)
trainer.train()
sh["network"]=network

network=sh["network"]
pres=[np.argmax(p, axis=0) for p in network.predict(x_test)]

genres=["it-life-hack/", "sports-watch/", "movie-enter/", "dokujo-tsushin/"]
for i in range(len(pres)):
	print("テキスト（抜粋）: ", meta_test[i]["text"])
	print("")
	print("正しいジャンル: ", genres[t_test[i]])
	print("予測したジャンル: ", genres[pres[i]])
	print("-"*100)

sh.close()