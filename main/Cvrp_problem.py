import Model
import MakeSolutionFile
import math
import time

def distance(from_node, to_node):
    dx = from_node.x - to_node.x
    dy = from_node.y - to_node.y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return dist


def find_routs(best_ratios, node, time_remaining, capacity_remaining, test_solve, prev, visited):
    global all_nodes, population, count, complexity, layer, N, flag
    visited.append(node)
    identity = return_all_ratio(N, node, time_remaining, capacity_remaining)
    best_ratios = find_best_ratios(identity)
    c = -1
    for ratio in best_ratios:
        c += 1
        if flag is False:
            prev = node
        node = identity[ratio]
        test_solve.append(node)
        time_remaining = time_remaining - all_nodes[node].st - distance(all_nodes[prev], all_nodes[node])
        capacity_remaining -= all_nodes[node].demand
        if node not in visited:
            flag = False
            find_routs(best_ratios, node, time_remaining, capacity_remaining, test_solve, prev, visited)
            time_remaining = time_remaining + all_nodes[node].st + distance(all_nodes[prev], all_nodes[node])
            capacity_remaining += all_nodes[node].demand
            new_solve = []
            for i in test_solve:
                new_solve.append(i)
            population.append(new_solve)
            test_solve.pop()
            visited.pop()
            flag = True


def return_all_ratio(N, node, time_remaining, capacity_remaining):
    all_ratio = []
    identity = {}
    for i in N:
        if i not in visited:
            ratio = all_nodes[i].profit / (distance(all_nodes[node], all_nodes[i]) + all_nodes[i].st)
            return_time = distance(all_nodes[i], all_nodes[0])
            time = all_nodes[i].st + distance(all_nodes[node], all_nodes[i]) + return_time
            if time <= time_remaining and all_nodes[i].demand <= capacity_remaining:
                all_ratio.append(ratio)
                if ratio not in identity:
                    identity[ratio] = all_nodes[i].id
    return identity


def find_best_ratios(identity):
    best_ratios = []
    identity_list = sorted(identity, reverse=True)
    c = -1
    for j in identity_list:
        c += 1
        if c < complexity:
            best_ratios.append(j)
        else:
            break
    return best_ratios


def check_if_new_route_is_possible(test_solve):
    global VEHICLES, CAPACITY, TIME_LIMIT, all_nodes
    time_remaining = TIME_LIMIT
    capacity_remaining = CAPACITY
    prev = 0
    count = 0
    for node in test_solve:
        return_time = distance(all_nodes[node], all_nodes[0])
        time = distance(all_nodes[prev], all_nodes[node]) + all_nodes[node].st + return_time
        if time <= time_remaining and all_nodes[node].demand <= capacity_remaining:
            count += 1
            time_remaining = time_remaining - distance(all_nodes[prev], all_nodes[node]) - all_nodes[node].st
            capacity_remaining -= all_nodes[node].demand
        prev = node
    if count == len(test_solve):
        return True
    else:
        return False


if __name__ == '__main__':
    
    global all_nodes, VEHICLES, CAPACITY, TIME_LIMIT, complexity, N

    print('Average running time: 38 sec')
    print('Please wait...')
    start_time = time.time()
    N = [i for i in range(337)]
    flag = False
    complexity = 3
    all_nodes, VEHICLES, CAPACITY, TIME_LIMIT = Model.load_model('docs/Instance.txt')
    visited = []
    all_visited = []
    profit = []
    total_profit = 0
    solves = []
    for o in range(1, 7):
        time_remaining = TIME_LIMIT
        capacity_remaining = CAPACITY
        count = 0
        layer = 0
        last_node = -1  
        population = []
        test_solve = []
        find_routs([], 0, time_remaining, capacity_remaining, test_solve, 0, visited)
        last = population.pop()
        population.append(last)
        all_profit = []
        solve = []
        maxi = -1
        count  = -1
        for p in population:
            count += 1
            profit = 0
            possible = check_if_new_route_is_possible(p)
            if possible:
                for node in p:
                    profit += all_nodes[node].profit
                all_profit.append(profit)
                if profit > maxi:
                    maxi = profit
                    max_pos = count
        solve.append(0)
        visited = []
        for node in population[max_pos]:
            solve.append(node)
            all_visited.append(node)
        for i in all_visited:
            visited.append(i)
        solve.append(0)
        solves.append(solve)
        total_profit += max(all_profit)

    MakeSolutionFile.make_solution_file(solves, total_profit)

    end_time = time.time()

    print()
    print('Running time:', end_time - start_time)
    print('Total profit:', total_profit)
    print('Please check the routes in solution.txt file!')
    print()