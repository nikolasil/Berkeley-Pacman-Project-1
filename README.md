# This project was made during my studies in UOA University and especially for the course Artificial Intelligence 1.

---

[Project 1: Search](https://inst.eecs.berkeley.edu/~cs188/sp19/project1.html)

> There are comments all over my code if there is something that i didn't covered here.

> **Run command:** python ./autograder.py

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

BFS is bassically UCS with g(n) = depth(n).
That is because BFS searches first the nodes with the smallest depth.
So again we have queue **but** with priority the cost and not the depth.

This change has the small peculiarity that the cost depending on when we meet the node
and from whom we will come may differ while the depth always remains the same.
So we add an if statement that checks to see in the nodes we have inside have greater new
cost than the one they had before. If they had we change the cost otherwise we leave as it is.

> The code remains the same expect from the data structure again.

---

## QUESTION 4

A* is also similar to UCS but it's "smarter".
A* uses a function to better calculate the priority.
With the formula f(n) = g(n) + h(n).
> f(n) the priority we will use.

> g(n) the cost we had before.

> h(n) is called a heuristic function.
>> And it can be any function that can help us make priority as closer to reality.

So again we have queue with priority cost + the result of the heuristic.
The code is similar. But we do not deal with any node we have
re-visited because that means we were in the same spot with lower total cost.
So we will move on unnecessarily.
That's why we need to proceed to the next iteration.

---

## QUESTION 5

In initialize we make a list of tuples to keep the not visited corners.
At getStartState we simply return it to its original position along with the corners
that we have not visited.
In order to reach our goal in a state we need this
state not to have corners next to it in the tuple (means that it has visited them all)
And to get the succesors we will do a check for each
possible allowed movement and we will return those movement without those
that leads to a corner.

---

## QUESTION 6

I choose manhattanDistance as heuristic from util.py.
If I go to the corner closest to me then I can just follow the smaller side to go
to the other corner and then just follow the sides.
If there wasn't any walls blocking this would be the best case.

---

## QUESTION 7

I use mazeDistance in searchAgents.py.
We will simply find our distance from each food and return the maximum of
these distances. So each time the nodes in the queue are stored with the largest possible priority.
The queue will take out the node with the smallest of those maximum priorities so every time we make the best of the worst choices.
8
---

## QUESTION 8

We just call the A* (with the problem) to find the path to the closest food.
> It does not matter which function we call A* or UCS or BFS.
