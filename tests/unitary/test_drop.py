from brownie import ZERO_ADDRESS, PACDaoBonus1


def test_non_beneficiary_can_deploy(alice, bob):
    PACDaoBonus1.deploy(alice, [ZERO_ADDRESS], {"from": bob})
