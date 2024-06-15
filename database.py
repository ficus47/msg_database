from sub_database import Database
from msg_unit import Unit
import pickle
import random
import os

class Full_database:
  def __init__(self, first_database:Database, n_row, case):
    os.makedirs(case, exist_ok=True)

    self.content = [first_database]
    self.n_row = n_row
    self.case = case

  def load(self):
    for i in os.listdir(self.case):
      yield pickle.load(open(f"{self.case}/{i}", "rb"))

  def update(self):
    if self.content[-1].full:
      self.content.append(Database(self.n_row))
      self.save()

  def stock(self, name):
    self.content[-1].stock(Unit(name))
    self.update()

  def save(self):
    with open(f"{self.case}/{len(os.listdir((self.case)))+1}.pickle", "wb") as file:
      pickle.dump(self.content[0], file)
      del self.content[0]
      
  def reset(self):
    for i in os.listdir(self.case):
      os.remove(f"{self.case}/{i}")

  def recv(self, msg, name, who):
    for i, j in zip(self.load(), range(1, len(os.listdir(self.case)))):
        i.recv(msg, name, who)
        with open(f"{self.case}/{j}.pickle", "wb") as file:
          pickle.dump(i, file)

    for i, j in zip(self.content, range(len(self.content))):
        i.recv(msg, name, who)
        self.content[j] = i

  def find_msg(self, name):
    if os.listdir(self.case):
      for i in self.load():
        j = i.find_name(name)
        if j is not None:
          return j
        
    for i in self.content:
        j = i.find_name(name)
        if j is not None:
          print("e")
          return j
    return None
  
  def print(self):
    for i in self.load():
      for i in i.content:
        print(i.name, i.msg)
        
    for i in self.content:
      for i in i.content:
        print(i.name, i.msg)

database = Full_database(Database(10), 10, "db")
database.reset()
for i in range(9**3):
  database.stock("maman")
  database.stock("papa")
  database.stock("chien")
  database.stock("chat")

database.recv("msg", "maman", "papa")

database.recv("2msg", "papa", "maman")

print(database.find_msg("papa").msg)