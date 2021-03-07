# This project was made during my studies in UOA University and especially for the course Artificial Intelligence 1.

---

## QUESTION 1

I created the DFS algorithm using stack because DFS logic is LIFO (LAST-IN FIRST-OUT).
I am using from util.py the already implemented stack and i insert the initial state of the problem.
I also create 2 lists. One to hold the nodes that i have visit and one to hold the path.
The logic in the while is:
- remove the first element from the stack.
> that is the one that got inserted last.
- check to see if we reached the goal.
- store that we visited this node.
- find the next nodes from these node.
- if i have not visited them yet put them to the stack.

---

## QUESTION 2

The logic here is the same with DFS but BFS is FIFO (FIRST-IN FIRST-OUT).
That means we need to use queue instead of stack here.
> But the code remains the same expect from the data structure.

---

## QUESTION 3

Ο BFS στην ουσία είναι UCS με g(n) = depth(n).
Δηλαδή ο BFS ψάχνει πρώτα τους κόμβους με το μικρότερο depth.
Άρα πάλι έχουμε queue αλλά με priority το κόστος και όχι το depth.
Ο κώδικας είναι πάλι ο ίδιος απλά αλλάζει η δομή.
Και έχει την μικρή ιδιαιτερότητα ότι το κόστος ανάλογα πότε θα συναντήσουμε τον κόμβο
και από ποιόν θα ερχόμαστε μπορεί να διαφέρει ενώ το depth (πάντα παραμένει το ίδιο)
άρα προσθέτουμε μία if που ελέγχει να δεί στους κόμβους που έχουμε μέσα αν το νέο 
κόστος που βρήκαμε για αυτούς αν είναι μικρότερο για να το αλλάξουμε αλλιώς το
αφήνουμε ως έχει.

BFS is bassically UCS with g(n) = depth(n).
That is because BFS searches first the nodes with the smallest depth.
So again we have queue **but** with priority the cost and not the depth.

This change has the small peculiarity that the cost depending on when we meet the node
and from whom we will come may differ while the depth always remains the same.
So we add an if statement that checks to see in the nodes we have inside, if the new
cost we found for them if it is lower to change it otherwise
we leave as it is.

> The code remains the same expect from the data structure again.



## QUESTION 4

Ο A* είναι και αυτός παρόμοιος με τον UCS αλλά είναι ποιο ‘’έξυπνος’’.
Ο Α* χρησιμοποιεί μία συνάρτηση για να υπολογίσει καλύτερα το priority. Με τον τύπο f(n)
= g(n) + h(n).
f(n) το priority που θα χρησιμοποιήσουμε.
g(n) = το κόστος που είχαμε πριν
Η h(n) λέγεται heuristic ( ευρευτική ) συνάρτηση. Και μπορεί να είναι οποιαδήποτε
συνάρτηση μπορεί να μας βοηθήσει να κάνουμε το Priority Ποιο κοντά στην
πραγματικότητα.
Άρα πάλι έχουμε queue με priority το κόστος + το αποτέλεσμα της ευρετικής.
Ο κώδικας είναι παρόμοιος. Αλλά δεν ασχολιόμαστε με κανένα κόμβο που έχουμε
ξαναεπισκευτεί γιατί σημαίνει ότι για να τον έχουμε επισκευτεί σημαίνει ότι ποιο πριν
ήμασταν στο ίδιο σημείο με μικρότερο συνολικό κόστος. Άρα άσκοπα θα προσωρήσουμε.
Οπότε πάμε στην επόμενη επανάληψη.

## QUESTION 5

Στο initialize φτιάχνουμε μία λίστα με tuples για να κρατήσουμε τις μια
μη visited γωνίες.
Στο getStartState απλά γυρνάμε το την αρχική θέση μαζί με τις γωνίες
που δεν έχουμε επισκεφτεί.
Για να έχουμε φτάσει στον στόχο μας σε ένα state θα πρέπει αυτό το
state να μην έχει δίπλα του στο tuple γωνίες(σημαίνει ότι τις
επισκέφτηκε όλες)
Και για να πάρουμε τους succesors θα κάνουμε έναν έλεγχο για κάθε
πιθανή επιτρεπόμενη κίνηση και θα της επιστρεψουμε και βέβαια θα
κοιτάξουμε αν κάποιες από αυτές τις κινήσεις καταλήγει σε γωνία για να
την αφαιρέσουμε.

## QUESTION 6

Επιλέγω σαν heuristic την manhattanDistance στο util.py.
Αν πάω στην ποιο κοντινή μου γωνία μετά απλά μπορώ να ακολουθήσω την μικρότερη
πλευρά για να πάω στην άλλη γωνία και μετά απλά ακολουθώ τις πλευρές αν δεν υπήρχαν
οι τοίχοι να με εμποδίσουν( αυτή η λογική είναι η καλύτερη περίπτωση).

## QUESTION 7

Χρησιμοποιώ την mazeDistance στο searchAgents.py.
Θα βρούμε απλά την απόσταση μας από κάθε φαγητό και θα επιστρέψουμε το μέγιστο
αυτών τον αποστάσεων. Οπότε κάθε φορά αποθηκεύονται οι κόμβοι στην ουρά με Priority
το μεγαλύτερο που είναι δυνατόν. Η ουρά θα βγάλει τον κόμβο με το μικρότερο αυτών τον
μεγαλύτερων άρα κάθε φορά κάνουμε το καλύτερο από τις χειρότερες επιλογές.

## QUESTION 8

Απλά καλούμε τον astar(με το πρόβλημα) για να βρεί το μονοπάτι για το ποιο κοντινό
φαγητό. Δεν έχει σημασία ποια συνάρτηση θα καλέσουμε Α* ή UCS ή BFS.
