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

def create_network(list_of_friends):
    dico = {}
    i = 0
    while i < len(amis):
        if amis[i] not in dico:
            dico[amis[i]] = []
            j = 0
        while j < len(amis):
            if amis[j] == amis[i]:
                if j%2 == 0:
                    dico[amis[i]].append(amis[j+1])
                else:
                    dico[amis[i]].append(amis[j-1])
            j+=1
        i+=1
    return dico

def get_people(network):
    liste = list(reseau.keys())
    return liste

def are_friends(network, person1, person2):
    i = 0
    while i < len(reseau[p1]):
        if reseau[p1][i] == p2:
            return True
        i += 1
  return False 

def all_his_friends(network, person, group):
    i=0
    tab = list(reseau[per])
    while i < len(grp):
        if grp[i] not in tab:
            return False
        i += 1
    return True

def is_a_community(network, group):
    tab = list(reseau[grp[0]])
    i = 1
    while i < len(grp):
        if grp[i] not in tab:
            return False
        i+=1
    return True


def find_community(network, group):
    com = [grp[0]]
    i = 1
    tab = list(reseau[grp[0]])
    while i < len(grp):
        if grp[i] in tab:
            com.append(grp[i])
        i += 1
    if is_a_community:
        return com

def order_by_decreasing_popularity(network, group):
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


def find_community_by_decreasing_popularity(network):
    pass

def find_community_from_person(network, person):
    pass

def find_max_community(network):
    pass
