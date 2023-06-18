import json
import chess
import chess.engine
from chessPuzzleInitilization import engine

def extraction():
    # Import the moves from the JSON file
    with open("moves.json", "r") as file:
        data = json.load(file)

    # Extract the white moves and black moves
    white_moves = data["White Moves"]
    black_moves = data["Black Moves"]

    # Create a new chess board
    board = chess.Board()

    # Play the moves on the chess board
    for i in range(max(len(white_moves), len(black_moves))):
        if i < len(white_moves):
            white_move = white_moves[i]
            try:
                # White's move
                move = chess.Move.from_uci(white_move)
                if move in board.legal_moves:
                    board.push(move)
                    print("White move:", white_move)
                else:
                    print("Invalid white move:", white_move)
                    break

            except Exception as e:
                print("Error processing white move:", white_move, "Error:", str(e))
                break

        if i < len(black_moves):
            black_move = black_moves[i]
            try:
                # Black's move
                move = chess.Move.from_uci(black_move)
                if move in board.legal_moves:
                    board.push(move)
                    print("Black move:", black_move)
                else:
                    print("Invalid black move:", black_move)
                    break

            except Exception as e:
                print("Error processing black move:", black_move, "Error:", str(e))
                break
    last_move = board.peek()
    board.pop()
    # Print the board before the last move
    print("Board before the last move:")
    print(board)
    print("Find the best move as " + winner + ".")

    # Go back to the state before the last move was executed
   

   
    # Stay in a loop and accept input in UCI notation format
    while True:
        user_input = input("Enter your move in UCI notation (or 'q' to quit): ")

        if user_input.lower() == "q":
            print("You have quit the game.")
            print("The last move was:", last_move)
            exit()

        try:
            move = chess.Move.from_uci(user_input)

            if move == last_move:
                print("Correct move!")
                exit()
            else:
                print("Incorrect move. Try again.")
        except ValueError:
            print("Invalid move. Try again.")


def generation():
    white_moves = []
    black_moves = []
    last_move = None
    checkmate = False
    draw_positions = ["1/2-1/2", "1/2 - 1/2"]  # List of draw positions

    while not checkmate:
        # Create a new chess board
        board = chess.Board()

        while not board.is_game_over():
            # Get the best move for the current position from the engine
            result = engine.play(board, chess.engine.Limit(time=0.01))
            move = result.move

            # Append the move to the corresponding array based on the side to move
            if board.turn:  # White's turn
                white_moves.append(str(move))
            else:  # Black's turn
                black_moves.append(str(move))

            board.push(move)

            # Check if checkmate occurred
            if board.is_checkmate():
                last_move = move
                checkmate = True
                global winner
                winner = "White" if board.turn else "Black"
                print("mate")
                # Save white moves and black moves arrays to a JSON file
                data = {
                    "White Moves": white_moves,
                    "Black Moves": black_moves,
                    "Last Move": str(last_move)
                }

                with open("moves.json", "w") as file:
                    json.dump(data, file)

                print("Moves saved to moves.json")

                # Call the extraction function
                extraction()

            elif board.result(claim_draw=True) in draw_positions:
                print("draw")
                break
       

while True:
    generation()
