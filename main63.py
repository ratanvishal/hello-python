import pickle
# insertion of pickle file create pickle file
vish=["audi","bmw","ferrai","g wagan","suzuki"]
file="myvish.pkl"
fileobj=open(file,'wb')
pickle.dump(vish,fileobj)
fileobj.close()
# reading of pickle file from binary
file="myvish.pkl"
fileobj=open(file,'rb')
my=pickle.load(fileobj)
print(my)
print(type(my))
