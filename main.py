from datetime import date, datetime
import pandas as pd
today = date.today()
now = datetime.now()

''' Defining constants '''
FILE_NAME = 'Cars.csv'
COLUMNS = ["SNo","Name", "Car Number", "Phone Number",
           "Date", "Entry Time", "Exit Time",]
AuthEmail = 'Python'
AuthPass = 'Python'


def length():
    ''' Function gives the lenght of columns '''
    
    df = pd.read_csv(FILE_NAME, encoding='latin1', index_col=0)
    count = 0
    for i in df["Name"]:
        count+=1
    return count 

    
def isCarExist(carNumber):
    '''Function to check the car exist or not in database'''

    try:
        df =pd.read_csv(FILE_NAME)
        for i in df.index:
            if df["Car Number"][i] == carNumber:
                return True
        return False
    except:
        print("Something went wrong")



def addCar():
    '''Function for adding car details'''

    isFileExist = False
    try:
        df = pd.read_csv(FILE_NAME, encoding='latin1', index_col=0)
        isFileExist = True
    except:
        print("File doest not exist")
        print(f"Creating a CSV file named {FILE_NAME}")

    name = input("Enter name of driver : ")
    phone = input("Enter contact number : ")
    carNumber = input("Enter Car Number : ")
    d = today.strftime("%d/%m/%Y")
    entryTime = now.strftime("%H:%M:%S")
    exitTime = " - "
    if name != "" and phone != "" and carNumber != "" and d != "" and entryTime != "" and exitTime != "":

        sampleData = [
            1, name, carNumber, phone, d, entryTime, exitTime
        ]
    else:
        print("Cannot be NULL")
        return

    if not isFileExist:
        try:
            data = pd.DataFrame(data=[sampleData], columns=COLUMNS)
            data.to_csv(path_or_buf=FILE_NAME, index=False)
            print(f"Car {carNumber} added in database")

        except:
            print("Something went wrong")
    else:
        l = length()
        sampleData = [
            l+1, name, carNumber, phone, d, entryTime, exitTime,
        ]
        try:
            data = pd.DataFrame(data=[sampleData], columns=COLUMNS)
            data.to_csv(path_or_buf=FILE_NAME, mode='a', header=False, index=False)
            print(f"Car {carNumber} added in database")

        except:
            print("Something went wrong")


def freeAParkedCar():
    ''' Function to free a parked Car'''

    carNumber = input("Enter car Number : ")
    exitTime = now.strftime("%H:%M:%S")
    df = pd.read_csv(FILE_NAME)
    if isCarExist(carNumber=carNumber):
        index = df[df['Car Number'] == carNumber].index[0]
        df.at[index, "Exit Time"] = exitTime
        df.to_csv(FILE_NAME, index=False)




def carDetails(carNumber, index):
    '''Function to print specific car's details'''
    
    try:
        df = pd.read_csv(FILE_NAME)
        print(f"Car Number - {carNumber}")
        print(f'''Driver name - {df["Name"][index]}''')
        print(f'''Phone Number - {df["Phone Number"][index]}''')
        print(f'''Date - {df["Date"][index]}''')
        print(f'''Entry Time - {df["Entry Time"][index]}''')
        print(f'''Exit Time - {df["Exit Time"][index]}''')
    except:
        print("Something went wrong")




def searchCar():
    '''Function for seaching a particular car according to different methods '''

    try:
        choice = int(input("Enter your choice : "))
        isFound = False
        carNum = input("Enter car number : ")
        df = pd.read_csv(FILE_NAME)
        index = 0
        for i in df.index:
            if df["Car Number"][i] == carNum:
                index+=1
                print("Car Found")
                isFound = True
                ch = input("Do you want to see details : y or n ? ")
                if ch == 'Y' or ch == 'y':
                    print(i)
                    carDetails(carNumber=carNum, index=i)
                else:
                    break 
                break

            if isFound:
                pass
            else:
                print(f"Car {carNum} does not exist")
    except:
        print("Something went wrong")




def displayHistory():
    ''' Function to display Cars history'''

    try:
        content = pd.read_csv(FILE_NAME)
        print(content)

    except:
        print("Something went wrong")




def menu():
    '''Menu function to display available operations'''

    print("******* Main menu ********")
    print("1 : Park a car")
    print("2 : Free a car")
    print("3 : Print history")
    print("4 : Search a Car")
    print("Any key to exit")




def login():
    '''Function to login in the program as Admin'''

    email = input("Enter your email : ")
    password = input("Enter your password : ")
    if email == AuthEmail and password == AuthPass:
        return True
    return False


# Driver method
if __name__ == "__main__":
    print("Please login to continue")
    while True:
        token = login()
        if token:
            print("Login in successfully")
            break
        else:
            print("Invalid credentials")

    menu()
    try:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            addCar()
        elif choice == 2:
            freeAParkedCar()
        elif choice == 3:
            displayHistory()
        elif choice == 4:
            searchCar()
        else:
            print("Exiting.......")
            exit(0)
    except:
        print("Something went wrong")
        