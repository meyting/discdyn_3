from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'start_employer2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField(
        label="Before we start, please provide your Prolific ID. ",
    )


# PAGES
class WelcomeEmployer2(Page):
    form_model = 'player'
    form_fields = ['prolific_id']


class InstructionsEmployer2(Page):
    pass


page_sequence = [WelcomeEmployer2,
                 #InstructionsEmployer2
                ]
