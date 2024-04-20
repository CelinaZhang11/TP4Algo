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

    for p in [2,3,5,7,11,13,17,19,23,29]:
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
        for j in range(max(initial_length, i + 1), len(existing_members)):
            if(isPrime(int(str(existing_members[i]) + str(existing_members[j])))):
                if(isPrime(int(str(existing_members[j]) + str(existing_members[i])))):
                    graph[existing_members[i]].append(existing_members[j])
                    graph[existing_members[j]].append(existing_members[i])
                    nouvelles_connections.append(existing_members[i])
                    nouvelles_connections.append(existing_members[j])

    return nouvelles_connections

def trouverClique4(graph, start, curr_members, groupes, sommes):
    
    if len(curr_members) == 3:
        curr_members.append(start)
        somme = sum(curr_members)
        if not somme in sommes:
            groupes.append(curr_members)
            sommes.append(somme)
        return

    for neighbor in graph[start]:
        if len(curr_members) == 0:
            obj = copy(curr_members)
            obj.append(neighbor)
            trouverClique4(graph, start, obj, groupes, sommes)
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
                    trouverClique4(graph, start, obj , groupes, sommes)


def getNthGroup(n):
    graph = {}
    currPrimes = []

    # Formule fuckall que jai inventer
    augment_factor = 500
    if(n > 20):
        augment_factor = 1000
    if(n >= 50):
        augment_factor = 1500

    AugmentGraph(graph, augment_factor, currPrimes)

    sommes = []
    groupes = []
    curr = []

    for node in currPrimes:
        trouverClique4(graph, node, curr, groupes, sommes)

    # Dans le fond je veux creer assez de groupes pr garentir quon a pas un groupe plus petit
    # Avec un nombre premier plus grand
    # Faq je cree un nombre de groupes arbitraireemnt plus grand
    while(len(sommes) < 2*n):
        print("Augmenting....")
        updatedNodes = AugmentGraph(graph, augment_factor//2, currPrimes)
        for node in updatedNodes:
            trouverClique4(graph, node, [], groupes, sommes)

    sommes.sort()
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