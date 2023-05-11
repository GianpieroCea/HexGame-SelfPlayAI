from hexgame.color import Color
from hexgame.board import Board
import copy


class NodeTree:
    def expand_tree_rec(board: Board,
                        action: tuple[int, int], depth: int):
        if action:
            current_color = Color.Red if depth % 2 == 1 else Color.Blue
            board.place_stone(
                action[0], action[1], current_color
            )
            if board._has_color_won(current_color):
                # print(f"player {current_color} has won\n")
                return {"data": action, "children": []}
        possible_actions = board.empty_positions
        children = []
        for a in possible_actions:
            next_board = copy.deepcopy(board)
            children.append(NodeTree.expand_tree_rec(
                next_board, a, depth+1))
        return {"data": action, "children": children}
