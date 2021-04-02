def lcs(M, N, a, b): 
    if a == 0 or b == 0: 
       return 0; 
    elif M[a-1] == N[b-1]: 
       return 1 + lcs(M, N, a-1, b-1); 
    else: 
       return max(lcs(M, N, a, b-1), lcs(M, N, a-1, b)); 
M = "PMMTPB"
N = "MXTXPYB"
print ("Length of LCS is ", lcs(M , N, len(M), len(N)))
