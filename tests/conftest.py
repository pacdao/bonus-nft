#!/usr/bin/python3

import pytest
from brownie import Contract, PACDaoBonus1


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="function")
def founder_token(nft):
    return Contract(nft.tokenAddrs()[0])


@pytest.fixture(scope="function")
def action_token(nft):
    return Contract(nft.tokenAddrs()[1])


@pytest.fixture(scope="function")
def alice(founder_token, accounts):
    return accounts.at(founder_token.ownerOf(1), force=True)


@pytest.fixture(scope="function")
def bob(action_token, accounts):
    return accounts.at(action_token.ownerOf(1), force=True)


@pytest.fixture(scope="function")
def charlie(accounts):
    return accounts[2]


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="module")
def nft(owner):
    tokens = [
        "0x63994B223F01b943eFf986b1B379312508dc15F8",  # Founder
        "0xE60A7825A80509DE847Ffe30ce2936dfc770DB6b",  # Common
        "0xb198936708ef94f494a4e753c44dcf8691cf7b87",  # Uncommon
        "0xd56c12efd06252f1f0098a8fe517da286245c0a8",  # Rare
        "0x3459cfce9c0306eb1d5d0e2b78144c9fbd94c87b",  # Gov
    ]

    return PACDaoBonus1.deploy(owner, tokens, {"from": owner})


@pytest.fixture(scope="function")
def nft_minted(nft, alice, bob):
    nft.mint({"from": alice})
    nft.mint({"from": bob})
    return nft


@pytest.fixture(scope="function")
def nft_funded(nft, accounts):
    accounts[1].transfer(nft, 10 ** 18)
    return nft


@pytest.fixture(scope="function")
def beneficiary(nft, accounts):
    return accounts.at(nft.beneficiary(), force=True)


@pytest.fixture(scope="module")
def gov_addr():
    return "0x3459cfce9c0306eb1d5d0e2b78144c9fbd94c87b"


@pytest.fixture(scope="function")
def nft_gov(nft, beneficiary, gov_addr):
    nft.updateTokenAddrs([gov_addr])
    return nft


@pytest.fixture(scope="module")
def gov_holder(gov_addr, accounts):
    _addr = "0xbfe384d79969bcb583b8a0e5fedc314aee480e7e"
    return accounts.at(_addr, force=True)


@pytest.fixture(scope="module")
def multi_owner(accounts):
    return accounts.at("0xf27AC88ac7e80487f21e5c2C847290b2AE5d7B8e", force=True)
