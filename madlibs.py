"""this program takes 2 nouns, 2 verbs and 1 adjective1 as inputs from the user and inserts them into a story outline"""

def get_input(word_type):
    user_input=input(f"Enter a {word_type}: ")
    return user_input

noun1=get_input("noun")
adjective1=get_input("adjective1")
noun2=get_input("noun")
verb1=get_input("verb")
verb2=get_input("verb")

story_outline=f"""One day, {noun1} decided to {verb1} to the {noun2}. Along the way, they saw a {noun2} {verb1} in the {noun2}. It was a {adjective1} sight!

When they reached the {noun2}, they {verb2} a {noun2} and decided to {verb1} with it. Suddenly, a {noun2} appeared and started to {verb1} around them. {noun1} quickly {verb2} and {verb2} to {verb1} the {noun2}.

Later, {noun1} went to a nearby {noun2} to {verb1} some {noun2}. They met {noun2} there, who was {verb1}ing a {noun2}. Together, they {verb2} and {verb2} all afternoon.

As the sun set, {noun1} and {noun2} decided to {verb1} back to the {noun2}. They {verb2} about the day and how {adjective1} it was to {verb1} so many {noun2}.

When they finally reached home, {noun1} {verb2} and {verb2} into bed, feeling {adjective1} about the {noun2} they had {verb2}. It was truly an adventure to remember!"""

print(story_outline)