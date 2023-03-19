# python3

def parallel_processing(n, m, data):
    output = [] 
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs     
    thread = [(0, k) for k in range(n)] 
    for t in range (m):
        tsk = data[t]
        nxt = min(thread)[1]  
        output.append((nxt, thread[nxt][0]))   
        thread[nxt] = (thread[nxt][0] + tsk, nxt) 
        
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
