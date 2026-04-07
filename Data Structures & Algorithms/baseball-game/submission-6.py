class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(0,len(operations)):
                if operations[i] == "+":
                    res = int(record[-1]) + int(record[-2])
                    record.append(res)       
                elif operations[i] == "D":
                    res = int(record[-1]) * 2
                    record.append(res)
                elif operations[i] == "C":
                    record.pop()
                else:
                    record.append(int(operations[i]))
        return sum(record)

            

        