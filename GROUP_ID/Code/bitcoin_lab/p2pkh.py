"""Task 1: Fund and spend a testnet P2PKH output."""

from .transaction import UTXO


def derive_p2pkh_address(public_key: bytes) -> str:
    """Derive the testnet P2PKH address for a public key."""
    raise NotImplementedError


def build_locking_script(address: str) -> bytes:
    """Return the serialized P2PKH scriptPubKey for the funding address."""
    raise NotImplementedError


def sign_spend(unsigned_tx_hex: str, utxo: UTXO, private_key_wif: str) -> str:
    """Unlock the referenced P2PKH output and return the signed transaction hex."""
    raise NotImplementedError


def main() -> None:
    """Coordinate address setup, faucet funding, UTXO selection, signing and broadcast."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
