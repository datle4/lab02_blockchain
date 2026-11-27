"""Shared wallet and transaction interfaces for both lab tasks."""

from typing import NamedTuple


class UTXO(NamedTuple):
    """An unspent output. Hex strings use the same format as a block explorer."""

    txid: str
    vout: int
    value_sats: int
    script_pubkey_hex: str


def generate_testnet_private_key() -> str:
    """Return a fresh testnet private key in Wallet Import Format (WIF)."""
    raise NotImplementedError


def derive_public_key(private_key_wif: str) -> bytes:
    """Return the compressed public key corresponding to the WIF key."""
    raise NotImplementedError


def build_unsigned_spend(utxo: UTXO, destination: str, fee_sats: int) -> str:
    """Serialize a one-input spend paying the UTXO value minus the fee to destination."""
    raise NotImplementedError
