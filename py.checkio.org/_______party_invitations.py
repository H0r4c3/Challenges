'https://py.checkio.org/en/mission/party-invitations/'

'''
You should create the class Party(place) which will send the invites to all of your friends. 
Also you should create the class Friend and each friend will be an instance of this class.
Sometimes the circle of friends is changing - new friends appear, the old ones disappear from your life (for example - move to another town). 
'''

class Friend:
    pass

class Party:
    pass




# Best Solution: 
# https://py.checkio.org/mission/party-invitations/publications/Sim0000/python-3/first/share/2785a3209f5a3ba31e4b74665201e25c/

class Friend:
    def __init__(self, name):
        self.name = name
        self.message = 'No party...'

    def invite(self, message):
        self.message = message

    def show_invite(self):
        return self.message


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
    
    def del_friend(self, friend):
        self.friends.remove(friend)

    def send_invites(self, date):
        for friend in self.friends:
            friend.invite(f'{self.place}: {date}')




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")