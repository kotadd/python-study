class User:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def sign_in(self):
    print('logged in')

  def greet(self):
    print(f'hello, Im {self._name}!')

  def run(self):
    return self

class Wizard(User):
  def __init__(self, name, age, mp):
    super().__init__(name, age)
    self.mp = mp

class Archer(User):
  pass

wizard1 = Wizard('wizard', 29, 100)

# print(dir(wizard1))
# print(wizard1.mp)

class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age

  def __str__(self):
    return f'{self.color}'

# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))

class SuperList(list):
  def __len__(self):
    return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
super_list1[0]
print(issubclass(SuperList, list))