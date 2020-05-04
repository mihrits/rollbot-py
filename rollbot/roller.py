import logging
import re
import random

from rollbot.model.DiceRoll import DiceRoll

logger = logging.getLogger(__name__)


def roll(rollCommand: str):
  if not re.search('\\d+d\\d+([+-]]\\d+)?', rollCommand):
    logger.error(f"Failed to parse {rollCommand}")
    return DiceRoll(rollCommand, valid=False)
  else:
    logger.info(f"Rolling {rollCommand}")
    modifier = 0
    dice = rollCommand
    if '+' in rollCommand:
      dice, modifier = rollCommand.split('+')
      modifier = int(modifier)
    if '-' in rollCommand:
      dice, modifier = rollCommand.split('-')
      modifier = -int(modifier)
    count, faces = list(map(int, dice.split('d')))
    return DiceRoll(rollCommand, count, faces, getResults(count, faces), modifier)


def reroll(roll: DiceRoll):
  return DiceRoll(roll.command, roll.diceCount, roll.diceFaces, getResults(roll.diceCount, roll.diceFaces),
                  roll.modifier)


def getResults(diceCount: int, diceFaces: int):
  results = []
  for i in range(0, diceCount):
    results.append(random.randint(1, diceFaces))  # todo inject random function
  logger.debug(f"results: {results}")
  return results