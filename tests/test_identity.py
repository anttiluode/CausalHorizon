import unittest, numpy as np, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import verify

class IdentityTests(unittest.TestCase):
    def test_real_and_complex(self):
        for complex_ in (False,True):
            for seed in range(10):
                A,e=verify.random_case(seed=seed,complex_=complex_)
                direct=verify.explicit_modified_product(A,e)
                reduced,_=verify.event_formula(A,e)
                self.assertLess(np.linalg.norm(direct-reduced),1e-9)

    def test_causal_orthogonality(self):
        n=T=4
        A=[np.eye(n) for _ in range(T)]
        u1=np.array([[1.],[0.],[0.],[0.]])
        v1=u1.copy()
        u2=np.array([[0.],[1.],[0.],[0.]])
        v2=u2.copy()
        e1={"tau":1,"U":u1,"M":np.array([[2.3]]),"V":v1}
        e2={"tau":2,"U":u2,"M":np.array([[-4.7]]),"V":v2}
        base=verify.segment(A,T,0)
        both=verify.explicit_modified_product(A,[e1,e2])-base
        separate=(verify.explicit_modified_product(A,[e1])-base)+(verify.explicit_modified_product(A,[e2])-base)
        self.assertTrue(np.allclose(both,separate))

if __name__=="__main__":
    unittest.main()
