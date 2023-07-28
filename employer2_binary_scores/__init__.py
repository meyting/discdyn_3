from otree.api import *


doc = """
Your app description
"""

import pandas as pd
import random
import numpy as np


df1 = pd.read_excel('_static/global/employer_pairs_scores.xlsx', keep_default_na = False, engine = 'openpyxl')

class C(BaseConstants):
    NAME_IN_URL = 'employer2_binary_scores'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 16
    number_of_workers = 32
    number_of_pairs = 16
    profiles_worker_score = [{'id_pair': df1['IDPair'][i],
                             'worker1_id': df1['IDWorker'][i],
                              'gender_worker1': df1['gender'][i],
                              'race_worker1': df1["race"][i],
                              'agegroup_worker1': df1["agegroup"][i],
                              'worker2_id': df1['IDOpponent'][i],
                              'gender_worker2': df1['genderOpp'][i],
                              'race_worker2': df1["raceOpp"][i],
                              'agegroup_worker2': df1["agegroupOpp"][i],
                              'score_worker1': df1["ScoreWorker1"][i],
                              'score_worker2': df1["ScoreWorker2"][i],
                              }
                    for i in range(len(df1))]
    # print ("PROFILES WORKER", profiles_worker)
    bonushiring = cu(1)
    num_sequences_worker = 50
    time_limit_sequences = 5


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        all_pairs2 = C.profiles_worker_score.copy()
        all_pairs2.extend(all_pairs2)
        player.participant.pairs2 = all_pairs2
        random.shuffle(player.participant.pairs2)
        # print ("PAIRS", player.participant.pairs)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision_stage2 = models.StringField(blank=True)
    gender1_stage2 = models.StringField(verbose_name='')
    gender2_stage2 = models.StringField(verbose_name='')
    race1_stage2 = models.StringField(verbose_name='')
    race2_stage2 = models.StringField(verbose_name='')
    offer1_stage2 = models.StringField(verbose_name='')
    offer2_stage2 = models.StringField(verbose_name='')
    age1_stage2 = models.StringField(verbose_name='')
    age2_stage2 = models.StringField(verbose_name='')
    usedprofiles_stage2 = models.StringField()
    score1_stage2 = models.StringField(verbose_name='')
    score2_stage2 = models.StringField(verbose_name='')
    score1_stage2_appx = models.StringField(verbose_name='')
    score2_stage2_appx = models.StringField(verbose_name='')


# PAGES
class InstructionsHiring2(Page):
    def is_displayed(player: Player):
        return player.round_number == 1


class DecisionsStage2(Page):
    form_model = 'player'
    form_fields = ['decision_stage2', 'offer1_stage2', 'offer2_stage2', 'age1_stage2', 'age2_stage2',
                   'race1_stage2', 'race2_stage2', 'gender1_stage2', 'gender2_stage2', 'score1_stage2', 'score2_stage2',
                   'score1_stage2_appx', 'score2_stage2_appx']

    def vars_for_template(player: Player):
        participant = player.participant
        profile_side = ['left', 'right']
        profile_side_decision2 = random.choice(profile_side)
        if player.round_number == 1:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 2:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 3:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 4:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 5:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 6:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 7:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 8:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 9:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 10:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 11:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 12:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 13:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 14:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 15:
            profiles2 = participant.pairs2[player.round_number - 1]
        if player.round_number == 16:
            profiles2 = participant.pairs2[player.round_number - 1]
        # print ("PROFILES", profiles)
        worker1_id = profiles2["worker1_id"]
        worker2_id = profiles2["worker2_id"]
        worker1_gender = profiles2["gender_worker1"]
        worker2_gender = profiles2["gender_worker2"]
        worker1_race = profiles2["race_worker1"]
        worker2_race = profiles2["race_worker2"]
        worker1_age = profiles2["agegroup_worker1"]
        worker2_age = profiles2["agegroup_worker2"]
        worker1_score = profiles2["score_worker1"]
        worker2_score = profiles2["score_worker2"]
        worker1_score_appx = profiles2["score_worker1"]+int(round(np.random.normal(0,3)))
        worker2_score_appx = profiles2["score_worker2"]+int(round(np.random.normal(0,3)))
        return {
            'worker1_id': worker1_id,
            'worker2_id': worker2_id,
            'worker1_gender': worker1_gender,
            'worker2_gender': worker2_gender,
            'worker1_race': worker1_race,
            'worker2_race': worker2_race,
            'worker1_age': worker1_age,
            'worker2_age': worker2_age,
            'worker1_score': worker1_score,
            'worker2_score': worker2_score,
            'worker1_score_appx': worker1_score_appx,
            'worker2_score_appx': worker2_score_appx,
            'i1': '<input name="decision_stage2" type="radio" id="w1" value="' + worker1_id + '"' + '/>',
            'i2': '<input name="decision_stage2" type="radio" id="w2" value="' + worker2_id + '"' + '/>',
            'profile_side_decision2': profile_side_decision2,
        }

    #write decision into excel file?

    def error_message(player, values):
        if values['decision_stage2'] == "":
            return 'You forgot to hire a worker. Please click on the worker who you want to hire.'


page_sequence = [InstructionsHiring2, DecisionsStage2]
