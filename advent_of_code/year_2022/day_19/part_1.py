import re

from copy import copy
from dataclasses import dataclass, fields
from functools import cached_property, cache
from typing import Self

from advent_of_code.config import get_input
from advent_of_code.logging import log


@dataclass(slots=True)
class Ressource:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __iadd__(self, other):
        for ressource in fields(self):
            setattr(self, ressource.name,
                    getattr(self, ressource.name) + getattr(other, ressource.name))
        return self
    
    def __isub__(self, other):
        for ressource in fields(self):
            setattr(self, ressource.name,
                    getattr(self, ressource.name) - getattr(other, ressource.name))
        return self
    
    def __le__(self, other: Self) -> bool:
        return all(getattr(self, ressource.name) <= getattr(other, ressource.name) for ressource in fields(self))


@dataclass(slots=True)
class RobotCollection:
    ore: int = 1
    clay: int = 0
    obsidian: int = 0
    geode: int = 0
    
    def welcome(self, specialty) -> None:
        """Welcome the new robot in factory"""
        setattr(self, specialty, getattr(self, specialty) + 1)


class Blueprint:
    """Describe a robot cost strategy to make factory implement"""
    def __init__(self, id: int, ore_ore: int, clay_ore: int,
                 obsidian_ore: int, obsidian_clay: int,
                 geode_ore: int, geode_obsidian: int):
        self.id = id
        # robot costs
        self.robot_cost = {'ore'      : Ressource(ore=ore_ore),
                           'clay'     : Ressource(ore=clay_ore),
                           'obsidian' : Ressource(ore=obsidian_ore, clay=obsidian_clay),
                           'geode'    : Ressource(ore=geode_ore,    obsidian=geode_obsidian)}


class Factory:
    def __init__(self, blueprint: Blueprint):
        self.blueprint = blueprint
        self.robot_cost = blueprint.robot_cost

        # Max number of geodes that could be collected using this blueprint
        self.max_geodes = 0
        self.minutes = 0
        self.robots = RobotCollection()
        self.robot_specialties = [f.name for f in fields(self.robots)]
        self.ressources = Ressource()
    
    @property
    def quality_level(self):
        return self.blueprint.id * self.max_geodes

    @cached_property
    def max_ore_robots(self):
        """ Get upperbound for OreRobot production

        For pruning, since we can only make a robot per minute
        we don't want more Ore robots than necessary to pay the
        robot with highest price in Ore"""
        return max(self.robot_cost.values(), key=lambda cost: cost.ore).ore

    @cache
    def upper_bound_geode_robots(self, minutes: int) -> int:
        """Maximum number of additional Geode that could be collected in remaining time assuming:
        - a GeodeRobot is produced every minute
        - Factory has unlimited resources.
        This upperbound begets efficient pruning"""
        return ((minutes - 1) * minutes) // 2

    def explore(self, minutes: int):
        "DFS to determine max geodes that can be produced by current blueprint"
        self.minutes = minutes
        self.max_geodes = 0

        for robot_candidate in self.robot_specialties:
            self._explore(minutes, robot_candidate, RobotCollection(), Ressource())
        return self
    
    def _explore(self, minutes: int, robot_candidate: str, robots : RobotCollection, ressources: Ressource):
        # Prune all cases when it's unnecessary to build these robots
        match robot_candidate:
            case 'ore':
                if robots.ore >= self.max_ore_robots: return
            case 'clay':
                if robots.clay >= self.robot_cost['obsidian'].clay: return 
            case 'obsidian':
                if (not robots.clay or 
                    ressources.obsidian >= self.robot_cost['geode'].obsidian): return
            case 'geode':
                if not robots.obsidian: return

        # If we cannot expect to collect more geode than on another branch, we prune
        if (ressources.geode +
            robots.geode * minutes + 
            self.upper_bound_geode_robots(minutes)) <= self.max_geodes: return
        
        for time_remaining in range(minutes, 0, -1):
            # buy robot and browse farther in this branch
            if self.robot_cost[robot_candidate] <= ressources:
                # Spend & Make new robot
                ressources -= self.robot_cost[robot_candidate]  # Spend ressources to make a robot
                ressources += robots                       # Active robots round collection
                robots.welcome(robot_candidate)       

                for next_robot_candidate in self.robot_specialties:
                    # Explore all possible remaining rounds assuming that we added one ore robot
                    self._explore(time_remaining-1, next_robot_candidate, copy(robots), copy(ressources))
                return
            # If no robot was made, the active ones still collect
            ressources += robots
        # Update the max_geodes if this branch produced a higher amount
        self.max_geodes = max(self.max_geodes, ressources.geode)
    

class SolutionOne:

    @classmethod
    def process(cls, input_raw: str) -> int:
        duration = 24
        blueprints = [Blueprint(*map(int, re.findall("(\d+)", line))) for line in input_raw.splitlines()]

        return sum(Factory(blueprint).explore(duration).quality_level for blueprint in blueprints)


def main() -> int:
    with get_input(year=2022, day=19) as input_raw:

        total = SolutionOne.process(input_raw)

        log.info(f"What do you get if you add up the quality level of all of the blueprints in your list? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
