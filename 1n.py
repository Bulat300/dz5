import requests
import json


def getCategories(numCategories):
    for i in range(1, numCategories):
        try:
            response = requests.get("https://jservice.io/api/clues?category="+str(i)).json()[0]['category']

            print('Category name {}, its ID {}'.format(response['title'], response['id']))

        except:
            print("------------------------------------------------------------------------------------------------------------")
        # category_dict = json.loads(response)
        # category_dict[0]['category']


def getQuestionAmount(categoryID):
    response = requests.get("https://jservice.io/api/clues?category="+str(categoryID)).json()
    print('--------------------------There are up to {} questions to choose from, how many you want to get?--------------------------'.format(len(response)+1))

    return len(response)


def questionsToJson(questions_am_user_choose, categoryId):
    questionsSelected = {}
    response = requests.get("https://jservice.io/api/clues?category="+str(categoryId)).json()

    for i in range(questions_am_user_choose):
        questionsSelected[i] = response[i]['question']

    with open('result.json', 'w') as f:
        json.dump(questionsSelected, f)


if __name__ == '__main__':
    print("------------------Hello, that's quiz, you can choose questions from the following categories------------------")
    getCategories(50)

    print("----------------------------Choose category ID you want to answer questions ----------------------------")
    categoryId = str(input())

    totalAmQuestions = getQuestionAmount(categoryId)
    questions_am_user_choose = int(input())

    try:
        questionsToJson(questions_am_user_choose, categoryId)
    except:
        raise ValueError('We have less questions, than you wanted')

