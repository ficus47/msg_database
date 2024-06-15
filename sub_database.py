class Database:
  def __init__(self, n_row : int):
    self.n_row, self.full = n_row, False
    self.content = []

  def stock(self, content):
    if len(self.content) >= self.n_row:
      #raise Exception("error : full capacity reached")
      self.full = True
    else:
      self.content.append(content)

  def recv(self, msg, name):
    for i in self.content:
      if i.name == name:
        i.recv(msg, name)

  def find_name(self, name):
    for i in self.content:
      if i.name == name:
        return i
    return None