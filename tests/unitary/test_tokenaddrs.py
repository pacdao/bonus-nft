import brownie


def test_update_with_gov_token(nft_gov, gov_addr):
    assert nft_gov.tokenAddrs()[0] == gov_addr


def test_gov_token_can_mint(nft_gov, gov_holder):
    nft_gov.mint({"from": gov_holder})
    assert nft_gov.balanceOf(gov_holder) > 0


def test_non_gov_token_cannot_mint(nft_gov, accounts):
    with brownie.reverts("No NFT Owned"):
        nft_gov.mint({"from": accounts[2]})
