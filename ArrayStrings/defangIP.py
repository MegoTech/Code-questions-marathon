# Given a valid (IPv4) IP address,
# return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address: str) -> str:
    #implament your code here
    return None

if __name__ == '__main__':
    #~~~~~~~~~~~~~~~this is the test for the defangIP.py~~~~~~~~~~~~~~~#
    address = "1.1.1.1"
    if defangIPaddr(address) == "1[.]1[.]1[.]1":
        print("Test 1 Passed")
    address = "255.100.50.0"
    if defangIPaddr(address) == "255[.]100[.]50[.]0":
        print("Test 2 Passed")


