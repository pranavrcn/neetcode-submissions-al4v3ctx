class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        score_sum = 0
        for i in range(0,len(operations)):
                if operations[i] == "x":
                    record.append(operations[i])
                elif operations[i] == "+":
                    res = int(record[-1]) + int(record[-2])
                    record.append(res)       
                elif operations[i] == "D":
                    res = int(record[-1]) * 2
                    record.append(res)
                elif operations[i] == "C":
                    record.pop()
                else:
                    record.append(int(operations[i]))
        print(record)
        for s in record:
            if isinstance(s, int):
                score_sum += s
        return score_sum

            

        