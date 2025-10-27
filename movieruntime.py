"""
Sometimes, if my brain is fried, I'd use it.  
"""
from datetime import datetime, timedelta
import pytz

def when():
    timezone = pytz.timezone('America/Chicago')
    
    try:
        runtime_minutes = int(input("How long is the movie in minutes? "))
    except ValueError:
        print("Please enter a valid number.")
        return
      
    while True:
        theater_option = input("Are you watching it in the theaters? Type '1' to add 20 minutes of ad time. Else, type '2': ").strip()
        if theater_option in ['1', '2']:
            break
        else:
            print("Invalid option. Please enter '1' or '2'.") 
    
    # Add 20 minutes if watching in theaters
    if theater_option == '1':
        runtime_minutes += 20
        print(f"Total time including ads: {runtime_minutes} minutes")

    while True:
        option = input("Type '1' to watch now, or '2' to specify a time: ").strip()
        if option in ['1', '2']:
            break
        else:
            print("Invalid option. Please enter '1' or '2'.")
    
    if option == '2':
        while True:
            start_time_str = input("When will you watch it? (e.g., 9:00): ").strip()
            try:
                start_time = datetime.strptime(start_time_str, '%I:%M').time()
                now = datetime.now(timezone)
                start_datetime = timezone.localize(datetime.combine(now.date(), start_time))
                break  
            except ValueError:
                print("Invalid time format. Please use format like '9:00'")
    else:
        start_datetime = datetime.now(timezone)
    
    end_datetime = start_datetime + timedelta(minutes=runtime_minutes)
    print(f"You will be done at {end_datetime.strftime('%I:%M')}")

if __name__ == "__main__":
    when()
