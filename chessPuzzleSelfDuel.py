from chessPuzzleInitilization import arguments, pondertime, maxmoves, gamecount, engine, dictsidetomove, notationdict, iterations
from chessPuzzleExtraction import extraction
import json
import chess
import chess.engine
import chess.svg

engine.options["Skill Level"] = 30

while True:
    white_moves = []
    black_moves = []
    winner = None  # Initialize the winner variable

    for i in range(iterations):
        # Create a new chess board for each iteration
        board = chess.Board()

        while not board.is_game_over():
            # Get the best move for the current position from the engine
            result = engine.play(board, chess.engine.Limit(time=0.01))
            # Print the move and apply it to the board
            print("Move:", result.move)

            # Append the move to the corresponding array based on the side to move
            if board.turn:  # White's turn
                white_moves.append(str(result.move))
            else:  # Black's turn
                black_moves.append(str(result.move))

            board.push(result.move)

            # Find end and its causes
            if board.is_checkmate():
                winner = dictsidetomove[board.turn]
                print("Checkmate! {} wins. Game over.".format(winner))

                # Determine which side won
                result = board.result()
                if result == "1-0":
                    winner = "White"
                elif result == "0-1":
                    winner = "Black"
                else:
                    winner = "Draw"
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

        if winner:
            break

    # Save white moves and black moves arrays to a JSON file
    data = {
        "White Moves": white_moves,
        "Black Moves": black_moves
    }

    with open("moves.json", "w") as file:
        json.dump(data, file)

    print("Moves saved to moves.json")

    extraction()

    if winner:
        break
