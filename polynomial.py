from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self,p1,p2,p3,a,b,coeffs='2'):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.a=a
        self.b=b
 # """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        pass

    def __add__(self,p1,p2,p3,a,b,):
       p3=p1+p2
       p1=a+b
       
       
    def set_poly(self):
        self.a = int(input('entrez les donnees de a'))
        self.b= int(input('Entrer les donnees de b'))
        
        print(p1*2)
    
        
if __name__ == '__main__':
    work = Poly2('p1','p2','p3','a','b',coeffs='2')
    work.set_poly()
    print(work)
    
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        pass

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        pass

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        pass

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        pass

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        pass

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        pass


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
