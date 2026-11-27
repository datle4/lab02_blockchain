"""Testnet integration shared by the P2PKH and multisig flows."""

from .transaction import UTXO


def list_unspent(address: str) -> list[UTXO]:
    """Return unspent outputs for the testnet address, including each locking script."""
    raise NotImplementedError


def broadcast_transaction(signed_tx_hex: str) -> str:
    """Submit a signed transaction to the selected testnet and return its txid."""
    raise NotImplementedError


def get_confirmations(txid: str) -> int:
    """Return the confirmation count for a known transaction, zero while pending."""
    raise NotImplementedError
