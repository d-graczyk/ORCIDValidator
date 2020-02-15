"""

"""

import pytest
from orcidvalidator.orcid_misc import orcid_id_to_list
from orcidvalidator.orcid_misc import calculate_orcid_id_checksum
from orcidvalidator.orcid_misc import check_orcid_id_checksum

input_orcid_ids = ['0000-0002-6006-647X',
                   '0000-0003-2123-4255',
                   '0000-0003-1805-603X',
                   '0000-0002-6021-3564',
                   '0000-0001-7359-2711']
input_bad_orcid_ids = ['0000-0102-6006-647X',
                       '0000-0003-1805-6039',
                       '0000-0003-2123-3255']
expected_assertions = [True, True, True, True, True, False, False, False]
expected_orcid_checksums = ['X', '5', 'X', '4', '1']
expected_orcid_list = ["0", "0", "0", "0", "0", "0", "0", "2", "6", "0", "0", "6", "6", "4", "7", "X"]


def test_orcid_id_to_list():
    assert orcid_id_to_list(input_orcid_ids[0]) == expected_orcid_list


@pytest.mark.parametrize('input_orcid,expected_checksum', zip(input_orcid_ids, expected_orcid_checksums))
def test_calculate_orcid_id_checksum(input_orcid, expected_checksum):
    orcid_as_list = [x for x in input_orcid if x in "01234567890X"]
    checksum = calculate_orcid_id_checksum(orcid_as_list)
    assert checksum == expected_checksum


@pytest.mark.parametrize('input_orcid,expected_assertion', zip(input_orcid_ids+input_bad_orcid_ids, expected_assertions))
def test_check_orcid_id_checksum(input_orcid, expected_assertion):
    assert check_orcid_id_checksum(input_orcid) == expected_assertion
