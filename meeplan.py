import datetime
import random


available_speakers = []

history = []


class Meeting:

    def __init__(self, topic, date, speaker=None):
        self.topic = topic
        self.date = date
        self.speaker = speaker or suggest_next_speaker(topic)


def suggest_next_speaker(topic):
    # TODO improve selection
    return random.choice(available_speakers)

