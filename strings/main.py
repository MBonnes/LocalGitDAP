# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
eerste_score = "Ruud Gullit"
tweede_score = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = eerste_score + " " + str(goal_0) + ", " + tweede_score + " " +  str(goal_1)
print (scorers)

report = eerste_score + " scored in the " + str(goal_0) + "nd minute" + "\n" + tweede_score + " scored in the " + str(goal_1) + "th minute"

print(report)

player = "Ronald Koeman"
first_name = player[:(player.find(" "))]
print(first_name)

last_name_len = len(player[(player.find(" "))+1:len(player)])
print(last_name_len)

name_short = player[0] + ". " + player[(player.find(" "))+1:len(player)]
print(name_short)

chanttest = "Gut! "*3
print (chanttest)

chant = ((first_name + "! ")*(len(first_name))).rstrip()
print(chant)
good_chant = (chant[len(chant)-1]!=" ")
print(good_chant)