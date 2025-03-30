L'algorithme A* (A star) est un algorithme de recherche de chemin utilisé en intelligence artificielle et en algorithmique pour trouver le chemin optimal d'un point de départ à un point d'arrivée dans un graphe pondéré. Il est couramment utilisé pour la recherche de chemins dans des jeux vidéo, la robotique, et la résolution de puzzles.

🔹 Principe de l'algorithme A*
A* fonctionne en utilisant une fonction de coût pour explorer les chemins potentiels tout en cherchant à minimiser le coût total du trajet. Cette fonction de coût est définie comme :

𝑓
(
𝑛
)
=
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
f(n)=g(n)+h(n)
𝑔
(
𝑛
)
g(n) : Coût du chemin parcouru depuis le point de départ jusqu'au nœud 
𝑛
n.

ℎ
(
𝑛
)
h(n) : Heuristique estimant le coût restant entre 
𝑛
n et l'objectif (c'est une estimation de la distance restante).

𝑓
(
𝑛
)
f(n) : Estimation du coût total du chemin passant par 
𝑛
n.

A* choisit toujours le nœud ayant la plus petite valeur de 
𝑓
(
𝑛
)
f(n), ce qui permet d'optimiser l'exploration.

Heuristiques utilisées avec A*
L'heuristique 
ℎ
(
𝑛
)
h(n) est un élément clé de A*, car elle influence la rapidité et l'efficacité de la recherche. Voici trois heuristiques populaires :

1️⃣ Distance de Manhattan
📌 Définition :
La distance de Manhattan mesure la distance entre deux points dans un espace en grille (comme un échiquier ou un puzzle en 2D). Elle suppose que l'on ne peut se déplacer que horizontalement et verticalement.

ℎ
(
𝑛
)
=
∣
𝑥
current
−
𝑥
goal
∣
+
∣
𝑦
current
−
𝑦
goal
∣
h(n)=∣x 
current
​
 −x 
goal
​
 ∣+∣y 
current
​
 −y 
goal
​
 ∣
✔️ Utilisation :

Très utilisée pour les puzzles comme le Taquin (8-puzzle, 15-puzzle).

Efficace pour les déplacements en grille (jeux vidéo, labyrinthe).

2️⃣ Conflit linéaire (Linear Conflict)
📌 Définition :
Une amélioration de la distance de Manhattan. Un conflit linéaire se produit lorsque deux tuiles sont dans la bonne ligne ou colonne mais dans le mauvais ordre, ce qui signifie qu'elles devront s'échanger pour atteindre leur position finale.

✔️ Formule :
L'heuristique Linear Conflict est définie comme :

ℎ
(
𝑛
)
=
Manhattan Distance
+
2
×
(
nombre de conflits lin
e
ˊ
aires
)
h(n)=Manhattan Distance+2×(nombre de conflits lin 
e
ˊ
 aires)
✔️ Utilisation :

Très efficace pour les puzzles glissants comme le 8-puzzle ou le 15-puzzle.

3️⃣ Nombre de tuiles mal placées (Misplaced Tiles)
📌 Définition :
Compte le nombre de tuiles qui ne sont pas à leur place finale.

ℎ
(
𝑛
)
=
∑
𝑖
=
1
𝑁
1
(
𝑡
𝑖
≠
𝑔
𝑖
)
h(n)= 
i=1
∑
N
​
 1(t 
i
​
 

=g 
i
​
 )
où 
1
(
𝑡
𝑖
≠
𝑔
𝑖
)
1(t 
i
​
 

=g 
i
​
 ) est 1 si la tuile 
𝑡
𝑖
t 
i
​
  est mal placée, et 0 sinon.

✔️ Utilisation :

Simple et rapide à calculer.

Moins précise que la distance de Manhattan, mais utile pour une première approche.

Comparaison des heuristiques
Heuristique	Précision	Rapidité	Utilisation
Misplaced Tiles	Faible	Très rapide	Bonne pour des estimations rapides
Manhattan Distance	Moyenne	Moyenne	Équilibrée, utilisée souvent
Linear Conflict	Élevée	Plus lente	Très efficace pour les puzzles
