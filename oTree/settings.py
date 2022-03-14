from os import environ


SESSION_CONFIGS = [
    dict(
        name='GTC_survey',
        display_name="GTC survey",
        app_sequence=['survey_part_1', 'xai_game', 'survey_part_2'],
        num_demo_participants=100,
    ),
    dict(
        name='survey_with_explanations',
        display_name="GTC with explanations",
        app_sequence=['survey_part_1', 'xai_game', 'survey_part_2'],
        num_demo_participants=100,
        explanations = True,
    ),
    dict(
        name='survey_without_explanations',
        display_name="GTC without explanations",
        app_sequence=['survey_part_1', 'xai_game', 'survey_part_2'],
        num_demo_participants=100,
        explanations = False,
    ),
    dict(
        name='survey_part_1',
        display_name="Survey Part 1",
        app_sequence=['survey_part_1'],
        num_demo_participants=100,
    ),
    dict(
        name='xai_game_exp',
        display_name="XAI Game wit explanations",
        app_sequence=['xai_game'],
        num_demo_participants=100,
        explanations = True,
    ),
    dict(
        name='xai_game_noexp',
        display_name="XAI Game no explanations",
        app_sequence=['xai_game'],
        num_demo_participants=100,
        explanations = False,
    ),
    dict(
        name='xai_game_random',
        display_name="XAI Game random",
        app_sequence=['xai_game'],
        num_demo_participants=100,
    ),
    dict(
        name='survey_part_2',
        display_name="Survey Part 2",
        app_sequence=['survey_part_2'],
        num_demo_participants=100,
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='survey', 
        display_name='Survey'),
    dict(
        name='test', 
        display_name='Test'),
    dict(
        name='pre_study', 
        display_name='Pre-Study'),
    dict(
        name='pre_study_test', 
        display_name='Pre-Study Test'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '9853832187501'

INSTALLED_APPS = ['otree']
