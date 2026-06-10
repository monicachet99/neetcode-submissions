class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for x in tokens:
            if x not in ['+', '-', '*', '/']:
                l.append(int(x))
            else:
                b = l.pop()
                a = l.pop()

                if x == '+':
                    l.append(a + b)
                elif x == '-':
                    l.append(a - b)
                elif x == '*':
                    l.append(a * b)
                elif x == '/':
                    l.append(int(a / b)) 

        return l[-1]