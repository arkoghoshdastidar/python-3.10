class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def get(self):
          print("name : " + self.name)
          print("age : " + str(self.age))

      def compare(self, P2):
          if self.age < P2.age:
              print("self < P2")
          elif self.age == P2.age:
              print("self == P2")
          else:
              print("self > P2")


P1 = Person('vergil', 24)
P1.get()

P2 = Person('dante', 20)
P2.get()

P1.compare(P2)
