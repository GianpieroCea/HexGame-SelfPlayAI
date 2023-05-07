from hexgame.color import Color
from hexgame.board import Board
import copy

from hexgame.unionfind import UnionFind
from hexgame.board import Board


class NodeTree:
    data : tuple[int,int]
    children: list['NodeTree']
    @property
    def is_leaf(self)-> bool:
        return len(self.children)==0
    
    def __init__(self,data: tuple[int,int], children : list['NodeTree']) -> None:
        self.data = data
        self.children = children

    def __str__(self) -> str:
        return self.print_rec(0)
    

    def print_rec(self,i) -> str:
        res = i*"   " +str(self.data)+"\n" if self.data else ""
        if len(self.children) == 0:
            return res
        else:
            for child in self.children:
                    res += child.print_rec(i+1)
        return res

   


        





def expand_tree_rec(board: Board,
                    action: tuple[int, int], depth: int)-> NodeTree:
    if action:
        current_color = Color.Red if depth % 2 == 1 else Color.Blue
        board.place_stone(
            action[0], action[1], current_color
        )
        if board._has_color_won(current_color):
            # print(f"player {current_color} has won\n")
            return NodeTree(action,[])
    possible_actions = board.empty_positions
    children = []
    for a in possible_actions:
        next_board = copy.deepcopy(board)
        children.append(expand_tree_rec(
            next_board, a, depth+1))
    return NodeTree(action,children)


if __name__ == "__main__":
    dim_x = 2
    dim_y = 2
    nodes = [(x, y) for y in range(dim_y) for x in range(dim_x)]
    uf_red = UnionFind(nodes)
    uf_blue = UnionFind(nodes)
    board = Board(dim_x=dim_x, dim_y=dim_y,
                    red_conn_comp=uf_red, blue_conn_comp=uf_blue)
    tree = expand_tree_rec(board, None, 0)
    print(tree)
    