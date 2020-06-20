"""PYTHON SCRIPT FOR AUTOMATION"""

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:34:53', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 16:02:30', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 20:50:10', 'login', 'myworkstation.local', 'lane'),
    Event('2020-01-22 05:20:49', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 20:50:10', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-23 05:20:49', 'login', 'webserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)