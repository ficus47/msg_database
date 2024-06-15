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

  def recv(self, msg, name, who):
    for i, j in zip(self.content, range(len(self.content))):
      if i.name == name:
        i.recv(msg, who)
        self.content[j] = i
        
  def find_name(self, name):
    for i in self.content:
      if i.find_name(name):
        return i
    return None
  