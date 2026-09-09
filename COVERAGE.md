# Observer-bank coverage

This note connects the finite-event resolvent to a narrower question raised by
bounded replay / preservation systems:

> When can a finite bank of remembered queries legitimately stand for an entire
> family of future queries?

The answer is exact in the linear event-space setting. The bank need not span the
raw input space. It must span the **event-entry space actually reachable by the
capability**.

## Setup

From the main theorem, for a fixed collection of finite-rank events and a fixed
readout `C`, the observer-visible change caused by an input/query vector `b` is

```math
\Delta y(b)
=
C(\widetilde\Phi-\Phi)b
=
H Q b,
```

where

```math
H = (CP)M(I-\Omega M)^{-1}.
```

All dependence on the query enters through

```math
q = Qb.
```

Let `U` be a linear space of admissible capability queries and define its
reachable event-entry space

```math
\mathcal E = Q\mathcal U.
```

Let a replay / reference bank contain queries

```math
b_1,\ldots,b_s
```

and define

```math
Z=[Qb_1\;Qb_2\;\cdots\;Qb_s].
```

---

# Theorem — exact bank sufficiency

If

```math
\operatorname{col}(Z)=\mathcal E,
```

then preserving the observer response on every bank query,

```math
HQb_j=0
\qquad j=1,\ldots,s,
```

implies

```math
HQb=0
\qquad\text{for every } b\in\mathcal U.
```

## Proof

For any `b in U`, the assumption `col(Z)=E` gives a coefficient vector `alpha`
such that

```math
Qb=Z\alpha.
```

Therefore

```math
HQb
=HZ\alpha
=\sum_j \alpha_j HQb_j
=0.
```

QED.

---

# Corollary — the relevant bank dimension

An exact spanning bank requires at least

```math
\dim(Q\mathcal U)
```

independent event-space query directions, and if the available queries can realize
a basis of `Q U`, that many are sufficient.

So the intrinsic exact coverage dimension is not

```text
number of remembered examples
```

and not necessarily

```text
raw input dimension.
```

It is

```math
\boxed{\dim(Q\mathcal U)}.
```

A huge replay bank can therefore still be uselessly redundant, while a much
smaller bank can be complete if its projected queries span the reachable event
space.

---

# What failure of spanning means

Suppose a new admissible query has

```math
Qb_* \notin \operatorname{col}(Z).
```

Then the bank alone cannot provide a general linear preservation certificate.
There exists a linear functional `h` on event space such that

```math
hZ=0
```

but

```math
hQb_*\ne0.
```

Thus, without additional restrictions on the allowed response-change operator,
all stored bank responses can remain exactly unchanged while an unseen query
changes.

This is an information statement. It does **not** say every such functional `h`
is realizable by a particular physical event system.

---

# Approximate coverage and conditioning

Exact rank is not enough in noisy or finite-tolerance settings.

If the bank spans `E`, then for

```math
Qb=Z\alpha
```

we have

```math
\|HQb\|
\le
\|HZ\|\,\|\alpha\|.
```

Using the minimum-norm coordinates

```math
\alpha=Z^\dagger Qb,
```

gives

```math
\boxed{
\|HQb\|
\le
\|HZ\|\,\|Z^\dagger Qb\|.
}
```

So a numerically fragile bank can have full rank yet provide a poor tolerance
certificate. A good bank should therefore seek both

```text
coverage       — span the event-entry directions
conditioning   — avoid nearly redundant projected queries
```

This is the same algebraic distinction seen in active observability experiments:
opening rank and obtaining noise-robust singular values are different jobs.

---

# Why this changes the interpretation of replay selection

A selector that asks

> Which stored query is damaged most by this particular proposed update?

is selecting large values of a current consequence such as

```math
\|HQb_j\|.
```

That is **not the same problem** as selecting a bank whose projected query vectors

```math
Qb_j
```

span `Q U` with good conditioning.

Consequently, vulnerability-based replay may repeatedly choose several versions
of the same event-space direction. It can be highly informed about the current
candidate and still have poor coverage of unseen cue routes.

This gives a precise linear analogue of the Gate-9 observation in
`IttnasNoruen`: all stored classifications can survive while unfamiliar partial
cues fail.

It does not retroactively turn that nonlinear classifier experiment into a test
of this theorem. `IttnasNoruen` uses a tanh model, parameter-space temporary
updates, and externally supplied cue families; it does not expose the exact `Q`
of a CausalHorizon factorization.

---

# Empirical proxy when Q is hidden

A black-box learner will usually not know `Q`.

One possible measured proxy is to apply a small, diverse panel of counted temporary
candidate updates `delta theta_l` and give each old query `b` a response signature

```math
s(b)
=
\begin{bmatrix}
 f_{\theta+\delta\theta_1}(b)-f_\theta(b)\\
 \vdots\\
 f_{\theta+\delta\theta_K}(b)-f_\theta(b)
\end{bmatrix}.
```

If the temporary updates interrogate sufficiently diverse left directions of the
hidden response geometry, distances/rank/conditioning among these signatures can
serve as an empirical sketch of query coverage.

A next experiment should compare, under equal measurement and learning budgets:

1. random replay;
2. low-margin / boundary replay;
3. current-interference / vulnerability replay;
4. **coverage replay** chosen by pivoted-QR, determinant/volume, or smallest-singular-value criteria on measured response signatures.

Evaluate at matched new-task progress on held-out cue routes that were not offered
to the bank selector.

A positive result would not prove that the signatures equal `Qb`; it would show
that a CausalHorizon-motivated coverage sketch is operationally useful.

---

# Relation to nonlinear compensation

Gate 9 also found a different failure: a tangent-preserving direction can violate
a curved constraint at finite step size.

That is real but separate.

CausalHorizon's main finite-event identity has no small-step assumption because it
is exact for finite-rank edits of **linear propagator factors**. A generic nonlinear
parameter update, such as a tanh-network weight change or the example

```math
b-a^2\ge0,
```

is not automatically representable by that theorem.

So the clean split is:

```text
coverage       which questions span the capability-relevant event space?
prediction     what will this finite update actually do?
compensation   can another coordinated change repair the predicted violation?
```

Gate 9 improved prediction/compensation. This corollary isolates what an exact
coverage certificate would require in the CausalHorizon setting.

---

## Claim boundary

The proof is elementary linear algebra once the main CausalHorizon factorization
is given. No novelty claim is made for the general fact that spanning test vectors
certify a linear operator.

The useful contribution here is the identification of the relevant span as the
**projected event-entry space `Q U`**, which makes the bounded-observer role in the
main theorem operational and gives a concrete failure criterion for replay banks.
