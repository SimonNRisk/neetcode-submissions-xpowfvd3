class Solution:
    SENIOR_AGE = 60 
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for detail in details:
            age = int(detail[11:13])
            if age > self.SENIOR_AGE:
                seniors += 1
        return seniors