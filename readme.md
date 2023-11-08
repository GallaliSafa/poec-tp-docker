1- j'ai fait une fonction apply_vat dans le fichier calc.py
2- j'ai importé la fonction en main
3- j'ai creer un fichier "test_calc.py" ou j'ai fait la declaration de test

4-j'ai fait le test en local
5-j'ai fait un dockerfile ou j'ai demande d'executer le main avec les valeurs qu'on veut tester
6-j'ai fait executé  "docker build -t tp-docker ."
             "docker run -it tp-docker python src/test_calc.py"
            "docker run -it tp-docker python src/main.py 100 20"
