from __future__ import annotations
from dataclasses import dataclass
import functools
from Options import Toggle, OptionSet
from typing import List, Dict, Set
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class VVVVVVOptions:
    vvvvvv_custom_levels: VVVVVVCustomLevels

class VVVVVVGame(Game):
    name = "VVVVVV"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [KeymastersKeepGamePlatforms.SW, KeymastersKeepGamePlatforms._3DS, KeymastersKeepGamePlatforms.VITA, KeymastersKeepGamePlatforms.PS4, KeymastersKeepGamePlatforms.IOS, KeymastersKeepGamePlatforms.AND]
    is_adult_only_or_unrated = False
    options_cls = VVVVVVOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Complete TRIAL in time trial mode CONSTRAINT",
                data={
                    "TRIAL": ((
                        "Space Station 1",
                        "Laboratory",
                        "The Tower",
                        "Space Station 2",
                        "Warp Zone",
                        "Final Level",
                    ), 1),
                    "CONSTRAINT": ((
                        "with no deaths",
                        "within the par time",
                        "collecting all trinkets",
                    ), 2),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Survive at least TIME seconds in the Super Gravitron",
                data={
                    "TIME": (range(1, 61), 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete INTERMISSION in under 2 minutes",
                data={
                    "INTERMISSION": ((
                        "Intermission 1",
                        "Intermission 2",
                    ), 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]

        if self.archipelago_options.vvvvvv_custom_levels:
            objectives.append(GameObjectiveTemplate(
                label="Play the custom level LEVEL",
                data={
                    "LEVEL": ((
                        "333333 (EASY MODE)",
                        "a new dimension",
                        "golden spiral",
                        "line wrap",
                        "pyramid of doom",
                        "quantum tunnel",
                        "roadtrip to the moon",
                        "seasons",
                        "soul searching",
                        "the dual challenge",
                        "the tower of power",
                        "variation venture",
                        "variety show",
                        "vertex vortex",
                        "vertiginous veridian",
                        "victuals",
                        "VVVV 4k",
                        ), 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=16,
            ))
        
        return objectives

class VVVVVVCustomLevels(Toggle):
    """Whether to include custom levels"""
    display_name = "VVVVVV Custom Levels"
    default = 0
