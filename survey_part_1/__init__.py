from otree.api import *


doc = 'survey_part_1'


class C(BaseConstants):
    NAME_IN_URL = 'gtc1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.IntegerField(
        choices=[
            [1, 'male'],
            [2, 'female'],
            [3, 'other'],
        ],
        label='What best describes your gender?'
    )

    year_of_birth = models.IntegerField(
        min=1922, max=2022, 
        label='What is your year of birth? ')

    nationality = models.IntegerField(
        choices=[
            [1, 'german'],
            [2, 'israeli'],
        ],
        label='What is your nationality?'
    )

    education = models.IntegerField(
        choices=[
            [1, 'High School'],
            [2, 'Undergraduate Degree'],
            [3, 'Graduate Degree'],
            [4, 'Post-graduate Degree'],
            [5, 'Vocational Education'],
            [6, 'Prefer not to say'],
        ],
        label='How would you describe your education?'
    )

    been_to_germany = models.BooleanField(
        choices=[[True, 'yes'],[False, 'no'],],
        label='Have you ever been to Germany?'
    )
    been_to_berlin = models.BooleanField(
        choices=[[True, 'yes'],[False, 'no'],],
        label='Have you ever been to Berlin?'
    )
    been_to_hamburg = models.BooleanField(
        choices=[[True, 'yes'],[False, 'no'],],
        label='Have you ever been to Hamburg?'
    )
    been_to_israel = models.BooleanField(
        choices=[[True, 'yes'],[False, 'no'],],
        label='Have you ever been to Israel?'
    )
    been_to_jerusalem = models.BooleanField(
        choices=[[True, 'yes'],[False, 'no'],],
        label='Have you ever been to Jerusalem?'
    )
    been_to_telaviv = models.BooleanField(
        choices=[[True, 'yes'],[False, 'no'],],
        label='Have you ever been to Tel Aviv?'
    )

# PAGES
class Introduction(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'year_of_birth', 'nationality', 'education']

class Pre_Game_Survey(Page):
    form_model = 'player'
    form_fields = ['been_to_germany', 'been_to_berlin','been_to_hamburg','been_to_israel', 'been_to_jerusalem','been_to_telaviv']



page_sequence = [Introduction, Demographics, Pre_Game_Survey]
