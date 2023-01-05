    # STUDENT REPORT SYSTEM
    #### Video Demo:  https://youtu.be/WkZ7ein8O9w
    #### Description:
    This is my final project for CS50's Introduction to Programming with Python. This is a small student report project with limited options. This project imports csv file and the user can choose which choices he wants to perform. First, the user has to import the csv file that has students' roll numbers, name,s and grades from the command line. Then, the command line will display four choices the user can perform. After that, the user has to choose four choices he would like to perform. The user has to enter from 1 to 4 depending on which choices he wants to make.

   The first choice is to display the csv file in a table format using pandas library.

   The second choice is to search individual student's grade by searching the name of the student. If the user enters an invalid csv file, the program will exit by displaying \"Can't read the CSV file.\". If there is no such name in the csv file, the program will display \"Not Found\".

   The third choice is to transform the marks into letter grades from A to F accordingly and save them into a new csv file. If the user enters an invalid csv file, the program will exit by displaying \"Can't read the CSV file.\". The program will first transform the csv file into a list and each row is a dictionary on its own. The a_to_f function will change the corresponding marks to corresponding letter grade. Then, the table with letter grade will be displayed on the screen. Finally, the whole table will be saved in the form of csv and later be used again.

   The last choice is to exit the program.

   The user can perform No.1 to No.3 choices again and again until he wants to exit the program.
