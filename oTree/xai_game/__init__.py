from otree.api import *
import itertools
import uuid

doc = 'xai_game_exp'


class C(BaseConstants):
	NAME_IN_URL = 'game'
	PLAYERS_PER_GROUP = None
	NUM_ROUNDS = 1


class Subsession(BaseSubsession):
	pass

def creating_session(subsession: Subsession):

	if subsession.round_number == 1:
		treatment = itertools.cycle([True, False])
		for player in subsession.get_players():
			player.explanation = next(treatment)
			player.unique_id = str(uuid.uuid4())
			print(player.id, player.explanation, player.unique_id)

class Group(BaseGroup):
	pass

class Player(BasePlayer):
	explanation = models.BooleanField()
	unique_id = models.StringField()

# PAGES

class Pre_Game_Instructions_with_exp(Page):
	@staticmethod
	def is_displayed(player):
		return player.explanation

class Game_with_exp(Page):
	@staticmethod
	def is_displayed(player):
		return player.explanation

class Pre_Game_Instructions_without_exp(Page):
	@staticmethod
	def is_displayed(player):
		return not player.explanation

class Game_without_exp(Page):
	@staticmethod
	def is_displayed(player):
		return not player.explanation



page_sequence = [Pre_Game_Instructions_with_exp, Pre_Game_Instructions_without_exp, Game_with_exp, Game_without_exp] 