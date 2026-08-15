from __future__ import annotations
from dataclasses import dataclass
import functools
from Options import Toggle, OptionSet
from typing import List, Dict, Set
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class HyperRogueArchipelagoOptions:
    hyperrogue_include_thorns_mod: HyperRogueIncludeThornsMod
    hyperrogue_include_orb_shuffle_mod: HyperRogueIncludeOrbShuffleMod

class HyperRogueGame(Game):
    name = "HyperRogue"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = []
    is_adult_only_or_unrated = False
    options_cls = HyperRogueArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="in shoot'em up mode",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="with the crossbow weapon in LINESTYLE style",
                data={
                    "LINESTYLE": (['bull line', 'geodesic', 'geometric'], 1),
                },
            ),
        ]

        if self.archipelago_options.hyperrogue_include_thorns_mod:
            objectives.append(GameObjectiveTemplate(
                label="with the Thorns weapon",
                data=dict(),
            ))

        if self.archipelago_options.hyperrogue_include_orb_shuffle_mod:
            objectives.append(GameObjectiveTemplate(
                label="in the Orb Shuffle mode",
                data=dict(),
            ))

        return objectives

    land_structure = ['Chaos mode', 'patched Chaos', 'total chaos', 'random-walk chaos', 'excessive walls', 'wall-less', 'landscape', 'excessive crossing walls', 'regular walls', 'cursed walls']

    lands = [
        "Desert", 
        "Icy Land", 
        "Living Cave", 
        "Jungle", 
        "Alchemist Lab", 
        "Hall of Mirrors", 
        "Graveyard", 
        "R'Lyeh", 
        "Hell", 
        "Cocytus", 
        "Land of Eternal Motion", 
        "Dry Forest", 
        "Emerald Mine", 
        "Vineyard", 
        "Dead Cave", 
        "Hive", 
        "Land of Power", 
        "Temple of Cthulhu", 
        "Caribbean", 
        "Red Rock Valley", 
        "Minefield", 
        "Ocean", 
        "Whirlpool", 
        "Palace", 
        "Living Fjord", 
        "Ivory Tower", 
        "Zebra", 
        "Elemental Planes",
        "Land of Storms", 
        "Overgrown Woods", 
        "Clearing", 
        "Haunted Woods", 
        "Windy Plains", 
        "Rose Garden", 
        "Warped Coast", 
        "Yendorian Forest", 
        "Galápagos", 
        "Dragon Chasms", 
        "Kraken Depths", 
        "Burial Grounds", 
        "Trollheim", 
        "Dungeon", 
        "Lost Mountain", 
        "Reptiles", 
        "Prairie", 
        "Bull Dash", 
        "Volcanic Wasteland", 
        "Blizzard", 
        "Hunting Ground", 
        "Terracotta Army", 
        "Ruined City", 
        "Jelly Kingdom", 
        "Brown Island", 
        "Free Fall", 
        "Irradiated Field", 
        "Wetland", 
        "Frog Park", 
        "Eclectic City", 
        "Cursed Canyon", 
        "Dice Reserve", 
    ]

    small_geometry = ['{7,3} field quotient', '{8,3} field quotient', '{5,4} field quotient', '{6,4} field quotient', '{7,4} field quotient', '{12,3} field quotient', '{7,3} Zebra quotient', '{7,3} Klein Quartic', '{8,3} Bolza Surface', '{8,3} Bolza Surface x2', '{5,3} dodecahedron bitruncated', '{6,3} Klein bottle']

    hyperbolic_geometry = ['pure {7,3} heptagonal', 'chamfered {7,3} heptagonal', '2x bitruncated heptagonal', '{8,3} octagonal', 'pure {8,3} octagonal', '{5,4} (four pentagons)', '{6,4} (four hexagons)', '{7,4} (four heptagons}', 'variant of the binary tiling', 'standard binary tiling']

    euclidian_geometry = ['{6,3} hex grid', '{4,4} square grid', 'aperiodic hat', 'aperiodic spectre', 'kite-and-dart', 'Archimedean (3,3,3,3,3,3)', 'Archimedean (4,4,4,4)', 'Archimedean (6,6,6)', 'Archimedean (8,8,4)', 'Archimedean (4,6,12)', 'Archimedean (6,4,3,4)', 'Archimedean (3,6,3,6)', 'Archimedean (3,12,12)', 'Archimedean (4,4,3L,3L,3L) [3,4]', 'Archimedean (3,3,3,3,6) (1,2)(0,4)(3)', ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Collect at least 50 treasures in LAND",
                data={
                    "LAND": (self.lands, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Collect at least 25 treasures in LAND",
                data={
                    "LAND": (self.lands, 2),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Collect at least 25 treasures in LAND",
                data={
                    "LAND": (self.lands, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Collect at least 10 treasures in LAND",
                data={
                    "LAND": (self.lands, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Rescue a Prince or Princess",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the Princess Challenge",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the Yendor Quest",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Complete the Yendor Quest in GEOMETRY",
                data={
                    "GEOMETRY": (self.hyperbolic_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the Yendor Quest in GEOMETRY",
                data={
                    "GEOMETRY": (self.euclidian_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete N lands.",
                data={
                    "N": (range(11, 63+1), 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=15,
            ),
            GameObjectiveTemplate(
                label="Collect a Holy Grail",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 25 in Space Rocks in GEOMETRY (shoot em up mode, land structure: single land: Space Rocks)",
                data={
                    "GEOMETRY": (self.small_geometry, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete hyperbolic minesweeper in SMALLGEOMETRY",
                data={
                    "SMALLGEOMETRY": (self.small_geometry, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 150 $$$ in GEOMETRY",
                data={
                    "GEOMETRY": (self.hyperbolic_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 150 $$$ in GEOMETRY",
                data={
                    "GEOMETRY": (self.euclidian_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 150 $$$ in LANDSTRUCTURE",
                data={
                    "LANDSTRUCTURE": (self.land_structure, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in LANDSTRUCTURE",
                data={
                    "LAND": (self.lands, 1),
                    "LANDSTRUCTURE": (self.land_structure, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in GEOMETRY",
                data={
                    "LAND": (self.lands, 1),
                    "GEOMETRY": (self.small_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in GEOMETRY",
                data={
                    "LAND": (self.lands, 1),
                    "GEOMETRY": (self.hyperbolic_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in GEOMETRY",
                data={
                    "LAND": (self.lands, 1),
                    "GEOMETRY": (self.euclidian_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 25 in Halloween in SMALLGEOMETRY",
                data={
                    "SMALLGEOMETRY": (self.small_geometry, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the CHALLENGE Yendor Challenge",
                data={
                    "CHALLENGE": ([
                        "Hell+Dead Orb",
                        "Graveyard",
                        "Desert+Jungle",
                        "Minefield",
                        "Emerald Mine",
                        "Overgrown Woods",
                        "Land of Eternal Motion+Alchemist Lab",
                        "Alchemist Lab",
                        "Ivory Tower+Elemental Planes",
                        "Mirror Land+Overgrown Woods",
                        "Whirlpool",
                        "Icy Land+Elemental Planes",
                        "Hive+Red Rock Valley",
                        "Caribbean",
                        "Ocean",
                        "Palace",
                        "Zebra",
                        "Vineyard",
                        "Land of Storms",
                        "Living Fjord",
                        "Jungle",
                        "Land of Power",
                        "Wild West",
                        "Windy Plains+R'Lyeh",
                        "Chaos mode+Dead Orb",
                        "Dragon Chasms+Dead Orb",
                        "Reptiles",
                        "Galapagos+Dead Orb",
                        "Living Cave",
                        "Free Fall",
                        "Eclectic City",
                    ], 1)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in GEOMETRY",
                data={
                    "LAND": (self.lands, 1),
                    'GEOMETRY': (self.small_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in GEOMETRY",
                data={
                    "LAND": (self.lands, 1),
                    'GEOMETRY': (self.hyperbolic_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in LAND in GEOMETRY",
                data={
                    "LAND": (self.lands, 1),
                    'GEOMETRY': (self.small_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in Snake Nest in {8,3}",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 10 in Docks in {8,3}",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 200 (with multiplier) in LAND in the pure tactics mode",
                data={
                    "LAND": (self.lands + [
                        "Crossroads",
                        "Crossroads II",
                        "Crossroads III",
                        "Camelot",
                        "Crossroads IV",
                        "Crossroads V",
                        "Crossroads VI",
                        "Master Crossroads",
                        "Wild West",
                        "Crystal World",
                        "Docks in the {8,3} geometry",
                        "Snake Nest in the {8,3} geometry",
                    ], 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Score at least 50 in the random pattern mode",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 50 in the random pattern mode in GEOMETRY",
                data={
                    "GEOMETRY": (self.hyperbolic_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 50 in the random pattern mode in GEOMETRY",
                data={
                    "GEOMETRY": (self.euclidian_geometry, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score at least 50 in dual geometry mode",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]
        
        return objectives

class HyperRogueIncludeThornsMod(Toggle):
    """If enabled, adds variations for the Thorns weapon."""
    display_name = "HyperRogue Include Thorns Mod"
    default = 0

class HyperRogueIncludeOrbShuffleMod(Toggle):
    """If enabled, adds variations for the Orb Shuffle mode."""
    display_name = "HyperRogue Include Orb Shuffle Mod"
    default = 0
