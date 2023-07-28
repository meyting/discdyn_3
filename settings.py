from os import environ

SESSION_CONFIGS = [
    dict(
         name='employer_stage2_binary',
         app_sequence=['employer2_binary_scores'],
         num_demo_participants=10,
     ),
    dict(
         name='survey_employer2',
         app_sequence=['survey_employer2'],
         num_demo_participants=10,
     ),
    dict(
         name='employer2_alles',
         app_sequence=['start_employer2', 'employer2_binary_scores', 'survey_employer2'],
         num_demo_participants=10,
     ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ["pairs2", "usedprofiles_stage2", 'task_rounds', 'expiry',
                      'total_points_sequence', "profile_participant"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8706067051652'
