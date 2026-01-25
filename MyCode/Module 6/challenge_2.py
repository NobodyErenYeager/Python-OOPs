class Sport:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"
    
    def __eq__(self, value):
        return self.name == value.name if isinstance(value, Sport) else False
    

class Football(Sport):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def __str__(self):
        return f"This {self.name} team is matched with {', '.join(self.team)}"
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    def __sub__(self, other):
        if isinstance(other, Football):
            shared_teams = [team for team in self.team if team in other.team]
            if shared_teams:
                return Football(self.name, shared_teams)
            else:
                return "No common teams between them"
        return "Not Possible"
    

class BasketBall(Sport):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def __str__(self):
        return f"This {self.name} team is matched with {', '.join(self.team)}"
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    def __sub__(self, other):
        if isinstance(other, BasketBall):
            shared_teams = [team for team in self.team if team in other.team]
            if shared_teams:
                return BasketBall(self.name, shared_teams)
            else:
                return "No common teams between them"
        return "Not Possible"


basic = Sport("super basic!")


football1 = Football("Football", ["Team A","Team B"])
football2 = Football("Football", ["Team A", "Team B"])

basketball1 = BasketBall("Basketball",["Kingss","Rockets"])
basketball2 = BasketBall("Basketball",["Jazz","Kings"])

print(basic)
print(football1)
print(basketball1)

print(football1 == football2)
print(basketball1 == football1)


print(basketball1 - basketball2)
