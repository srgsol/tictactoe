#! -*- coding: utf-8 -*-
"""
Minimax algorithm.

Joshua Eckroth is the author of the minimax algorithm implementation an all this
materials are licensed under Creative Commons Attribution-ShareAlike 3.0 Unported
License.
http://creativecommons.org/licenses/by-sa/3.0/

http://cse3521.artifice.cc/adversarial-search.html
"""
import copy


def minimax(state):
    max_trans = None
    max_u = None
    transitions = possible_transitions(state, 'x')
    # Find the transition (move) that provides the maximum
    # utility, assuming the opponent also makes a best move
    for trans, nextstate in transitions.items():
        # after making our move, find the best move the
        # opponent can make (best for opponent = worse for us;
        # if we consider the opponent winning as negative
        # utility, we want to find the minimum utility move
        # of the opponent's possible moves)
        u = min_utility(nextstate, 'o')
        if max_u is None or u > max_u:
            max_trans = trans
            max_u = u
    return max_trans


def min_utility(state, player):
    # if the current state is a win/loss/tie, stop searching
    if is_winning(state, player) or \
            is_winning(state, switch_player(player)) or \
            is_tie(state):
        return utility(state, 'x')
    else:
        transitions = possible_transitions(state, player)
        min_u = None
        for nextstate in transitions.values():
            # after making a move (current player is in the
            # "player" variable), find the minimum next
            # move and return its utility
            u = max_utility(nextstate, switch_player(player))
            if min_u is None or u < min_u:
                min_u = u
        return min_u


def max_utility(state, player):
    # if the current state is a win/loss/tie, stop searching
    if is_winning(state, player) or \
            is_winning(state, switch_player(player)) or \
            is_tie(state):
        return utility(state, 'x')
    else:
        transitions = possible_transitions(state, player)
        max_u = None
        for nextstate in transitions.values():
            # after making a move (current player is in the
            # "player" variable), find the maximum next
            # move and return its utility
            u = min_utility(nextstate, switch_player(player))
            if max_u is None or u > max_u:
                max_u = u
        return max_u


def possible_transitions(state, player):
    nextstates = {}
    trans = 0
    # Iterate all board positions. For each free position create a new board
    # and set player to this free position.
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                newstate = copy.deepcopy(state)
                newstate[i][j] = player
                nextstates[trans] = newstate
            trans += 1
    return nextstates


def switch_player(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'


def is_winning(state, player):
    winning = False
    for i in [0,1,2]:
        if state[i][0] == state[i][1] == state[i][2] == player:
            winning = True
    for j in [0,1,2]:
        if state[0][j] == state[1][j] == state[2][j] == player:
            winning = True
    if state[0][0] == state[1][1] == state[2][2] == player:
        winning = True
    if state[0][2] == state[1][1] == state[2][0] == player:
        winning = True
    return winning


def is_tie(state):
    blanks = 0
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if state[i][j] == ' ':
                blanks += 1
    return (
        blanks == 0
        and not is_winning(state, 'x')
        and not is_winning(state, 'o')
    )


def utility(state, player):
    if is_winning(state, player): return 1
    if is_winning(state, switch_player(player)): return -1
    return 0
