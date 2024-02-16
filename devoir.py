def est_premier(nombre):
  if nombre < 2:
     return False
  for i in range(2, int(nombre ** 0.5) + 1):
    if nombre % i == 0:
      return False
  return True

def compter_mots(phrase):
    mots = phrase.strip().split()
    return len(mots)

class CompteBancaire:
  def __init__(self, solde_initial):
    self.solde = solde_initial

  def deposer(self, montant):
    self.solde += montant

  def retirer(self, montant):
    if self.solde < montant:
      raise ValueError("Solde insuffisant")
    self.solde -= montant

  def obtenir_solde(self):
    return self.solde
  
class SommeList:
  def somme_liste(liste):
    somme = 0
    for element in liste:
      somme += element
    return somme
  
class Rectangle:
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur

  def calculer_perimetre(self):

    return 2 * (self.longueur + self.largeur)
  
  def calculer_surface(self):
    return self.longueur * self.largeur

class Palindrome:
  def est_palindrome(chaine):
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse

class MoyenListe:
  def calculer_moyenne(liste):
    if not liste:
        return None
    return sum(liste) / len(liste)