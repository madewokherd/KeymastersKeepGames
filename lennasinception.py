from __future__ import annotations
from dataclasses import dataclass
import functools
from Options import Toggle, OptionSet
from typing import List, Dict, Set
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class LennasInceptionOptions:
    pass

class LennasInceptionGame(Game):
    name = "Lenna's Inception"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = []
    is_adult_only_or_unrated = False
    options_cls = LennasInceptionOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Be followed by COMPANION",
                data={
                    "COMPANION": ((
                        "Bruce the Bat",
                        "Gourdon the Pumpkin",
                        "MeggaHenrietta",
                        "Paige",
                        ), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Obtain ITEM",
                data={
                    "ITEM": ((
                        "the Phoenix Ash",
                        "the Hammer",
                        "the Woodcutter's Axe",
                        "the Lasso or Chain",
                        "the Lance",
                        "the Claymore",
                        "the Stiletto",
                        ), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=9,
            ),
            GameObjectiveTemplate(
                label="Obtain ITEM",
                data={
                    "ITEM": ((
                        "Binoculars",
                        "the Police Report",
                        "the Book of Changes",
                        "an IOU",
                        "the Beta Cup",
                        "Patent No. 950996",
                        "Error Log",
                        "Paige's Locket",
                        ), 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=8,
            ),
            GameObjectiveTemplate(
                label="Obtain ITEM",
                data={
                    "ITEM": ((
                        "the Revolver",
                        "the Buoy",
                        "Cross Bombs",
                        "Glider Bombs",
                        "Spring Shoes",
                        "Chain",
                        "Damascus Katana",
                        ), 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the game with the Catastrophe ending",
                data={
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the game with the Sacrifice or Perfect ending",
                data={
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the game with the Perfect ending",
                data={
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat or spare BOSS",
                data={
                    "BOSS": ((
                        "Archangel Azraflail",
                        "Archangel Catsiel",
                        "Archangel Crabaddon",
                        "Archangel Hatasiah",
                        "Archangel Headraniel",
                        "Archangel Sandolphin",
                        "Archangel Santaquiel",
                        "Archangel Tentaluchus",
                        ), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=8,
            ),
            GameObjectiveTemplate(
                label="Obtain all 4 ventricles",
                data={
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Identify EFFECT Potion or Tunic",
                data={
                    "EFFECT": ((
                        "a Strength",
                        "a Defense",
                        "a Slow",
                        "a Speed",
                        "a Healing",
                        "a Poison",
                        "a Weak Poison",
                        "a Camouflage",
                        "a Fire",
                        "a Fire Resistance",
                        "a Growth",
                        "a Frugal",
                        "a Beer",
                        "a Hallucination",
                        "a Blast Protection",
                        "an Explosion",
                        "an Undead",
                        "a Hover",
                        "a Water",
                        "a Blood",
                        "a Urine",
                        ), 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Spare BOSS",
                data={
                    "BOSS": ((
                        "Archangel Azraflail",
                        "Archangel Catsiel",
                        "Archangel Crabaddon",
                        "Archangel Hatasiah",
                        "Archangel Headraniel",
                        "Archangel Sandolphin",
                        "Archangel Santaquiel",
                        "Archangel Tentaluchus",
                        "The Chairman",
                        "Delvin",
                        ), 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]
        
        return objectives

