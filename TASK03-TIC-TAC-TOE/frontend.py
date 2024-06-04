import tkinter as tk
from tkinter import messagebox
from src.board import print_board, check_winner, is_board_full
from src.minimax import find_best_move

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'
        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg='lightgray', padx=10, pady=10)
        frame.grid(row=0, column=0)

        for i in range(3):
            for j in range(3):
                button = tk.Button(frame, text=' ', font=('Helvetica', 32), width=5, height=2,
                                   bg='white', fg='black', command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        self.status_label = tk.Label(self.root, text="Player O's turn", font=('Helvetica', 20), bg='lightgray')
        self.status_label.grid(row=1, column=0, pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset", font=('Helvetica', 20), command=self.reset_board)
        self.reset_button.grid(row=2, column=0, pady=10)

    def on_button_click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player, fg='blue' if self.current_player == 'O' else 'red')
            if self.check_game_over():
                return
            self.switch_player()
            self.update_status()
            if self.current_player == 'X':
                self.root.after(500, self.ai_move)

    def switch_player(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def ai_move(self):
        move = find_best_move(self.board)
        if move:
            self.board[move[0]][move[1]] = 'X'
            self.buttons[move[0]][move[1]].config(text='X', fg='red')
            if self.check_game_over():
                return
            self.switch_player()
            self.update_status()

    def update_status(self):
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_game_over(self):
        winner = check_winner(self.board)
        if winner:
            self.highlight_winner(winner)
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
            return True
        elif is_board_full(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        return False

    def highlight_winner(self, winner):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == winner:
                    self.buttons[i][j].config(bg='yellow')

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', bg='white', state=tk.NORMAL)
        self.current_player = 'O'
        self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

