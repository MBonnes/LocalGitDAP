# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet (name, template='Hello, <name>!') :
    result = template.replace("<name>",name)
    return result

#print(greet('Doc'))
#print(greet('Bob', "What's up, <name>!"))

"""
Your implementation should support all 11 bodies listed on the reference website given above (in lowercase). 
Make sure you process these bodies with the correlated gravity factor in a dictionary. 
Before using the gravity of a celestial body round its gravity factor to 1 decimal. 
You can "hardcode" this, for example: the gravity of Earth becomes 9.8.
force = mass × gravity
https://www.smartconversion.com/otherInfo/gravity_of_planets_and_the_sun.aspx
"""
def force (mass, body='earth') :
    body_gravities = {  "sun" :	274,
                        "jupiter" :	24.9,
                        "neptune" :	11.2,
                        "saturn" :	10.4,
                        "earth" :	9.8,
                        "uranus" :	8.9,
                        "venus" :	8.9,
                        "mars" :	3.7,
                        "mercury" :	3.7,
                        "moon" :	1.6,
                        "pluto" :	0.6}
    force = body_gravities[body]*mass
    return force

""""
pull = G × ((m1×m2)/d2)
m1 An object's mass in kg (float)
m2 Another object's mass in kg (float)
d Their distance in meters (float)
G is the gravitational constant, approximately 6.674×10-11 N m2/kg2
"""
def pull(m1,m2,d) :
    G=6.674*(10**(-11))
    result = G*((m1*m2)/(d**2))
    return result

#print(pull(800,1500,3))
