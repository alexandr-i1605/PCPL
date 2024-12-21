using System;

namespace Lab2
{
    internal class Rectangle : GeometricShape, IPrint
    {
        protected float m_Width;
        protected float m_Height;

        public Rectangle(float length)
        {
            Width = length;
            Height = length;
            m_Name = "Прямоугольник";
            GetArea();
        }

        public Rectangle(float width, float height) 
        {
            Width = width;
            Height = height;
            m_Name = "Прямоугольник";
            GetArea();
        }
        public float Width
        {
            get => m_Width;
            set => m_Width = value;
        }

        public float Height
        {
            get => m_Height;
            set => m_Height = value;
        }

        protected override void GetArea()
        {
            m_Area = m_Width * m_Height;
        }

        public override string ToString()
        {
            return m_Name + ":\n Ширина: " + m_Width + "\n Высота: " + m_Height + "\n Площадь: " + m_Area;
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
