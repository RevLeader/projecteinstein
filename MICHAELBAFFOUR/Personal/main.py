#working on student report
def student_score():
    print('WELCOME TO YOUR SCORE DASHBORD')
    score = int(input('Enter your score here\n Student score: '))
    if score >= 90 and score <= 100:
       return 'Passed successfully'
    elif score >= 80 and score < 90:
        return 'Grade B' 
    elif score >= 70 and score < 80:
        return 'Grade C'
    elif score < 70:
        return 'Failed'
    else:
        return 'Error'

print(student_score())
    
