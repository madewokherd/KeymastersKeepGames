from __future__ import annotations
from dataclasses import dataclass
import functools
from Options import Toggle, OptionSet
from typing import List, Dict, Set
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class SmwPracticeCartOptions:
    pass

class SmwPracticeCartGame(Game):
    name = "SMW Practice Cart"
    platform = KeymastersKeepGamePlatforms.SNES
    platforms_other = []
    is_adult_only_or_unrated = False
    options_cls = SmwPracticeCartOptions

    full_exits = [
        "Yoshi's Island 1",
        "Yoshi's Island 2",
        "Yoshi's Island 3",
        "Yoshi's Island 4",
        "Donut Plains 1",
        "Donut Plains 1 Secret",
        "Donut Plains 2",
        "Donut Plains 3",
        "Donut Plains 4",
        "Donut Secret 1",
        "Donut Secret 1 Secret",
        "Donut Secret 2",
        "Vanilla Dome 1",
        "Vanilla Dome 1 Secret",
        "Vanilla Dome 2",
        "Vanilla Dome 2 Secret",
        "Vanilla Ghose House",
        "Vanilla Dome 3",
        "Vanilla Dome 4",
        "Cheese Bridge Area",
        "Cheese Bridge Area Secret",
        "Cookie Mountain",
        "Vanilla Secret 1",
        "Vanilla Secret 1 Secret",
        "Vanilla Secret 2",
        "Vanilla Secret 3",
        "Butter Bridge 1",
        "Butter Bridge 2",
        "Forest of Illusion 2",
        "Forest of Illusion 2 Secret",
        "Forest of Illusion 3",
        "Forest of Illusion 3 Secret",
        "Forest Ghost House",
        "Forest of Illusion 4",
        "Forest of Illusion 4 Secret",
        "Forest Secret Area",
        "#5 Roy's Castle",
        "Chocolate Island 1",
        "Chocolate Island 2",
        "Chocolate Island 3",
        "Chocolate Island 3 Secret",
        "Chocolate Island 4",
        "Chocolate Island 5",
        "Sunken Ghost Ship",
        "Valley of Bowser 1",
        "Valley of Bowser 2",
        "Valley Ghost House",
        "Valley of Bowser 3",
        "#7 Larry's Castle",
        "Gnarly",
        "Tubular",
        "Way Cool",
        "Awesome",
        "Groovy",
        "Mondo",
        "Outrageous",
        "Funky",
    ]

    no_ld_exits = [
        "Yellow Switch Palace",
        "#1 Iggy's Castle",
        "Donut Plains 2 Secret",
        "Green Switch Palace",
        "Donut Ghost House (exit to Donut Plains 3)",
        "#2 Morton's Castle",
        "Donut Secret House",
        "Donut Secret House Secret",
        "Red Swich Palace",
        "#3 Lemmy's Castle",
        "Vanilla Fortress",
        "#4 Ludwig's Castle",
        "Forest of Illusion 1",
        "Forest of Illusion 1 Secret",
        "Blue Switch Palace",
        "Forest Ghose House Secret",
        "Forest Fortress",
        "Choco-Ghost House",
        "Chocolate Island 2 Secret",
        "Chocolate Fortress",
        "Chocolate Secret",
        "#6 Wendy's Castle",
        "Valley of Bowser 2 Secret",
        "Valley Fortress",
        "Back Door",
        "Valley Ghost House Secret",
        "Valley of Bowser 4",
        "Valley of Bowser 4 Secret",
        "Front Door",
        "Star World 2",
        "Star World 2 Secret",
        "Star World 3 Secret",
        "Star World 4",
        "Star World 4 Secret",
        "Star World 5",
        "Star World 5 Secret",
    ]

    cape_only_exits = [
        "Donut Ghost House (exit to Top Secret Area)",
        "Star World 3",
    ]

    mush_full_exits = [
        "Star World 1",
        "Star World 1 Secret",
    ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Get the small-only gold time in EXIT",
                data={
                    "EXIT": (self.full_exits + self.no_ld_exits, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=len(self.full_exits) + len(self.no_ld_exits),
            ),
            GameObjectiveTemplate(
                label="Get the no cape gold time in EXIT",
                data={
                    "EXIT": (self.full_exits + self.no_ld_exits + self.mush_full_exits, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=len(self.full_exits) + len(self.no_ld_exits) + len(self.mush_full_exits),
            ),
            GameObjectiveTemplate(
                label="Get the cape gold time in EXIT",
                data={
                    "EXIT": (self.full_exits + self.no_ld_exits + self.mush_full_exits + self.cape_only_exits, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=len(self.full_exits) + len(self.no_ld_exits) + len(self.mush_full_exits) + len(self.cape_only_exits),
            ),
            GameObjectiveTemplate(
                label="Get the lunar dragon gold time in EXIT",
                data={
                    "EXIT": (self.full_exits + self.mush_full_exits, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=len(self.full_exits) + len(self.mush_full_exits),
            ),
        ]
        
        return objectives
