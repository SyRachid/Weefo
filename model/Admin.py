from Livreur import Livreur
class Admin(Livreur):
    def __init__(self,nom_utilisateur, mdp,num_fone,num_cnib,dispo):
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
        self.num_fone = num_fone
        self.num_cnib = num_cnib
        self.dispo = dispo
    def creer_Livreur(nom_utilisateur,mdp,num_fone,num_cnib,dispo)->Livreur:
        new_livreur = Livreur(nom_utilisateur,mdp,num_fone,num_cnib,dispo=0)
        return new_livreur