list = ["tom", "jerry", "mike", "jim", "joe", "jane"]
string = "joe"
if string in list:
    print(list.index(string))
else:
    print("Not found")


# def open_board(client):
#     """
#     This function will print the name, id, and url of all the boards that the user has access to

#     :param client: TrelloClient object
#     """
#     boards = client.list_boards()
#     i = 0
#     while len(boards) > 1:
#         print(board_list)
#         for board in boards:
#             speak("Which board do you want to open?")
#             command = takeCommand().lower()
#             print(command)
#             if command == "None".lower():
#                 speak("Sorry, I didn't get that")
#             if command in board_list:
#                 boards = client.list_boards()
#                 board = board_list.index(command)
#                 webbrowser.open(boards[board].url)
#         break
