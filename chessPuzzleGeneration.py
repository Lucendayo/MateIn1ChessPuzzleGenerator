import chess
import chess.engine
import chess.svg
import os
import sys
import platform

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

arguments = sys.argv
pondertime = 3600
maxmoves = 100
gamecount = 1
path = os.getcwd()
os.chmod(path, 0o0111)
if operatingSystem == "Windows":
    engine = chess.engine.SimpleEngine.popen_uci(os.path.join(path, "Stockfish_Win"))
elif operatingSystem == "macOS":
    engine = chess.engine.SimpleEngine.popen_uci("/Applications/Stockfish.app")
elif operatingSystem == "Linux":
    engine = chess.engine.SimpleEngine.popen_uci(os.path.join())
dictsidetomove = {True:'white',False:'black'}
notationdict = {True:'.', False:'...'}
iterations = 1

for i in range(iterations):
    print("Iteration:", i+1)

    # Create a new chess board for each iteration
    board = chess.Board()

    while not board.is_game_over():
        # Get the best move for the current position from the engine
        result = engine.play(board, chess.engine.Limit
        (time=2.0))

        # Print the move and apply it to the board
        print("Move:", result.move)
        
        board.push(result.move)

        # Display the current chessboard
        print(board)

    print("Game over\n")

# Close the engine
engine.quit()
