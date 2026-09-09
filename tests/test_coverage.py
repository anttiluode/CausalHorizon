import unittest
import numpy as np


class CoverageCorollaryTests(unittest.TestCase):
    def test_spanning_bank_certifies_all_queries_in_span(self):
        # Event-entry map Q: raw 4-D queries collapse to a 3-D event space.
        Q = np.array([
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ])

        # Three bank queries whose projected images span Q U = R^3.
        B = np.eye(4)[:, [0, 1, 3]]
        Z = Q @ B
        self.assertEqual(np.linalg.matrix_rank(Z), 3)

        # Any observer-visible change operator H that preserves the spanning
        # bank exactly must vanish on the whole projected query space.
        # Construct H from a generic matrix and project out the bank span.
        rng = np.random.default_rng(3)
        H0 = rng.normal(size=(2, 3))
        proj = Z @ np.linalg.pinv(Z)
        H = H0 @ (np.eye(3) - proj)
        self.assertLess(np.linalg.norm(H @ Z), 1e-12)

        for _ in range(50):
            b = rng.normal(size=4)
            self.assertLess(np.linalg.norm(H @ Q @ b), 1e-12)

    def test_nonspanning_bank_can_miss_unseen_query(self):
        # Identity Q makes the geometry transparent.
        Q = np.eye(3)
        bank = np.eye(3)[:, :2]
        Z = Q @ bank
        self.assertEqual(np.linalg.matrix_rank(Z), 2)

        unseen = np.array([0.0, 0.0, 1.0])
        H = np.array([[0.0, 0.0, 1.0]])

        # Every stored query is preserved, but an unseen event-space direction
        # changes maximally.
        self.assertTrue(np.allclose(H @ Z, 0.0))
        self.assertAlmostEqual(float(H @ (Q @ unseen)), 1.0)

    def test_full_rank_can_still_be_badly_conditioned(self):
        eps = 1e-8
        Z = np.array([
            [1.0, 1.0],
            [0.0, eps],
        ])
        self.assertEqual(np.linalg.matrix_rank(Z), 2)
        s = np.linalg.svd(Z, compute_uv=False)
        self.assertGreater(s[0] / s[-1], 1e7)


if __name__ == "__main__":
    unittest.main()
