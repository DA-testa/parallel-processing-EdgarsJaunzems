# python3

def parallel_processing(n, m, data):
    output = [] 
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs     
    trd = [(0, k) for k in range(n)] 
    for t in range (m):
        d = data[t]
        mini = min(trd)[1]  
        output.append((mini, trd[mini][0]))   
        trd[mini] = (trd[mini][0] + d, mini) 
        
    return output 

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m = map(int, input().split())

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
