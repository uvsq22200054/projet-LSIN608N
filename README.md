# Projet IN608N
Ce projet a été construit par Anissa KOURBAN HOUSSEN FASSY, He YU, Hajar CHERQI, et Yohann FRONT-REIGNIER dans le cadre de l'UE Projet de l'UVSQ.
Nous allons refaire le jeu "Othello" en python. On va dans un premier temps le faire en 1vs1, puis rajouter un ordinateur qui suivrait la stratégie algorithme minmax

## Règles du jeu
Noir commence toujours la partie. Puis les joueurs jouent à tour de rôle, chacun étant tenu de capturer des pions adverses lors de son mouvement. Si un joueur ne peut pas capturer de pion(s) adverse(s), il est forcé de passer son tour. Si aucun des deux joueurs ne peut jouer, ou si l'othellier ne comporte plus de case vide, la partie s'arrête. Le gagnant en fin de partie est celui qui possède le plus de pions.

La capture de pions survient lorsqu'un joueur place un de ses pions à l'extrémité d'un alignement de pions adverses contigus et dont l'autre extrémité est déjà occupée par un de ses propres pions. Les alignements considérés peuvent être une colonne, une ligne, ou une diagonale. Si le pion nouvellement placé vient fermer plusieurs alignements, il capture tous les pions adverses des lignes ainsi fermées. La capture se traduit par le retournement des pions capturés. Ces retournements n'entraînent pas d'effet de capture en cascade : seul le pion nouvellement posé est pris en compte.

Par exemple, la figure de gauche ci-dessous montre la position de départ. La figure centrale montre les 4 cases où Noir peut jouer, grâce à la capture d'un pion Blanc. Enfin, la figure de droite montre la position résultante si Noir joue en d3. Le pion Blanc d4 a été capturé (retourné), devenant ainsi un pion Noir.

(source : Wikipédia)
