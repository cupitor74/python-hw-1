import sys
value = ""
if len(sys.argv) == 4:
   try:
      for arg in range(1, len(sys.argv)): 
         value += sys.argv[arg]
      print(eval(value))
   except:
      print("Please use numbers and arithmetic operators")
else:
   print("Number of parameters for calculation not enough. Needed 4 but was entered {}. 1 - 3 parameters for calculation".format(len(sys.argv)))