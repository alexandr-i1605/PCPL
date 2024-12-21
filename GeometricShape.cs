using System;

namespace Lab2
{
    internal abstract class GeometricShape
    {
        protected string m_Name;
        protected float m_Area;

        protected virtual void GetArea()
        {

        }

        protected void SetName(string name)
        {
            m_Name = name;
        }
    }
}
