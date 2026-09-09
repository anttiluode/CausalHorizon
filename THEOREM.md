# Finite-event resolvent theorem

## Setup

Let \(A_0,\dots,A_{T-1}\in\mathbb C^{n\times n}\), with
\[
\Phi(b,a)=A_{b-1}\cdots A_a,\qquad \Phi(a,a)=I.
\]

At ordered event times
\[
0\le\tau_1<\cdots<\tau_m\le T-1,
\]
replace
\[
A_{\tau_i}\mapsto A_{\tau_i}+U_iM_iV_i^*,
\]
where \(U_i,V_i\in\mathbb C^{n\times r_i}\) and \(M_i\in\mathbb C^{r_i\times r_i}\).

Define
\[
L_i=\Phi(T,\tau_i+1),\qquad R_i=\Phi(\tau_i,0),
\]
and for \(j>i\),
\[
\Omega_{ji}=V_j^*\Phi(\tau_j,\tau_i+1)U_i,
\]
with \(\Omega_{ji}=0\) for \(j\le i\).

Let
\[
P=[L_1U_1\;\cdots\;L_mU_m],
\]
\[
Q=\begin{bmatrix}V_1^*R_1\\ \vdots\\ V_m^*R_m\end{bmatrix},
\qquad
M=\operatorname{diag}(M_1,\ldots,M_m).
\]

## Theorem

\[
\boxed{\widetilde\Phi(T,0)-\Phi(T,0)=PM(I-\Omega M)^{-1}Q.}
\]

Since \(\Omega M\) is strictly block-lower triangular,
\[
(\Omega M)^m=0
\]
and
\[
(I-\Omega M)^{-1}=\sum_{k=0}^{m-1}(\Omega M)^k.
\]

No norm, invertibility of the baseline factors, stability, smallness, or convergence assumption is required.

## Proof

Expand the modified product multilinearly.

For a nonempty ordered subset
\[
i_1<i_2<\cdots<i_k,
\]
the corresponding term is
\[
L_{i_k}U_{i_k}M_{i_k}
V_{i_k}^*\Phi(\tau_{i_k},\tau_{i_{k-1}}+1)U_{i_{k-1}}M_{i_{k-1}}
\cdots
V_{i_2}^*\Phi(\tau_{i_2},\tau_{i_1}+1)U_{i_1}M_{i_1}V_{i_1}^*R_{i_1}.
\]

Using the definition of \(\Omega\), this becomes
\[
L_{i_k}U_{i_k}M_{i_k}
\Omega_{i_ki_{k-1}}M_{i_{k-1}}
\cdots
\Omega_{i_2i_1}M_{i_1}V_{i_1}^*R_{i_1}.
\]

The block product
\[
PM(\Omega M)^{k-1}Q
\]
is exactly the sum of all terms containing \(k\) selected events.

Therefore
\[
\widetilde\Phi-\Phi
=
\sum_{k=1}^{m}PM(\Omega M)^{k-1}Q.
\]

Nilpotence gives the resolvent form. QED.

## Corollary: rank bound

\[
\operatorname{rank}(\widetilde\Phi-\Phi)\le\sum_i r_i.
\]

## Corollary: exact pair interaction

For \(i<j\),
\[
\mathcal I_{j\leftarrow i}
=
L_jU_jM_j\Omega_{ji}M_iV_i^*R_i.
\]

Hence \(\Omega_{ji}=0\) implies exact finite-strength additivity.

## Corollary: observer projection

For compatible input/readout matrices \(B,C\),
\[
C(\widetilde\Phi-\Phi)B=(CP)M(I-\Omega M)^{-1}(QB).
\]

## Corollary: algebraic interaction horizon

Scale every \(M_i\) by a formal scalar \(z\):
\[
\Delta Y(z)=\sum_{k=1}^{m}z^kK_k,
\qquad
K_k=CPM(\Omega M)^{k-1}QB.
\]

Define
\[
d_{B,C}=\max\{k:K_k\ne0\},
\]
or \(0\) if all \(K_k=0\).

Then all interaction orders greater than \(d_{B,C}\) are exactly invisible to that observer.
