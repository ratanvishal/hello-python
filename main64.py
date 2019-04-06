import pickle
import requests
url='http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
respons=requests.get(url)
restext=respons.text
data=restext.splitlines()
read=[[i] for i in data]
fileobj=open('irisData.pkl','wb')
pickle.dump(read,fileobj)
fileobj.close()


fileobj=open('irisData.pkl','rb')
data=pickle.load(fileobj)
print(data)
