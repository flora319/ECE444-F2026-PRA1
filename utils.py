class utils:
    def reversed(number):
        if type(number) != int:
            return None

        return int(str(number)[::-1])

    def formatter(number):
        if type(number) != int:
            return None

        binary = bin(number)
        octal = oct(number)

        return binary, octal