try:
    score = int(input("Enter your test score (0-100): "))

    if score >= 90:
          print("Grade: A - VERY GOOD")
    elif score >= 80:
          print("Grade: B - GOOD JOB")
    elif score >= 70:
          print("Grade: C - GOOD")
    elif score >= 60:
          print("Grade: D - NICE TRY")
    else:
          print("Grade: F - VERY GOOFYY")
 
except ValueError:
   print("Invalid!! PLEASE ENTER A NUMBER 0-100")  