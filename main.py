print("Name and Age counter V1.1 2/12/19  (C)Arin Bryan")
Name = input("Name:")
DOB = int(input("Date Of Birth"))
if DOB >= 1900 and DOB <= 2019:
  if DOB >= 2000:
    print("Hello,",Name,"you are born in the 21st century.")
  if DOB <= 2000:
    print("Hello,",Name,"you are born in the 20th century")
else:
  print("Enter Valid Birth Year After Restarting Program")
