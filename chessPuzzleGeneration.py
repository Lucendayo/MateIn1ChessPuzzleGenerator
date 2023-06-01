import chess
import chess.engine
import chess.svg
import os
import sys
import platform
import json


def get_operating_system():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "macOS"
    else:
        print("Error. Operating System not identified/unsupported.")
        quit()

# Get the operating system and save to operatingSystem variable
operatingSystem = get_operating_system()

def save_positions_before_checkmate():
    # Check if the game is still ongoing
    if not board.is_game_over():
        # Get the current FEN (Forsyth–Edwards Notation) representation of the board
        current_position = board.fen()
        []
        # Save the current position to a file
        with open("positions.txt", "a") as file:
            file.write(current_position + "\n")


arguments = sys.argv
pondertime = 3600
maxmoves = 100
gamecount = 1
path = os.getcwd()
os.chmod(path, 0o0111)
# Assigning different Stockfish version depending on the OperatingSystem variable
if operatingSystem == "Windows":
    engine = chess.engine.SimpleEngine.popen_uci(os.path.join(path, "Stockfish"))
elif operatingSystem == "macOS":
    engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/Cellar/stockfish/15.1/bin/stockfish")
else:
    print("Error, operatingSystem variable null")
dictsidetomove = {True:'white',False:'black'}
notationdict = {True:'.', False:'...'}
iterations = 1

engine.options["Skill Level"] = 30
print("worked")
for i in range(iterations):
    print("Iteration:", i+1)

    # Create a new chess board for each iteration
    board = chess.Board()

    while not board.is_game_over():
        # Get the best move for the current position from the engine
        result = engine.play(board, chess.engine.Limit(time=0.01))
        # Print the move and apply it to the board
        print("Move:", result.move)
        
        board.push(result.move)

        save_positions_before_checkmate()

        # Find end and its causes
        if board.is_checkmate():
            winner = dictsidetomove[board.turn]
            print("Checkmate! {} wins. Game over.".format(winner))
            engine.quit()
            break
        elif board.is_stalemate():
            print("Stalemate! Game over.")
            engine.quit()
            break
        elif board.is_repetition():
            print("Repetition! Draw! Game over.")
            engine.quit()
            break
        elif board.is_insufficient_material():
            print("Insufficient material! Draw! Game over.")
            engine.quit()
            break





