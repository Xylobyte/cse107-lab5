def validate(num):
    """returns true if num is a valid credit card number, else it returns false. 
    Uses luhns algorithm
    """
    nums = [int(n) for n in num]
    nums.reverse()  # Reverse order since we start with second to last element
    for i in range(len(nums)):
        if i % 2 == 1:
            nums[i] *= 2
    nums.reverse()  # After doubling every other element reverse list to orignal order
    # Returns true if sum is evenly divisible by 10, otherwise it returns false
    return True if sum([int(n) for n in "".join([str(s) for s in nums])]) % 10 == 0 else False


def main():
    inpt = input("Please enter a card number: ")
    print("This card number is " + ("valid" if validate(inpt) else "invalid"))


if __name__ == "__main__":
    main()
