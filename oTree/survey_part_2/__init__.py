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
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #postgamesurvey
    q1 = make_question('The AI provides me with sufficient information to match Google Streetview pictures to their four originating cities.')
    q2 = make_question('The AI provides me with accurate information to match Google Streetview pictures to their four originating cities.')
    q3 = make_question('The AI provides me with useful information to match Google Streetview pictures to their four originating cities.')
    q4 = make_question('The AI provides me with relevant information to match Google Streetview pictures to their four originating cities.')
    q5 = make_question('Overall information on matching Google Streetview pictures to their four originating cities by the AI is satisfactory')

    q6 = make_question('Interaction with the AI is simple.')
    q7 = make_question('Interaction with the AI is easy to comprehend.')
    q8 = make_question('As a whole, interaction with the AI is easy.')

    q9 = make_question('Interaction with the AI enables me to quickly match Google Streetview pictures to their four originating cities.')
    q10 = make_question('Interaction with the AI improves the quality of  matching Google Streetview pictures to their four originating cities.')
    q11 = make_question('Interaction with the AI enables effective matching of Google Streetview pictures to their four originating cities.')
    q12 = make_question('As a whole, interaction with the AI is useful in matching Google Streetview pictures to their four originating cities.')

    q13 = make_question('Interaction with the AI would give me sense of self-control over my learning process in matching Google Streetview pictures to their four originating cities.')
    q14 = make_question('In case I want to learn how to match Google Streetview pictures to their four originating cities, my decision to interact with the AI would be a wise one.')
    q15 = make_question('In general, interacting with the AI to match Google Streetview pictures to their four originating cities would give me a sense of satisfaction.')
    q16 = make_question('Interacting with the AI would give me a satisfying opportunity to explore matching Google Streetview pictures to their four originating cities.')

    q17 = make_question('Interaction with the AI was useful for learning about matching Google Streetview pictures to their four originating cities.')
    q18 = make_question('The AI helped me to learn about matching Google Streetview pictures to their four originating cities.')
    q19 = make_question('The AI facilitated my understanding of matching Google Streetview pictures to their four originating cities.')
    q20 = make_question('My knowledge of matching Google Streetview pictures to their four originating cities was increased by interacting with the AI.')
    
    q21 = make_question('I would interact with the AI for future learning on matching Google Streetview pictures to their cities.')
    q22 = make_question('Given the opportunity, I would like to interact with the AI to match different Google Streetview pictures.')
    q23 = make_question('I would like to interact with the AI in another context..')
    q24 = make_question('Given the opportunity, I would like to increase my interaction with the AI for future learning on Google Streetview picture matching.')

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
    form_fields = ['q13', 'q14', 'q15', 'q16'] #4 questions

class Likert5(Page):
    form_model = 'player'
    form_fields = ['q17', 'q18', 'q19', 'q20', 'attentioncheck2'] #4 questions

class Likert6(Page):
    form_model = 'player'
    form_fields = ['q21', 'q22', 'q23', 'q24'] #4 questions

class Closing_passed(Page):
    @staticmethod
    def vars_for_template(player):
        try: 
            p_code = player.participant.unique_id #unique_code statt participant code
            print(p_code)
            score = requests.get("https://gtc.xaidemo.de/api/study/"+str(p_code)+"/final_score").json() 
            ai_score = score["ai_score"]
            player_score = score["player_score"]
        except:
            player_score = 11
            ai_score = 11
        return {"score_ai": ai_score, "score_player": player_score}
    @staticmethod
    def is_displayed(player):
        return ((player.attentioncheck1 != (1 or 2)) and (player.attentioncheck2 != (4 or 5)) and not(player.attentioncheck1 == 3 and player.attentioncheck2 == 3))
    form_model = 'player'
    form_fields = ['feedback'] 

class Closing_failed(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return ((player.attentioncheck1 == (1 or 2)) or (player.attentioncheck2 == (4 or 5)) or (player.attentioncheck1 == 3 and player.attentioncheck2 == 3))


page_sequence = [Likert_Instructions, Likert1, Likert2, Likert3, Likert4, Likert5, Likert6, Closing_passed, Closing_failed] 