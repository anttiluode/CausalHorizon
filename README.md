# CausalHorizon

**Exact finite-rank event interactions in time-ordered linear propagators, and the interaction depth visible to a bounded observer.**

> Status: candidate mathematics note. The algebra and numerical checks are exact. **Novelty/priority is not claimed.**

## Core identity

Let
\[
x_{t+1}=A_t x_t,\qquad \Phi(b,a)=A_{b-1}\cdots A_a.
\]

At ordered times \(\tau_1<\cdots<\tau_m\), replace
\[
A_{\tau_i}\mapsto A_{\tau_i}+U_iM_iV_i^*.
\]

Define
\[
\Omega_{ji}=V_j^*\Phi(\tau_j,\tau_i+1)U_i\quad (j>i),
\]
and zero otherwise. Stack
\[
P=[\Phi(T,\tau_1+1)U_1\;\cdots\;\Phi(T,\tau_m+1)U_m],
\]
\[
Q=\begin{bmatrix}
V_1^*\Phi(\tau_1,0)\\
\vdots\\
V_m^*\Phi(\tau_m,0)
\end{bmatrix},
\qquad
M=\operatorname{diag}(M_1,\ldots,M_m).
\]

Then
\[
\boxed{
\widetilde\Phi(T,0)-\Phi(T,0)=PM(I-\Omega M)^{-1}Q.
}
\]

Because \(\Omega M\) is strictly block-lower triangular,
\[
(\Omega M)^m=0,
\]
so the inverse is a finite polynomial. No small-update, convergence, stability, or commutativity assumption is needed.

## Corollaries

### Exact rank bound
\[
\operatorname{rank}(\widetilde\Phi-\Phi)\le \sum_i r_i.
\]

### Exact two-event interference
For \(i<j\), the non-additive cross term is
\[
\mathcal I_{j\leftarrow i}
=
L_jU_jM_j
\underbrace{V_j^*\Phi(\tau_j,\tau_i+1)U_i}_{\Omega_{ji}}
M_iV_i^*R_i.
\]

Thus \(\Omega_{ji}=0\) implies exact finite-strength additivity. We provisionally call this **causal orthogonality**.

### Observer projection
With input map \(B\) and readout \(C\),
\[
\boxed{
C(\widetilde\Phi-\Phi)B=(CP)M(I-\Omega M)^{-1}(QB).
}
\]

This separates:
- `QB`: how a question reaches event space,
- `(I-Omega M)^-1`: how event edits interact internally,
- `CP`: how consequences reach the observer.

### Observer-bank coverage

For a linear family of admissible query directions `U`, define the reachable
event-entry space
\[
\mathcal E=Q\mathcal U.
\]
If remembered queries `b_1,...,b_s` satisfy
\[
\operatorname{span}\{Qb_1,\ldots,Qb_s\}=\mathcal E,
\]
then exact preservation on that bank implies exact preservation for **every**
query in `U` under the same event update and readout.

So a bounded bank earns the right to represent a capability by spanning its
**projected event-entry space**, not by merely containing many examples or the
currently most vulnerable examples. The exact coverage dimension is
\[
\dim(Q\mathcal U).
\]
Full rank is not enough under noise: conditioning controls how bank tolerances
amplify to unseen queries. See [`COVERAGE.md`](COVERAGE.md).

### Algebraic interaction horizon
Scale all event matrices by \(z\):
\[
\Delta Y(z)=z\,CPM(I-z\Omega M)^{-1}QB
=\sum_{k=1}^{m} z^k K_k,
\]
where
\[
K_k=CPM(\Omega M)^{k-1}QB.
\]

Define
\[
d_{B,C}=\max\{k:K_k\ne 0\}.
\]

This is the largest interaction order visible to that input/readout geometry. It is an **exact algebraic horizon**, distinct from a metric/resolution horizon where deeper effects are merely too small to resolve.

## Why this repo exists

The theorem was motivated by `AnttisBrain2`, `SighImageSuper`, `GeometricNeuronV24`, `Operaattori`, `OperaattoriJako`, `Kompressori`, `JelloBrain`, and `IttnasNoruen`.

Those repos are motivation only. The theorem here is a standalone finite-dimensional linear algebra statement.

The strongest immediate empirical handoff to `Kompressori` is to replace static patch-overlap metrics with the directed propagated overlap
\[
\boxed{\Omega_{ji}=V_j^*\Phi_{j\leftarrow i}U_i}
\]
and test whether it predicts finite non-additivity better than physical distance or static subspace overlap.

The strongest handoff to `IttnasNoruen` is different: current-interference replay asks which stored cues this proposal hurts most, whereas the coverage corollary asks which measured cue signatures span the future-response directions the capability can use. Gate 9's null result therefore does not contradict the theorem; it motivates a different selector.

## Files

- `THEOREM.md` — statement, proof, and corollaries
- `COVERAGE.md` — exact observer-bank sufficiency and conditioning
- `PRIOR_ART.md` — novelty fence and closest known neighborhoods
- `verify.py` — random dense numerical verification
- `tests/test_identity.py` — event-resolvent tests
- `tests/test_coverage.py` — coverage / missing-direction / conditioning tests
- `paper/main.tex` — short paper draft

## Verification

The initial verifier checked 200 random dense real/complex systems with mixed event ranks. Worst relative error between the direct modified product and the event-space formula was `2.686e-15`.

Run:

```bash
python -m pip install -r requirements.txt
python verify.py
python -m unittest discover -s tests -v
```

## Claim discipline

Established here:
- exact finite-event identity,
- finite event-path expansion,
- rank bound,
- exact pair-interaction term,
- observer projection,
- algebraic interaction horizon,
- exact bank-sufficiency corollary in the linear event-space setting,
- numerical verification.

Not established:
- historical priority,
- general nonlinear applicability,
- a brain or fluid mechanism,
- that Kompressori's nonlinear field must obey this factorization,
- that IttnasNoruen's tanh classifier exposes the exact hidden `Q` required by the coverage theorem.
