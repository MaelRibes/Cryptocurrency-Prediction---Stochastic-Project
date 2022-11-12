Projet Stochastique - Prédiction des cryptomonnaies
============

[![GitHub Contributors](https://img.shields.io/github/contributors/MaelRibes/Cryptocurrency-Prediction---Stochastic-Project)](https://github.com/MaelRibes/Cryptocurrency-Prediction---Stochastic-Project/graphs/contributors) 
[![Python](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/) 

Notre objectif pour ce projet était de tenter d'établir à l'aide de calculs stochastiques une stratégie d'investissement dans les crypto-actifs. Nous avons alors choisi quelques outils mathématiques pertinents pour démontrer des phénomènes tels que l'inversion de tendance, le surachat ou encore la corrélation entre toutes ces monnaies.



---
## Outils d'analyse et interprétation des résultats
### __Moyennes Mobiles__  

Les moyennes mobiles sont des indicateurs de tendance techniques, qui sont utilisés dans l'analyse technique pour investir dans différents instruments financiers.
Une moyenne mobile fournit le cours moyen d’une action sur une période donnée.  
Soit *MM* la moyenne mobile, *t* l’instant choisi et *n* le nombre de périodes choisies :

<p align="center">
<img src="ressources/mm-formula.png"  width="250">
</p>

Cette moyenne permet de permet de lisser une série de valeurs exprimées en fonction du temps.

Cependant les investisseurs préfèrent avoir recours à une moyenne mobile exponentielle qui est beaucoup plus réactive que la moyenne mobile simple car elle est pondérée par rapport aux dernières valeurs. 
Soit *MME* la moyenne mobile exponentiel, *t* l’instant choisie, *C(t)* le courant actuel de l’actif et n le nombre de périodes choisie :

<p align="center">
<img src="ressources/mme-formula.png"  width="650">
</p>


On s'intéresse aux moyennes mobiles exponnentielles car elles sont plus réactives et donc plus intéréssantes à analyser.  

<p align="center">
<img src="ressources/BTC-USD-h-EMA.png"  width="600">
</p>

Nous savons que quand une courbe de moyenne mobile croise une autre moyenne mobile, la tendance baissière ou haussière de la monnaie s'inverse. Quand une moyenne mobile d'une certaine période passe "en dessous" d'un moyenne mobile ayant une période plus longue, la tendance de la courbe devient baissère et inversement.  
C'est exactement ce que nous pouvons observer sur cette courbe : La moyenne mobile sur 10h passe en dessous de celle sur 50h qui elle même passe en de dessous de celle sur 100h juste après. On remarque à la suite de ces inversions une très forte chute de la valeur du Bitcoin (≈-23% en 3j).  
Bien évidement, cette chute n'est pas arrivé à cause du croisement de ces courbes de moyennes mais bel et bien à cause d'un réel événement économique. La faillite de la 4ème plus grosse plateforme d'échanges de crypto FTX à entrainé une panique générale encourageant les gens à vendre en masses leurs cryptomonnaies, faisant baisser le prix du BTC, de l'ETH et donc de tous les autres tokens (cf. [Matrice de Corrélation](#matrice-de-corrélation)).  
Néanmoins, l'analyse des moyennes mobiles indiquait une chute prochaine du marché et permettait d'anticiper ces événements sans être au courant de l'actualité.
### __Indice Stochastique__  
L’indice stochastique est un indice fréquemment utilisé il représente la position relative du cours situé dans un écart historique.  
Il est calculé à l’aide de cette formule :
<p align="center">
<img src="ressources/indice-formula.png"  width="700">
</p>

Les investisseurs comparent souvent cet indice aux lignes droites situées à 80% et 20%. Lorsque l’indice passe en dessous des 20% on peut considérer que l’actif est en survente donc un achat à ce moment devrait être rentable à l’inverse lorsque l’indice va dépasser les 80% il est en surachat et va donc très probablement se rééquilibrer et repasser en dessous des 80%.

<p align="center">
<img src="ressources/BTC-USD-h-Indice.png"  width="600">
</p>

On remarque que la chute récente des cryptomonnaies due à FTX à entrainé la courbe du Bitcoin dans la zone de survente en dessous des 20%. C'est théoriquement le bon moment pour prendre position puisque nous pouvons imaginer que le cours remonte bientôt. Cependant, rien n'est certain et le marché pourrait être baissier encore longtemps à contexte économique.

### __Modèle autorégressif__
Un modèle autorégressif est une méthode linéaire permettant de prédire une valeur *X(t+1)* en fonction d'un nombre *p* de valeurs précédent celle-ci.

<p align="center">
<img src="ressources/ar-formula.png"  width="250">
</p>

 Nous avons donc choisi de tester notre modèle sur la courbe du Bitcoin sur les 2000 derniers jours afin de comparer notre prédiction avec les vraies valeurs.

<p align="center">
<img src="ressources/model-ar.png"  width="600">
</p>

On observe que notre prédiction de courbe se rapproche très fortement de la courbe réelle avec très peu d'erreurs. Cependant, ceci peut s'expliquer par le fait que nous avons entraîné notre modèle avec les valeurs précédentes de la vraie courbe et non pas avec les valeurs précédentes générées par notre modèle. Si cela avait été le cas, notre modèle aurait été bien moins fiable. Cependant, cela nous a ainsi bien permis de comprendre l'intérêt et le fonctionnement d'un modèle autorégressif sur un tel ensemble de données.

### __Matrice de Corrélation__
L'écosystème des cryptomonnaies est connu pour sa forte volatilité et ses périodes dîtes de bull run et bear market importante, qui affecte l'ensemble de ces actifs. Nous avons donc voulu montrer ici que les cryptomonnaies possèdent toute une très forte corrélation, notamment avec le bitcoin qui semble être le maître de ce marché.

<p align="center">
<img src="ressources/correlation.png"  width="600">
</p>

Comme nous pouvons le voir dans cette matrice générée à partir de notre script *correlation.py*, quasiment toutes les valeurs de corrélations sont au dessus de 0.5, exceptées les actifs dîts stables qui suivent des monnaies FIAT tel que le dollar américain (représentés en violet).
On observe même qu'il y a des valeurs très importante comme 0.77 entre le Bitcoin et l'Ethereum, ce qui témoigne d'une incidence très forte de l'un comme sur l'autre. C'est pourquoi la plupart des investisseurs possèdent en grande partie du Bitcoin et de l'Ethereum car ce sont ces cryptomonnaies qui dictent le marché. Ainsi, ceci nous permet de rappeler que lorsque lorsqu'un investisseur veut prendre position, il faut toujours faire attention aux autres cryptomonnaies, dont les plus importantes comme le BTC, l'ETH, le BNB... Car en effet, s'il vient à y avoir une baisse d'une cryptomonnaie à cause d'une nouvelle qui entraîne un mouvement de panique, c'est l'ensemble du marché qui peut s'effondrer.

---
## Conclusion
Grâce à ce projet, nous avons pu découvrir l'analyse de séries temporelles à l'aide d'outils mathématiques. Nous avons pu voir qu'il est possible de tirer énormément d'informations des valeurs passées, afin de pouvoir prédire le futur. Néanmoins, il existe toujours des risques et les prédictions ne seront jamais complétement fiables du fait de la volatilité de ce marché. Ce projet fût donc une très bonne introduction aux notions de machine learning que nous explorerons plus tard.
