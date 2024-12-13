import time

def progress_bar():
  L = [" Processing....{█████████                            } %14 "," Processing....{██████████████                       } %38 ",
       " Processing....{█████████████████                    } %50 "," Processing....{█████████████████████████            } %66 ",
       " Processing....{███████████████████████████████████  } %98 "," Processing....{█████████████████████████████████████} %100" ]
  for i in L:
       print(i, end = "\n\n")
       time.sleep(0.5)

progress_bar()
