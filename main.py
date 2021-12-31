from rock_paper_scissors import *
current_winCount = 0
current_lossCount = 0
current_tieCount = 0

recent_win, recent_loss, recent_tie = showdown()

#Send to GUI
current_winCount = current_winCount + recent_win
current_lossCount = current_lossCount + recent_loss
current_tieCount = current_tieCount + recent_tie
