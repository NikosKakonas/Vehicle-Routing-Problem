class Node:
    def __init__(self, idd, xx, yy, dem = 0, st = 0, profit = 0):
        self.x = xx
        self.y = yy
        self.id = idd
        self.isRouted = False
        self.st = st
        self.demand = dem
        self.profit = profit

def load_model(file_name):
    all_nodes = []
    all_lines = list(open(file_name, "r"))

    line_counter = 0
    ln = all_lines[line_counter]
    no_spaces = ln.split(sep='\t')
    vehicles = int(no_spaces[1])

    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = ln.split(sep='\t')
    capacity = int(no_spaces[1])

    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = ln.split(sep='\t')
    time_limit = int(no_spaces[1])

    line_counter += 3
    ln = all_lines[line_counter]

    no_spaces = ln.split(sep='\t')
    x = float(no_spaces[1])
    y = float(no_spaces[2])
    depot = Node(0, x, y)
    all_nodes.append(depot)

    line_counter += 2
    ln = all_lines[line_counter]
    no_spaces = ln.split(sep='\t')
    tot_customers = int(no_spaces[1])

    line_counter += 4

    for i in range(tot_customers):
        ln = all_lines[line_counter]
        no_spaces = ln.split(sep='\t')
        idd = int(no_spaces[0])
        x = float(no_spaces[1])
        y = float(no_spaces[2])
        demand = int(no_spaces[3])
        st = int(no_spaces[4])
        profit = int(no_spaces[5])
        customer = Node(idd, x, y, demand, st, profit)
        all_nodes.append(customer)
        line_counter += 1

    return all_nodes, vehicles, capacity, time_limit