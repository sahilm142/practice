using System;

namespace TicTacToeLLD
{
    public class Game
    {
        private static int size;
        private static char[] symbols = new char[2] { 'X', 'O' };
        private static char[,] board;
        private static string[] players;

        public Game()
        {
            size = 3;
            players = new string[2];
            board = InitBoard();
        }
        public Game(int gameSize, int numberOfPlayers)
        {
            size = gameSize;
            players = new string[numberOfPlayers];
            board = InitBoard();
        }

        #region GameStart
        public Player AddPlayer(int id)
        {
            Player player = new Player();
            Console.WriteLine("Enter player " + id + " name:");
            player.PlayerName = Console.ReadLine();
            player.Symbol = symbols[id];
            players[id] = player.PlayerName;
            return player;
        }

        private static void PrintBoard(char[,] board)
        {
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    Console.Write(board[i, j]);
                }
                Console.WriteLine();
            }
        }

        public bool UpdateBoard(int x, int y, int playerId)
        {

            if (board[x, y] == '-')
            {
                board[x, y] = symbols[playerId];
                PrintBoard(board);
                if (CheckGameWon(playerId))
                {
                    Console.WriteLine("-----------------" + players[playerId] + " WON ----------------");
                }
                else if (CheckGameOver())
                {
                    Console.WriteLine("======================== Game Over ======================== ");
                }
                return true;
            }
            else
            {
                Console.WriteLine("Invalid Move, Try Again");
                return false;
            }
        }

        private static char[,] InitBoard()
        {
            char[,] board = new char[size, size];
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    board[i, j] = '-';
                }
            }
            PrintBoard(board);
            return board;
        }
        #endregion GameStart

        #region GameRules
        private static bool CheckDiagonal(char symbol)
        {
            bool isMatchedOne = true, isMatchedTwo = true;
            for (int i = 0; i < size; i++)
            {
                if (board[i, i] != symbol)
                {
                    isMatchedOne = false;
                }
            }
            for (int i = size - 1; i >= 0; i--)
            {
                if (board[i, size - i - 1] != symbol)
                {
                    isMatchedTwo = false;
                }
            }
            return isMatchedOne || isMatchedTwo;
        }
        private static bool CheckHorizontal(int i, char symbol)
        {
            for (int col = 0; col < size; col++)
            {
                if (board[i, col] != symbol)
                {
                    return false;
                }
            }
            return true;
        }

        private static bool CheckVertical(int j, char symbol)
        {
            for (int row = 0; row < size; row++)
            {
                if (board[row, j] != symbol)
                {
                    return false;
                }
            }
            return true;
        }
        private static bool CheckGameOver()
        {
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    if (board[i, j] == '-')
                    {
                        return false;
                    }
                }
            }
            return true;
        }
        private static bool CheckGameWon(int playerId)
        {
            char playerSymbol = symbols[playerId];
            for (int i = 0; i < size; i++)
            {
                if (CheckVertical(i, playerSymbol) || CheckHorizontal(i, playerSymbol))
                {
                    return true;
                }
            }
            return CheckDiagonal(playerSymbol);
        }
        #endregion GameRules
    }
}
