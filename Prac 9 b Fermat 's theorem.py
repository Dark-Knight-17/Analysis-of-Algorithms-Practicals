def testSomeNumbers(limit, n) : 
    if (n < 3): 
        return
    for a in range(1, limit + 1): 
        for b in range(a, limit + 1): 
            pow_sum = pow(a, n) + pow(b, n) 
            c = pow(pow_sum, 1.0 / n)
            c_pow = pow(int(c), n)  
            if (c_pow == pow_sum): 
                print("Count example found") 
                return
    print("No counter example within given range and data") 
testSomeNumbers(3, 4) 
