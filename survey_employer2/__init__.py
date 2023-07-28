from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey_employer2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="How old are you?")
    gender = models.StringField(
        choices=[[0, 'male'], [1, 'female'], [2, 'other'], [3, 'prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    race = models.StringField(
        choices=["Hispanic or Latin", "Asian", "White", "Black or African American",
                 "other / prefer not to answer"],
                label='What is your ethnic group?',
        widgets=widgets.RadioSelect,
    )
    education = models.IntegerField(
        choices=[[0, 'did not graduate high school'], [1, 'High school or GED'], [2, 'began college, no degree yet'],
                 [3, 'Bachelor'], [4, 'Associate'], [5, 'Master'], [6, 'Doctoral'], [7, 'other']],
        label='What is the highest level of education you have completed?',
        widgets=widgets.RadioSelect,
    )
    gpa_highschool = models.FloatField(
        label='What is your (current/ final) high school GPA?',
        blank=True,
    )
    gpa_college = models.FloatField(
        label='What is your (current/ final) college GPA?',
        blank=True,
    )
    political_affiliation = models.StringField(choices=["Democrat", "Republican", "Independent", "other"],
                                                label="In politics today, do you consider yourself a Republican, a Democrat, or an Independent?",
                                               widgets=widgets.RadioSelect,
                                               )
    discrimination = models.LongStringField(
        initial = None,
        blank=True,
        verbose_name='During your hiring decision, have you thought about whether you are discriminating against the workers?',
    )
    purpose = models.LongStringField(initial=None,
                                     blank=True,
                                     verbose_name="What do you think this study is about?")


# PAGES

class SurveyEmployer2(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'race', 'education', 'gpa_highschool', 'gpa_college', 'political_affiliation',
                    'discrimination', 'purpose']


page_sequence = [SurveyEmployer2]
