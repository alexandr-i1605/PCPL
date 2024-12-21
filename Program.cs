using System;

namespace lab1
{

    class Program
    {
        static void Main(string[] args)
        {
            double A = GetCoefficient("A", args.Length > 0 ? args[0] : null);
            double B = GetCoefficient("B", args.Length > 1 ? args[1] : null);
            double C = GetCoefficient("C", args.Length > 2 ? args[2] : null);
            CalculateAndDisplayRoots(A, B, C);
        }

        static double GetCoefficient(string CoefficientName, string Value)
        {
            double coefficient;
            if(!string.IsNullOrEmpty(Value) && double.TryParse(Value, out coefficient))
            {
                return coefficient;
            }
            while (true)
            {
                Console.Write($"Введите коэффициент {CoefficientName}: ");
                string input = Console.ReadLine();
                if (double.TryParse(input, out coefficient))
                {
                    return coefficient;
                }
                Console.WriteLine($"Некорректное значение.");
            }
        }

        static void CalculateAndDisplayRoots(double A, double B, double C)
        {
            double discriminant = B * B - 4 * A * C;

            if (A == 0)
            {
                DisplayMessage("Нет корней ( A < 0 ).", ConsoleColor.Red);
                return;
            }

            if (discriminant < 0)
            {
                DisplayMessage("Нет корней.", ConsoleColor.Red);
            }
            else
            {
                double y1 = (-B + Math.Sqrt(discriminant)) / (2 * A);
                double y2 = (-B - Math.Sqrt(discriminant)) / (2 * A);

                DisplayRoots(y1);
                DisplayRoots(y2);

            }
        }

        static void DisplayRoots(double y)
        {
            if (y < 0)
            {
                return;
            }
            double root1 = Math.Sqrt(y);
            double root2 = -Math.Sqrt(y);

            DisplayMessage($"Корни: x1 = {root1}, x2 = {root2}", ConsoleColor.Green);
        }

        static void DisplayMessage(string message, ConsoleColor color)
        {
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ResetColor();
        }

    }
}
