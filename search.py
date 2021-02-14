# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack  # we use stack cause we want depth
    stack = Stack()
    stack.push((problem.getStartState(), []))   # Initialize stack. stack has tuples (xy , path)
    visited = []    # visited (x,y)
    path = []   # every state keeps his path

    # if initial state is goal state then return empty list of moves
    if problem.isGoalState(problem.getStartState()):
        return []

    while(not stack.isEmpty()):  # loop if stack is not empty
        xy, path = stack.pop()  # get position and path

        if problem.isGoalState(xy):  # if we found a solution
            return path  # return the path. No need to search any more!

        visited.append(xy)  # add xy to visited
        # get the successors of current state
        successors = problem.getSuccessors(xy)
        for s in successors:  # and add them to the stack if the xy has not been visited
            if s[0] not in visited:
                # push them in with the new path
                stack.push((s[0], path + [s[1]]))
    return []  # Did not find any solution


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue  # we use queue cause we want breadth

    queue = Queue()
    queue.push((problem.getStartState(), []))  # Initialize queue. queue has tuples (xy , path)
    visited = []    # visited (x,y)
    path = []   # every state keeps his path

    # if initial state is goal then return empty list of moves
    if problem.isGoalState(problem.getStartState()):
        return []

    while(not queue.isEmpty()):  # loop if queue is not empty
        xy, path = queue.pop()   # get position and path

        if problem.isGoalState(xy):  # if we found a solution
            return path  # return the path. No need to search any more!

        visited.append(xy)  # add xy to visited
        # get the successors of current state
        successors = problem.getSuccessors(xy)
        for s in successors:    # and add them to the queue if the xy has not been visited
            if s[0] not in visited and s[0] not in (state[0] for state in queue.list):
                # push them in with the new path
                queue.push((s[0], path + [s[1]]))
    return []  # Did not find any solution


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # UCS is very similar to BFS
    # BFS is UCS but the only change is g(n)=DEPTH(n)
    from util import PriorityQueue  # we use queue cause we want breadth

    priorityQueue = PriorityQueue()
    # priorityQueue has tuples (xy , path, priority)
    # we put 0 for the lowest priority
    priorityQueue.push((problem.getStartState(), []), 0)    # Initialize priorityQueue
    visited = []    # visited (x,y)
    path = []   # every state keeps his path

    # if initial state is goal then return empty list of moves
    if problem.isGoalState(problem.getStartState()):
        return []

    while(not priorityQueue.isEmpty()):  # loop if priorityQueue is not empty
        xy, path = priorityQueue.pop()  # get position and path

        if problem.isGoalState(xy):  # if we found a solution
            return path  # return the path. No need to search any more!

        visited.append(xy)  # add xy to visited
        # get the successors of current state
        successors = problem.getSuccessors(xy)
        for s1 in successors:    # and add them to the priorityQueue if the xy has not been visited
            if s1[0] not in visited:
                if s1[0] not in (state[2][0] for state in priorityQueue.heap): # if s1 not already in the priorityQueue
                    # add them like the BFS but with priority
                    priorityQueue.push((s1[0], path + [s1[1]]), problem.getCostOfActions(path + [s1[1]]))
                
                else:   # if s1 is already in the priorityQueue
                    for s2 in priorityQueue.heap:   # find the already pushed state
                        if s2[2][0] == s1[0]: 
                            old = problem.getCostOfActions(s2[2][1]) # and get the priority that it has so we can check it with our new priority

                    if old > problem.getCostOfActions(path + [s1[1]]): # if the new priority is better than the old
                        priorityQueue.update((s1[0],path + [s1[1]]),problem.getCostOfActions(path + [s1[1]]))   # then just update it
    return []   # Did not find any solution


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    # A* is very similar to UCS
    # The diference is that the priority on A* is f(n)=g(n)+h(n). g(n) = the cost from start to n. h(n) = heuristic function that estimates the cheapest path from n to the goal.
    priorityQueueH = PriorityQueue()
    # priorityQueueFunction has tuples (xy , path, priority) as in the UCS
    priorityQueueH.push((problem.getStartState(), []),heuristic(problem.getStartState(),problem)) # in the start f(n) = 0 + heuristic
    visited = []    # visited (x,y)
    path = []   # every state keeps his path

    # if initial state is goal then return empty list of moves
    if problem.isGoalState(problem.getStartState()):
        return []

    while(not priorityQueueH.isEmpty()):  # loop if priorityQueue is not empty
        xy, path = priorityQueueH.pop()  # get position and path

        if problem.isGoalState(xy):  # if we found a solution
            return path  # return the path. No need to search any more!

        if xy in visited:   # if xy has already been visited means that the first time we found xy the cost was lower so we must leave this path
            continue    # go to the next iteration

        visited.append(xy)  # add xy to visited
        # get the successors of current state
        successors = problem.getSuccessors(xy)
        for s in successors:    # and add them to the priorityQueue if the xy has not been visited
            if s[0] not in visited:
                # add them like the UCS but with priority = g(n) + h(n)
                g = problem.getCostOfActions(path + [s[1]]) # calculate g(n)
                h = heuristic(s[0],problem) # calculate h(n)
                priorityQueueH.push((s[0], path + [s[1]]), g + h)
    return []   # Did not find any solution


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
