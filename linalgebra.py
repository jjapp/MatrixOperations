'''Functions for working with matrices.'''

def vector_addition(v1, v2):
    '''(list, list)->list

    Adds two column vectors and returns a column vector
    as a list of float.

    >>>vector_addition([1,3,5],[3,6,7])
    [4,9,12]

    '''

    result=[]
    for i in range(0, len(v1)):
        new_value=v1[i]+v2[i]
        result.append(new_value)
    return result

def scalar_multiple(c, u):
    '''(number, list)->list

    Returns the scalar multiple of u where c is a real number
    and u is a vector.

    >>>scalar_multiple(3,[2,5,7])
    [6,15,21]

    '''

    result=[]
    for i in range(0,len(u)):
        new_value=c*u[i]
        result.append(new_value)
    return result

def vector_sum(vectors):
    '''(list)->list
    Takes a list of vectors and returns a single vector that is the
    sum of all vectors in the list.

    >>>vector_sum([[1,2],[3,5],[2,4]])
    [6,11]
    '''
    result=[]
    for i in range(len(vectors[0])):
        result.append(sum(row[i] for row in vectors))

    return result

            

def product_Ax(A, x):
    '''(Object, list)->list

    Returns the product of A and x where Ax is the linear
    combination of the columns of A using the corresponding
    entries in x as weights.  A is an m x n matrix and x is a vector.

    >>>product_Ax([[1,0],[2,-5],[-1,3]],[4,3,7])
    [3,6]
    
    '''
    
    result=[]
    sum_of_result=[]
    for i in range(0, len(x)):
        new_vector=scalar_multiple(x[i],A[i])
        result.append(new_vector)
    sum_of_result=vector_sum(result)
    return sum_of_result
        


            

    
