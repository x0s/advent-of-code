from advent_of_code.config import get_input
from advent_of_code.logging import log


def process_all_moves(moves: list[list[str, str]]) -> tuple[int, int, int, int]:
    """From a list a moves, will determine the final 
    position, depth, aim and product of the submarine"""
    aim = depth = position = 0

    for move in moves:
        action, value = move[0], int(move[1])

        if action == "down":
            aim += value
        elif action == "up":
            aim -= value
        elif action == "forward":
            position += value
            depth += aim*value

    return position, depth, aim, position*depth


def main() -> tuple[int, int, int]:
    with get_input(year=2021, day=2) as moves_raw:
        moves = list(move.split(' ') for move in moves_raw.strip().split('\n'))

        position, depth, aim, product = process_all_moves(moves)

        log.info(f"Horizontal position = {position}\n"
        f"Final Depth = {depth}\n"
        f"Final Aim = {aim}\n"
        f"Product = {product}")

        # we return what's been asked
        return position, depth, product

if __name__ == "__main__":
    main()
