"""

"""


def orcid_id_to_list(orcid_id_str: str) -> list:
    return [x for x in orcid_id_str.strip() if x in "01234567890X"]


def calculate_orcid_id_checksum(orcid_id_list: list) -> str:
    total = 0
    for i in range(0, len(orcid_id_list)-1):
        total = (total+int(orcid_id_list[i]))*2
    remainder = total%11
    checksum = (12-remainder)%11
    return 'X' if checksum == 10 else str(checksum)


def check_orcid_id_checksum(orcid_id: str) -> bool:
    orcid_id_list = orcid_id_to_list(orcid_id)
    checksum = calculate_orcid_id_checksum(orcid_id_list)
    return orcid_id_list[-1] == checksum

