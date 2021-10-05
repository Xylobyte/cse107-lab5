def apply_cipher(msg):
    """returns a reversed version of the string passed into it

    applied: reversed string of msg
    """
    applied = ""
    for i in range(len(msg) - 1, -1, -1):
        applied += msg[i]
    return applied


def main():
    word = input("Please enter in your message: ")
    print("Your message is now: " + apply_cipher(word))


if __name__ == "__main__":
    main()
