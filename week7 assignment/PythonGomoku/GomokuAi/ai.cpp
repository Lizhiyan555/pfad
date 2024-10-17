#include <stdio.h>
#include <math.h>
#include "ai.h"


int Node::JudgeRes()
{
   
    for(int x = 0; x <= 10; x++){
        for (int y = 0; y <= 14; y++){
            if (GameMap[x][y] == 1 && GameMap[x + 1][y] == 1 && GameMap[x + 2][y] == 1 && GameMap[x + 3][y] == 1 && GameMap[x + 4][y] == 1)
                return 1;
            if (GameMap[x][y] == 2 && GameMap[x + 1][y] == 2 && GameMap[x + 2][y] == 2 && GameMap[x + 3][y] == 2 && GameMap[x + 4][y] == 2)
                return 2;
        }
    }
    
    for (int x = 0; x <= 14; x++){
        for (int y = 0; y <= 10; y++){
            if (GameMap[x][y] == 1 && GameMap[x][y + 1] == 1 && GameMap[x][y + 2] == 1 && GameMap[x][y + 3] == 1 && GameMap[x][y + 4] == 1)
                return 1;
            if (GameMap[x][y] == 2 && GameMap[x][y + 1] == 2 && GameMap[x][y + 2] == 2 && GameMap[x][y + 3] == 2 && GameMap[x][y + 4] == 2)
                return 2;
        }
    }
   
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 10; y++){
            if (GameMap[x][y] == 1 && GameMap[x + 1][y + 1] == 1 && GameMap[x + 2][y + 2] == 1 && GameMap[x + 3][y + 3] == 1 && GameMap[x + 4][y + 4] == 1)
                return 1;
            if (GameMap[x][y] == 2 && GameMap[x + 1][y + 1] == 2 && GameMap[x + 2][y + 2] == 2 && GameMap[x + 3][y + 3] == 2 && GameMap[x + 4][y + 4] == 2)
                return 2;
        }
    }
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 10; y++){
            if (GameMap[x + 4][y] == 1 && GameMap[x + 3][y + 1] == 1 && GameMap[x + 2][y + 2] == 1 && GameMap[x + 1][y + 3] == 1 && GameMap[x][y + 4] == 1)
                return 1;
            if (GameMap[x + 4][y] == 2 && GameMap[x + 3][y + 1] == 2 && GameMap[x + 2][y + 2] == 2 && GameMap[x + 1][y + 3] == 2 && GameMap[x][y + 4] == 2)
                return 1;
        }
    }
    return 0;
}

void Node::Judge4(uint32_t& ai_4_num, uint32_t& player_4_num){
    player_4_num = 0;
    ai_4_num = 0;
    int player_cnt, ai_cnt;
    
    for(int x = 0; x <= 10; x++){
        for (int y = 0; y <= 14; y++){
            player_cnt = (GameMap[x][y] == 1) + (GameMap[x + 1][y] == 1) + (GameMap[x + 2][y] == 1) + (GameMap[x + 3][y] == 1) + (GameMap[x + 4][y] == 1);
            ai_cnt = (GameMap[x][y] == 2) + (GameMap[x + 1][y] == 2) + (GameMap[x + 2][y] == 2) + (GameMap[x + 3][y] == 2) + (GameMap[x + 4][y] == 2);
            if ((player_cnt == 4) && (ai_cnt == 0))
                player_4_num += 1;
            if ((player_cnt == 0) && (ai_cnt == 4))
                ai_4_num += 1;
        }
    }
    
    for (int x = 0; x <= 14; x++){
        for (int y = 0; y <= 10; y++){
            player_cnt = (GameMap[x][y] == 1) + (GameMap[x][y + 1] == 1) + (GameMap[x][y + 2] == 1) + (GameMap[x][y + 3] == 1) + (GameMap[x][y + 4] == 1);
            ai_cnt = (GameMap[x][y] == 2) + (GameMap[x][y + 1] == 2) + (GameMap[x][y + 2] == 2) + (GameMap[x][y + 3] == 2) + (GameMap[x][y + 4] == 2);
            if ((player_cnt == 4) && (ai_cnt == 0))
                player_4_num += 1;
            if ((player_cnt == 0) && (ai_cnt == 4))
                ai_4_num += 1;
        }
    }
   
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 10; y++){
            player_cnt = (GameMap[x][y] == 1) + (GameMap[x + 1][y + 1] == 1) + (GameMap[x + 2][y + 2] == 1) + (GameMap[x + 3][y + 3] == 1) + (GameMap[x + 4][y + 4] == 1);
            ai_cnt = (GameMap[x][y] == 2) + (GameMap[x + 1][y + 1] == 2) + (GameMap[x + 2][y + 2] == 2) + (GameMap[x + 3][y + 3] == 2) + (GameMap[x + 4][y + 4] == 2);
            if ((player_cnt == 4) && (ai_cnt == 0))
                player_4_num += 1;
            if ((player_cnt == 0) && (ai_cnt == 4))
                ai_4_num += 1;
        }
    }
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 10; y++){
            player_cnt = (GameMap[x + 4][y] == 1) + (GameMap[x + 3][y + 1] == 1) + (GameMap[x + 2][y + 2] == 1) + (GameMap[x + 1][y + 3] == 1) + (GameMap[x][y + 4] == 1);
            ai_cnt = (GameMap[x + 4][y] == 2) + (GameMap[x + 3][y + 1] == 2) + (GameMap[x + 2][y + 2] == 2) + (GameMap[x + 1][y + 3] == 2) + (GameMap[x][y + 4] == 2);
            if ((player_cnt == 4) && (ai_cnt == 0))
                player_4_num += 1;
            if ((player_cnt == 0) && (ai_cnt == 4))
                ai_4_num += 1;
        }
    }
}

void Node::Judge3D(uint32_t& ai_3d_num, uint32_t& player_3d_num){
    player_3d_num = 0;
    ai_3d_num = 0;
    
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 14; y++){
            if (GameMap[x][y] == 0 && GameMap[x + 1][y] == 1 && GameMap[x + 2][y] == 1 && GameMap[x + 3][y] == 1 && GameMap[x + 4][y] == 0)
                player_3d_num += 1;
            if (GameMap[x][y] == 0 && GameMap[x + 1][y] == 2 && GameMap[x + 2][y] == 2 && GameMap[x + 3][y] == 2 && GameMap[x + 4][y] == 0)
                ai_3d_num += 1;
        }
    }
    
    for (int x = 0; x <= 14; x++){
        for (int y = 0; y <= 10; y++){
            if (GameMap[x][y] == 0 && GameMap[x][y + 1] == 1 && GameMap[x][y + 2] == 1 && GameMap[x][y + 3] == 1 && GameMap[x][y + 4] == 0)
                player_3d_num += 1;
            if (GameMap[x][y] == 0 && GameMap[x][y + 1] == 2 && GameMap[x][y + 2] == 2 && GameMap[x][y + 3] == 2 && GameMap[x][y + 4] == 0)
                ai_3d_num += 1;
        }
    }
    
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 10; y++){
            if (GameMap[x][y] == 0 && GameMap[x + 1][y + 1] == 1 && GameMap[x + 2][y + 2] == 1 && GameMap[x + 3][y + 3] == 1 && GameMap[x + 4][y + 4] == 0)
                player_3d_num += 1;
            if (GameMap[x][y] == 0 && GameMap[x + 1][y + 1] == 2 && GameMap[x + 2][y + 2] == 2 && GameMap[x + 3][y + 3] == 2 && GameMap[x + 4][y + 4] == 0)
                ai_3d_num += 1;
        }
    }
    for (int x = 0; x <= 10; x++){
        for (int y = 0; y <= 10; y++){
            if (GameMap[x + 4][y] == 0 && GameMap[x + 3][y + 1] == 1 && GameMap[x + 2][y + 2] == 1 && GameMap[x + 1][y + 3] == 1 && GameMap[x][y + 4] == 0)
                player_3d_num += 1;
            if (GameMap[x + 4][y] == 0 && GameMap[x + 3][y + 1] == 2 && GameMap[x + 2][y + 2] == 2 && GameMap[x + 1][y + 3] == 2 && GameMap[x][y + 4] == 0)
                ai_3d_num += 1;
        }
    }

   
    for (int x = 0; x <= 9; x++){
        for (int y = 0; y <= 14; y++){
            if (GameMap[x][y] == 0 && GameMap[x + 1][y] == 1 && ((GameMap[x + 2][y] == 1) ^ (GameMap[x + 3][y] == 1)) && GameMap[x + 4][y] == 1 && GameMap[x + 5][y] == 0)
                player_3d_num += 1;
            if (GameMap[x][y] == 0 && GameMap[x + 1][y] == 2 && ((GameMap[x + 2][y] == 2) ^ (GameMap[x + 3][y] == 2)) && GameMap[x + 4][y] == 2 && GameMap[x + 5][y] == 0)
                ai_3d_num += 1;
        }
    }
    
    for (int x = 0; x <= 14; x++){
        for (int y = 0; y <= 9; y++){
            if (GameMap[x][y] == 0 && GameMap[x][y + 1] == 1 && ((GameMap[x][y + 2] == 1) ^ (GameMap[x][y + 3] == 1)) && GameMap[x][y + 4] == 1 && GameMap[x][y + 5] == 0)
                player_3d_num += 1;
            if (GameMap[x][y] == 0 && GameMap[x][y + 1] == 2 && ((GameMap[x][y + 2] == 2) ^ (GameMap[x][y + 3] == 2)) && GameMap[x][y + 4] == 2 && GameMap[x][y + 5] == 0)
                ai_3d_num += 1;
        }
    }
   
    for (int x = 0; x <= 9; x++){
        for (int y = 0; y <= 9; y++){
            if (GameMap[x][y] == 0 && GameMap[x + 1][y + 1] == 1 && ((GameMap[x + 2][y + 2] == 1) ^ (GameMap[x + 3][y + 3] == 1)) && GameMap[x + 4][y + 4] == 1 && GameMap[x + 5][y + 5] == 0)
                player_3d_num += 1;
            if (GameMap[x][y] == 0 && GameMap[x + 1][y + 1] == 2 && ((GameMap[x + 2][y + 2] == 2) ^ (GameMap[x + 3][y + 3] == 2)) && GameMap[x + 4][y + 4] == 2 && GameMap[x + 5][y + 5] == 0)
                ai_3d_num += 1;
        }
    }
    for (int x = 0; x <= 9; x++){
        for (int y = 0; y <= 9; y++){
            if (GameMap[x + 5][y] == 0 && GameMap[x + 4][y + 1] == 1 && ((GameMap[x + 3][y + 2] == 1) ^ (GameMap[x + 2][y + 3] == 1)) && GameMap[x + 1][y + 4] == 1 && GameMap[x][y + 5] == 0)
                player_3d_num += 1;
            if (GameMap[x + 5][y] == 0 && GameMap[x + 4][y + 1] == 2 && ((GameMap[x + 3][y + 2] == 2) ^ (GameMap[x + 2][y + 3] == 2)) && GameMap[x + 1][y + 4] == 2 && GameMap[x][y + 5] == 0)
                ai_3d_num += 1;
        }
    }
}

int Node::CalcScore(){
    
    const int res = JudgeRes();
    if (res == 2)
        return 100;
    else if (res == 1)
        return -100;

    
    uint32_t ai_4_num;
    uint32_t player_4_num;
    Judge4(ai_4_num, player_4_num);

    
    if (PlayerFirst){
        if (Depth % 2 == 0){ 
            if (player_4_num >= 2)
                return -90;
            else if (ai_4_num >= 2 && player_4_num == 0)
                return 90;
        }else{
            if (ai_4_num >= 2)
                return 90;
            else if (player_4_num >= 2 && ai_4_num == 0)
                return -90;
        }
    }else{
        if (Depth % 2 == 0){ 
            if (ai_4_num >= 2)
                return 90;
            else if (player_4_num >= 2 && ai_4_num == 0)
                return -90;
        }else{
            if (player_4_num >= 2)
                return -90;
            else if (ai_4_num >= 2 && player_4_num == 0)
                return 90;
        }
    }

    
    if (ForceScore == false){
        if (PlayerFirst){
            if (Depth % 2 == 0) 
                return INF;
            else 
                return -INF;
        }else{
            if (Depth % 2 == 0) 
                return -INF;
            else 
                return INF;
        }
    }

    
    uint32_t ai_3d_num;
    uint32_t player_3d_num;
    Judge3D(ai_3d_num, player_3d_num);

    
    if (PlayerFirst){
        if (Depth % 2 == 0){ 
            if (player_4_num && player_3d_num)
                return -80;
            if (ai_4_num && ai_3d_num)
                return 80;
        }else{  
            if (ai_4_num && ai_3d_num)
                return 80;
            if (player_4_num && player_3d_num)
                return -80;
        }
    }else{
        if (Depth % 2 == 0){ 
            if (ai_4_num && ai_3d_num)
                return 80;
            if (player_4_num && player_3d_num)
                return -80;
        }else{ 
            if (ai_4_num && ai_3d_num)
                return 80;
            if (player_4_num && player_3d_num)
                return -80;
        }
    }

    
    if (PlayerFirst){
        if (Depth % 2 == 0){ 
            if (player_4_num)
                return -70;
            if (ai_4_num)
                return 70;
        }else{  
            if (ai_4_num)
                return 70;
            if (player_4_num)
                return -70;
        }
    }else{
        if (Depth % 2 == 0){ 
            if (ai_4_num)
                return 70;
            if (player_4_num)
                return -70;
        }else{ 
            if (ai_4_num)
                return 70;
            if (player_4_num)
                return -70;
        }
    }

    
    if (PlayerFirst){
        if (Depth % 2 == 0){ 
            if (player_3d_num >= 2)
                return -60;
            if (ai_3d_num >= 2)
                return 60;
        }else{  
            if (ai_3d_num >= 2)
                return 60;
            if (player_3d_num >= 2)
                return -60;
        }
    }else{
        if (Depth % 2 == 0){ 
            if (ai_3d_num >= 2)
                return 60;
            if (player_3d_num >= 2)
                return -60;
        }else{ 
            if (ai_3d_num >= 2)
                return 60;
            if (player_3d_num >= 2)
                return -60;
        }
    }

   
    if (PlayerFirst){
        if (Depth % 2 == 0){ 
            if (player_3d_num)
                return -50;
            if (ai_3d_num)
                return 50;
        }else{  
            if (ai_3d_num)
                return 50;
            if (player_3d_num)
                return -50;
        }
    }else{
        if (Depth % 2 == 0){ 
            if (ai_3d_num)
                return 50;
            if (player_3d_num)
                return -50;
        }else{ 
            if (ai_3d_num)
                return 50;
            if (player_3d_num)
                return -50;
        }
    }
    
    int player_score_num = 0; 
    int ai_score_num = 0;
    int player_piece_cnt = 0; 
    int ai_piece_cnt = 0;
    for (int x = 0; x <= 14; x++){
        for (int y = 0; y <= 14; y++){
            if (GameMap[x][y] == 1){
                int around_cnt = 0;
                for (int x0 = x - 1; x0 <= x + 1; x0++){
                    for (int y0 = y - 1; y0 <= y + 1; y0++){
                        if (x0 >= 0 && x0 <= 14 && y0 >= 0 && y0 <= 14 && GameMap[x0][y0] != 0)
                            around_cnt += 1;
                    }
                }
                player_score_num += ScoreByNumArount[around_cnt] - abs(x - 7) - abs(y - 7);
                player_piece_cnt += 1;
            }
            if (GameMap[x][y] == 2){
                int around_cnt = 0;
                for (int x0 = x - 1; x0 <= x + 1; x0++){
                    for (int y0 = y - 1; y0 <= y + 1; y0++){
                        if (x0 >= 0 && x0 <= 14 && y0 >= 0 && y0 <= 14 && GameMap[x0][y0] != 0)
                            around_cnt += 1;
                    }
                }
                ai_score_num += ScoreByNumArount[around_cnt] - abs(x - 7) - abs(y - 7);
                ai_piece_cnt += 1;
            }
        }
    }
    if (ai_piece_cnt == 0 || player_piece_cnt == 0)
        return 0;
    return ai_score_num / ai_piece_cnt - player_score_num / player_piece_cnt;
}



set<Point> Node::GetOpeList()
{
    
    set<Point> ope_list = set<Point>();
    for (int x = 0; x <= 14; x++){
        for (int y = 0; y <= 14; y++){
            if (GameMap[x][y] != 0){
                for (int x0 = x - 1; x0 <= x + 1; x0++){
                    for (int y0 = y - 1; y0 <= y + 1; y0++){
                        Point temp_point(x0, y0);
                        if (x0 >= 0 && x0 <= 14 && y0 >= 0 && y0 <= 14 && ope_list.find(temp_point) == ope_list.end() && GameMap[x0][y0] == 0)
                            ope_list.insert(temp_point);
                    }
                }
            }
        }
    }
    return ope_list;
}

void AI1Step::Search(const uint32_t cur_node_dx, const uint32_t max_depth){
    
    set<Point> ope_list = MethodTree[cur_node_dx].GetOpeList();
    
    for (set<Point>::iterator cell_it = ope_list.begin(); cell_it != ope_list.end(); cell_it++)
    {
        
        int i_map[15][15];
        memcpy(i_map, MethodTree[cur_node_dx].GameMap, sizeof(int) * 15 * 15);
        if (PlayerFirst){
            if (MethodTree[cur_node_dx].Depth % 2 == 0) 
                i_map[cell_it->X][cell_it->Y] = 1;
            else 
                i_map[cell_it->X][cell_it->Y] = 2;
        }else{
            
            if (MethodTree[cur_node_dx].Depth % 2 == 0) 
                i_map[cell_it->X][cell_it->Y] = 2;
            else 
                i_map[cell_it->X][cell_it->Y] = 1;
        }

        if (max_depth >= 2 && ope_list.size() >= 2) 
        {
            Node node_new(i_map, *cell_it, MethodTree[cur_node_dx].Depth + 1, MethodTree[cur_node_dx].Alpha, MethodTree[cur_node_dx].Beta, false, PlayerFirst);
            node_new.Score = node_new.CalcScore();
            MethodTree.push_back(node_new);
        }else{
            Node node_new(i_map, *cell_it, MethodTree[cur_node_dx].Depth + 1, MethodTree[cur_node_dx].Alpha, MethodTree[cur_node_dx].Beta, true, PlayerFirst);
            node_new.Score = node_new.CalcScore();
            MethodTree.push_back(node_new);
        }
        unsigned long node_new_dx;
        node_new_dx = MethodTree.size() - 1;
        NextNodeList.push_back(-1); 
        if (MethodTree.size() >= MaxNodeNum)
        {
            printf("Method Tree is too big.\n");
            abort();
        }

       
        if (MethodTree[node_new_dx].Score > -INF && MethodTree[node_new_dx].Score < INF){
            
            if (PlayerFirst){
                if (MethodTree[cur_node_dx].Depth % 2 == 0){ 
                    if (MethodTree[node_new_dx].Score < MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Beta = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }else{ 
                    if (MethodTree[node_new_dx].Score > MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Alpha = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }
            }else{
                if (MethodTree[cur_node_dx].Depth % 2 == 0){ 
                    if (MethodTree[node_new_dx].Score > MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Alpha = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }else{  
                    if (MethodTree[cur_node_dx].Depth % 2 == 0){ 
                        if (MethodTree[node_new_dx].Score < MethodTree[cur_node_dx].Score){
                            MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                            MethodTree[cur_node_dx].Beta = MethodTree[node_new_dx].Score;
                            NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                        }
                    }
                }
            }
        }else{
            
            if (max_depth >= 2)
                Search(static_cast<uint32_t>(node_new_dx), max_depth - 1);
           
            if (PlayerFirst){
                if (MethodTree[cur_node_dx].Depth % 2 == 0){ 
                    if (MethodTree[node_new_dx].Score < MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Beta = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }else{ 
                    if (MethodTree[node_new_dx].Score > MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Alpha = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }
            }else{
                if (MethodTree[cur_node_dx].Depth % 2 == 0){ 
                    if (MethodTree[node_new_dx].Score > MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Alpha = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }else{ 
                    if (MethodTree[node_new_dx].Score < MethodTree[cur_node_dx].Score){
                        MethodTree[cur_node_dx].Score = MethodTree[node_new_dx].Score;
                        MethodTree[cur_node_dx].Beta = MethodTree[node_new_dx].Score;
                        NextNodeList[cur_node_dx] = static_cast<int>(node_new_dx);
                    }
                }
            }
            
            if (MethodTree[cur_node_dx].Alpha > MethodTree[cur_node_dx].Beta)
                return;
            if (MethodTree.size() >= MaxNodeNum / 2)
                return;
        }
    }
}

Point AI1Step::GetFinalRes(){
    if (NextNodeList[0] == -1){
        printf("NextNodeList[0] = -1.\n");

    }
    return MethodTree[NextNodeList[0]].Ope;
}
