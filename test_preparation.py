INPUT_FILE_PATH = 'questions.txt'

questions = list()
temp_list = list()
correct_answers = list()


def preparation():
    with open(INPUT_FILE_PATH, "r", encoding="UTF-8") as my_file:

        for line in my_file:
            questions.append(line.strip())  # question
            temp_list.append(my_file.readline().strip())  # opt1
            temp_list.append(my_file.readline().strip())  # opt2
            temp_list.append(my_file.readline().strip())  # opt3
            correct_answers.append(int(my_file.readline().split(":")[1].strip()))  # ans

        options = list()

        for i in range(0, len(temp_list), 3):
            options.append(
                            temp_list[i] + "\n" +
                            temp_list[i + 1] + "\n" +
                            temp_list[i + 2]
                           )

    return questions, options, correct_answers
