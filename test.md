L'**algorithme A\*** (A star) est un **algorithme de recherche de chemin** utilisé en intelligence artificielle et en algorithmique pour trouver le chemin optimal d'un point de départ à un point d'arrivée dans un graphe pondéré. Il est couramment utilisé pour la recherche de chemins dans des jeux vidéo, la robotique, et la résolution de puzzles.

### 🔹 **Principe de l'algorithme A\***

A\* fonctionne en utilisant une **fonction de coût** pour explorer les chemins potentiels tout en cherchant à minimiser le coût total du trajet. Cette fonction de coût est définie comme :

f(n) = g(n) + h(n)

* g(n) : Coût du chemin parcouru depuis le point de départ jusqu'au nœud nn.
* h(n) : Heuristique estimant le coût restant entre nn et l'objectif (c'est une estimation de la distance restante).
* f(n) : Estimation du coût total du chemin passant par nn.

A\* choisit toujours le nœud ayant la plus petite valeur de f(n)f(n), ce qui permet d'optimiser l'exploration.

---

## **Heuristiques utilisées avec A\***

L'heuristique h(n)h(n) est un élément clé de A\*, car elle influence la rapidité et l'efficacité de la recherche. Voici trois heuristiques populaires :

### **1️⃣ Distance de Manhattan**

📌 **Définition :**
La distance de Manhattan mesure la distance entre deux points dans un **espace en grille** (comme un échiquier ou un puzzle en 2D). Elle suppose que l'on ne peut se déplacer que **horizontalement et verticalement**.

h(n)=∣xcurrent−xgoal∣+∣ycurrent−ygoal∣h(n) = |x\_{\\text{current}} - x\_{\\text{goal}}| + |y\_{\\text{current}} - y\_{\\text{goal}}|✔️ **Utilisation :**

* Très utilisée pour les puzzles comme le **Taquin (8-puzzle, 15-puzzle)**.
* Efficace pour les **déplacements en grille** (jeux vidéo, labyrinthe).

---

### **2️⃣ Conflit linéaire (Linear Conflict)**

📌 **Définition :**
Une amélioration de la distance de Manhattan. Un **conflit linéaire** se produit lorsque **deux tuiles sont dans la bonne ligne ou colonne mais dans le mauvais ordre**, ce qui signifie qu'elles devront s'échanger pour atteindre leur position finale.

✔️ **Formule :**
L'heuristique Linear Conflict est définie comme :

h(n)=Manhattan Distance+2×(nombre de conflits lineˊaires)h(n) = \\text{Manhattan Distance} + 2 \\times (\\text{nombre de conflits linéaires})✔️ **Utilisation :**

* Très efficace pour **les puzzles glissants** comme le **8-puzzle** ou le **15-puzzle**.

---

### **3️⃣ Nombre de tuiles mal placées (Misplaced Tiles)**

📌 **Définition :**
Compte le **nombre de tuiles qui ne sont pas à leur place finale**.

h(n)=∑i=1N1(ti≠gi)h(n) = \\sum\_{i=1}^{N} \\mathbb{1}(t\_i \\neq g\_i)où 1(ti≠gi)\\mathbb{1}(t\_i \\neq g\_i) est **1** si la tuile tit\_i est mal placée, et **0** sinon.

✔️ **Utilisation :**

* Simple et rapide à calculer.
* Moins précise que la distance de Manhattan, mais utile pour **une première approche**.

---

## **Comparaison des heuristiques**


| Heuristique            | Précision | Rapidité    | Utilisation                        |
| ---------------------- | ---------- | ------------ | ---------------------------------- |
| **Misplaced Tiles**    | Faible     | Très rapide | Bonne pour des estimations rapides |
| **Manhattan Distance** | Moyenne    | Moyenne      | Équilibrée, utilisée souvent    |
| **Linear Conflict**    | Élevée   | Plus lente   | Très efficace pour les puzzles    |
