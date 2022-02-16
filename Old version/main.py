#Quinn Hodges
#CompSci 30 -- M.Bender
#Exteral Files Assignment: Markbook

markbook = {}


#open the mark book and make a local copy in the Program instance
infile = open('Markbook.txt', 'r')
line = infile.readline()
while line:
	print(line, end = '')
	if line.startswith('<'):
		name = line[1:].rstrip('\n')
		line = infile.readline()
		marks = []
		continue
	else:
		while not line.startswith('>'):
			marks.append(line.rstrip('\n').split(','))
			line = infile.readline()
			
		for mark in marks:
			mark[1] = int(mark[1])
			
		markbook[name] = marks
		line = infile.readline()
infile.close()
del marks


#User inputs -- The meat and Gravy of the program
choice1 = 0
while choice1 != 4:
	choice1 = int(input(('What would you like to do? \n1) Add a student \n2) View students \n3) Change a students marks \n4) Quit\n')))
	
	#adds a student
	if choice1 == 1:
		newStudent = input('Please input the new students name: ')
		if newStudent in markbook.keys():
			print('That name is already in use. Returning to main menu.')
		else:
			print('Print the name of the class followed by the grade. Print stop when finished')
			user = '' 
			marks = []
			while user != 'stop':
				mark = input().split()
				user = mark[0]
				if user != 'stop':
					marks.append(mark)
					print(marks)
			del mark
			markbook[newStudent] = marks
	#displays students
	if choice1 == 2:
		print('Student List: ')
		for student in markbook.keys():
			print(student)
		choice2 = 0
		while choice2 != 2:
			choice2 = int(input('Would you like to: \n1) View a student\'s marks \n2)Return to main menu'))
			if choice2 == 1:
				for i in markbook[input('Which student\'s marks would you like to view?')]:
					print(i)
			elif choice2 == 2:
				print('Returning to main menu.')
				
#Saves the markbook before terminating the program
outfile = open('Markbook.txt', 'w')
for i in markbook.keys():
	outfile.write('<'+ i + '\n')
	for mark in markbook[i]:
		outfile.write(mark[0] + ', ' + str(mark[1]) + '\n')
	outfile.write('>\n' )
outfile.close()