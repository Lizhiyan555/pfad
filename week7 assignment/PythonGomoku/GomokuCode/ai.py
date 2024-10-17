import numpy as np
import copy
import time


class Node:
    """A node when the AI searches"""

    def __init__(self, game, ope, depth, alpha, beta, force_score, player_first):
        """
        Createa minimax node
        :param game: 
        :param ope: 
        :param depth: 
        :param alpha: 
        :param beta: 
        :param force_score: 
        :param player_first: 
        """
        self.game = game
        self.ope = ope
        self.depth = depth
        self.alpha = alpha
        self.beta = beta
        self.force_score = force_score
        self.player_first = player_first
        st = time.time()
        self.score = self.calc_score()
        ed = time.time()
        self.t = ed - st

    def calc_score(self):
        """The score for this node is calculated. 
        The more favorable it is to the AI, the higher the score, 
        and vice versa, the lower the score"""

        res = self.game.game_result()
        if res == 2:
            return 100
        elif res == 1:
            return -100

        ai_4_num = 0
        player_4_num = 0
        for x in range(11):
            for y in range(15):
                player_cnt = sum([self.game.g_map[x][y] == 1, self.game.g_map[x + 1][y] == 1, self.game.g_map[x + 2][y] == 1, self.game.g_map[x + 3][y] == 1, self.game.g_map[x + 4][y] == 1])
                ai_cnt = sum([self.game.g_map[x][y] == 2, self.game.g_map[x + 1][y] == 2, self.game.g_map[x + 2][y] == 2, self.game.g_map[x + 3][y] == 2, self.game.g_map[x + 4][y] == 2])
                if player_cnt == 4 and ai_cnt == 0:
                    player_4_num += 1
                if ai_cnt == 4 and player_cnt == 0:
                    ai_4_num += 1
        for x in range(15):
            for y in range(11):
                player_cnt = sum([self.game.g_map[x][y] == 1, self.game.g_map[x][y + 1] == 1, self.game.g_map[x][y + 2] == 1, self.game.g_map[x][y + 3] == 1, self.game.g_map[x][y + 4] == 1])
                ai_cnt = sum([self.game.g_map[x][y] == 2, self.game.g_map[x][y + 1] == 2, self.game.g_map[x][y + 2] == 2, self.game.g_map[x][y + 3] == 2, self.game.g_map[x][y + 4] == 2])
                if player_cnt == 4 and ai_cnt == 0:
                    player_4_num += 1
                if ai_cnt == 4 and player_cnt == 0:
                    ai_4_num += 1
        for x in range(11):
            for y in range(11):
                player_cnt = sum([self.game.g_map[x][y] == 1, self.game.g_map[x + 1][y + 1] == 1, self.game.g_map[x + 2][y + 2] == 1, self.game.g_map[x + 3][y + 3] == 1, self.game.g_map[x + 4][y + 4] == 1])
                ai_cnt = sum([self.game.g_map[x][y] == 2, self.game.g_map[x + 1][y + 1] == 2, self.game.g_map[x + 2][y + 2] == 2, self.game.g_map[x + 3][y + 3] == 2, self.game.g_map[x + 4][y + 4] == 2])
                if player_cnt == 4 and ai_cnt == 0:
                    player_4_num += 1
                if ai_cnt == 4 and player_cnt == 0:
                    ai_4_num += 1
        for x in range(11):
            for y in range(11):
                player_cnt = sum([self.game.g_map[x + 4][y] == 1, self.game.g_map[x + 3][y + 1] == 1, self.game.g_map[x + 2][y + 2] == 1, self.game.g_map[x + 1][y + 3] == 1, self.game.g_map[x][y + 4] == 1])
                ai_cnt = sum([self.game.g_map[x + 4][y] == 2, self.game.g_map[x + 3][y + 1] == 2, self.game.g_map[x + 2][y + 2] == 2, self.game.g_map[x + 1][y + 3] == 2, self.game.g_map[x][y + 4] == 2])
                if player_cnt == 4 and ai_cnt == 0:
                    player_4_num += 1
                if ai_cnt == 4 and player_cnt == 0:
                    ai_4_num += 1

        if self.player_first:
            if self.depth % 2 == 0:  
                if player_4_num >= 2:
                    return -90
                elif ai_4_num >= 2 and player_4_num == 0:
                    return 90
            else:  
                if ai_4_num >= 2:
                    return 90
                elif player_4_num >= 2 and ai_4_num == 0:
                    return -90
        else:
            if self.depth % 2 == 0:  
                if ai_4_num >= 2:
                    return 90
                elif player_4_num >= 2 and ai_4_num == 0:
                    return -90
            else:  
                if player_4_num >= 2:
                    return -90
                elif ai_4_num >= 2 and player_4_num == 0:
                    return 90

        if self.force_score is False:
            if self.player_first:
                if self.depth % 2 == 0:  
                    return np.inf
                else:  
                    return -np.inf
            else:
                if self.depth % 2 == 0:  
                    return -np.inf
                else:  
                    return np.inf

        player_3d_num = 0
        ai_3d_num = 0
        
        for x in range(11):
            for y in range(15):
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y] == 1 and self.game.g_map[x + 2][y] == 1 and self.game.g_map[x + 3][y] == 1 and self.game.g_map[x + 4][y] == 0:
                    player_3d_num += 1
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y] == 2 and self.game.g_map[x + 2][y] == 2 and self.game.g_map[x + 3][y] == 2 and self.game.g_map[x + 4][y] == 0:
                    ai_3d_num += 1
        for x in range(15):
            for y in range(11):
                if self.game.g_map[x][y] == 0 and self.game.g_map[x][y + 1] == 1 and self.game.g_map[x][y + 2] == 1 and self.game.g_map[x][y + 3] == 1 and self.game.g_map[x][y + 4] == 0:
                    player_3d_num += 1
                if self.game.g_map[x][y] == 0 and self.game.g_map[x][y + 1] == 2 and self.game.g_map[x][y + 2] == 2 and self.game.g_map[x][y + 3] == 2 and self.game.g_map[x][y + 4] == 0:
                    ai_3d_num += 1
        for x in range(11):
            for y in range(11):
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y + 1] == 1 and self.game.g_map[x + 2][y + 2] == 1 and self.game.g_map[x + 3][y + 3] == 1 and self.game.g_map[x + 4][y + 4] == 0:
                    player_3d_num += 1
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y + 1] == 2 and self.game.g_map[x + 2][y + 2] == 2 and self.game.g_map[x + 3][y + 3] == 2 and self.game.g_map[x + 4][y + 4] == 0:
                    ai_3d_num += 1
        for x in range(11):
            for y in range(11):
                if self.game.g_map[x + 4][y] == 0 and self.game.g_map[x + 3][y + 1] == 1 and self.game.g_map[x + 2][y + 2] == 1 and self.game.g_map[x + 1][y + 3] == 1 and self.game.g_map[x][y + 4] == 0:
                    player_3d_num += 1
                if self.game.g_map[x + 4][y] == 0 and self.game.g_map[x + 3][y + 1] == 2 and self.game.g_map[x + 2][y + 2] == 2 and self.game.g_map[x + 1][y + 3] == 2 and self.game.g_map[x][y + 4] == 0:
                    ai_3d_num += 1
        
        for x in range(10):
            for y in range(15):
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y] == 1 and ((self.game.g_map[x + 2][y] == 1) ^ (self.game.g_map[x + 3][y] == 1)) and self.game.g_map[x + 4][y] == 1 and self.game.g_map[x + 5][y] == 0:
                    player_3d_num += 1
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y] == 2 and ((self.game.g_map[x + 2][y] == 2) ^ (self.game.g_map[x + 3][y] == 2)) and self.game.g_map[x + 4][y] == 2 and self.game.g_map[x + 5][y] == 0:
                    ai_3d_num += 1
        for x in range(15):
            for y in range(10):
                if self.game.g_map[x][y] == 0 and self.game.g_map[x][y + 1] == 1 and ((self.game.g_map[x][y + 2] == 1) ^ (self.game.g_map[x][y + 3] == 1)) and self.game.g_map[x][y + 4] == 1 and self.game.g_map[x][y + 5] == 0:
                    player_3d_num += 1
                if self.game.g_map[x][y] == 0 and self.game.g_map[x][y + 1] == 2 and ((self.game.g_map[x][y + 2] == 2) ^ (self.game.g_map[x][y + 3] == 2)) and self.game.g_map[x][y + 4] == 2 and self.game.g_map[x][y + 5] == 0:
                    ai_3d_num += 1
        for x in range(10):
            for y in range(10):
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y + 1] == 1 and ((self.game.g_map[x + 2][y + 2] == 1) ^ (self.game.g_map[x + 3][y + 3] == 1)) and self.game.g_map[x + 4][y + 4] == 1 and self.game.g_map[x + 5][y + 5] == 0:
                    player_3d_num += 1
                if self.game.g_map[x][y] == 0 and self.game.g_map[x + 1][y + 1] == 2 and ((self.game.g_map[x + 2][y + 2] == 2) ^ (self.game.g_map[x + 3][y + 3] == 2)) and self.game.g_map[x + 4][y + 4] == 2 and self.game.g_map[x + 5][y + 5] == 0:
                    ai_3d_num += 1
        for x in range(10):
            for y in range(10):
                if self.game.g_map[x + 5][y] == 0 and self.game.g_map[x + 4][y + 1] == 1 and ((self.game.g_map[x + 3][y + 2] == 1) ^ (self.game.g_map[x + 2][y + 3] == 1)) and self.game.g_map[x + 1][y + 4] == 1 and self.game.g_map[x][y + 5] == 0:
                    player_3d_num += 1
                if self.game.g_map[x + 5][y] == 0 and self.game.g_map[x + 4][y + 1] == 2 and ((self.game.g_map[x + 3][y + 2] == 2) ^ (self.game.g_map[x + 2][y + 3] == 2)) and self.game.g_map[x + 1][y + 4] == 2 and self.game.g_map[x][y + 5] == 0:
                    ai_3d_num += 1

        
        if self.player_first:
            if self.depth % 2 == 0:  
                if player_4_num and player_3d_num >= 1:
                    return -80
                elif ai_4_num and ai_3d_num >= 1:
                    return 80
            else:  
                if ai_4_num and ai_3d_num >= 1:
                    return 80
                elif player_4_num and player_3d_num >= 1:
                    return -80
        else:
            if self.depth % 2 == 0:  
                if ai_4_num and ai_3d_num >= 1:
                    return 80
                elif player_4_num and player_3d_num >= 1:
                    return -80
            else:  
                if player_4_num and player_3d_num >= 1:
                    return -80
                elif ai_4_num and ai_3d_num >= 1:
                    return 80

        
        if self.player_first:
            if self.depth % 2 == 0:  
                if player_4_num:
                    return -70
                elif ai_4_num:
                    return 70
            else:  
                if ai_4_num:
                    return 70
                elif player_4_num:
                    return -70
        else:
            if self.depth % 2 == 0:  
                if ai_4_num:
                    return 70
                elif player_4_num:
                    return -70
            else:  
                if player_4_num:
                    return -70
                elif ai_4_num:
                    return 70

        if self.player_first:
            if self.depth % 2 == 0:  
                if player_3d_num >= 2:
                    return -60
                elif ai_3d_num >= 2:
                    return 60
            else:  
                if ai_3d_num >= 2:
                    return 60
                elif player_3d_num >= 2:
                    return -60
        else:
            if self.depth % 2 == 0:  
                if ai_3d_num >= 2:
                    return 60
                elif player_3d_num >= 2:
                    return -60
            else:  
                if player_3d_num >= 2:
                    return -60
                elif ai_3d_num >= 2:
                    return 60

        if self.player_first:
            if self.depth % 2 == 0:  
                if player_3d_num:
                    return -50
                elif ai_3d_num:
                    return 50
            else: 
                if ai_3d_num:
                    return 50
                elif player_3d_num:
                    return -50
        else:
            if self.depth % 2 == 0:  
                if ai_3d_num:
                    return 50
                elif player_3d_num:
                    return -50
            else:  
                if player_3d_num:
                    return -50
                elif ai_3d_num:
                    return 50

        score_by_num_around = [0, 1, 20, 30, 26, 24, 22, 20, 18, 16, 15]
        player_score_num = 0
        ai_score_num = 0
        player_cnt = 0
        ai_cnt = 0
        for x in range(15):
            for y in range(15):
                if self.game.g_map[x][y] == 1:
                    around_cnt = 0
                    for x0 in range(x - 1, x + 2):
                        for y0 in range(y - 1, y + 2):
                            if 0 <= x0 <= 14 and 0 <= y0 <= 14 and self.game.g_map[x0][y0] != 0:
                                around_cnt += 1
                    player_score_num += score_by_num_around[around_cnt] - abs(x - 7) - abs(y - 7)
                    player_cnt += 1
                if self.game.g_map[x][y] == 2:
                    around_cnt = 0
                    for x0 in range(x - 1, x + 2):
                        for y0 in range(y - 1, y + 2):
                            if 0 <= x0 <= 14 and 0 <= y0 <= 14 and self.game.g_map[x0][y0] != 0:
                                around_cnt += 1
                    ai_score_num += score_by_num_around[around_cnt] - abs(x - 7) - abs(y - 7)
                    ai_cnt += 1
        if ai_cnt == 0 or player_cnt == 0:
            return 0
        score = ai_score_num / ai_cnt - player_score_num / player_cnt
        return score


class AI1Step:

    max_node_num = 100000 

    def __init__(self, init_game, init_depth, player_first):
        """
        Decide where should the AI go
        :param init_game: 
        :param init_depth: 
        :param player_first: 
        """
        node_init = Node(copy.deepcopy(init_game), None, init_depth, -np.inf, np.inf, False, player_first)  
        node_init.score = -np.inf
        self.player_first = player_first
        self.method_tree = [node_init]  
        self.next_node_dx_list = [-1]  
        self.child_node_dx_list = [[]]  
        self.ope_hist_list = []  
        self.t = 0

    def search(self, cur_node_dx, ope_hist, max_depth):
        """
        The optimal results under a root node were searched according to the minimax 
        and alpha-beta pruning methods.
        :param cur_node_dx: 
        :param ope_hist: 
        :param max_depth: 
        """
        
        ope_list = set()
        for x in range(15):
            for y in range(15):
                if self.method_tree[cur_node_dx].game.g_map[x][y] != 0:
                    for x0 in range(x - 1, x + 2):
                        for y0 in range(y - 1, y + 2):
                            if 0 <= x0 <= 14 and 0 <= y0 <= 14 and (x0, y0) not in ope_list:
                                if self.method_tree[cur_node_dx].game.g_map[x0][y0] == 0:
                                    ope_list.add((x0, y0))
       
        for cell in ope_list:
            
            i_game = copy.deepcopy(self.method_tree[cur_node_dx].game)
            if self.player_first:
                if self.method_tree[cur_node_dx].depth % 2 == 0:  
                    i_game.g_map[cell[0]][cell[1]] = 1
                else:  
                    i_game.g_map[cell[0]][cell[1]] = 2
            else:
                if self.method_tree[cur_node_dx].depth % 2 == 0:  
                    i_game.g_map[cell[0]][cell[1]] = 1
                else:  
                    i_game.g_map[cell[0]][cell[1]] = 2
            if max_depth >= 2 and len(ope_list) >= 2: 
                node_new = Node(i_game, cell, self.method_tree[cur_node_dx].depth + 1, self.method_tree[cur_node_dx].alpha, self.method_tree[cur_node_dx].beta, False, self.player_first)
            else:
                node_new = Node(i_game, cell, self.method_tree[cur_node_dx].depth + 1, self.method_tree[cur_node_dx].alpha, self.method_tree[cur_node_dx].beta, True, self.player_first)
            self.t += node_new.t
            self.method_tree.append(node_new)  
            node_new_dx = len(self.method_tree) - 1
            self.child_node_dx_list.append([])
            self.child_node_dx_list[cur_node_dx].append(node_new_dx)  
            self.next_node_dx_list.append(-1)  
            
            if len(self.method_tree) >= self.max_node_num: 
                raise ValueError('Method Tree too big')

            
            if -np.inf < self.method_tree[node_new_dx].score < np.inf:
                
                if self.player_first:
                    if self.method_tree[cur_node_dx].depth % 2 == 0:  
                        if self.method_tree[node_new_dx].score < self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].beta = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                    else:  
                        if self.method_tree[node_new_dx].score > self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].alpha = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                else:
                    if self.method_tree[cur_node_dx].depth % 2 == 0:  
                        if self.method_tree[node_new_dx].score > self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].alpha = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                    else:  
                        if self.method_tree[node_new_dx].score < self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].beta = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
            else:
                
                if max_depth >= 2:
                    self.search(node_new_dx, ope_hist, max_depth - 1)
                
                if self.player_first:
                    if self.method_tree[cur_node_dx].depth % 2 == 0:  
                        if self.method_tree[node_new_dx].score < self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].beta = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                    else:  
                        if self.method_tree[node_new_dx].score > self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].alpha = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                else:
                    if self.method_tree[cur_node_dx].depth % 2 == 0:  
                        if self.method_tree[node_new_dx].score > self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].alpha = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                    else:  
                        if self.method_tree[node_new_dx].score < self.method_tree[cur_node_dx].score:
                            self.method_tree[cur_node_dx].score = self.method_tree[node_new_dx].score
                            self.method_tree[cur_node_dx].beta = self.method_tree[node_new_dx].score
                            self.next_node_dx_list[cur_node_dx] = node_new_dx
                if self.method_tree[cur_node_dx].alpha > self.method_tree[cur_node_dx].beta:  
                    return
