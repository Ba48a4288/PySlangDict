from replit import db
import random as r

try:
  with open("req_words.txt", "r+") as rw:
    rw_file_lines = rw.readlines()
    rw.seek(0)
    rw.truncate()
except FileNotFoundError:
  with open("req_words.txt", "x+") as rw:
    rw_file_lines = rw.readlines()

go = True
while go:
  wtd = input("""What do you want to do? 
  To add a word, type a.
  To search for a word, type s.
  To see a list of words that need defined, type h.
  To get a random word, type r.
  To exit, type q.

  Enter your response here --> """).upper()

  if wtd == "A":
    to_add = input("\nEnter word to add --> ").upper()
    if db.get(to_add) is not None:
      seeyn = input("""\nThis word already exists. 
      Do you want to see the definition?
      If yes, type y.
      If no, type n.

      Enter your response here --> """).upper()
      if seeyn == "Y":
        print(db[to_add])
      elif seeyn == "N":
        continue
      else:
        go = False
    else:
      definit = input(f"\nDefine {to_add} --> ")
      db[to_add] = definit
  elif wtd == "S":
    to_search = input("\nEnter the word to search --> ").upper()
    if db.get(to_search) is None:
      def_yn = input(f"""The word {to_search} has not yet been defined! 
      Do you want to define it? (type y if yes or n if no --> """).upper()
      if def_yn == "Y":
        definit = input(f"\nDefine {to_search} --> ")
      elif def_yn == "N":
        req_yn = input("""Do you want to request the word to be defined?
        Type y if yes or n if no

        Type your response here --> """).upper()
        if req_yn == "Y":
          rw_file_lines.append(to_search)
        elif req_yn == "N":
          continue
        else:
          go = False
      else:
        go = False
    else:
      print(db[to_search])
      print("\n")
  elif wtd == "H":
    print("The following words have been requested a definition:")
    if len(rw_file_lines) == 0:
      print("<null>\n")
    else:
      for _l in rw_file_lines:
        print(f"{_l}\n")
  elif wtd == "R":
    keys = db.keys()
    rand = r.choice(list(keys))
    def_of_rand = db[rand]
    print(f"{rand} - {def_of_rand}\n")
  elif wtd == "Q":
    go = False
  else:
    go = False
if not go:
  print(
      "Invalid input OR you chose to exit. Please start program again to continue."
  )
