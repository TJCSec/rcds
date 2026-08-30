import pytest

from rcds.backends.rctf.rctf import RCTFAdminV1


def test_response_kind_compatibility():
    RCTFAdminV1.assertResponseKind({"kind": "goodChallenges"}, "goodChallenges")
    RCTFAdminV1.assertResponseKind(
        {"kind": "goodAdminChallenges"}, "goodChallenges", "goodAdminChallenges"
    )

    with pytest.raises(RuntimeError):
        RCTFAdminV1.assertResponseKind(
            {"kind": "badRequest"}, "goodChallenges", "goodAdminChallenges"
        )
