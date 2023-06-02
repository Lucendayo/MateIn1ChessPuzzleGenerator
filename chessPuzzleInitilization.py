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
# Assigning different Stockfish version depending on the operatingSystem variable
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