import random as rnd


class CallCenter:
    def __init__(self, name, n_respondents, n_manager, n_director):
        self.name = name
        self.n_respondents = n_respondents
        self.n_manager = n_manager
        self.n_director = n_director
        self.n_employees = n_respondents + n_director + n_manager
        self.managers = []
        self.directors = []
        self.respondents = []
        self.init_call_center()

    def init_call_center(self):
        for i in range(self.n_respondents):
            random_status = rnd.randint(0, 1)
            respondent = Respondent('Respondent ' + str(i + 1), random_status)
            self.respondents.append(respondent)

        for i in range(self.n_manager):
            random_status = rnd.randint(0, 1)
            manager = Manager('Manager ' + str(i + 1), random_status)
            self.managers.append(manager)

        for i in range(self.n_director):
            random_status = rnd.randint(0, 1)
            director = Director('Director ' + str(i + 1), random_status)
            self.directors.append(director)

    def show_employees(self):
        print('----------' + self.name + '----------')
        print('Respondents')
        for i in self.respondents: i.print()
        print('Managers')
        for i in self.managers: i.print()
        print('Directors')
        for i in self.directors: i.print()

    def dispatch_call(self):
        print()
        print('Dispatching call ... ')
        call = Call(accepted=False)
        employees = self.respondents + self.managers + self.directors
        for i in employees:
            if not call.accepted:
                if i.status:
                    print(i.name + ' is allocated to the call ... ')
                    call.accepted = True
            else:
                print('Call is accepted and answered ... ')
                break


class Call:
    def __init__(self, accepted):
        self.accepted = accepted


class Employee:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def print(self):
        print('Name: ' + self.name + "  Status: " + ('Free' if self.status else 'Busy'))


class Respondent(Employee):
    pass


class Manager(Employee):
    pass


class Director(Employee):
    pass


call_center = CallCenter('My Call Center', 5, 3, 1)
call_center.show_employees()
call_center.dispatch_call()
