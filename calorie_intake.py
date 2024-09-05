def user_info():
    
    height = int(input("please enter your height (in inches): "))
    weight = int(input("please enter your weight (in pounds): "))
    age = int(input("Please enter your age: "))
    
    #empty string for gender
    gender = ''
    #while loop to make sure gender is either m or f
    while gender not in ['m', 'f']:
        gender = input("Please enter your gender(m or f): ")
        #the if statement is to make sure the user enters m or f
        if gender not in['m', 'f']:
            print('Please enter your age or gender m for male or f for female.')

    #empty string for weight goal
    weight_goal = ''
    #while loop to make sure weight goal is either gain, lose, or maintain
    while weight_goal not in ['gain', 'lose', 'maintain']:
        weight_goal = input('Would you like to gain, lose, or maintain weight? ')
        #the if statement is to make sure the user enters gain, lose, or maintain
        if weight_goal not in ['gain', 'lose', 'maintain']:
            print('Please enter if you would like to gain, lose, or maintain weight.')

    activity_level = ''
    #while loop to make sure activity goal is either 'none', 'light', 'moderate', 'heavy', 'extreme'
    while activity_level not in ['none', 'light', 'moderate', 'heavy', 'extreme']:
        activity_level = input('Please enter your activity level (none, light, moderate, heavy, or extreme): ')
        #the if statement is to make sure the user enters 'none','light', 'moderate', 'heavy', 'extreme'
        if weight_goal not in ['none','light', 'moderate', 'heavy', 'extreme']:
            print('Please enter your activity level (none, light, moderate, heavy, or extreme).')

    return height, age, gender, weight, weight_goal, activity_level

def calculates_bmr(height, age, gender, weight):
    if gender =='m':
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calorie_calculated(weight_goal, activity_level, bmr):

    if activity_level == 'none':
        calorie_intake = bmr * 1.2
    elif activity_level =='little':
        calorie_intake = bmr * 1.375
    elif activity_level == 'moderate':
        calorie_intake = bmr * 1.55
    elif activity_level == 'heavy':
        calorie_intake = bmr * 1.725
    elif activity_level == 'extreme':
        calorie_intake = bmr * 1.9
    

    if weight_goal == 'gain':
        calorie_intake += 500
    elif weight_goal == 'lose':
        calorie_intake -= 500

    #turns calorie intake into an integer
    calorie_intake = int(calorie_intake)

    return calorie_intake
    
def main():
    height, age, gender, weight, weight_goal, activity_level = user_info()
    bmr = calculates_bmr(height, age, gender, weight)
    calorie_intake = calorie_calculated(weight_goal, activity_level, bmr)
    print('Based on your weight goal to', weight_goal, 'weight and your activity level being', activity_level, 'your calorie intake should be',f"{calorie_intake:,}", 'per day.')

main()

