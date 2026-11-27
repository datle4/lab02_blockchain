"""Task 2: Fund and spend a testnet P2SH 2-of-2 multisig output."""


def build_redeem_script(public_key_1: bytes, public_key_2: bytes) -> bytes:
    """Serialize a 2-of-2 redeem script, preserving the supplied public key order."""
    raise NotImplementedError


def derive_p2sh_address(redeem_script: bytes) -> str:
    """Return the testnet P2SH funding address for this redeem script."""
    raise NotImplementedError


def sign_input(unsigned_tx_hex: str, redeem_script: bytes, private_key_wif: str) -> bytes:
    """Return one signature for input zero, including its sighash type byte."""
    raise NotImplementedError


def assemble_signed_spend(
    unsigned_tx_hex: str,
    redeem_script: bytes,
    signature_1: bytes,
    signature_2: bytes,
) -> str:
    """Unlock input zero with signatures in redeem-script key order and return tx hex."""
    raise NotImplementedError


def main() -> None:
    """Coordinate the funding address, faucet deposit, two signers and broadcast."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
