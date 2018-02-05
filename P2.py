#Cheryl Zogg HW3 - Problem 2

class Node:
    """base class"""
    def __init__(self, name, cost, utility):
        """
        :param name: name of this node
        :param cost: cost of this node
        :param utility: utility of this node
        """
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):
    def __init__(self, name, cost, utility, future_nodes, probs):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of future nodes
        """
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):
        """
        :return: expected utility of this chance node
        """
        exp_utility = self.utility
        i = 0
        for node in self.futureNodes:
            exp_utility += self.probs[i]*node.get_expected_utility()
            i += 1
        return exp_utility


class TerminalNode(Node):
    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        return self.cost

    def get_expected_utility(self):
        return self.utility


class DecisionNode(Node):
    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()
        return outcomes

    def get_expected_utility(self):
        """returns the expected utility of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_utility()
        return outcomes


#######################
#create the terminal nodes
T1 = TerminalNode(name='T1', cost=10, utility=0.9)
T2 = TerminalNode(name='T2', cost=20, utility=0.8)
T3 = TerminalNode(name='T3', cost=30, utility=0.7)
T4 = TerminalNode(name='T4', cost=40, utility=0.6)
T5 = TerminalNode(name='T5', cost=50, utility=0.5)

#create the chance nodes
C2 = ChanceNode(name='C2', cost=35, utility=0, future_nodes=[T1,T2], probs=[0.7,0.3])

C1 = ChanceNode(name='C1', cost=25, utility=0, future_nodes=[C2,T3], probs=[0.2,0.8])
C3 = ChanceNode(name='C3', cost=45, utility=0, future_nodes=[T4,T5], probs=[0.1,0.9])

#create the decision node
D1 = DecisionNode(name='D1', cost=0, utility=0, future_nodes=[C1,C3])

#print the expect cost and utility of C1 and C3
print(D1.get_expected_costs(), D1.get_expected_utility())