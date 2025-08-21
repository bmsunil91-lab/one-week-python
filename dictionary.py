dict = {
    "sunil": [85, 90, 78],
    "ajay": [88, 92, 95],  
}
calulate_average = lambda scores: sum(scores) / len(scores)
average_scores = {name: calulate_average(scores) for name, scores in dict.items()}
print(average_scores)