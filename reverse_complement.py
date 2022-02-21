def input_seq():
    original_seq = input("Introduce DNA sequence: \n")
    return original_seq


def answer():
    usr_answer = input("Reverse -> Press R \n"
                       "Complement -> Press C \n"
                       "Reverse and Complement -> Press 0 \n")
    return usr_answer


def reverse(original_seq):
    reverse = original_seq[::-1]
    return reverse


def complement(original_seq):
    complement_list = []
    for i in original_seq:
        if i == "A":
            complement_list.append("T")
        elif i == "T":
            complement_list.append("A")
        elif i == "C":
            complement_list.append("G")
        elif i == "G":
            complement_list.append("C")
    complement_seq = "".join(complement_list)
    return complement_seq


def reverse_complement(original_seq):
    complement_seq = complement(original_seq)
    reverse_complement = complement_seq[::-1]
    return reverse_complement


def main():
    original_seq = input_seq()
    usr_answer = answer()
    if usr_answer == "R":
        print(reverse(original_seq))
    elif usr_answer == "C":
        print(complement(original_seq))
    elif usr_answer == "0":
        print(reverse_complement(original_seq))
    return


main()
