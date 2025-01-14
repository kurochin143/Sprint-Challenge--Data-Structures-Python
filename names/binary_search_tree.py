class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left != None:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if self.right != None:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if target == self.value: return True

    if target < self.value:
      if self.left != None:
        return self.left.contains(target)
      else:
        return False
    else:
      if self.right != None:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    if self.right != None:
      return self.right.get_max()
    elif self.left != None:
      return self.right.get_max()
    else:
      return self.value

  def for_each(self, cb):
    cb(self.value)
    if self.left != None:
      self.left.for_each(cb)
    if self.right != None:
      self.right.for_each(cb)

