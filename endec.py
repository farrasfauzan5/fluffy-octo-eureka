from Crypto.Cipher import AES
import string
import base64
import time
#import modules
PADDING = '{'
BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#prepare crypto method
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
#set encryption/decryption variables
loop=5
while loop==5:
     #set up loop, so the program can be rerun again if desired, without restarting
    option=raw_input("Would You Like to Encrypt Or Decrypt Text?\nEncrypt: a\nDecrypt: b\n")
    if option=='a':
        letter=3
        while letter==3:
            secret = raw_input("Please Enter An Encryption Key {must be 16 characters long}: ")
            countTotal= (len(secret))
            if countTotal==16:
                cipher = AES.new(secret)
                letter=0
            else:
                print "Please Ensure The Key You Entered Is 16 Characters In Length\n"
                letter=3
                #this checks the encryption key to ensure it matches the correct length
        # encode a string
        data=raw_input("Please Enter Text You'd Like Encrypted: ")
        encoded = EncodeAES(cipher, data)
        print 'Encrypted string:', encoded
        options=raw_input("Would You Like To Encrypt/Decrypt Again? Y/N\n")
        if options=='y':
            loop=5
        if options=='n':
            loop=0
          
    if option=='b':
      
        encoded=raw_input("Please Enter The Encoded String:\n")
        letter=3
        while letter==3:
            secret=raw_input("Please Enter The Decryption Key:\n")
            countTotal= (len(secret))
            #this checks the encryption key to ensure it matches the correct length
            if countTotal==16:
                cipher = AES.new(secret)
                letter=0
                decoded = DecodeAES(cipher, encoded)
                print 'Decrypted string:', decoded
                options=raw_input("Would You Like To Encrypt/Decrypt Again? Y/N\n")
                if options=='y':
                    loop=5
                if options=='n':
                    loop=0
            else:
                print "Please Ensure The Key You Entered Is 16 Characters In Length\n"
                letter=3
              
if loop==0:
    print "Goodbye!!"
    time.sleep(2)
    exit
    #exits the program if desired by user 
