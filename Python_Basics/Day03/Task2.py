Units= int(input("Enter Units:"))
if Units<100:
    print("No Charge")#Unit less then 100
elif Units>=100 and Units<=300:
    print("Normal USage") #Unit between 100-300
else:
    print("High Usage-Save Energy!")

