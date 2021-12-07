import re


def data_extraction(input_data):

    highland_regex = '(h|H)(|.)(i|I)(|.)(g|G)(|.)(h|H)(|.)(L|l)(|.)(a|A)(|.)(n|N)(|.)(d|D)'

    highland_regex_2 = '(R|r)(|.)(e|E)(|.)(c|C)(|.)(E|e)(|.)(i|I)(|.)(P|p)(|.)(t|T)'

    phuclong_regex = '(P|p)(|.)(h|H)(|.)(u|U)(|.)(C|c)(|.)(L|l)(|.)(O|o)(|.)(n|N)(|.)(g|G)'

    starbucks_regex = 'asd'

    starbucks_regex_2 = 'asd'

    circlek_regex = '((C|c)(|.)(I|i)(|.)(R|r)(|.)(C|c)(|.)(L|l)(|.)(E|e)(|.)(k|K))'

    if (re.search(highland_regex, input_data) or re.search(highland_regex_2, input_data)):
        return 'highlands'
    elif (re.search(phuclong_regex, input_data)):
        return 'phuclong'
    elif (re.search(starbucks_regex, input_data) or re.search(starbucks_regex_2, input_data)):
        return 'starbucks'
    else:
        return 'others'


if __name__ == "__main__":

    # Chinese Filter
    pattern = re.compile("[\u4E00-\u9FFF]+")

    test_data = "PHULCLONGbILIE:(028)39arviceWo FhuaaTrarS:578,AIten &Tra Den W 20GToa]:TO ALCiam0ea0eT M0 N :Nc/s0yMach can h0a ona cn1rt00uM0Poma .1:LLC"

    print(data_extraction(test_data))