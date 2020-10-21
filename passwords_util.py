from collections import defaultdict
from typing import List, Set


class PasswordsUtils:

    def __init__(self, passwords: List[str]):
        self.passwords = passwords
        self.pass_count = defaultdict(int)
        for password in self.passwords:
            self.pass_count[password] += 1
        pass_count_items = self.pass_count.items()
        self.ordered_passwords = sorted(list(pass_count_items), key=lambda pass_item: pass_item[1], reverse=True)

    def get_most_k(self, k) -> Set[str]:
        pass_items = self.ordered_passwords[:k]
        return {pass_item[0] for pass_item in pass_items}


def main():
    passwords = ['123123', '123123', '123123123', '123123', '123123123', '1234', 'password']
    pass_util = PasswordsUtils(passwords)
    k_1_pass = pass_util.get_most_k(1)
    k_1_expected = {'123123'}
    assert k_1_expected == k_1_pass, str(k_1_pass)


if __name__ == '__main__':
    main()
