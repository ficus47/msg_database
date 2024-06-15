class Unit:
  def __init__(self, name):
    self.msg = {}
    self.name = name

  def recv(self, msg, name)
    if name in self.msg:
      self.msg[name].append(msg)
    else:
      self.msg.upadte({name:[msg]})

