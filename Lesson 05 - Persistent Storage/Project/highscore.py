import shelve
import re
import glob
import os

scoreboard  = r'.\highscores.shlf'

def newScore(player, score, sb = scoreboard):
    sb = shelve.open(sb, writeback = True)
    #Filter player name to alpha numeric plus apostrophe, comma, space and period
    player = re.sub(r'[^A-Za-z0-9\'., ]', "", player.strip())
    player = re.sub(r'(\W)(?=\1)', '', player)
    #Filter score to numbers
    score = int(re.sub('[^\d-]', "", str(score)))
    if not player in sb.keys() or score > sb[player]:
        sb[player] = score
    ns = sb[player]
    sb.close()
    return ns
    
def remPlayer(player, sb = scoreboard):
    sb = shelve.open(sb, writeback = True)
    if player in sb.keys():
        del sb[player]
    sb.close()
        
def dumpSB(sb):
    shelfFiles = glob.glob(sb + '*')
    for fn in shelfFiles:
        os.remove(fn)

        
    