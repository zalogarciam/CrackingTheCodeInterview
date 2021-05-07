class ChatServer:
    def __init__(self):
        self.group_chats = []
        self.simple_chats = []
        self.init_server()

    def init_server(self):
        print('Initializing Chat Server ...')

    def create_group_chat(self, group_chat):
        self.group_chats.append(group_chat)
        print('Adding Group Chat:', group_chat.name, 'to the Chat Server')

    def create_simple_chat(self, simple_chat):
        self.simple_chats.append(simple_chat)
        print('Adding Simple Chat between:', simple_chat.user_b.name, 'and', simple_chat.user_a.name,
              'to the Chat Server')

    @staticmethod
    def send_message_group_chat(user, group_chat, message):
        message = Message(message)
        if user in group_chat.users:
            print(user.name, 'send a message to the Group Chat:', group_chat.name)
            print('Message:', message.description)
        else:
            print('Error')

    @staticmethod
    def send_message_simple_chat(user, simple_chat, message):
        message = Message(message)
        if user in simple_chat.users:
            simple_chat.users.remove(user)
            print(user.name, 'send a message to', simple_chat.users.pop().name)
            print('Message:', message.description)
        else:
            print('Error')


class GroupChat:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(user.name, 'was added to the Group Chat', self.name)

    def remove_user(self, user):
        self.users.remove(user)
        print(user.name, 'was removed of the Group Chat', self.name)


class SimpleChat:
    def __init__(self, user_a, user_b):
        self.user_a = user_a
        self.user_b = user_b
        self.users = [user_a, user_b]


class User:
    def __init__(self, name):
        self.name = name


class Message:
    def __init__(self, description):
        self.description = description


user1 = User('Usuario 1')
user2 = User('Usuario 2')
user3 = User('Usuario 3')
user4 = User('Usuario 4')
user5 = User('Usuario 5')
user6 = User('Usuario 6')

simple_chat1 = SimpleChat(user1, user2)
simple_chat2 = SimpleChat(user2, user3)

group_chat1 = GroupChat('Group Chat 1')
group_chat1.add_user(user3)
group_chat1.add_user(user1)
group_chat1.add_user(user6)
group_chat2 = GroupChat('Group Chat 2')
group_chat2.add_user(user5)
group_chat2.add_user(user4)
group_chat2.add_user(user2)

chat_server = ChatServer()
chat_server.create_group_chat(group_chat1)
chat_server.create_group_chat(group_chat2)
chat_server.create_simple_chat(simple_chat1)
chat_server.create_simple_chat(simple_chat2)
print()
chat_server.send_message_group_chat(user1, group_chat1, 'Hello There!')
chat_server.send_message_group_chat(user2, group_chat1, 'Hello There!')
print()


chat_server.send_message_simple_chat(user1, simple_chat1, 'Hello user 2!')
chat_server.send_message_simple_chat(user3, simple_chat1, 'Hello user!')