import random
import time

class SimpleReflexAgent:
    def __init__(self):
        self.door = False

    def detectPerson(self):
        return random.choice([True] * 1 + [False] * 3)

    def openDoor(self):
        self.door = True
        print("Door opened ")

    def closeDoor(self):
        self.door = False
        print("Door closed ")

    def run(self):
        while True:
            person_detected = self.detectPerson()
            if person_detected:
                self.openDoor()
            else:
                self.closeDoor()
            time.sleep(1)


agent = SimpleReflexAgent()
agent.run()
