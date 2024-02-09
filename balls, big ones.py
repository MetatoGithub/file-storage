def vec(A,B):
    X=B[0]-A[0]
    Y=B[1]-A[1]
    L=[X,Y]
    return(L)

def pscal(U,V):
    PS=U[0]*U[1]+V[0]*V[1]
    return(PS)

def rec(A,B,C):
    L=vec(A,B)
    Lprm=vec(A,C)
    if pscal(L,Lprm)==0:
        p=True
        return(p)
    else:
        p=False
        return(p)
    return(p)

def TRec(A,B,C):
    rec(A,B,C)
    if p==True:
        return('ABC est rectangle en A')
    else:
        rec(B,C,A)
        if p==True:
            return('ABC est rectangle en B')
        else:
            rec(C,A,B)
            if p==True:
                return('ABC est rectangle en C')
            else:
                return("ABC n'est pas rectangle")
    

