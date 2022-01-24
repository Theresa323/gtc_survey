from otree.api import *


doc = 'survey_part_2'


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
    NAME_IN_URL = 'gtc3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #postgamesurvey
    q1 = make_question('Question 1: _')
    q2 = make_question('Question 2: _')
    q3 = make_question('Question 3: _')
    q4 = make_question('Question 4: _')
    q5 = make_question('Question 5: _')
    q6 = make_question('Question 6: _')
    q7 = make_question('Question 7: _')
    q8 = make_question('Question 8: _')
    q9 = make_question('Question 9: _')
    q10 = make_question('Question 10: _')
    q11 = make_question('Question 11: _')
    q12 = make_question('Question 12: _')
    q13 = make_question('Question 13: _')
    q14 = make_question('Question 14: _')
    q15 = make_question('Question 15: _')
    q16 = make_question('Question 16: _')
    q17 = make_question('Question 17: _')
    q18 = make_question('Question 18: _')
    q19 = make_question('Question 19: _')
    q20 = make_question('Question 20: _')
    q21 = make_question('Question 21: _')
    q22 = make_question('Question 22: _')
    q23 = make_question('Question 23: _')

# PAGES

class Likert_Instructions(Page):
    pass

class Likert1(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5'] #5 questions

class Likert2(Page):
    form_model = 'player'
    form_fields = ['q6', 'q7', 'q8'] #3 questions

class Likert3(Page):
    form_model = 'player'
    form_fields = ['q9', 'q10', 'q11', 'q12'] #4 questions

class Likert4(Page):
    form_model = 'player'
    form_fields = ['q13', 'q14', 'q15'] #3 questions

class Likert5(Page):
    form_model = 'player'
    form_fields = ['q16', 'q17', 'q18', 'q19'] #4 questions

class Likert6(Page):
    form_model = 'player'
    form_fields = ['q20', 'q21', 'q22', 'q23'] #4 questions

class Closing(Page):
    pass


page_sequence = [Likert_Instructions, Likert1, Likert2, Likert3, Likert4, Likert5, Likert6, Closing] 