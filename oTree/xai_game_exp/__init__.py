from otree.api import *


doc = 'xai_game_exp'


class C(BaseConstants):
    NAME_IN_URL = 'game_a'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# PAGES

class Pre_Game_Instructions(Page):
    pass

class Game(Page):
    pass



page_sequence = [Pre_Game_Instructions, Game] 