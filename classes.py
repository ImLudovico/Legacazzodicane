class Player:
    def __init__(self, idin, namein, teamin, avaluein, ivaluein):
        self.name = namein
        self.team = teamin
        self.avalue = avaluein
        self.ivaluein = ivaluein

class Team:
    def __init__(self, namein):
        self.name = namein
        self.team_goalkeepers = []
        self.team_defenders = []
        self.team_midfielders = []
        self.team_forwards = []

    def add_gk(self, playerin):
        self.team_goalkeepers.append(playerin)

    def add_def(self, playerin):
        self.team_defenders.append(playerin)

    def add_mid(self, playerin):
        self.team_midfielders.append(playerin)

    def add_fw(self, playerin):
        self.team_forwards.append(playerin)

    def get_value_gk(self):
        out = 0
        for i in range(len(self.team_goalkeepers)):
            out = out + int(self.team_goalkeepers[i].avalue)
        return out

    def get_value_def(self):
        out = 0
        for i in range(len(self.team_defenders)):
            out = out + int(self.team_defenders[i].avalue)
        return out

    def get_value_mid(self):
        out = 0
        for i in range(len(self.team_midfielders)):
            out = out + int(self.team_midfielders[i].avalue)
        return out

    def get_value_fw(self):
        out = 0
        for i in range(len(self.team_forwards)):
            out = out + int(self.team_forwards[i].avalue)
        return out

    def get_value(self):
        out = self.get_value_gk() + self.get_value_def() + self.get_value_mid() + self.get_value_fw()
        return out



class Competition:
    def __init__(self):
        self.competition_team_list = []

    def addTeam(self, team):
        self.competition_team_list.append(team)

    def printCompetition(self):
        for i in range(len(self.competition_team_list)):

            print("[",i+1,"] ", self.competition_team_list[i].name)
