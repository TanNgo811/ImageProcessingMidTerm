
import re

if __name__ == "__main__":

    highland_regex = 'asd'

    highland_regex_2 = 'asd'

    phuclong_regex = '(P|p)(|.)(h|H)(|.)(u|U)(|.)(C|c)(|.)(L|l)(|.)(O|o)(|.)(n|N)(|.)(g|G)'

    starbucks_regex = 'asd'

    starbucks_regex_2 = 'asd'

    circlek_regex = '((C|c)(|.)(I|i)(|.)(R|r)(|.)(C|c)(|.)(L|l)(|.)(E|e)(|.)(k|K))'

    test_data = "PHULCLONGbILIE:(028)39arviceWo FhuaaTrarS:578,AIten &Tra Den W 20GToa]:TO ALCiam0ea0eT M0 N :Nc/s0yMach can h0a ona cn1rt00uM0Poma .1:LLC"

    r1 = re.search(phuclong_regex, test_data)

    print(r1)