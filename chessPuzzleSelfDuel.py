from chessPuzzleInitilization import arguments, pondertime, maxmoves, gamecount, engine, dictsidetomove, notationdict, iterations
import json
import chess
import chess.engine
import chess.svg
engine.options["Skill Level"] = 30

def save_positions_before_checkmate():
    # Check if the game is still ongoing
    if not board.is_game_over():
        # Get the current FEN (Forsyth–Edwards Notation) representation of the board
        current_position = {
            "Position" : board.fen()
        }
        # Save the current position to a file
        with open("positions.json", "r") as file:
            json.write(current_position, file)

for i in range(iterations):

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





