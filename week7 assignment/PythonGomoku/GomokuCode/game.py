import os
import time

AI_USE_CPP = False

if not AI_USE_CPP:  
    from ai import AI1Step
else:
    import example


class Gomoku:

    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]  
        self.cur_step = 0  
        self.max_search_steps = 3  

    def move_1step(self, input_by_window=False, pos_x=None, pos_y=None):
        """
        Player's turn
        :param input_by_window: 
        :param pos_x: 
        :param pos_y: 
        """
        while True:
            try:
                if not input_by_window:
                    pos_x = int(input('x: '))  
                    pos_y = int(input('y: '))
                if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:  
                    if self.g_map[pos_x][pos_y] == 0:
                        self.g_map[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError:  
                continue

    def game_result(self, show=False):
        """Judge the ending of the game. 0 is in progress, 1 is the player wins, 2 is the computer wins, and 3 is a draw"""
        
        for x in range(11):
            for y in range(15):
                if self.g_map[x][y] == 1 and self.g_map[x + 1][y] == 1 and self.g_map[x + 2][y] == 1 and self.g_map[x + 3][y] == 1 and self.g_map[x + 4][y] == 1:
                    if show:
                        return 1, [(x0, y) for x0 in range(x, x + 5)]
                    else:
                        return 1
                if self.g_map[x][y] == 2 and self.g_map[x + 1][y] == 2 and self.g_map[x + 2][y] == 2 and self.g_map[x + 3][y] == 2 and self.g_map[x + 4][y] == 2:
                    if show:
                        return 2, [(x0, y) for x0 in range(x, x + 5)]
                    else:
                        return 2

       
        for x in range(15):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x][y + 1] == 1 and self.g_map[x][y + 2] == 1 and self.g_map[x][y + 3] == 1 and self.g_map[x][y + 4] == 1:
                    if show:
                        return 1, [(x, y0) for y0 in range(y, y + 5)]
                    else:
                        return 1
                if self.g_map[x][y] == 2 and self.g_map[x][y + 1] == 2 and self.g_map[x][y + 2] == 2 and self.g_map[x][y + 3] == 2 and self.g_map[x][y + 4] == 2:
                    if show:
                        return 2, [(x, y0) for y0 in range(y, y + 5)]
                    else:
                        return 2

        
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x + 1][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and self.g_map[x + 3][y + 3] == 1 and self.g_map[x + 4][y + 4] == 1:
                    if show:
                        return 1, [(x + t, y + t) for t in range(5)]
                    else:
                        return 1
                if self.g_map[x][y] == 2 and self.g_map[x + 1][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and self.g_map[x + 3][y + 3] == 2 and self.g_map[x + 4][y + 4] == 2:
                    if show:
                        return 2, [(x + t, y + t) for t in range(5)]
                    else:
                        return 2

        
        for x in range(11):
            for y in range(11):
                if self.g_map[x + 4][y] == 1 and self.g_map[x + 3][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and self.g_map[x + 1][y + 3] == 1 and self.g_map[x][y + 4] == 1:
                    if show:
                        return 1, [(x + t, y + 4 - t) for t in range(5)]
                    else:
                        return 1
                if self.g_map[x + 4][y] == 2 and self.g_map[x + 3][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and self.g_map[x + 1][y + 3] == 2 and self.g_map[x][y + 4] == 2:
                    if show:
                        return 2, [(x + t, y + 4 - t) for t in range(5)]
                    else:
                        return 2

        
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:  
                    if show:
                        return 0, [(-1, -1)]
                    else:
                        return 0

        if show:
            return 3, [(-1, -1)]
        else:
            return 3

    def ai_move_1step(self):
        """Computer's turn"""
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    self.g_map[x][y] = 2
                    self.cur_step += 1
                    return

    def ai_play_1step_by_cpp(self):
        # ai = AI1Step(self, self.cur_step, True)  
        st = time.time()
        mapstring = list()
        for x in range(15):
            mapstring.extend(self.g_map[x])
        try:
            node_len, ai_ope_x, ai_poe_y = example.ai_1step(self.cur_step, int(True), self.max_search_steps, mapstring)
            ai_ope = [ai_ope_x, ai_poe_y]
        except ValueError:
            raise ValueError('The value calculated by the AI program is incorrect')
        ed = time.time()
        print('%dnodes were generated，takes time%.4f' % (node_len, ed - st))
        self.g_map[ai_ope[0]][ai_ope[1]] = 2
        self.cur_step += 1

    def ai_play_1step_py_python(self):
        ai = AI1Step(self, self.cur_step, True)  
        st = time.time()
        ai.search(0, [set(), set()], self.max_search_steps)  
        ed = time.time()
        print('%dnodes were generated，takes time%.4f，evaluation time%.4f' % (len(ai.method_tree), ed - st, ai.t))
        if ai.next_node_dx_list[0] == -1:
            raise ValueError('ai.next_node_dx_list[0] == -1')
        ai_ope = ai.method_tree[ai.next_node_dx_list[0]].ope
        if self.g_map[ai_ope[0]][ai_ope[1]] != 0:
            raise ValueError('self.game_map[ai_ope[0]][ai_ope[1]] = %d' % self.g_map[ai_ope[0]][ai_ope[1]])
        self.g_map[ai_ope[0]][ai_ope[1]] = 2
        self.cur_step += 1

    def ai_play_1step(self):
        if AI_USE_CPP:
            self.max_search_steps = 3
            self.ai_play_1step_by_cpp()
        else:
            self.max_search_steps = 2
            self.ai_play_1step_py_python()

    def show(self, res):
        """Display Game Content"""
        for y in range(15):
            for x in range(15):
                if self.g_map[x][y] == 0:
                    print('  ', end='')
                elif self.g_map[x][y] == 1:
                    print('〇', end='')
                elif self.g_map[x][y] == 2:
                    print('×', end='')

                if x != 14:
                    print('-', end='')
            print('\n', end='')
            for x in range(15):
                print('|  ', end='')
            print('\n', end='')

        if res == 1:
            print('Player win!')
        elif res == 2:
            print('Computer win!')
        elif res == 3:
            print('A Draw!')

    def play(self):
        while True:
            self.move_1step()  
            res = self.game_result()  
            if res != 0:  
                self.show(res)
                return
            self.ai_move_1step()  
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.show(0)  

    def map2string(self):
        mapstring = list()
        for x in range(15):
            mapstring.extend(list(map(lambda x0: x0 + 48, self.g_map[x])))
        return bytearray(mapstring).decode('utf8')
