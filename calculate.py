import sys
value = ""
operations = ["+", "-", "*", "/"]
if len(sys.argv) == 4:
   try:
      for arg in range(1, len(sys.argv)): 
         if arg == 2 and sys.argv[arg] not in operations:
            print("invalid arithmetic operator")
            value = ""
            break
         value += sys.argv[arg]
      print(eval(value))
   except:
      print("Please use numbers and acceptable arithmetic operators")
else:
   print("Number of parameters for calculation not enough. Needed 4 but was entered {}. 1 - 3 parameters for calculation".format(len(sys.argv)))