import random
import time
from os import system, name

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = Node(data)
        if self.head:
            p = self.head
            while p.next != self.head: 
                p = p.next
            p.next = n
            n.next = self.head
        else:
            self.head = n
            n.next = self.head

    def showlinkedlist(self):
        ret = []
        if self.head:
            p = self.head
            while p.next != self.head:
                ret.append(p.data)
                p = p.next
            ret.append(p.data)
        else:
            ret.append("Circular Linked List is empty")
        return ret

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class SlotGame:
    def __init__(self):
        self.coin = 0
        self.last = 0
        self.max = 0

        self.firstWheel = "------"
        self.secondWheel = "------"
        self.thirdWheel = "------"

        self.log = Queue()

        self.items = CircularLinkedList()
        self.items.insert("CHERRY")
        self.items.insert("ORANGE")
        self.items.insert("BANANA")
        self.items.insert("POMELO")
        self.items.insert("TOMATO")
        self.items.insert("CARROT")

        self.welcome()

    def set_coin(self, coin):
        self.coin = coin

    def update_coin(self, win):
        self.coin += win
        self.last = win
        if win > self.max:
            self.max = win
        self.log.enqueue(f"\t{self.firstWheel} | {self.secondWheel} | {self.thirdWheel} {self.last:>6} {self.coin:>8}")

    def spin_wheel(self, wheel):
        p = self.items.head
        for i in range(random.randint(1, 6)):
            if wheel == 1:
                self.firstWheel = p.data
            elif wheel == 2:
                self.secondWheel = p.data
            else:
                self.thirdWheel = p.data
            p = p.next
            self.clear("in_for")

    def play(self):
        if self.coin < 1:
            insert_coin = int(input("\n\tINSERT COIN PLEASE $"))
            self.set_coin(insert_coin)

        self.spin_wheel(1)
        self.spin_wheel(2)
        self.spin_wheel(3)

        self.clear("normal")

        self.welcome()
        self.calculate()
        self.display()

    def calculate(self):
        if (self.firstWheel == "POMELO") and (self.secondWheel != "POMELO"):
            self.update_coin(2)
        elif (self.firstWheel == "POMELO") and (self.secondWheel == "POMELO") and (self.thirdWheel != "POMELO"):
            self.update_coin(5)
        elif (self.firstWheel == "POMELO") and (self.secondWheel == "POMELO") and (self.thirdWheel == "POMELO"):
            self.update_coin(7)
        elif (self.firstWheel == "TOMATO") and (self.secondWheel == "TOMATO") and (self.thirdWheel == "TOMATO" or self.thirdWheel == "CHERRY"):
            self.update_coin(10)
        elif (self.firstWheel == "BANANA") and (self.secondWheel == "BANANA") and (self.thirdWheel == "BANANA" or self.thirdWheel == "CHERRY"):
            self.update_coin(14)
        elif (self.firstWheel == "ORANGE") and (self.secondWheel == "ORANGE") and (self.thirdWheel == "ORANGE" or self.thirdWheel == "CHERRY"):
            self.update_coin(20)
        elif (self.firstWheel == "CHERRY") and (self.secondWheel == "CHERRY") and (self.thirdWheel == "CHERRY"):
            self.update_coin(250)
        else:
            self.update_coin(-1)

    def clear(self, instruction):
        system('clear')
        if instruction == 'in_for':
            self.welcome()
            self.display()
            time.sleep(0.2)

    def display(self):
        print("\n\t|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("\t|              SLOT MACHINE            |  |‾‾‾|")
        print("\t|                                      |  |___|")
        print("\t|   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   |   | | ")
        print(f"\t| > | {self.firstWheel}  |  {self.secondWheel}  |  {self.thirdWheel} | < |‾| | |")
        print("\t|   |______________________________|   | |‾  |")
        print("\t|                                      |_|‾‾‾")
        print("\t|______________________________________|")
        print("\t|                                      |")
        print(f"\t|      coin       {'$' + str(self.coin):>16}     |")
        print(f"\t|      last       {'$' + str(self.last):>16}     |")
        print(f"\t|      max         {'$' + str(self.max):>15}     |")
        print("\t|______________________________________|")

    def welcome(self):
        print("\n\tWELCOME TO THE SLOT MACHINE SIMULATOR\n")
        print("\t-----------------REWARD-----------------")
        print("\t         ITEMS                      PAYS")
        print("\tCHERRY | CHERRY | CHERRY            $250")
        print("\tORANGE | ORANGE | ORANGE/CHERRY      $20")
        print("\tBANANA | BANANA | BANANA/CHERRY      $14")
        print("\tPOMELO | POMELO | POMELO              $7")
        print("\tPOMELO | POMELO | ------              $5")
        print("\tPOMELO | ------ | ------              $2")
    
    def statement(self):
        print("\n\t----------------STATEMENT---------------")
        print("\t         ITEMS               WIN     BAL")
        for i in range(self.log.size()):
            print(self.log.dequeue())
        print(f"\n\tYOU ENDED THE GAME WITH ${self.coin} IN YOUR HAND.")

def main():
    slot_game = SlotGame()
    while(True):
        answer = input("\n\tWOULD YOU LIKE TO PLAY? ").lower()
        if answer in ["yes", "y"]:
            slot_game.play()
        elif answer in ["no", "n"]:
            slot_game.statement()
            break
        else:
            print("\tAGAIN PLEASE")

if __name__ == '__main__':
    main()