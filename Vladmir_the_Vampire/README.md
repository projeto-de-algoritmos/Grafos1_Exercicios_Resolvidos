# Vladimir the Vampire #
_beecrowd | 1733_

[Vladimir the Vampire](https://www.beecrowd.com.br/judge/en/problems/view/1733)

## Descrição ##
Vladimir has white skin, very long teeth and is 600 years old, but this is no problem because Vladimir is a vampire.

Vladimir has never had any problems with being a vampire. In fact, he is a very successful doctor who always takes the night shift and so has made many friends among his colleagues. He has a very impressive trick which he shows at dinner partys: He can tell the blood group by taste.

Vladimir loves to travel, but being a vampire he has to overcome three problems.

First, he can only travel by train because he has to take his coffin with him. (On the up side he can always travel first class because he has invested a lot of money in long term stocks.)
Second, he can only travel from dusk till dawn, namely from 6 pm to 6 am. During the day he has to stay inside a train station.
Third, he has to take something to eat with him. He needs one litre of blood per day, which he drinks at noon (12:00) inside his coffin.
You should help Vladimir to find the shortest route between two given cities, so that he can travel with the minimum amount of blood. (If he takes too much with him, people will ask funny questions like "What do you do with all that blood?")

Input
The first line of the input will contain a single number telling you the number of test cases.

Each test case specification begins with a single number telling you how many route specifications follow.

Each route specification consists of the names of two cities, the departure time from city one and the total travelling time. The times are in hours. Note that Vladimir can't use routes departing earlier than 18:00 or arriving later than 6:00.

There will be at most 100 cities and less than 1000 connections. No route takes less than one hour and more than 24 hours. (Note that Vladimir can use only routes with a maximum of 12 hours travel time (from dusk till dawn).) All city names are shorter than 32 characters.

The last line contains two city names. The first is Vladimir's start city, the second is Vladimir's destination.

Output
For each test case you should output the number of the test case followed by "Vladimir needs # litre(s) of blood." or "There is no route Vladimir can take."

## Entrada ##

```
2
3
Ulm Muenchen 17 2
Ulm Muenchen 19 12
Ulm Muenchen 5 2
Ulm Muenchen
10
Lugoj Sibiu 12 6
Lugoj Sibiu 18 6
Lugoj Sibiu 24 5
Lugoj Medias 22 8
Lugoj Medias 18 8
Lugoj Reghin 17 4
Sibiu Reghin 19 9
Sibiu Medias 20 3
Reghin Medias 20 4
Reghin Bacau 24 6
Lugoj Bacau
```

## Saida ##

