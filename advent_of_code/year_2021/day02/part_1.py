from collections import defaultdict

from advent_of_code.config import get_input
from advent_of_code.logging import log


#log.setLevel('DEBUG')

def process_all_moves(moves: list[list[str, str]]) -> tuple[int, int, int]:

    # we store moves as cumulative sums
    moves_cumsum = defaultdict(int)

    for action, value in moves:
        moves_cumsum[action] += int(value)

    log.debug(f"cumsum done for : {', '.join([f'{k}:{v}' for k,v in moves_cumsum.items()])}")
    
    moves_cumsum['depth'] = moves_cumsum['down'] - moves_cumsum['up']
    product = moves_cumsum['forward'] * moves_cumsum['depth']

    return moves_cumsum['forward'], moves_cumsum['depth'], product

def main() -> tuple[int, int, int]:
    with get_input(year=2021, day=2) as moves_raw:
        moves = list(move.split(' ') for move in moves_raw.strip().split('\n'))

        position, depth, product = process_all_moves(moves)

        log.info(f"Horizontal position = {position}\n"
        f"Final Depth = {depth}\n"
        f"Product = {product}")

        # we return what's been asked
        return position, depth, product

if __name__ == "__main__":
    main()