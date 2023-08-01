dec={ 1:{"name":"john","age":27,"sex":"male"},
      2:{"name":"marie","age":13,"sex":"female"},
      3:{"name":"sali","age":23,"sex":"female"},
    }


for key, item in dec.items():
    if item ["age"] > 22 :
        print( item["name"])
        
x=dict(sorted(dec.items(), key=lambda dec:dec[1]["age"]))
print(x)


    

