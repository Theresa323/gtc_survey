from otree.api import *


doc = 'GTC_survey'


def make_question(label):
    return models.IntegerField(
        choices=[
            (1, "(1) strongly disagree"),
            (2, "(2) disagree"),
            (3, "(3) unsure"),
            (4, "(4) agree"),
            (5, "(5) strongly agree")
        ],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )

class C(BaseConstants):
    NAME_IN_URL = 'gtc'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #pregamesurvey
    gender = models.IntegerField(
        choices=[
            [1, 'male'],
            [2, 'female'],
            [3, 'other'],
        ]
    )

    year_of_birth = models.IntegerField(min=1922, max=2022)

    been_to_germany = models.BooleanField(
        choices=[
            [False, 'no'],
            [True, 'yes'],
        ]
    )
    #postgamesurvey
    q1 = make_question('Question 1: _')
    q2 = make_question('Question 2: _')
    q3 = make_question('Question 3: _')
    q4 = make_question('Question 4: _')
    q5 = make_question('Question 5: _')
    q6 = make_question('Question 6: _')

# PAGES
class Introduction(Page):
    pass

class Pre_Game_Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'year_of_birth', 'been_to_germany']

class Pre_Game_Instructions(Page):
    pass

class Post_Game_Instructions(Page):
    pass

class Likert1(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3']

class Likert2(Page):
    form_model = 'player'
    form_fields = ['q4', 'q5', 'q6']

class Closing(Page):
    pass

class Results(Page): #nur zum Testen
    pass


page_sequence = [Pre_Game_Survey, Likert1, Likert2, Results] #zum testen nur die Seiten mit Feldern
#page_sequence = [Introduction, Pre_Game_Survey, Pre_Game_Instructions, Post_Game_Instructions, Likert1, Likert2, Closing]