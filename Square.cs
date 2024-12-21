using System;

namespace Lab2
{
    internal class Square : Rectangle, IPrint
    {
        public Square(float length) : base(length)
        {
            Width = length;
            Height = length;
            m_Name = "Квадрат";
            GetArea();
        }

        public override string ToString()
        {
            return m_Name + ":\n Сторона: " + m_Width + "\n Площадь: " + m_Area;
        }
    }
}
