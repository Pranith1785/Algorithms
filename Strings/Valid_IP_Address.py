### Problem statement
'''
Create a function which generates all the possible IP address from a given string
constraints : str len <= 12
              valid Ip address = "xxx.xxx.xxx.xxx"
              each 3 digit should be in range [0-255]
              3 digit should not be prefix with 0

Ex : string = "1921680" ,
     output = ["1.9.216.80","1.92.168.0","1.92.16.80","19.2.16.80","19.216.8.0","19.2.168.0","19.21.68.0",
                "19.21.68.0","192.1.6.80","192.1.68.0","192.16.8.0"]
'''

### Solution - 1
## Time - O(1)    | Space - O(1)

def checkIP(strValue):

    if strValue == " " or strValue == "":
        return False
    if len(strValue) > 1:
        if strValue[0] == "0" or strValue[0:2] == "00" or strValue == "000":
            return False
    if len(strValue) == 0 or len(strValue) > 3 :
        return False
    if int(strValue) < 0 or int(strValue) > 255 :
        return False
    return True


def validIPAddresses(string):

    validIPs = []
    strLen = len(string)
    for i in range(0,3):
        str1 = string[:i+1]
        if(checkIP(str1)):
            for j in range(i+1,i+4):
                str2 = string[i+1:j+1]
                if(checkIP(str2)):
                    for k in range(j+1,j+4):
                        str3 = string[j+1:k+1]
                        if(checkIP(str3)):
                            str4 = string[k+1:]
                            if(checkIP(str4)):
                                validIPs.append(str1+"."+str2+"."+str3+"."+str4)
    print(validIPs )
    return validIPs


### Solution - 2
## Time - O(1)    |  Space - O(1)

def isValidIP(stringPart):

    intStr = int(stringPart)
    if intStr > 255:
        return False
    return len(stringPart) == len(str(intStr)) ## checking for leading 0 


def validIPAddresses2(string):

    validIPs = []

    for i in range(1,min(len(string),4)):
        
        currentIPAddress = ["", "", "", ""]
        currentIPAddress[0] = string[:i]
        if not isValidIP(currentIPAddress[0]):
            continue

        for j in range(i+1, i + min(len(string) - i,4)):
            
            currentIPAddress[1] = string[i:j]
            if not isValidIP(currentIPAddress[1]):
                continue
            
            for k in range(j+1, j + min(len(string)- j,4)):
                currentIPAddress[2] = string[j:k]
                currentIPAddress[3] = string[k:]

                if isValidIP(currentIPAddress[2]) and isValidIP(currentIPAddress[3]):
                    validIPs.append(".".join(currentIPAddress))
    
    return validIPs


                
print(validIPAddresses2("1921680"))

