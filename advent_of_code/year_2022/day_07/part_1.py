from itertools import combinations, chain
from typing import Iterator

import networkx as nx

from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    
    # A call is a command followed by results
    CallType = list[str]

    @staticmethod
    def infer_calls(input_raw: str) -> list[CallType]:
        """
              $ cd e       [['cd e'],
        from  $ ls    to    ['ls', '584 i', 'dir f'], 
              584 i         ['cd ..']]
              dir f
              $ cd ..
        """
        return [call_raw.strip().split('\n') for call_raw in input_raw.split('$ ')[1:]][1:]
    
    @staticmethod
    def infer_tree(calls: list[CallType]) -> nx.DiGraph:
        """Infer directed files tree view according to the calls"""
        G = nx.DiGraph()
        top_node = '/'

        for command, *results in calls:
            if command == "cd ..":
                # Move UP top_node
                top_node = list(G.predecessors(top_node))[0] # only one pred in Tree

            elif command.startswith("cd"):  
                # (top_node=//a) cd e ---> (top_node=//a/e)
                bottom_node = f"{top_node}/{command.split(' ')[1]}"

                G.add_edge(top_node, bottom_node)

                # Move DOWN top_node
                top_node = bottom_node

            elif command.startswith("ls"):
                # 'dir e', '29116 f', '2557 g', '62596 h.lst'
                for result in results:
                    size, bottom_node = result.split(' ')
                    bottom_node = f"{top_node}/{bottom_node}"
                    try:
                        G.add_edge(top_node, bottom_node, size=int(size))
                    except ValueError: # dir
                        G.add_edge(top_node, bottom_node)
        return G
    

    @staticmethod
    def is_dir(G: nx.Graph, node: str) -> bool:
        """Check if node is non-empty directory (neither a file nor a empty directory)"""
        return not(G.out_degree(node)==0 and G.in_degree(node)==1)

    @classmethod
    def get_dirs(cls, G: nx.Graph) -> Iterator[str]:
        return (node for node in G.nodes if cls.is_dir(G, node))

    @classmethod
    def get_dir_sizes(cls, G, below: int|float = float("inf")) -> Iterator[int]:
        size_computed = lambda node: 'size' in G.nodes[node]
        return (G.nodes[node]['size'] for node in cls.get_dirs(G) if size_computed(node) and G.nodes[node]['size'] <= below)
    
    def max_capped_sum(sizes: list[int], ceiling:int) -> int:
        """Look for the max sum possible under a capped value
           [600, 350, 100] with ceiling=800 yields 700
           This is not required by AoC, that's here only as a fun bonus :)
        """
        return max(sum(size) for size in chain(*(combinations(sizes, r=i+1) for i in range(len(sizes)))) if sum(size)<=ceiling)

    @classmethod
    def compute_size(cls, G, top_node) -> int:
        """Recursively compute the size of the directory(top_node)"""
        G.nodes[top_node]['size'] = (
                    sum(G.edges[top_node,adj]['size'] if 'size' in G.edges[top_node,adj] else cls.compute_size(G, adj)
                        for adj in G.adj[top_node])
        )
        return G.nodes[top_node]['size']
    

    @classmethod
    def process(cls, input_raw: str) -> int:
        # Extract the calls from input
        calls = cls.infer_calls(input_raw)

        # Infer the graph from the commands execution
        G = cls.infer_tree(calls)

        # Compute the size of the directories (update the graph)
        cls.compute_size(G, '/')

        # Return sum of directories whose size is below 100,000
        return sum(cls.get_dir_sizes(G, below=100_000))


def main() -> int:
    with get_input(year=2022, day=7) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"Total size of files whose size < 100,000 = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
