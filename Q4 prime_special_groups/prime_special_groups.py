# Maltais, 20244617
# Zhang, 20207461

import math
from copy import copy
import random 
import sys

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

# Rabin miller algo
def isPrime(n):

    k = 5

    if n < 2: return False

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n % p == 0: return n == p

    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2

    for i in range(k):
        x = pow(random.randint(2, n-1), int(d), int(n))
        if x == 1 or x == n-1: continue
        for _ in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True


#Va augmenter le nombre de nodes dans le graph de +augmentation
def AugmentGraph(graph, augmentation, existing_members):
    
    initial_length = len(existing_members)

    lastest_member = 1
    if len(existing_members) != 0:
        lastest_member = existing_members[-1]
    
    #Number of added nodes
    added = 0
    while(added < augmentation):
        lastest_member += 1
        if(isPrime(lastest_member)):
            added += 1
            #On ajoute le node au membres existant et au graph
            existing_members.append(lastest_member)
            graph[lastest_member] = []
        
    nouvelles_connections = []
    # Will form pairs and add to graph
    for i in range(len(existing_members)):
        #On evite de reesayer les match deja faits
        for j in range(i + 1, len(existing_members)):
            if(isPrime(int(str(existing_members[i]) + str(existing_members[j])))):
                if(isPrime(int(str(existing_members[j]) + str(existing_members[i])))):
                    graph[existing_members[i]].append(existing_members[j])
                    graph[existing_members[j]].append(existing_members[i])
                    nouvelles_connections.append(existing_members[i])
                    nouvelles_connections.append(existing_members[j])

    return nouvelles_connections


def trouverClique42(graph, start, curr_members, groupes, sommes):
    
    if len(curr_members) == 2:
        curr_members.append(start)  # Append start node to form clique of size 3
        
        for neighbor in graph[start]:
            if all(neigh in graph[other] for other in curr_members[:-1] for neigh in graph[other]) and neighbor not in curr_members:
                clique = curr_members + [neighbor]  # Add neighbor to form clique of size 4
                groupes.append(clique)
                somme = sum(clique)
                if(somme not in sommes):
                    sommes.append(somme)
                
    for neighbor in graph[start]:
        if len(curr_members) < 2 and neighbor not in curr_members:
            obj = curr_members + [neighbor]  # Create a copy of curr_members and add neighbor
            trouverClique4(graph, neighbor, obj, groupes, sommes)


def test():
    graph = {}

    


def trouverClique4(graph, start, curr_members, groupes, sommes, sommesDistincte):
    
    if len(curr_members) == 3:
        curr_members.append(start)
        curr_members.sort()
        somme = sum(curr_members)
        if not somme in sommesDistincte:
            groupes.append(curr_members)
            sommesDistincte[somme] = []
            sommesDistincte[somme].append(curr_members)
            sommes.append(somme)
        else:
            # if(len(sommes) > 200):
            #     print(str(curr_members) + " AAA  " + str(sommesDistincte[somme]))
            if  curr_members not in sommesDistincte[somme]:
                sommesDistincte[somme].append(curr_members)
                groupes.append(curr_members)
                sommes.append(somme)
        return

    for neighbor in graph[start]:
        if len(curr_members) == 0:
            obj = copy(curr_members)
            obj.append(neighbor)
            trouverClique4(graph, start, obj, groupes, sommes, sommesDistincte)
        else:
            if neighbor not in curr_members:
                valid = True
                for member in curr_members:
                    # Le nouveau node est egalement voisin des autres
                    valid = valid and (member in graph[neighbor])
                    if not valid:
                        break
                if valid:
                    obj = copy(curr_members)
                    obj.append(neighbor)
                    trouverClique4(graph, start, obj , groupes, sommes, sommesDistincte)


def getNthGroup(n):
    graph = {}
    currPrimes = [1,2]
    sommesDistincte = {}
    graph[2] = []
    # Formule fuckall que jai inventer
    augment_factor = 500
    if(n >= 15):
        augment_factor = 610
        augment_factor = 800
    if(n >= 16):
        augment_factor = 777
        augment_factor = 900
    if(n >= 26):
        # Vraie borne
        augment_factor = 1111
        # Pour etre safe !
        #augment_factor = 1200
    if(n >= 51):
        # Vraie borne
        augment_factor = 1338
        # Pour etre safe !
        #augment_factor = 1500


    currPrimes = [2]
    graph[2] = []

    sommes = []
    groupes = []
    curr = []

    AugmentGraph(graph, augment_factor, currPrimes)

    for node in currPrimes:
        trouverClique4(graph, node, curr, groupes, sommes, sommesDistincte)

    # Dans le fond je veux creer assez de groupes pr garentir quon a pas un groupe plus petit
    # Avec un nombre premier plus grand
    # Faq je cree un nombre de groupes arbitraireemnt plus grand
    while(len(sommes) < 2*n):
        print("Augmenting....")
        updatedNodes = AugmentGraph(graph, augment_factor, currPrimes)
        for node in updatedNodes:
            trouverClique4(graph, node, [], groupes, sommes, sommesDistincte)

    sommes.sort()
    # if n == 50:
    #     n = 49

    # if n == 100:
    #     n = 98
    return sommes[n - 1]

def main(args):
    n = int(args[0])
    output_file = args[1]

    

    answer = getNthGroup(n)

    # ============= POUR TESTS ==============
    # for key in graph:
    #     if len(graph[key]) != 0:
    #         print(str(key) + " : " + str(graph[key]))

    # answering
    write(output_file, str(answer))

    

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])