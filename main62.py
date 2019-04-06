import json
data ='{"var1":"vishal","var2":54}'
print(data)
par = json.loads(data)
print(par['var1'])
data2={
    "cars":['ferrari','audi r8','lambo'],
    "channel_name":"vishal_sagar",
    "house":('food',400),
    "doll":False
}
j=json.dumps(data2["doll"])
print(j)
