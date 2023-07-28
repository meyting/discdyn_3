from otree.api import *


doc = """
Your app description
"""

import pandas as pd
import random
import numpy as np


df1 = pd.read_excel('_static/global/employer_pairs.xlsx', keep_default_na = False, engine = 'openpyxl')
"""
df1["mat_range"] = "middle 4"
df1.loc[(df1.mat_rank <= 4), "mat_range"] = "top 4"
df1.loc[(df1.mat_rank >= 9), "mat_range"] = "bottom 4"
df2["re_range"] = "middle 4"
df2.loc[(df2.re_rank <= 4), "re_range"] = "top 4"
df2.loc[(df2.re_rank >= 9), "re_range"] = "bottom 4"


print("DF1 IN BINARY",df1)
print("DF2 IN BINARY",df2)

df1.to_excel('_static/global/binaryrankings/workers_rank_mat.xlsx')
df2.to_excel('_static/global/binaryrankings/workers_rank_re.xlsx')
"""

class C(BaseConstants):
    NAME_IN_URL = 'decisions_binary_employer1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 16
    number_of_workers = 32
    number_of_pairs = 16
    profiles_worker = [{'id_pair': df1['IDPair'][i],
                     'worker1_general_id': df1['IDWorker'][i],
                        'worker1_id': df1['UniqueID'][i],
                     'gender_worker1': df1['gender'][i],
                     'race_worker1': df1["race"][i],
                     'agegroup_worker1': df1["agegroup"][i],
                        'worker2_id': df1['IDOpponent'][i],
                        'gender_worker2': df1['genderOpp'][i],
                     'race_worker2': df1["raceOpp"][i],
                     'agegroup_worker2': df1["agegroupOpp"][i],
                     }
                    for i in range(len(df1))]
    # print ("PROFILES WORKER", profiles_worker)
    """
    conversionrate = cu(0.1)
    examplescore = 5
    examplebonus = examplescore * conversionrate
    bonus_employer = 50
    flatbonus = cu(2)
    # dummy worker profiles:
    profile_worker1 = {'ID': '1', 'race': 'white', 'gender': 'male', 'agegroup': '20-24'},
    profile_worker2 = {'ID': '2', 'race': 'white', 'gender': 'female', 'agegroup': '20-24'},
    profile_worker3 ={'ID': '3', 'race': 'black', 'gender': 'male', 'agegroup': '20-24'},
    profile_worker4 = {'ID': '4', 'race': 'black', 'gender': 'female', 'agegroup': '20-24'},
    """

class Subsession(BaseSubsession):
    pass

"""
def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        profiles = []
        decision_a = [C.profile_worker1, C.profile_worker2]
        random.shuffle(decision_a)
        profiles.append(decision_a)
        decision_b = [C.profile_worker3, C.profile_worker4]
        random.shuffle(decision_b)
        profiles.append(decision_b)
        decision_c = [C.profile_worker1, C.profile_worker3]
        random.shuffle(decision_c)
        profiles.append(decision_c)
        decision_d = [C.profile_worker2, C.profile_worker4]
        random.shuffle(decision_d)
        profiles.append(decision_d)
        player.participant.profiles = profiles
        random.shuffle(player.participant.profiles)
"""

def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        all_pairs = C.profiles_worker.copy()
        all_pairs.extend(all_pairs)
        player.participant.pairs = all_pairs
        random.shuffle(player.participant.pairs)
        # print ("PAIRS", player.participant.pairs)
        """
        pairs = []
        pair1 = [C.profiles_worker[0]]
        pairs.append(pair1)
        pair2 = [C.profiles_worker[1]]
        pairs.append(pair2)
        print ("PAIRS", pairs)
        pair3 = [C.profiles_worker[2]]
        pairs.append(pair3)
        pair4 = [C.profiles_worker[3]]
        pairs.append(pair4)
        pair5 = [C.profiles_worker[4]]
        pairs.append(pair5)
        pair6 = [C.profiles_worker[5]]
        pairs.append(pair6)
        pair7 = [C.profiles_worker[6]]
        pairs.append(pair7)
        pair8 = [C.profiles_worker[7]]
        pairs.append(pair8)
        pair9 = [C.profiles_worker[8]]
        pairs.append(pair9)
        pair10 = [C.profiles_worker[9]]
        pairs.append(pair10)
        pair11 = [C.profiles_worker[10]]
        pairs.append(pair11)
        pair12 = [C.profiles_worker[11]]
        pairs.append(pair12)
        pair13 = [C.profiles_worker[12]]
        pairs.append(pair13)
        pair14 = [C.profiles_worker[13]]
        pairs.append(pair14)
        pair15 = [C.profiles_worker[14]]
        pairs.append(pair15)
        pair16 = [C.profiles_worker[15]]
        pairs.append(pair16)
        player.participant.pairs = pairs
        random.shuffle(player.participant.pairs)
        mat_topf_topm = [C.profiles_mat[0], C.profiles_mat[12]]
        random.shuffle(mat_topf_topm)
        profiles.append(mat_topf_topm)
        player.participant.profiles = profiles
        random.shuffle(player.participant.profiles)
        """


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(blank=True)
    decision_race = models.StringField(blank=True)
    gender1 = models.StringField(verbose_name='')
    gender2 = models.StringField(verbose_name='')
    race1 = models.StringField(verbose_name='')
    race2 = models.StringField(verbose_name='')
    offer1 = models.StringField(verbose_name='')
    offer2 = models.StringField(verbose_name='')
    age1 = models.StringField(verbose_name='')
    age2 = models.StringField(verbose_name='')
    usedprofiles = models.StringField()
    norankdecision = models.IntegerField()


# PAGES
class InstructionsHiring(Page):
    def is_displayed(player: Player):
        return player.round_number == 1


class Decision1(Page):
    form_model = 'player'
    form_fields = ['decision', 'offer1', 'offer2', 'age1', 'age2', 'decision_race', 'race1',
                   'race2', 'gender1', 'gender2']
    # decision_race löschen? 

    def vars_for_template(player: Player):
        participant = player.participant
        if player.round_number == 1:
            # profiles1 = player.participant.pairs[player.round_number - 1][0]
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 2:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 3:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 4:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 5:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 6:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 7:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 8:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 9:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 10:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 11:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 12:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 13:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 14:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 15:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 16:
            profiles = participant.pairs[player.round_number - 1]
        # print ("PROFILES", profiles)
        """
        if player.round_number == 5:
            profile1 = player.participant.profiles[player.round_number - 1][0] --> ohne participant = player.participant
            profile2 = player.participant.profiles[player.round_number - 1][1]
        """
        worker1_id = profiles["worker1_id"]
        worker2_id = profiles["worker2_id"]
        worker1_gender = profiles["gender_worker1"]
        worker2_gender = profiles["gender_worker2"]
        worker1_race = profiles["race_worker1"]
        worker2_race = profiles["race_worker2"]
        worker1_age = profiles["agegroup_worker1"]
        worker2_age = profiles["agegroup_worker2"]
        return {
            'worker1_id': worker1_id,
            'worker2_id': worker2_id,
            'worker1_gender': worker1_gender,
            'worker2_gender': worker2_gender,
            'worker1_race': worker1_race,
            'worker2_race': worker2_race,
            'worker1_age': worker1_age,
            'worker2_age': worker2_age,
            'i1': '<input name="decision" type="radio" id="w1" value="' + worker1_id + '"' + '/>',
            'i2': '<input name="decision" type="radio" id="w2" value="' + worker2_id + '"' + '/>',
        }

    #missing: write decision into excel file?

    #def before_next_page(player, timeout_happened):
     #   player.decision_race = str(df1.loc[(df1.prolificid == player.decision), "race"].values[0])
      #  if player.participant.profiles[player.round_number - 1][0]["mat_rank"] == 4:
       #     player.norankdecision = 1
        #else:
         #   player.norankdecision = 0

    def error_message(player, values):
        if values['decision'] == "":
            return 'You forgot to hire a worker. Please click on the worker who you want to hire.'

""" maybe: 
{{ formfield_errors 'offer1' }}
{{ formfield_errors 'offer2' }}
{{ formfield_errors 'age1' }}
{{ formfield_errors 'age2' }}
{{ formfield_errors 'race1' }}
{{ formfield_errors 'race2' }}
{{ formfield_errors 'decision' }}
{{ formfield_errors 'decision_race' }}
in html file (bottom)"""


page_sequence = [InstructionsHiring, Decision1]
