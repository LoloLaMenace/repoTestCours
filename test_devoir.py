import unittest
from devoir import *

#Question 1 Test premier ...
class TestEstPremier(unittest.TestCase):
    # Tests pour la fonction est_premier
    def test_nombre_premier(self):
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertTrue(est_premier(5))
    #non premier
    def test_nombre_non_premier(self):
        self.assertFalse(est_premier(4))
        self.assertFalse(est_premier(6))
        self.assertFalse(est_premier(9))
    #inferieur a 2
    def test_nombre_inferieur_a_deux(self):
        self.assertFalse(est_premier(0))
        self.assertFalse(est_premier(1))
        
#Question 2 :compter mots
class TestCompterMots(unittest.TestCase):
    # phrase non vide
    def test_phrase_non_vide(self):
        self.assertEqual(compter_mots("Ceci est une phrase"), 4)
    
    #phrase vide
    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)
    
    # espaces supplémentaires
    def test_espaces_supplementaires(self):
        self.assertEqual(compter_mots("   Ceci   est   une   phrase   "), 4)

#Question3 :Test Compte bancaire
class TestCompteBancaire(unittest.TestCase):
        # Créer un compte bancaire avec un solde initial de 100
    def setUp(self):
        self.compte = CompteBancaire(100)
    
        # Test du dépôt d'un montant de 50
    def test_deposer(self):
        self.compte.deposer(50)
        self.assertEqual(self.compte.obtenir_solde(), 150)
    
        # Test du retrait d'un montant de 30
    def test_retirer(self):
        self.compte.retirer(30)
        self.assertEqual(self.compte.obtenir_solde(), 70)
    
        # Test du retrait d'un montant supérieur au solde
    def test_retirer_solde_insuffisant(self):
        with self.assertRaises(ValueError):
            self.compte.retirer(200)
    
        # Vérification du solde initial
    def test_obtenir_solde(self):
        self.assertEqual(self.compte.obtenir_solde(), 100)

#Question4: SOmme list
class TestSommeList(unittest.TestCase):
        #  non vide
    def test_liste_non_vide(self):
        self.assertEqual(SommeList.somme_liste([1, 2, 3, 4]), 10)
    
        # liste vide
    def test_liste_vide(self):
        self.assertEqual(SommeList.somme_liste([]), 0)
    
        # liste avec des éléments négatifs
    def test_liste_negatifs(self):
        self.assertEqual(SommeList.somme_liste([-1, -2, -3, -4]), -10)
    
        # liste avec des éléments positifs et négatifs
    def test_liste_melange(self):
        self.assertEqual(SommeList.somme_liste([1, -2, 3, -4]), -2)

#Question5:  Test Rectangle
class TestRectangle(unittest.TestCase):
        # Créer Rectangle pour les tests
    def setUp(self):
        self.rectangle = Rectangle(5, 4)
    
        # calculer_perimetre()
    def test_calculer_perimetre(self):
        self.assertEqual(self.rectangle.calculer_perimetre(), 18)
    
        # calculer_surface()
    def test_calculer_surface(self):
        self.assertEqual(self.rectangle.calculer_surface(), 20)

#Question 6 : Savoir si c'est un palindrome
class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(Palindrome.est_palindrome("radar"))
        self.assertTrue(Palindrome.est_palindrome("laval"))
    
    def test_non_palindrome(self):
        self.assertFalse(Palindrome.est_palindrome("hello"))
        self.assertFalse(Palindrome.est_palindrome("world"))
    
    def test_palindrome_avec_espaces(self):
        self.assertTrue(Palindrome.est_palindrome("amanaplanacanalpanama".replace(" ", "")))
    
    def test_palindrome_sensitive_a_la_casse(self):
        self.assertTrue(Palindrome.est_palindrome("Racecar".lower()))

#Question 7 : Calculer moyenne      
class TestCalculerMoyenne(unittest.TestCase):
    #list pas vie
    def test_liste_non_vide(self):
        self.assertAlmostEqual(MoyenListe.calculer_moyenne([1, 2, 3, 4, 5]), 3.0)
    #list vide
    def test_liste_vide(self):
        self.assertIsNone(MoyenListe.calculer_moyenne([]))
        
if __name__ == '__main__':
    unittest.main()