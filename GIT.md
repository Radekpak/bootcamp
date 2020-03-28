 #Podsawy Git
 
 #konfiguracja 
 
 git config --global user.name=<nazwa>
 
 ##tworzenie nowego repozytorium
 
 w katalogu projektu piszemy
 
 git init

 
 ##Branch
 Gałąź
 
 master
 
 devel
 git branch #sprawdza jaki to branch
 git checkout -b nazwa_brancha
 
 ##commit
 punkt przywracania
 
 By utworzyć commit musimy
 0. sprawdzenie obecnego stanu
   git status
   
 1.dodać pliki które chcemy mieć w commicie
 git add <sciezka pliku>
 mozna dodać wszyskie pliki:
 
 git add .
 
 a n koniec commit
 
 git commit
 
 git commit -m "prosta zmiana"
 