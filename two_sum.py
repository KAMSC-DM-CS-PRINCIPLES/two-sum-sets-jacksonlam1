def two_sum_pairs(numbers, target):
    answer = []
    for i in range (0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if(numbers[i]+numbers[j]==target):
                answer.append({numbers[i],numbers[j]})
    return answer
