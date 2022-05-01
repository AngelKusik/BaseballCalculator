'''
==========================================================================================

Title:    Baseball Calculator Revised
Author:   Angelica Kusik
Date:     November 23, 2021
Description:
  A simple Python application that will prompt the user to enter the scores for two baseball
  teams and will calculate the average runs that each team scored and determine which team has 
  won the game - Now revised and printing the output headings using a loop.

===========================================================================================
'''
######## CONSTANTS DECLARATION ##########
# The constants below hold respectively the minimum and maximum acceptable scores of a inning
# and will be used to validate the user input that must be within this range.
MIN_SCORE = 0
MAX_SCORE = 100

# The constants below hold respectively the total number of teams in a game and 
# the total number of innings that a baseball game have. These constants will be used to
# determine the number of times that the program must ask the user for inputs. 
TOTAL_TEAMS = 2
TOTAL_INNINGS = 9

######## VARIABLES DECLARATION ##########
# The team_count holds the team number (1 or 2) to indicate for which team the user 
# is entering the scores for.
team_count = 1

# The inning_count holds the number of inning (1-9) to indicate for which inning the 
# user is entering the score.
inning_count = 1

# The variables below hold respectively the sum of the runs that each team has scored in the game.
total_score_first_team = 0
total_score_second_team = 0

# The variables below hold respectively the average of runs that each team has scored in the game.
average_score_first_team = 0.0
average_score_second_team = 0.0

# The variables below hold the name of each team and will be used to print the name of the winner team.
first_team_name = 'Team 1'
second_team_name = 'Team 2'

# The winner will hold the team name of the team that has won the game.
winner = ''

# The continue_processing flag indicates if the program must restart or not based on the user input.
continue_processing = True

# The statement below creates a loop that will restart the program as long as continue_processing is true.
while continue_processing:

    ######## ARRAYS DECLARATION ##########
    # The arrays below hold the number of runs that each team has scored in each of the 9 innings.
    first_team_scores = list()
    second_team_scores = list()

    ########### INPUT ############
    # Print Program's name.
    print('\n               BASEBALL SCORE CALCULATOR              ')

    #The statement below creates an iteration that will repeat up to the total number of teams in the game (2).
    for team_count in range(1,TOTAL_TEAMS+ 1):
        # Thestatement below creates a second iteration that will repeat up to the total number of inning
        #in a baseball game (9).
        for inning_count in range(1,TOTAL_INNINGS+1):
            #The variable below is a flag that will determine when the while loop in the sequence must end.
            input_validated = False
            # The variable below contains the message that will be displayed to the user.
            input_message = 'Please enter Team ' + str(team_count) + ' runs for inning ' + str(inning_count) + ': '

            #The statement below creates a loop that will prompt the user for the input until a valid input is entered.
            while not input_validated:
                try:
                    #The program will try to store the input as a whole number. If successfull the program will check the next condition.
                    user_input = int(input(input_message))
                    #The statement below sets a condition that the input must follow to be valid. The input must be
                    #in the range of 0 and 100 inclusive as the min and max constants demonstrate.
                    if MIN_SCORE <= user_input <= MAX_SCORE:
                        #If both validations succeed the statement below will determine from which team is the score being proccessed 
                        #by checking the value of the team count variable.
                        if team_count == 1:
                            first_team_scores.append(user_input)
                        else:
                            second_team_scores.append(user_input)
                        input_validated = True
                        #If the input is not within the desidered range, a error message will be displayed and the user will be asked to enter a valid input.
                    else:
                        input_message = 'Score must be between ' + str(MIN_SCORE) + ' and ' + str(MAX_SCORE) + '. Please try again: '
                #If the input is not a whole number, an error message will be displayed and the user will be asked to enter a valid input.
                except:
                    input_message = 'The score for an inning must be entered as a whole number.'

    ########### PROCESS ############
    #After the user enter the scores from both teams for all 9 innings we calculate the total runs that team scored
    # and store the value in a variable. 
    total_score_first_team = sum(first_team_scores)
    #Next we calculate the average runs that the first teams scored by dividing the sum of runs by the total number of innings.
    average_score_first_team = sum(first_team_scores) / len(first_team_scores)

    #We repeat the same process for the second team. First calculate the sum, second the average runs.
    total_score_second_team = sum(second_team_scores)
    average_score_second_team = sum(second_team_scores) / len(second_team_scores)

    #The statement below will compare the total number of runs that each team scored to determine which team is the winner.
    if total_score_first_team > total_score_second_team:
        winner = first_team_name

    elif total_score_first_team < total_score_second_team:
        winner = second_team_name
    
    else:
        winner = first_team_name + ' and ' + second_team_name + ' drew. No one'

    ########### OUTPUT ############

    #Next we print the user inputs for each inning.   
    print_output_heading = ''
    for count in range(0, TOTAL_INNINGS):
        print_output_heading = print_output_heading + 'Inning#' + str(count+1) + '    '
    print('\n===============================================================================================================')  
    print('\nTeam     ' + print_output_heading)

    #The variable print_first_team holds the value of each index within the array first_team_scores.
    print_first_team = ""
    #The statement below creates a loop that will print each index of the array in sequence.
    for count in range(0,TOTAL_INNINGS):
        print_first_team = print_first_team + str(first_team_scores[count]) + '         '
    print(first_team_name + '      ' + print_first_team)

    #We repeat the same iteration here to print each index of the array containing the scores from the second team.
    print_second_team = ""
    for count in range(0,TOTAL_INNINGS):
        print_second_team = print_second_team + str(second_team_scores[count]) + '         '
    print(second_team_name + '      ' + print_second_team)
    
    #We print the average runs scored by each team
    print(first_team_name + ' scored ' + str(total_score_first_team) + ' runs, averaging {:.1f} per inning.'.format(average_score_first_team))
    print(second_team_name + ' scored ' + str(total_score_second_team) + ' runs, averaging {:.1f} per inning.'.format(average_score_second_team))
    #We print the winner variable that contains the name of the winner team.
    print(winner + ' wins!')

    #We assign a new value to the variable input message to prompt the user if they want to enter scores
    #for a new game.
    input_message = '\nWould you like to enter scores for a new game? (yes/no): '
    #The continue_program is a flag that will determine when the iteration in the sequence must end.
    continue_program = True

    #The statement below creates an iteration that will run until the user enter yes to restart or no to end program.
    while continue_program:
        #We prompt the user the yes or no input
        user_input = input(input_message).lower()

        #If user enters yes we end this loop and restart program as determined by the continue_program
        # and continue_processing flags.
        if user_input == 'yes':
            continue_program = False
            continue_processing = True

        else:
            #If user enter no we set both flags to false to end this loop and the loop keeping the program running.
            if user_input == 'no':
                continue_program = False
                continue_processing = False

            #If the user enter anything but yes or no we display an error message and prompt user again until
            #a valid answer is entered.
            else:
                input_message = 'Please enter yes to continue or no to end program: '
                continue_program = True
                continue_processing = True
