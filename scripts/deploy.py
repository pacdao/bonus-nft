from brownie import ZERO_ADDRESS, PACDaoBonus1, accounts, network
from brownie.network import max_fee, priority_fee


def main():
    publish_source = True
    multisig = "0xf27AC88ac7e80487f21e5c2C847290b2AE5d7B8e"
    beneficiary_address = multisig

    if network.show_active() in ["development"]:
        tokens = [ZERO_ADDRESS]
        deployer = accounts[0]
        publish_source = False
        beneficiary_address = deployer

    elif network.show_active() == "rinkeby":
        tokens = [
            "0x899CC89C0A094709CEbBB4AA8C3c2744B75B17Cd", 
            "0xf9503244980425e910f622077Bd8671de644279C",
            "0xe35BaEa12CC0281D601CF53FfEE01e6439655a94"
        ]
        tokens = [
            "0x63994B223F01b943eFf986b1B379312508dc15F8",  # Founder
            "0xE60A7825A80509DE847Ffe30ce2936dfc770DB6b",  # Common
            "0xb198936708ef94f494a4e753c44dcf8691cf7b87",  # Uncommon
            "0xd56c12efd06252f1f0098a8fe517da286245c0a8",  # Rare
            "0x3459cfce9c0306eb1d5d0e2b78144c9fbd94c87b",  # Gov
        ]

        deployer = accounts.load("husky")
        beneficiary_address = deployer
        publish_source = True
    elif network.show_active() in ["mainnet", "mainnet-fork"]:
        tokens = [
            "0x63994B223F01b943eFf986b1B379312508dc15F8",  # Founder
            "0xE60A7825A80509DE847Ffe30ce2936dfc770DB6b",  # Common
            "0xb198936708ef94f494a4e753c44dcf8691cf7b87",  # Uncommon
            "0xd56c12efd06252f1f0098a8fe517da286245c0a8",  # Rare
            "0x3459cfce9c0306eb1d5d0e2b78144c9fbd94c87b",  # Gov
        ]

        if network.show_active() == "mainnet-fork":
            publish_source = False
            deployer = accounts[0]
        if network.show_active() == "mainnet":
            deployer = accounts.load("minnow")
            max_fee(input("Max fee in gwei: ") + " gwei")
            priority_fee("2 gwei")
            publish_source = True
    else:
        deployer = accounts.load("husky")
        publish_source = True

    return PACDaoBonus1.deploy(
        beneficiary_address, tokens, {"from": deployer}, publish_source=publish_source
    )
