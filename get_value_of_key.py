from functools import reduce  # forward compatibility for Python 3
import operator

def getbybuiltin(dataDict, keys):
    mapList=keys.split("/")
    return reduce(operator.getitem, mapList, dataDict)

def getbyuserdefined(dic, userkey):

    keys=userkey.split("/")
    for key in keys:
        dic = dic[key]
    return dic



def main():
    choice=input("Enter 1 if you want to try a built-in method. Enter 2 if want to select a user defined method")
    #print(choice)
    object = {"a": {"b": {"x": {"c": "d"}}}}
    if(choice == "1") :
        res = getbybuiltin(object,"a/b/x/c")
    elif(choice == "2"):
        res = getbyuserdefined(object,"a/b/x/c")
    else:
        print("You have entered wrong choice. Reselect")

    print("Your value is: "+res)

  if __name__ == '__main__': main()
