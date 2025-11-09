class UserProfile:
    def __init__(self, name):
        self.name = name
        self.preferences = {} 
        self.history = []     

    def update_preferences(self, item, rating):
      
        if item in self.preferences:
            self.preferences[item] += rating
        else:
            self.preferences[item] = rating

        self.history.append(item)  


class RecommendationAgent:
    def __init__(self):
        self.recommendations = {}  

    def recommend(self, user):
        sorted_preferences = sorted(user.preferences.items(), key=lambda x: x[1], reverse=True)
   
        return [item for item, _ in sorted_preferences][:2]

    def adapt(self, user, new_item, rating):
        user.update_preferences(new_item, rating)



if __name__ == "__main__":
    
    user = UserProfile(name="Alice")
    agent = RecommendationAgent()

    user.update_preferences("Horror Movie", 4)
    user.update_preferences("Thriller Movie", 3)

    print(" Initial Recommendations:", agent.recommend(user))

    print("\n User starts watching more thriller movies...")
    agent.adapt(user, "Thriller-2", 4)
    agent.adapt(user, "Thriller-3", 3)

    print(" Updated Recommendations:", agent.recommend(user))
