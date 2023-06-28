import random, time

r = ""
chars = ["  ", "██"]

while 1==1:
  r = ""
  for i in range(0, 32):
      for j in range(0, 32):
          r += random.choice(chars)
      r += "\n"
  print(r)
  time.sleep(0.1)
