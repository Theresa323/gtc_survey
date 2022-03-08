from os import environ


SESSION_CONFIGS = [
    dict(
        name='full_gtc_survey',
        display_name="GTC survey",
        app_sequence=['survey_part_1', 'xai_game', 'survey_part_2'],
        num_demo_participants=3,
    ),
    dict(
        name='survey_part_1',
        display_name="Survey Part 1",
        app_sequence=['survey_part_1'],
        num_demo_participants=3,
    ),
    dict(
        name='xai_game',
        display_name="XAI Game",
        app_sequence=['xai_game'],
        num_demo_participants=3,
    ),
    dict(
        name='survey_part_2',
        display_name="Survey Part 2",
        app_sequence=['survey_part_2'],
        num_demo_participants=3,
    ),
    dict(
        name='gtc_survey_with_explanations',
        display_name="Guess the Country",
        app_sequence=['survey_part_1', 'xai_game', 'survey_part_2'],
        num_demo_participants=3,
    ),
    dict(
        name='gtc_survey_without_explanations',
        display_name="Guess the Country",
        app_sequence=['survey_part_1', 'xai_game', 'survey_part_2'],
        num_demo_participants=3,
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
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '9853832187501'

INSTALLED_APPS = ['otree']
