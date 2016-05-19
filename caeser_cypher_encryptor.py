
def caesar_cipher(Text, shift):
     if shift > 25 or shift < -25:
          return "Shift value is out of range"
     message_text = []
     text_file = open(Text, 'r')#imports a text file named "message.txt"
     text = text_file.read()
     text_file.close()
     for characters in text:
          if characters.isalpha()==True:
               message_text.append(ord(characters.lower()))#converts characters in file to lowercase ascii values
     for x in range(0,len(message_text) ):
          message_text[x] += shift #applies the "shift"
          if message_text[x] > 122:
               message_text[x] -= 26
          if message_text[x] < 97:
               message_text[x] += 26
          message_text[x] = chr(message_text[x])# converts the shifted ascii values into characters
     encrypted_file = str( "".join(message_text))
     f = open("encrypted_text.txt","w")
     f.write(encrypted_file)
     f.close()# outputs a file with the shifted ascii value
     return "Encryption complete"

     
     

