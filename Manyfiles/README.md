# Manyfiles #
_beecrowd | 2545_

https://www.beecrowd.com.br/judge/en/problems/view/2545

## Descrição ##
n the year 2569, Vasya receives a great birthday present from his mother, the source-code of his favorite video-game, Solitaire Spider. Vasya goes directly to his computer with 4096 processor cores, inserts the disk, types ls in the directory of the source-code and realizes that it is composed by N files and a Manyfile.

A Manyfile is something like a cake recipe used to compile the source code. By entering the command many, the Manyfile is read and the files are compiled, such that the maximum number of cores are used simultaneously. If everything was fine, this process would be really fast, since each source file takes exactly one minute to be compiled. However, the compilation of some files depend on the conclusion of others, what may make it impossible to compile all files simultaneously.

Consider the compilation of Solitaire Spider finished when all its N files are compiled. Knowing which files depend on which, write a program that calculates how many minutes it will take to compile the game.
## Entrada ##

The input contains several test cases. The first line of each test case contains an integer N (1 ≤ N ≤ 1000), the number of source files of Solitaire Spider. The files are numbered from 1 to N. The next N lines describe the files. i-th line contains an integer Mi (0 ≤ Mi < N) followed by Mi integers between 1 and N, all different than i, representing the index of the files which file i depends on.

The input ends with end-of-file (EOF).


Example:

2

1 2

1 1

3

0

1 3

0



## Saida ##

For each test case, print a single line containing the total time, in minutes, it will take to compile Solitaire Spider. If it is impossible to compile it, print -1.
Example:

-1

2
