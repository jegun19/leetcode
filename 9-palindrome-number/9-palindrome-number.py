class Solution:
    def isPalindrome(self, x: int) -> bool:
        res_list = list()
        if x < 0:
            return False
        elif (x > -1) and (x < 10):
            return True
        else:
            rank = int(math.log10(x))
            if rank % 2 == 0:
                # Odd digit

                for it in range(rank, 0, -1):
                    if x % 10 ** it == 0:
                        res_list.append(0)

                    # Detect in-between zeroes
                    elif it - 1 != int(math.log10(x % 10 ** it)):
                        res_list.append(0)

                    elif int(math.log10(x % 10 ** it)) >= 1:
                        digit = (x % 10 ** it) / (10 ** int(math.log10(x % 10 ** it)))
                        res_list.append(int(digit))
                        
                    elif int(math.log10(x % 10 ** it)) < 1:
                        digit = (x % 10 ** it) / (10 ** int(math.log10(x % 10 ** it)))
                        res_list.append(int(digit))

                first_digit = x / 10 ** int(math.log10(x))
                res_list.insert(0, int(first_digit))
                inverse = res_list[::-1]
                
                if res_list == inverse:
                    # print('True')
                    return True
                else:
                    # print('False')
                    return False

            else:
                # Even digit
                for it in range(rank, 0, -1):


                    if x % 10**it == 0:
                        res_list.append(0)

                    # Detect in-between zeroes
                    elif it-1 != int(math.log10(x % 10**it)):
                        res_list.append(0)

                    elif int(math.log10(x % 10**it)) >= 1:
                        digit = (x % 10**it) / (10 ** int(math.log10(x % 10**it)))
                        res_list.append(int(digit))
                        
                    elif int(math.log10(x % 10**it)) < 1:
                        digit = (x % 10 ** it) / (10 ** int(math.log10(x % 10 ** it)))
                        res_list.append(int(digit))

                first_digit = x / 10**int(math.log10(x))
                res_list.insert(0, int(first_digit))
                inverse = res_list[::-1]

                if res_list == inverse:
                    # print('True')
                    return True
                else:
                    # print('False')
                    return False