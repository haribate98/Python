def read_events():
    with open('../data/projekcije.txt', 'r') as data:
        events = data.readlines()
        return events


def find_event(event_ID):
    all_events = read_events()
    for e in all_events:
        event = e.split('|')[0]
        if event == event_ID:
            return e
