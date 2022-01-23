using System;

namespace TicTacToeLLD
{
    public class TicTacToe
    {
        static void Main(string[] args)
        {
            Game game = new Game(3,2);
            Player playerZero = game.AddPlayer(0);
            Player playerOne = game.AddPlayer(1);
            
            Console.WriteLine(playerZero.PlayerName + " with symbol: "+ playerZero.Symbol +" and " + playerOne.PlayerName + " with symbol: " + playerOne.Symbol + " has joined the game");

            Console.WriteLine("======================== GAME STARTS ========================");

            string input = Console.ReadLine();
            int playerTurn = 0;
            while (!String.IsNullOrEmpty(input) && input != "exit")
            {   
                string[] coordinates = input.Split();
                if (coordinates.Length == 2 && Int32.TryParse(coordinates[0], out int x) && Int32.TryParse(coordinates[1], out int y))
                {
                    bool moveSuccess = game.UpdateBoard(x - 1, y - 1, playerTurn % 2);
                    playerTurn += moveSuccess ? 1 : 0;
                }
                else
                {
                    Console.WriteLine("Wrong Input, Try Again.");
                }

                input = Console.ReadLine();
            }
            Console.Read();
        }
    }
}
