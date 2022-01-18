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
    fringe = util.Stack()  # setting up the stack for holding states (Depth-First-Search uses stack)
    if problem.isGoalState(problem.getStartState()):  # base case of goal state matching start state
        return []
    states_visited = []  # defining a list to avoid expanding states that have been expanded
    final_path = []  # defining a list to be returned at the end of the function
    current_state = problem.getStartState()  # initializing current state
    current_path = util.Stack()  # defining a stack holding all actions until the current state

    while not problem.isGoalState(current_state):  # while we have not reached the goal
        if current_state not in states_visited:  # if we have not already visited the current state (loc + direction)
            states_visited.append(current_state)  # add current state to visited states
            successors = problem.getSuccessors(current_state)
            for successor in successors:
                fringe.push(successor[0])  # successor[0] is the next state
                partial_path = final_path + [successor[1]]  # successor[1] is the possible action in this state
                current_path.push(partial_path)  # adding expansion of current state to the path so far
        current_state = fringe.pop()  # setting current state to expand the next viable successor
        final_path = current_path.pop()  # adding path to current state to our final return path
    return final_path
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()  # setting up the queue for holding states (Breadth-First-Search uses queue)
    if problem.isGoalState(problem.getStartState()):  # base case of goal state matching start state
        return []
    states_visited = []  # defining a list to avoid expanding states that have been expanded
    final_path = []  # defining a list to be returned at the end of the function
    current_state = problem.getStartState()  # initializing current state
    current_path = util.Queue()  # defining a queue holding all actions until the current state

    while not problem.isGoalState(current_state):  # while we have not reached the goal
        if current_state not in states_visited:  # if we have not already visited the current state (loc + direction)
            states_visited.append(current_state)  # add current state to visited states
            successors = problem.getSuccessors(current_state)
            for successor in successors:
                fringe.push(successor[0])  # successor[0] is the next state
                partial_path = final_path + [successor[1]]  # successor[1] is the possible action in this state
                current_path.push(partial_path)  # adding expansion of current state to the path so far
        current_state = fringe.pop()  # setting current state to expand the next viable successor
        final_path = current_path.pop()  # adding path to current state to our final return path
    return final_path
    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"  # Uniform-Cost-Search uses priority queue
    fringe = util.PriorityQueue()  # setting up the priority queue for holding states and their costs
    if problem.isGoalState(problem.getStartState()):  # base case of goal state matching start state
        return []
    states_visited = []  # defining a list to avoid expanding states that have been expanded
    final_path = []  # defining a list to be returned at the end of the function
    current_state = problem.getStartState()  # initializing current state
    current_path = util.PriorityQueue()  # defining a priority queue holding actions with their costs

    while not problem.isGoalState(current_state):  # while we have not reached the goal
        if current_state not in states_visited:  # if we have not already visited the current state (loc + direction)
            states_visited.append(current_state)  # add current state to visited states
            successors = problem.getSuccessors(current_state)
            for successor in successors:
                partial_path = final_path + [successor[1]]  # successor[1] is the possible action in this state
                remaining_cost = problem.getCostOfActions(partial_path)  # used as priority value for fringe/path
                if successor[0] not in states_visited:  # if the child has not been visited
                    fringe.push(successor[0], remaining_cost)  # successor[0] is the next state
                    current_path.push(partial_path, remaining_cost)  # adding expansion of current state to path
        current_state = fringe.pop()  # setting current state to expand the next viable successor
        final_path = current_path.pop()  # adding path to current state to our final return path
    return final_path
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"  # A* search is identical to UCS, except added cost checking based on heuristic
    fringe = util.PriorityQueue()  # setting up the priority queue for holding states and their costs
    if problem.isGoalState(problem.getStartState()):  # base case of goal state matching start state
        return []
    states_visited = []  # defining a list to avoid expanding states that have been expanded
    final_path = []  # defining a list to be returned at the end of the function
    current_state = problem.getStartState()  # initializing current state
    current_path = util.PriorityQueue()  # defining a priority queue holding actions with their costs

    while not problem.isGoalState(current_state):  # while we have not reached the goal
        if current_state not in states_visited:  # if we have not already visited the current state (loc + direction)
            states_visited.append(current_state)  # add current state to visited states
            successors = problem.getSuccessors(current_state)
            for successor in successors:
                partial_path = final_path + [successor[1]]  # successor[1] is the possible action in this state
                remaining_cost = problem.getCostOfActions(partial_path) + heuristic(successor[0], problem)
                if successor[0] not in states_visited:  # if the child has not been visited
                    fringe.push(successor[0], remaining_cost)  # successor[0] is the next state
                    current_path.push(partial_path, remaining_cost)  # adding expansion of current state to path
        current_state = fringe.pop()  # setting current state to expand the next viable successor
        final_path = current_path.pop()  # adding path to current state to our final return path
    return final_path
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
