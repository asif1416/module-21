# This is the main file for L1 Activity 2
from abc import ABC, abstractmethod
class Animal(ABC):

	def move(self):
		pass

class Human(Animal):

	def move(self):
		print("I can walk and run")

class Snake(Animal):

	def move(self):
		print("I can crawl")

class Dog(Animal):

	def move(self):
		print("I can bark")

class Lion(Animal):

	def move(self):
		print("I can roar")
		
A = Human()
A.move()

B = Snake()
B.move()

C = Dog()
C.move()

D = Lion()
D.move()