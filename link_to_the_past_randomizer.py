from __future__ import annotations
from dataclasses import dataclass
import functools
from Options import Toggle, OptionSet
from typing import List, Dict, Set
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class LttprArchipelagoOptions:
    pass

class LttprGame(Game):
    name = "A Link To The Past Randomizer"
    platform = KeymastersKeepGamePlatforms.SNES
    platforms_other = []
    is_adult_only_or_unrated = False
    options_cls = LttprArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Defeat the boss of DUNGEON",
                data={
                    "DUNGEON": ((
                        "Eastern Palace",
                        "Desert Palace",
                        "Tower of Hera",
                        "Castle Tower",
                        "Palace of Darkness",
                        "Skull Woods",
                        "Swamp Palace",
                        "Thieves Town",
                        "Ice Palace",
                        "Misery Mire",
                        "Turtle Rock",
                        "Ganon's Tower",
                        ), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Catch the runner in Kakariko",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Purple Chest",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="King's Tomb entrance",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Pay for a mini-game in 3 distinct locations, or enter 3 take-any caves",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Mimic Cave entrance",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Master Sword Pedestal",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Pyramid Fairy entrance",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Activate Flute",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Open the chest in Zelda's Cell",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach the non-bombable pyramid opening",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Fishbone room keydrop",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Throw a fish in the water",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Visit the Catfish with a Follower",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Sell something to the bottle vendor",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat a Deadrock",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat a Lynel",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat GT basement boss",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Clear 2 tile rooms",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Rescue the lost old man",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Catch the runner in Kakariko, or defeat Agahnim in Castle Tower",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat Ganon",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="15 bomb capacity",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="40 arrow capacity, or Rupee Quiver",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Open Turtle Rock",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Open Misery Mire",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Collect a Fairy in DUNGEON",
                data={
                    "DUNGEON": ((
                        "Eastern Palace",
                        "Desert Palace",
                        "Tower of Hera",
                        "Castle Tower",
                        "Palace of Darkness",
                        "Skull Woods",
                        "Swamp Palace",
                        "Thieves Town",
                        "Ice Palace",
                        "Misery Mire",
                        "Turtle Rock",
                        "Ganon's Tower",
                        ), 5),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Activate a telepathic tile in DUNGEON",
                data={
                    "DUNGEON": ((
                        "Eastern Palace",
                        "Desert Palace",
                        "Tower of Hera",
                        "Palace of Darkness",
                        "Swamp Palace",
                        "Thieves Town",
                        "Ice Palace",
                        "Misery Mire",
                        "Turtle Rock",
                        "Ganon's Tower",
                        ), 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to 3 stories for 20 rupees each",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to the storytelling bird",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to the storytelling bird",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to the storytelling insect",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to the storytelling octopus",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to the storytelling tree",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Listen to the storytelling hand",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get followed by the former Thief",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Buy something from a dark world shopkeeper",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Buy advice from all 3 fortune tellers",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Magic Bat",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Talk to everyone in the tavern",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Use powder on the sweeping lady in Kakariko",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Talk to 8 bomb trees in the dark world",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Take 4 waterfall portals",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Read a book",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Powder a Buzz Blob (green zappy enemies)",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Stun a Toppo, or defeat Agahnim in Castle Tower",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Lose your shield, or collect Mirror Shield",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Hammer a frozen enemy",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Pull something from the Turtle Rock paw",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Pull something from a portrait",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Enter the 20-rupee and 50-rupee caves, or 2 take-any caves",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Read the sign in race game",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Pull a tongue statue",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Obtain 4 unique bottle items (can be in sequence)",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="10 health capacity",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Find 3 fairy fountains",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Find 3 fairy healers, or 3 take-any caves",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Enter all segments of the 3-segmented room in Thieves Town",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Thieves Town bumper room",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Swamp Palace dead end pot rooms",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Spike Cave",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Eat an apple",
                data={
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]
        
        return objectives

