import heapq
import re

from dataclasses import dataclass
from typing import Iterable

import networkx as nx

from advent_of_code.config import get_input
from advent_of_code.logging import log


@dataclass(frozen=True, order=True)
class State:
    valve: str
    time_remaining: int
    pressure: int
    closed_valves : frozenset

class Volcano:
    
    def __init__(self, input_raw: str):
        
        self.G = self.infer_graph(input_raw)
        self.neighbors = {n: list(nx.neighbors(self.G, n)) for n in self.G.nodes}
        self.distances = dict(nx.all_pairs_shortest_path_length(self.G))
        
    @staticmethod
    def infer_graph(input_raw):
        G = nx.Graph()
        for valve_from, flow, *valves_to in (re.findall("([A-Z]{2}|[\d]+)", line) for line in input_raw.splitlines()):
            G.add_node(valve_from, flow=int(flow), open=False)
            G.add_edges_from([(valve_from, valve_to) for valve_to in valves_to], weigth=1)
        return G
    
    def release_pressure(self, valve: str, state: State) -> int | None:
        if (valve in state.closed_valves) and (flow := self.G.nodes[valve]['flow']):
            # opening the valve cost 1 unit of time
            return (state.time_remaining - 1) * flow
    
    def estimate_pressure(self, state: State) -> int:
        """From a given state estimate the sum of the gain if we simulteanously open all closed valves

        It is of course not possible, but that's a good heuristic to estimate the potential gain from a state, 
        therefore helping priorizing the moves"""
        pressure_upper_bound = 0
        for valve_to in state.closed_valves:
            # How many moves + 1(opening the valve) is it needed to release pressure at valve_to ?
            distance = self.distances[state.valve][valve_to]
            pressure_upper_bound += max(0, (state.time_remaining - distance) * self.G.nodes[valve_to]['flow'])

        return pressure_upper_bound

    
    def state_candidates(self, state: State) -> Iterable[State]:
        """From a given state, yields possible other state to move to:
            - None if run <out of time>
            - new State with current Valve <opened>
            - new State <moving> to each neighbour
        """
        if state.time_remaining == 0: return None

        # First we try to release the current valve:
        if (new_pressure := self.release_pressure(state.valve, state)) is not None:
            yield State(state.valve,
                        state.time_remaining - 1,
                        state.pressure + new_pressure,
                        state.closed_valves - {state.valve})
            
        # Can we move to close-by unvisited valves?
        for valve_to in self.neighbors[state.valve]:
            yield State(valve_to,
                        max(0, state.time_remaining - self.distances[state.valve][valve_to]),
                        state.pressure,
                        state.closed_valves)
    
    def search(self) -> int:
        start = State(valve='AA', time_remaining=30, pressure=0, closed_valves=frozenset({*self.G.nodes}))
        return self.a_star_search(start) 
            
    
    def a_star_search(cls, start: State) -> State:
        """A star search algorithm applied on negative pressure so it aims at minimizing it"""
        # We use a heap with negative pressure as first key, retrieving the lowest first
        state_finish : State = None
        states_heap = []
        heapq.heappush(states_heap, (0, start))
        closed_states = {start: 0}
        
        while len(states_heap):
            pressure_negative, state_current = heapq.heappop(states_heap)
            
            # if we run out of time OR ther're no more valves to open
            if state_current.time_remaining == 0 or len(state_current.closed_valves) == 0:
                state_finish = state_current
                break

            for state_new in cls.state_candidates(state_current):
                if state_new not in closed_states or state_new.pressure > closed_states[state_new]:
                    # Record the pressure for this new state, so it does not browse it again
                    closed_states[state_new] = state_new.pressure
                    
                    # Compute the estimated pressure so we can prioritize browsing the states
                    pressure_estimate = state_new.pressure + cls.estimate_pressure(state_new)
                    
                    # Insert into heap new state
                    heapq.heappush(states_heap,(-pressure_estimate, state_new))
                    
        return state_finish.pressure


class SolutionOne:
    @classmethod
    def process(self, input_raw) -> int:
        return Volcano(input_raw).search()


def main() -> int:
    with get_input(year=2022, day=16) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"What is the most pressure you can release? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
