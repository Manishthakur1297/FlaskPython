from Emp import *;
from InvalidChoiceException import *;
from numpy import *;
import numpy as np;
import pickle;
#from RestService import *;
#from RestServiceClient import *;

def displayEmp(a):
    for i in a:
         print("Name : "+i.name+"\nAge : "+str(i.age) + "\nSalary : "+str(i.salary) + "\nDesignation : "+i.designation+"\n")


def main():
    #arr = array([],Emp)
    f1 = open("person.ser","rb")
    res = pickle.load(f1)
    arr = []
    for i in res:
        arr.append(i)
    f1.close()
    while(True):
        print("-"*30)
        print("1. Create")
        print("2. Display")
        print("3. Raise Salary")
        print("4. Exit")
        print("-"*30)
        try:
            mChoice = int(input("Enter Choice : "))
            if(mChoice<1 or mChoice>4):
                raise InvalidChoiceException
        except (ValueError, InvalidChoiceException):
            print("Enter number only between [1-4]")
            mChoice = InvalidChoiceException.readChoice()
        except Exception as e:
            print("Error : ",e)
        
        if(mChoice==1):
                f1 = open("person.ser","wb")
                while(True):
                    print("-"*30)
                    print("1. Clerk")
                    print("2. Programmer")
                    print("3. Manager")
                    print("4. Exit")
                    print("-"*30)
                    try:
                        sChoice = int(input("Enter Choice : "))
                        if(sChoice<1 or sChoice>4):
                            raise InvalidChoiceException
                    except (ValueError, InvalidChoiceException):
                        print("Enter number only between [1-4]")
                        sChoice = InvalidChoiceException.readChoice()
                    except Exception as e:
                        print("Error : ",e)
                    if(sChoice==1):
                        #arr = np.append(arr,Clerk())
                        arr.append(Clerk())
                    elif(sChoice==2):
                        #arr = np.append(arr,Programmer())
                        arr.append(Programmer())
                    elif(sChoice==3):
                        #arr = np.append(arr,Manager())
                        arr.append(Manager())
                    else:
                        pickle.dump(arr,f1)
                        f1.close()
                        break

        elif(mChoice==2):
            f1 = open("person.ser","rb")
            res = pickle.load(f1)
            results =[]
            for i in res:
                print(i)
                results.append({"Name : ": i.name,
                            "Age : ": i.age,
                            "Salary : ": i.salary,
                            "Designation : ": i.designation})
            print(results)
            
        elif(mChoice==3):
            for i in arr:
                DuckType.raiseAllSalary(i)
        else:
            break

        
    print("Total Employee Created : ",Emp.count)
