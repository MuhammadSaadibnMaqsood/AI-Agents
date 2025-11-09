import time
import random

class SmokeDetector:
    def __init__(self):
        self.alert_active = False 

    def detectSmoke(self):
        return random.choice([True] * 1 + [False] * 9)
    
    def activateAlert(self):
        if not self.alert_active:
            self.alert_active = True
            print(" SMOKE DETECTED!")
    
    def deactivateAlert(self):
        if self.alert_active:
            self.alert_active = False
            print(" No smoke detected.")
    
    def run(self):
        print("🟢 SMOKE DETECTOR ACTIVATED")
        while True:
            detect = self.detectSmoke()  

            if detect:
                self.activateAlert()
            else:
                self.deactivateAlert()

            time.sleep(1)

smokeDetector = SmokeDetector()
smokeDetector.run()
