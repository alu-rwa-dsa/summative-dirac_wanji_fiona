import requests

# Sorting using quicksort
# listC = [5, 3, 2, 77, 56]  # expected list: 2, 3, 5, 56, 77  # practice list for testing

url = "https://api-career-dev-quizz.herokuapp.com/users/all/student"

response = requests.get(url)
data = response.json()

dict_data = data[0]  # this gives us just the dictionary stored in the list structure from the db
scores = data[0].get('score')
scores_as_strings = str(scores)

user_scores = []
for score in scores_as_strings:
    user_scores.append(int(score))  # add the scores from the database


def quick_sorting_scores(listZ):
    low = []
    same = []
    high = []

    # here, we are working with the method of having the pivot being
    if len(listZ) > 1:
        pivot_index = 0
        for i in range(pivot_index, len(listZ)):
            if listZ[i] < listZ[pivot_index]:
                low.append(listZ[i])

            elif listZ[i] == listZ[pivot_index]:
                same.append(listZ[i])

            elif listZ[i] > listZ[pivot_index]:
                high.append(listZ[i])

        print(low, same, high)
        return quick_sorting_scores(low) + same + quick_sorting_scores(high)

    else:
        return listZ

# sortedListC = quick_sorting_scores(listC)
# print("Sorted list: " + str(sortedListC))


# Ranking


def ranking_scores(listZ):
    user_score_input = int(input("What was your score?"))
    i = user_score_input
    if i in listZ:
        item_index = listZ.index(i)
        # print(item_index)  # checking it works
        rank = item_index + 1
        print("You are in the number " + str(rank) + " place!")


# ranking_scores(sortedListC)

print(user_scores)
quick_sorting_scores(user_scores)
ranking_scores(user_scores)
