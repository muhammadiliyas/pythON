data = ["Neal","Caffrey","New York"]
print("I'm",data[0],data[1])
print("I'm From",data[2])

data.append("USA")
print(data[3])
data.pop()

data.extend(["USA", 29])
print(data[3],"\nI'm ",data[4],"old.")

target = ["Mexico","Moskow","Madrid","Venice"]
print(target)

target.append("Paris")
target.insert(2,"San Diego")
target.extend(["Vienna","Vern","Basel"])

print("Whole Target : ",target)
print("Done With ",target.pop())

print("Threat Terminated : Paris")
target.remove("Paris")

print("Updated Target ", target)
print("Total Targets :",len(target))

