# script to calculate body fat

from fitness_tools.composition.bodyfat import DurninWomersley
data = DurninWomersley(24, 'female', (5, 7, 8, 12))
data.body_density()
print("body fat percentage: " + str(data) )
print("script executed successfully")
