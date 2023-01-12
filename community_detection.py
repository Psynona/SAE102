##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def ami(dico : dict, i : int, liste : list):
    """
    Prend en paramètre un dictionnaire où mettre les valeurs, l'indice du premier ami 
    et une liste de couple d'ami.
    Met le premier ami en valeur du deuxième et inversement.
    """
    dico[liste[i]].append(liste[i+1])
    dico[liste[i+1]].append(liste[i])

def create_network(list_of_friends : list) -> dict:
    """
    Retourne un dictionnaire qui représente le réseau d'une liste d'amis prise en paramètre 
    """
    dico = {}
    i = 0
    while i < len(list_of_friends):
        if list_of_friends[i] not in dico:
            dico[list_of_friends[i]] = []
        if list_of_friends[i+1] not in dico:
            dico[list_of_friends[i+1]] = []
        ami(dico, i, list_of_friends)
        i+=2
    return dico

def get_people(network : dict) -> list:
    """
    Retourne la liste de toutes les personnes participant au réseau network.
    """
    liste = list(network.keys())
    return liste

def are_friends(network : dict, person1 : str, person2 : str) -> bool:
    """
    Retourne vrai ou faux selon si la première personne (person1)
    et seconde personne (person2) sont amis grâce au dictionnaire network.
    """
    i = 0
    while i < len(network[person1]):
        if network[person1][i] == person2:
            return True
        i += 1
    return False 

def all_his_friends(network : dict, person : str, group : list) -> bool:
    """
    Retourne vrai ou faux selon si la personne person est ami(e) avec toutes 
    les personnes du groupe group grâce au dictionnaire network.
    """
    i=0
    tab = list(network[person])
    while i < len(group):
        if group[i] not in tab:
            return False
        i += 1
    return True

def is_a_community(network : dict, group : list) -> bool:
    """
    Retourne vrai ou faux selon si le groupe group est une communauté grâce
    au dictionnaire network.
    """
    i = 0
    while i < len(group):
        tab = group.copy()
        tab.pop(i)
        if not all_his_friends(network, group[i], tab):
            return False
        i+=1
    return True


def find_community(network : dict, group : list) -> list:
    """
    Retourne une liste qui représente la communauté de la première personne
    de la liste group à l'aide du dictionnaire network.
    """
    com = [group[0]]
    i = 1
    while i < len(group):
        if all_his_friends(network, group[i], com):
            com.append(group[i])
        i+=1
    return com

def order_by_decreasing_popularity(network : dict, group : list) -> list:
    """
    Retourne la liste triée dans l'ordre décroissant de popularité grâce
    au dictionnaire network.
    """
    i = 0
    while i < len(group):
        j = i
        imax = i
        while j < len(group):
            if len(network[group[j]]) > len(network[group[imax]]):
                imax = j
            j+= 1
        group[i], group[imax] = group[imax], group[i]
        i+= 1
    return group


def find_community_by_decreasing_popularity(network : dict) -> list:
    """
    Retourne une liste de la communauté de la personne la plus populaire 
    du dictionnaire network.
    """
    group = list(network)
    pop = order_by_decreasing_popularity(network, group)
    res = find_community(network, pop)
    return res

def find_community_from_person(network : dict, person : str) -> list:
    """
    Retourne la liste de la communauté de la personne person grâce au 
    dictionnaire network
    """
    commu = [person]
    amis = find_community_by_decreasing_popularity(network)
    i = 0
    while i < len(amis):
        if all_his_friends(network, amis[i], commu):
            commu.append(amis[i])
        i+=1
    return commu

def find_max_community(network : dict) -> list:
    """
    Retourne la liste de la plus grande communauté du dictionnaire network.
    """
    people = get_people(network)
    c_max = find_community_from_person(network, people[0])
    i = 1
    while i < len(people):
        if is_a_community(network, find_community_from_person(network, people[i])):
            if len(find_community_from_person(network, people[i])) > len(c_max):
                c_max = find_community_from_person(network, people[i])
        i+=1
    return c_max
