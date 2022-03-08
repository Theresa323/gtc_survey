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
    q1 = make_question('This e-Learning game provides sufficient information [for the intended learning purpose/the game/for extending my knowledge (on different cities)].')
    q2 = make_question('The e-Learning game provides accurate information for [-‘‘-].')
    q3 = make_question('The e-Learning game provides useful information for [-‘‘-].')
    q4 = make_question('The e-Learning game provides relevant information for [-‘‘-].')
    q5 = make_question('Overall information provided by the e-Learning game is satisfactory.')
    q6 = make_question('Use of the this e-Learning game is simple.')
    q7 = make_question('The e-Learning game is easy to comprehend.')
    q8 = make_question('As a whole, the e-Learning game is easy to use.')
    q9 = make_question('Use of this e-Learning game enabled me to accomplish [learning about different cities] more quickly.')
    q10 = make_question('Use of the e-Learning game improved the quality of my tasks.')
    q11 = make_question('Use of the e-Learning game enhanced the effectiveness of my tasks.')
    q12 = make_question('As a whole, the e-Learning game is useful to me.')
    q13 = make_question('Using this e-Learning game would give me a sense of self-control of my learning pace.')
    q14 = make_question('My decision to use the e-Learning game was a wise one.')
    q15 = make_question('In general, using the e-Learning game would give me a sense of satisfaction.')
    q16 = make_question('This e-Learning game was useful for my  learning about cities in Israel and Germany.')
    q17 = make_question('The e-Learning game helped me learn about cities in Israel and Germany well.')
    q18 = make_question('The e-Learning game facilitated my understanding of[differences between cities in Israel and Germany.')
    q19 = make_question('My knowledge of cites in Israel and Germany was enlarged with the use of e-Learning game .')
    q20 = make_question('I [would] use this e-Learning game in the future.')
    q21 = make_question('[Given the opportunity,] I [would] intend to use the e-Learning game more [for learning about different cities].')
    q22 = make_question('I [would] intend to use the e-Learning game more in another context .')
    q23 = make_question('[Given the opportunity,] I [would] intend to increase my use of the e-Learning game in the future.')

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