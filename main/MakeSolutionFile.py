def make_solution_file(solves, total_profit):
    wf = open('docs/solution.txt', 'w')
    wf.write('Total Profit\n')
    wf.write(str(total_profit))
    count = 0
    for i in solves:
        count += 1
        wf.write('\nRoute %d\n' %count)
        c = 0
        for j in i:
            c += 1
            wf.write(str(j))
            if j != 0 or c == 1:
                wf.write(' ')
 