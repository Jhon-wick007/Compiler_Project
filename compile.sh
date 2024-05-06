lex lexicalAnalyser.l
yacc -d syntaxChecker.y
gcc lex.yy.c y.tab.c  -w -g
./a.out ip.txt
g++ syntax.cpp -o syntax
./syntax
python3 Code_opt.py
