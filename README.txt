1. Simulate four games between yourself and the minimax player on a 4x4 board, with the
depth parameter set to 5, 3, 2, and 1, respectively.
a. What were the results of each game?
    Human First:
        5: Agent victory
        4: Agent victory
        3: Agent victory
        2: Human victory
        1: Human victory
            after the first game, i tried a different first move, (0,2),
            once that move got me a win, I repeated it, I am going to run
            the program with the agent first now and see if that is one of the moves is likes to make
        Times(first move):
            5: 0.1
            4: 0.03
            3: 0.01
            2: 0.005
            1: 0.003
    Agent First:
        5: Agent victory, first move was 0,2
        4: Agent victory, first move was 0,2
        3: Human victory, first move was 0,2
        2: Tie game, first move was 0,2
        1: Human victory, first move was 0,2
        Times(first move):
            5: 0.12
            4: 0.06
            3: 0.04
            2: 0.004
            1: 0.0008


b. Did the minimax player’s moves change when the depth was limited to smaller
and smaller values?
    There was a change, but the first few moves were pretty consistent
c. What was the average time per move for each of the games? Comment on why
there is or is not a difference.
    Human First:
        5: 0.031
        4: 0.013
        3: 0.004
        2: 0.002
        1: 0.0006
    Agent First:
        5: 0.074
        4: 0.026
        3: 0.012
        2: 0.003
        1: 0.001
The search being limited reduces the number or cycles necessary before making a move, therefore, 
reducing time between moves as the depth is reduced. The agent-first times are also longer due to 
the agent calculating with 1 extra possible turn than the human-first games

2. Simulate two games between yourself and the minimax player on an 8x8 board, with the
depth parameter set to 5 and 2.
a. What were the results of each game?
    Human First:
        5: Agent victory
        2: I WON!!!!!
    Agent First:
        5: I WON!!!
        2: Joey won
b. Did the minimax player’s moves change when the depth changed?
    Yes, but only slightly

c. What was the average time per move for each of the games? Comment on why
there is or is not a difference.
    Human First:
        5: 7.663
        2: .02
    Agent First:
        5: 3.41, I'm not sure why this was faster, I did plug in my laptop during the game
        2: 0.026

There is a huge difference in computation time betwen 2 depth and 5 depth, 
this is due to the differenct in computation between these depths. The braching factore of
this game makes the number of comparisons huge. 


