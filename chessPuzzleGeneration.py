#import chess
#import chess.engine
#import os
#import sys

#arguments = sys.argv
#pondertime = 3600
#maxmoves = 100
#gamecount = 1
#here we assume the engine file is in same folder as our python script
#path = os.getcwd()
#os.chmod(path, 0o0111)
#engine = chess.engine.SimpleEngine.popen_uci('Stockfish')

#dictsidetomove = {True:'white',False:'black'}
#\notationdict = {True:'.', False:'...'}

#for i in range(gamecount):
    #board = chess.Board()
    #while not board.is_game_over() and board.fullmove_number<=maxmoves:
        #result = engine.play(board,chess.engine.Limit(time=pondertime))
        #print(dictsidetomove[board.turn]+' played '+str(board.fullmove_number)+notationdict[board.turn]+str(board.san(result.move)))
        #board.push(result.move)
    #print('Iteration '+str(i+1)+'-----')
    #print(board)
    
#engine.quit()
    