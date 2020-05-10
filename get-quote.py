import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  n = len(quotes)

  rnd = random.randint(0, n)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
