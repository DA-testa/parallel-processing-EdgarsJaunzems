# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    laiks = 0
    s = 0
    k = 0
    lar = []
    
    for job in range(m):
        output.append((k, laiks))
        lar.append(laiks)
        k += 1
        if len(lar) >= n:
            if len(lar) > n:
                s += 1
            laiks = lar[len(lar)-n] + runtimes[s]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n = map(int, input().split())
    m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = (list(map(int, input().split())))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for r1, r2 in result:
        print(r1,r2)



if __name__ == "__main__":
    main()
