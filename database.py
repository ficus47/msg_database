from sub_database import Database
from msg_unit import Unit

class full_database:
  def __init__(self, first_database:Database, n_row, case):
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

  def stock(self):
    self.content[-1].stock(Unit(name))
    self.update()

  def save(self):
    with open(f"{self.case}/{len(os.listdir((self.case)))+1}.pickle", "wb") as file:
      pickle.dump(self.content[0], file)
      del self.content[0]
      
  def reset(self):
    for i in os.listdir(self.case):
      os.remove(f"{self.case}/{i}")

  def recv(self, name, msg):
    for i, j in zip(self.load(), range(1, len(os.listdir(self.case)))):
      if i.name == name:
        i.recv(msg, name)
        with open(f"{self.case}/{j}.pickle", "wb") as file:
          pickle.dump(i, file)

  def find_msg(self, name):
    for i in self.load():
      j = i.find_name(name)
      if j is not None:
        return j
    return None
        

database = full_Database(Database(10), 10, "db")

database.stock(Unit("maman"))
database.stock(Unit("papa"))

database.recv("msg", "maman")

database.recv("2msg", "papa")

print(database.find_msg("papa"))