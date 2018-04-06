send=input('Enter the message to send to your friend: ')
key=int(input("Enter the Key to encrypt (1-26 only): "))
while key<1 or key>26:
    print("Wrong Key, Entered")
    key=int(input("Enter the Key to encrypt (1-26 only): "))
e=""
l=[ord(i) for i in send]        #converting the each letter in the message to its ASCIIZ value
for i in range(len(l)):
    if l[i] != 32:
        if l[i]>=65 and l[i]<=90:       #ensuring the letter lies [A-Z]
            l[i]=l[i]+key
            if l[i]>90:
                l[i]=l[i]-26            #if goes befond Z, taking it back to correct place
        elif l[i]>=97 and l[i]<=122:    #ensuring the letter lies [a-z]
            l[i]=l[i]+key
            if l[i]>122:
                l[i]=l[i]-26            #if goes befond z, taking it back to correct place
        e=e+chr(l[i])                   #changing from ASCIIZ value to character
    else:
        e=e+chr(l[i])
print(e)            #printing the encrypted message