"""
Student Name: 
Class: Computer Programming 1
Period: BX
Project 1: The Barbie Movie
"""

def beach_day_challenge():
    print("\nBeach Day Challenge")
    print("Barbie and her friends are spending a day at the beach.")
    print("They want to manage their expenses.")

    # ---------------------------------------------- BEGIN CODE ----------------------------------------------------- #

    """
    Prompt the user for the following:
    -- Number of people in the group
    -- Cost of beach chairs
    -- Cost of sunscreen
    -- Cost of ice cream
    -- Cost of beach toys
    
    Convert the user input to the appropriate data type (int for number of people, float for costs).
    """

    num_people = 0
    beach_chairs_cost = 0
    sunscreen_cost = 0
    ice_cream_cost = 0
    beach_toys_cost = 0

    """
    Calculate the total cost of the beach day that includes all items.
    """

    total_cost = 0

    """
    Apply discounts:
    -- 20% discount on beach chairs
    -- 10% discount on ice cream
    Calculate the discounted costs and the new total cost including discounts.
    """

    discounted_total_cost = 0

    """
    Calculate each person's share of the costs.
    """

    each_person_share = 0

    # ----------------------------------------------- END CODE ------------------------------------------------------ #

    print(f"\nTotal cost before discounts: ${total_cost:.2f}")
    print(f"Total cost after discounts: ${discounted_total_cost:.2f}")
    print(f"Each person's share: ${each_person_share:.2f}")
    
    return total_cost, discounted_total_cost, each_person_share, num_people

def escape_plan_challenge():
    print("\nEscape Plan Challenge")
    print("Barbie, Ken, and Gloria need to devise an escape plan.")
    print("They have three escape routes to consider.")

    # ---------------------------------------------- BEGIN CODE ----------------------------------------------------- #

    """
    For each of the 3 escape routes, prompt the user to enter:
    -- Distance in miles
    -- Speed in mph
    
    Convert the input values to float.
    """

    route1_distance = 0
    route1_speed = 0

    route2_distance = 0
    route2_speed = 0

    route3_distance = 0
    route3_speed = 0

    """
    Calculate the time taken for each escape route.
    Time taken is distance divided by speed.
    """

    time_route1 = 0
    time_route2 = 0
    time_route3 = 0

    """
    Determine which escape route takes the shortest amount of time.
    """

    fastest_route = 0

    """
    Calculate the time saved by choosing the fastest route compared to the slowest route.
    """

    time_saved = 0

    # ----------------------------------------------- END CODE ------------------------------------------------------ #

    print(f"\nTime required for Route 1: {time_route1:.2f} hours")
    print(f"Time required for Route 2: {time_route2:.2f} hours")
    print(f"Time required for Route 3: {time_route3:.2f} hours")
    print(f"The fastest route takes {fastest_route:.2f} hours.")
    print(f"Time saved by choosing the fastest route: {time_saved:.2f} hours")
    
    return time_route1, time_route2, time_route3, fastest_route, time_saved

def society_reformation_challenge():
    print("\nSociety Reformation Challenge")
    print("Barbie returns to Barbieland to reform the society.")
    print("She wants to implement changes to promote equality and fairness.")

    # ---------------------------------------------- BEGIN CODE ----------------------------------------------------- #

    """
    Prompt the user to enter:
    -- Number of proposed societal changes
    -- Number of successfully implemented changes
    
    Convert the user input values to int.
    """

    total_proposed_changes = 0
    successful_changes = 0

    """
    Calculate the percentage of societal changes that were successfully implemented.
    """

    success_rate = 0

    """
    Calculate how many additional changes need to be implemented to achieve a 75% success rate.
    """

    needed_changes = 0

    """
    Calculate the remaining changes to be implemented.
    This is the difference between the total proposed changes and the successful changes.
    """

    remaining_changes = 0

    # ----------------------------------------------- END CODE ------------------------------------------------------ #

    print(f"\nPercentage of successful changes: {success_rate:.2f}%")
    print(f"Number of additional changes needed to achieve a 75% success rate: {needed_changes}")
    print(f"Remaining changes to be implemented: {remaining_changes}")
    
    return success_rate, needed_changes, remaining_changes
    
# Main program to run all challenges
def main():
    beach_day_challenge()
    escape_plan_challenge()
    society_reformation_challenge()


if __name__ == "__main__":
    main()
