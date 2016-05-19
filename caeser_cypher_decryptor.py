
def caeser_cipher_decoder(Text, shift): # same shift value used to encode text should be used here
     ascii = []
     encrypted_file= open(Text,"r")# imports an encrypted text file
     encryption = encrypted_file.read()
     encrypted_file.close()
     for characters in encryption: # converts characters in text file to their ascii values
          ascii.append(ord(characters))
     for x in range(0,len(ascii)):
          ascii[x] -= shift      # applies shift to the ascii values
          if ascii[x] < 97:
               ascii[x]+=26
          if ascii[x] > 122:
               ascii[x] -= 26
          ascii[x] = chr(ascii[x])# converts the shifted ascii values into characters
     f = open("decrypted text.txt", 'w')# outputs a text file with the original message
     f.write(''.join(ascii))
     f.close()

     
