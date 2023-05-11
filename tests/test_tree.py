from hexgame_ai.tree_creator import NodeTree
from hexgame.unionfind import UnionFind
from hexgame.board import Board


class TestNodeTree:

    def test_expand_tree_rec(self):
        dim_x = 2
        dim_y = 2
        nodes = [(x, y) for y in range(dim_y) for x in range(dim_x)]
        uf_red = UnionFind(nodes)
        uf_blue = UnionFind(nodes)
        board = Board(dim_x=dim_x, dim_y=dim_y,
                      red_conn_comp=uf_red, blue_conn_comp=uf_blue)
        tree = NodeTree.expand_tree_rec(board, None, 0)
        assert len(tree["children"]) == 4
