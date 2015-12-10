import datetime

import pytest

import meeplan


@pytest.fixture
def test_meeting():
    meeting = meeplan.Meeting(
        topic="Crew Meeting",
        date=datetime.date.today(),
        speaker="Jeb",
    )
    return meeting


@pytest.fixture
def past_meeting():
    meeting = meeplan.Meeting(
        topic="Activity Report",
        date=datetime.date(2015, 10, 9),
        speaker="Bill",
    )
    return meeting


def test_meeting_has_topic(test_meeting):
    assert test_meeting.topic


def test_meeting_has_date(test_meeting):
    assert test_meeting.date


def test_meeting_has_speaker(test_meeting):
    assert test_meeting.speaker


def test_meeting_str(past_meeting):
    assert str(past_meeting) == "2015-10-09, Activity Report, Bill"


def test_meeting_speaker_is_suggested():
    meeplan.available_speakers = ["Jeb", "Bob", "Bill"]  # FIXME
    meeting = meeplan.Meeting("Crew Report", datetime.date.today())
    assert meeting.speaker is not None


def test_meeting_speaker_suggested_is_valid():
    meeplan.available_speakers = ["Jeb", "Bob", "Bill"]  # FIXME
    meeting = meeplan.Meeting("Crew Report", datetime.date.today())
    assert meeting.speaker in meeplan.available_speakers


def test_speaker_suggestion_for_same_meeting_cycles_all_available_speakers():
    meeplan.available_speakers = ["Jeb", "Bob", "Bill"]  # FIXME
    speaker1 = meeplan.Meeting("Crew Report", datetime.date.today()).speaker
    speaker2 = meeplan.Meeting("Crew Report", datetime.date.today()).speaker
    assert speaker2 != speaker1
    speaker3 = meeplan.Meeting("Crew Report", datetime.date.today()).speaker
    assert (speaker3 != speaker1) and (speaker3 != speaker2)
    speaker4 = meeplan.Meeting("Crew Report", datetime.date.today()).speaker
    assert (speaker4 != speaker3) and (speaker4 != speaker2)


# def test_meeplan_init_empty():
#     assert meeplan.history == False
#     assert meeplan.speakers == False


# def test_add_speaker():
#     meeplan.add_speaker("Jeb")
#     assert len(meeplan.speakers) == 1


# def test_add_last_meeting():
#     meeplan.add_meeting(speaker="Jeb")

# def test_suggest_speaker_for_next_meeting():
#     next_meeting = meeplan.get_next_meeting()


# def test_next_meeting_is_on_tuesday():
#     meeplan.next_meeting.day = 'Tuesday'
