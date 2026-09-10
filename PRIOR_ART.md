# Prior-art fence

**Do not claim historical priority.** A September-2026 literature attack substantially narrows the claim.

The core identity remains exact and useful as a compact derivation for time-ordered finite-rank edits, but the broad idea

> local low-rank events interact through propagated couplings in a small event-space resolvent

is established territory in several neighboring fields.

## Strongest neighborhoods

1. **Dyson / Peano-Baker expansions** — ordered interaction expansions of time-varying linear evolution.
2. **Path-sum methods** — exact graph/path resummations of matrix functions and time-ordered exponentials.
   - P.-L. Giscard, S. J. Thwaite, D. Jaksch, *Evaluating Matrix Functions by Resummations on Graphs: The Method of Path-Sums*, SIAM J. Matrix Anal. Appl. (2013), arXiv:1112.1588.
   - P.-L. Giscard et al., *An Exact Formulation of the Time-Ordered Exponential using Path-Sums*, J. Math. Phys. 56, 053503 (2015), arXiv:1410.6637.
3. **Impulsive linear systems** — state-transition products with discrete jump maps.
4. **Sherman-Morrison-Woodbury / finite-rank perturbation theory** — low-dimensional factorizations and inverses.
5. **Controllability / observability** — dependence of accessible behavior on input and readout maps.
6. **Foldy-Lax / T-matrix multiple scattering** — local scatterers are coupled by Green-function propagation and solved through a finite interaction matrix. This is structurally very close to an event-space resolvent. Examples include:
   - K. Green & K. Lumme, *Multiple scattering by the iterative Foldy-Lax scheme*, JOSA A 22, 1555–1558 (2005), doi:10.1364/JOSAA.22.001555.
   - generalized Foldy-Lax formulations in which free-space Green functions propagate between scatterers and the mutual interactions are solved as a coupled linear system.
7. **Localized-defect Green-function updates and multiple-scattering epistasis.** Dutta et al., *Green function of correlated genes in a minimal mechanical model of protein evolution*, PNAS 115, E4559–E4568 (2018), doi:10.1073/pnas.1716215115, is particularly close in architecture. A local mutation gives a small-rank defect Hamiltonian; the Green-function update is evaluated with Woodbury; and two-mutation nonadditivity is written as a sum over multiple-scattering paths containing both defects.

## What this kills

Do **not** use CausalHorizon to claim discovery of any of the following:

- that local low-rank perturbations produce low-dimensional response updates;
- that multiple local perturbations interact through propagated Green-function couplings;
- that a finite interaction matrix/resolvent can resum those couplings;
- that two localized edits can have non-additive effects through paths visiting both edits;
- that observer/source projections can make only part of a propagator relevant.

Those ideas have strong prior art in finite-rank perturbation theory, multiple scattering, Green-function defect theory, and control.

## What remains mathematically specific here

The exact package in this repo is still a clean special case worth retaining:

\[
\widetilde\Phi-\Phi=PM(I-\Omega M)^{-1}Q,
\]

for finite-rank edits to **distinct ordered factors of a discrete time-varying propagator**, with

\[
\Omega_{ji}=V_j^*\Phi(\tau_j,\tau_i+1)U_i,\qquad j>i,
\]

and zero otherwise.

Because time order makes \(\Omega M\) strictly block-lower triangular,

\[
(\Omega M)^m=0,
\]

the event-space inverse is exactly a finite polynomial. This gives a particularly transparent derivation of:

- an exact finite-strength rank bound;
- the exact directed two-event cross term;
- finite-strength additivity under \(\Omega_{ji}=0\);
- the source/readout projection \(CPM(I-\Omega M)^{-1}QB\);
- an observer-dependent **algebraic** maximum interaction order.

This may be a useful pedagogical or specialized algebraic note. **This audit does not establish that this exact formula or the term “algebraic interaction horizon” is historically new.**

## Empirical handoff after the prior-art kill

The strongest use of the formula is no longer “publish the interaction calculus.” It is as a hypothesis generator for `Kompressori`.

The empirical question is:

> In a nonlinear state-changing field, does a small-probe estimate of propagated local coupling predict the later finite non-additivity of two local operator updates better than physical distance or static low-rank-subspace overlap?

That is deliberately weaker than asserting that the nonlinear field obeys the exact linear factorization.

A useful analogue is

\[
\widehat\Omega_{j\leftarrow i}
\propto
\langle p_j,\; D\Phi_{\rm base}[p_i]\rangle,
\]

where `p_i` is a localized small probe and the derivative is measured experimentally around the current nonlinear base trajectory. For simultaneous finite events, a symmetric predictor can be constructed from the two directed couplings and compared against preregistered baselines.

If this does not outperform distance/static overlap on held-out event pairs, the cross-repo handoff is killed as a useful predictor even though the linear algebra identity remains true.

## Remaining literature questions

A deeper historical search would still be needed before publishing the mathematics itself. Useful search terms include:

- finite rank perturbation product of matrices
- low rank updates state transition product
- time ordered finite rank perturbation propagator
- impulsive system low rank jump matrix state transition
- multiple low rank updates product identity
- Dyson series finite rank impulses
- event space resolvent propagator
- Woodbury time ordered product
- observer dependent interaction order linear system
- Foldy-Lax event interaction matrix time ordered scatterers

The correct current status is therefore:

```text
algebra: exact
numerical verification: exact to floating-point precision
historical priority: unestablished and substantially crowded
nonlinear Kompressori relevance: empirical question, not theorem
```
