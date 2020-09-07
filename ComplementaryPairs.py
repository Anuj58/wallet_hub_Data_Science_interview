from itertools import combinations 
  
def findPairsWithSumK(lst, K): 
    #removing the duplicate columns
    # lst=set(lst)
    return [pair for pair in combinations(lst, 2) if sum(pair) == K] 
      
print ("Test Case 1")
lst = [2, 5, 3, 8, 7] 
K = 10
print (K,"-complementary pairs in ",lst,":",findPairsWithSumK(lst, K) )
print ("\nTest Case 2")
lst = [1, 5, 3, 2, 4] 
K = 6
print (K,"-complementary pairs in ",lst,":",findPairsWithSumK(lst, K) )
print ("\nTest Case 3")
lst = [15, 10,8, 3, 9, 9] 
K = 18
print (K,"-complementary pairs in ",lst,":",findPairsWithSumK(lst, K) )
print ("\nTest Case 4")
lst = [1, 5, 3, 7, 9] 
K = 8
print (K,"-complementary pairs in ",lst,":",findPairsWithSumK(lst, K) )
print ("\nTest Case 5")
lst = [11, -1, 1, 7, 9] 
K = 10
print (K,"-complementary pairs in ",lst,":",findPairsWithSumK(lst, K) )
print ("\nTest Case 6")
lst = [1, 5, 3, 2, 4,1] 
K = 6
print (K,"-complementary pairs in ",lst,":",findPairsWithSumK(lst, K) )