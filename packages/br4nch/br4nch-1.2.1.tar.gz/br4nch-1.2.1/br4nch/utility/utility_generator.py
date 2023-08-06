# br4nch - Data Structure Tree Builder
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import uuid

from br4nch.utility.utility_librarian import branches, uids


def generate_uid(branch, length=10):
    """
    - Generates the uid.

    If the branch variable is equal to '-':
      While loop:
        - If the uid exists in the 'branches' dictionary, a new one is generated.
        - If the uid does not exist in the 'branches' dictionary, then the uid is returned.

    If the branch variable is not equal to '-':
      While loop:
        - If the uid exists in the current branch uids list, a new one is generated.
        - If the uid does not exist in the current branch uids list, then the uid is added to the branch uids list.

      - Returns the generated uid.
    """
    uid = str(uuid.uuid4()).replace("-", "")[0:length]

    if branch == "-":
        while True:
            if uid in list(branches):
                return generate_uid(branch, length)
            else:
                return uid

    else:
        while True:
            if uid in uids[branch]:
                return generate_uid(branch, length)
            else:
                uids[branch].append(uid)
                break

        return ":uid=" + uid
