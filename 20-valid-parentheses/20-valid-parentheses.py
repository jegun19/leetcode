class Solution:
    def isValid(self, s: str) -> bool:

        length = len(s)
        if length < 2:
            return False
        elif length % 2 != 0:
            return False
        else:
            half = s[:int(length/2)]
            if ("}" in half) or (")" in half) or ("]" in half):
                # Pairwise
                if (s[0] == ")") or (s[0] == "}") or (s[0] == "]"):
                    return False
                else:                
                    current = ""
                    for i in range(0, length):
                        if s[i] == "(":
                            current += s[i]
                        elif s[i] == "{":
                            current += s[i]
                        elif s[i] == "[":
                            current += s[i]


                        elif s[i] == ")":
                            if current == "":
                                return False
                            
                            elif current[-1] !=  "(":
                                return False
                            else:
                                current = current[:-1]
                        elif s[i] == "}":
                            if current == "":
                                return False
                            
                            elif current[-1] !=  "{":
                                return False
                            else:
                                current = current[:-1]
                        elif s[i] == "]":
                            if current == "":
                                return False
                            
                            elif current[-1] !=  "[":
                                return False
                            else:
                                current = current[:-1]
                    return True
                
            else:
                # Multiple brackets
                for i in range(0, int(length/2)):
                    first_char = s[i]
                    second_char = s[(length-1)-i]

                    if first_char == '(' and second_char != ')':
                        return False
                    elif first_char == '{' and second_char != '}':
                        return False
                    elif first_char == '[' and second_char != ']':
                        return False
                
                return True