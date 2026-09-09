#!/usr/bin/env python3
import numpy as np

def segment(A, b, a):
    n=A[0].shape[0]
    out=np.eye(n,dtype=np.result_type(*A))
    for t in range(a,b):
        out=A[t]@out
    return out

def explicit_modified_product(A, events):
    mats=[x.copy() for x in A]
    for e in events:
        mats[e["tau"]]=mats[e["tau"]]+e["U"]@e["M"]@e["V"].conj().T
    return segment(mats,len(mats),0)

def event_formula(A, events):
    events=sorted(events,key=lambda e:e["tau"])
    T=len(A); n=A[0].shape[0]
    rs=[e["M"].shape[0] for e in events]
    off=np.cumsum([0]+rs); rtot=off[-1]
    dtype=np.result_type(*A,*(e["U"] for e in events),*(e["M"] for e in events))
    P=np.zeros((n,rtot),dtype=dtype)
    Q=np.zeros((rtot,n),dtype=dtype)
    M=np.zeros((rtot,rtot),dtype=dtype)
    O=np.zeros((rtot,rtot),dtype=dtype)
    for i,e in enumerate(events):
        s=slice(off[i],off[i+1])
        P[:,s]=segment(A,T,e["tau"]+1)@e["U"]
        Q[s,:]=e["V"].conj().T@segment(A,e["tau"],0)
        M[s,s]=e["M"]
    for j,ej in enumerate(events):
        sj=slice(off[j],off[j+1])
        for i in range(j):
            ei=events[i]; si=slice(off[i],off[i+1])
            O[sj,si]=ej["V"].conj().T@segment(A,ej["tau"],ei["tau"]+1)@ei["U"]
    base=segment(A,T,0)
    delta=P@M@np.linalg.inv(np.eye(rtot,dtype=dtype)-O@M)@Q
    return base+delta, {"delta":delta,"Omega":O,"M":M}

def random_case(seed=0, n=17, T=11, times=(1,4,7,9), ranks=(1,3,2,4), complex_=False):
    rng=np.random.default_rng(seed)
    def rnd(shape):
        x=rng.normal(size=shape)
        if complex_: x=x+1j*rng.normal(size=shape)
        return x/np.sqrt(max(shape))
    A=[rnd((n,n)) for _ in range(T)]
    ev=[]
    for tau,r in zip(times,ranks):
        ev.append({"tau":tau,"U":rnd((n,r)),"M":rnd((r,r)),"V":rnd((n,r))})
    return A,ev

if __name__=="__main__":
    worst=0.0
    for complex_ in (False,True):
        for seed in range(100):
            A,e=random_case(seed=seed,complex_=complex_)
            direct=explicit_modified_product(A,e)
            reduced,info=event_formula(A,e)
            rel=np.linalg.norm(direct-reduced)/max(np.linalg.norm(direct),1e-15)
            worst=max(worst,float(rel))
            assert rel<5e-10
            assert np.linalg.norm(np.linalg.matrix_power(info["Omega"]@info["M"],len(e)))<1e-10
    print(f"verified 200 random dense cases; worst relative error = {worst:.3e}")
