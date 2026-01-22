import numpy as np

class Vector:
    def __init__(self, components):
        self.vektor = np.array(components)
    
    def add(self, other):
        if len(self.vektor) != len(other.vektor):
            raise ValueError("Vectors must have the same length to add")
        return Vector(self.vektor + other.vektor)
    
    def subtract(self, other):
        if len(self.vektor) != len(other.vektor):
            raise ValueError("Vectors must have the same length to subtract")
        return Vector(self.vektor - other.vektor)
    
    def dot(self, other):
        if len(self.vektor) != len(other.vektor):
            raise ValueError("Vectors must have the same length for dot product")
        return np.dot(self.vektor, other.vektor)
    
    def norm(self):
        return np.linalg.norm(self.vektor)
    
    def equals(self, other):
        if not isinstance(other, Vector):
            return False
        return np.array_equal(self.vektor, other.vektor)
    
    def __str__(self):
        return f"({','.join(map(str, self.vektor.tolist()))})"
    
    def __repr__(self):
        return f"Vector({self.vektor.tolist()})"