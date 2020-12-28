import codecs

fileName = "/home/robinb/Documents/Learning_/Hacking/Hack_the_box/Forensics/Password/password"

with open(fileName, encoding='utf-16-be') as file: # b is important -> binary
    fileContent = file.read()
    print(fileContent)
    #codecs.decode(fileContent, 'UTF-8')
    #str(fileContent, 'UTF-8')
    #test = fileContent.decode('utf-8', "backslashreplace")
  
    #print(test)
