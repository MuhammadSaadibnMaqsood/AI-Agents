class User: 
    def __init__(self, name):
        self.name = name
        self.speech = {}      
        self.history = []     

    def update_preference(self, item, prefer):
       
        if item in self.speech:
            self.speech[item] += prefer
        else: 
            self.speech[item] = prefer


class Agent: 
    def predict(self, user):
       
        sorted_speech = sorted(user.speech.items(), key=lambda x: x[1], reverse=True)
        
        if sorted_speech:
            best_match = sorted_speech[0][0]
            user.history.append(best_match)
            return best_match
        else:
            return "No speech data yet."

    def adapt(self, user, item, prefer):
        user.update_preference(item, prefer)
        print(f"Agent learned from '{item}' (preference: {prefer})")


user = User("Saad")
agent = Agent()

agent.adapt(user, "hello", 3)
agent.adapt(user, "yo", 2)
agent.adapt(user, "wassup", 1)

print("Agent Prediction:", agent.predict(user))

agent.adapt(user, "yo", 3)
print("Updated Prediction:", agent.predict(user))
