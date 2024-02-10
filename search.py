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
Pacman agents (in search_agents.py).
"""

from builtins import object
import util
STATE = 0
ACTION = 1
COST = 2

def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depth_first_search(problem):
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    # What does this function need to return?
    #     list of actions that reaches the goal
    # 
    # What data is available?
    #     start_state = problem.get_start_state() # returns a string
    # 
    #     problem.is_goal_state(start_state) # returns boolean
    # 
    #     transitions = problem.get_successors(start_state)
    #     transitions[0].state
    #     transitions[0].action
    #     transitions[0].cost
    # 
    #     print(transitions) # would look like the list-of-lists on the next line
    #     [
    #         [ "B", "0:A->B", 1.0, ],
    #         [ "C", "1:A->C", 2.0, ],
    #         [ "D", "2:A->D", 4.0, ],
    #     ]
    # 
    #Example:
    ##use priority PriorityQueue to take lowest cost
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    # start_state = problem.get_start_state() #state, rev
    # # if problem.is_goal_state(start_state):
    # #     return [start_state]
    # frontier = util.Stack()
    # frontier.push((start_state, []))
    # explored = set()
    # explored.add(start_state)
    # while not frontier.is_empty():
    #     node = frontier.pop()
    #     if problem.is_goal_state(node[STATE]):
    #         return node[ACTION]
        
    #     for child in problem.get_successors(node[STATE]):
    #         if child[STATE] not in explored:
    #             explored.add(child[STATE])
    #             frontier.push((child[STATE],node[ACTION] + [child[ACTION]]))
                
    #             print((child[STATE],node[ACTION] + [child[ACTION]]))

    # print(transitions)
    stack = util.Stack()
    visited = set()
    if problem.is_goal_state(problem.get_start_state()):
        return []
    stack.push((problem.get_start_state(),[]))
    while not stack.is_empty():
        position, path = stack.pop()
        visited.add(position)
        if problem.is_goal_state(position):
            return path
        for node in problem.get_successors(position):
            newposition = node[0]
            state = node[1]
            if newposition not in visited:
                stack.push((newposition, path + [state]))
    
    
    util.raise_not_defined()


def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    start_state = problem.get_start_state() #state, rev
    if problem.is_goal_state(start_state):
        return [start_state]
    frontier = util.Queue()
    frontier.push((start_state, []))
    explored = set()
    explored.add(start_state)
    while not frontier.is_empty():
        node = frontier.pop()
        if problem.is_goal_state(node[STATE]):
            return node[ACTION]
        
        for child in problem.get_successors(node[STATE]):
            if child[STATE] not in explored:
                explored.add(child[STATE])
                frontier.push((child[STATE],node[ACTION] + [child[ACTION]]))
       


def uniform_cost_search(problem, heuristic=None):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    start_state = problem.get_start_state() #state, rev
    if problem.is_goal_state(start_state):
        return [start_state]
    frontier = util.PriorityQueue()
    frontier.push((start_state, []), 0)
    explored = {}
    explored[start_state] = (0, []) #(cost, path)
    while not frontier.is_empty():
        node = frontier.pop()
        if problem.is_goal_state(node[STATE]):
            return node[ACTION]
       
        for child in problem.get_successors(node[STATE]):
            newcost = explored[node[STATE]][0] + child[COST] # get the cost to the current node plus the child cost to get path to that node
            if child[STATE] not in explored or newcost < explored[child[STATE]][0]:
                explored[child[STATE]] = (newcost, node[ACTION] + [child[ACTION]])
                frontier.update((child[STATE],node[ACTION] + [child[ACTION]]), newcost)
    util.raise_not_defined()
    


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# What does this function need to return?
    #     list of actions that reaches the goal
    # 
    # What data is available?
    #     start_state = problem.get_start_state() # returns a string
    # 
    #     problem.is_goal_state(start_state) # returns boolean
    # 
    #     transitions = problem.get_successors(start_state)
    #     transitions[0].state
    #     transitions[0].action
    #     transitions[0].cost
    # 
    #     print(transitions) # would look like the list-of-lists on the next line
    #     [
    #         [ "B", "0:A->B", 1.0, ],
    #         [ "C", "1:A->C", 2.0, ],
    #         [ "D", "2:A->D", 4.0, ],
    #     ]
    # 
    # Example:
    #     start_state = problem.get_start_state()
    #     transitions = problem.get_successors(start_state)
    #     return [  transitions[0].action  ]
def a_star_search(problem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    ## the heuerstic shoud only be used to determine which is next in priorirty
    ## only add the actual path to the oath cost 
    start_state = problem.get_start_state() #state, rev
    if problem.is_goal_state(start_state):
        return [start_state]
    frontier = util.PriorityQueue()
    frontier.push(start_state, heuristic(start_state, problem)) # state, cost
    explored = {}
    explored[start_state] = (heuristic(start_state, problem), [])  # state -> cost
    while not frontier.is_empty():
        node = frontier.pop()
        currentstate = node
        currentpathcost, currentpath = explored[currentstate][0], explored[currentstate][1]
        
        if problem.is_goal_state(currentstate):
            return currentpath
       
        for child in problem.get_successors(currentstate):
            childstate, childaction, childcost = child[0], child[1], child[2]
            newpathcost = currentpathcost + childcost ##+ heuristic(childstate, problem)
            if childstate not in explored or newpathcost < explored[childstate][0]: 
                # explored[childstate][0] should be the current tracked cost
                explored[childstate] = (newpathcost, currentpath + [childaction])
                frontier.update(childstate, newpathcost + heuristic(childstate, problem))
            
            
    
    util.raise_not_defined()

# (you can ignore this, although it might be helpful to know about)
# This is effectively an abstract class
# it should give you an idea of what methods will be available on problem-objects
class SearchProblem(object):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, step_cost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'step_cost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()

# fallback on a_star_search
for function in [breadth_first_search, depth_first_search, uniform_cost_search, ]:
    try: function(None)
    except util.NotDefined as error: exec(f"{function.__name__} = a_star_search", globals(), globals())
    except: pass

# Abbreviations
bfs   = breadth_first_search
dfs   = depth_first_search
astar = a_star_search
ucs   = uniform_cost_search