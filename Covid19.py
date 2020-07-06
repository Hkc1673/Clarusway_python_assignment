age=(input("Are you a cigarette addict older than 75 years old? True/False: ").title())== "Yes"

chronic=(input("Do you have a severe chronic disease? True/False: ").title())== "Yes"

immune=(input("Is your immune system too weak? True/False: ").title())=="Yes"

if age or chronic or immune:

    print("You are in risky group")

else:

    print("You are not in risky group")
