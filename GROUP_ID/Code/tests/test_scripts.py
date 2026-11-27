"""Offline acceptance tests for the two spending conditions in Lab 02."""

import unittest


class SpendingConditionsTests(unittest.TestCase):
    def test_p2pkh_accepts_matching_key(self) -> None:
        """Verify a spend against the previous P2PKH output using the matching key."""
        raise NotImplementedError

    def test_p2pkh_rejects_wrong_key(self) -> None:
        """Check that another key cannot unlock the same P2PKH output."""
        raise NotImplementedError

    def test_multisig_accepts_both_signatures(self) -> None:
        """Verify the P2SH spend with both signatures and the funding redeem script."""
        raise NotImplementedError

    def test_multisig_rejects_one_signature(self) -> None:
        """Evaluate a spend containing only one signature against the 2-of-2 output."""
        raise NotImplementedError
