class User: 
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Opponent:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class AgentSuggestion:
    def __init__(self, user, opponent):
        self.user = user
        self.opponent = opponent

    def decide_strategy(self):
        if self.user.level < self.opponent.level:
            print(f"{self.user.name} should DEFEND against {self.opponent.name}")
        else:
            print(f"{self.user.name} should ATTACK {self.opponent.name}")



user = User("Player1", 5)
opponent = Opponent("Dragon", 8)

agent = AgentSuggestion(user, opponent)
agent.decide_strategy()
