from otree.api import *
import requests
import json


doc = 'survey_part_2_exp'


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
    NAME_IN_URL = 'survey_a'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #postgamesurvey
    q1 = make_question('This game provides sufficient information for expanding my knowledge on German and Israeli cities.')
    q2 = make_question('The game provides accurate information for expanding my knowledge on German and Israeli cities.')
    q3 = make_question('The game provides useful information for expanding my knowledge on German and Israeli cities.')
    q4 = make_question('The game provides relevant information for expanding my knowledge on German and Israeli cities.')
    q5 = make_question('Overall information provided by the game is satisfactory.')

    q6 = make_question('Use of the this game is simple.')
    q7 = make_question('The game is easy to comprehend.')
    q8 = make_question('As a whole, the game is easy to use.')

    q9 = make_question('Use of this game enabled me to learn about German and Israeli cities  quickly.')
    q10 = make_question('Use of the game enables high-quality learning about German and Israeli cities.')
    q11 = make_question('Use of the game enables effective learning about German and Israeli cities.')
    q12 = make_question('As a whole, the game is useful to me.')

    q13 = make_question('Using this game would give me a sense of self-control of my learning pace.')
    q14 = make_question('My decision to use the game was a wise one.')
    q15 = make_question('In general, using the game would give me a sense of satisfaction.')

    q16 = make_question('This game was useful for learning about cities in Israel and Germany.')
    q17 = make_question('The game helped me learn about cities in Israel and Germany well.')
    q18 = make_question('The game facilitated my understanding of German and Israeli cities.')
    q19 = make_question('My knowledge of cites in Israel and Germany was increased by playing this game.')
    
    q20 = make_question('I would use this game for learning in the future.')
    q21 = make_question('Given the opportunity, I would like to use this game for learning about different cities.')
    q22 = make_question('I would like to use this game for learning in another context.')
    q23 = make_question('Given the opportunity, I would like to increase my use of this game for future learning about the four cities.')

    attentioncheck1 = make_question('Tel Aviv was one of the four options to choose from in the game.')
    attentioncheck2 = make_question('Cologne was one of the four options to choose from in the game.')

    feedback = models.LongStringField(label = 'If you have any feedback or suggestions on how to improve the game and respective survey, we’d love to hear your thoughts.')


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
    form_fields = ['q9', 'q10', 'attentioncheck1', 'q11', 'q12'] #4 questions

class Likert4(Page):
    form_model = 'player'
    form_fields = ['q13', 'q14', 'q15'] #3 questions

class Likert5(Page):
    form_model = 'player'
    form_fields = ['q16', 'q17', 'q18', 'q19', 'attentioncheck2'] #4 questions

class Likert6(Page):
    form_model = 'player'
    form_fields = ['q20', 'q21', 'q22', 'q23'] #4 questions

class Closing(Page):
    @staticmethod
    def vars_for_template(player):
        p_code = player.participant.code
        #score = requests.get("https://gtc.xaidemo.de/?player="+str(p_code)+"/final_score").json()
        #ai_score = score["ai_score"]
        #player_score = score["player_score"]
        #print ("Type score_ai: ", type(score_ai))
        #print ("json score_ai: ", score_ai.json())
        player_score = 11
        ai_score = 11
        return {"score_ai": ai_score, "score_player": player_score}
    form_model = 'player'
    form_fields = ['feedback'] 



page_sequence = [Likert_Instructions, Likert1, Likert2, Likert3, Likert4, Likert5, Likert6, Closing] 