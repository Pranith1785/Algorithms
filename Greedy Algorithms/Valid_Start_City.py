### Problem Statement
'''
Write a function that returns the starting city number(index) from where you can visit all the cities 
and return to the starting city with 0 or more litres of fuel left.

Note : 1. Assume cities are connected in circular - last city is connected back to first way
       2. Given distance b/w the cities
       3. fuel available in each city 
       4. you will start with 0 litres of fuel
       5. given mileage per litre
       6. if not possible starting point then return -1

city[i] is the distance to city[i+1]
and fuel[i] is available litres of fuel in that city

Examples :  cities distance = [5, 25, 15, 10, 15]
            fuel = [1, 2, 1, 0, 3]
            mileage = 10

            Ans = 4 // start from index 4 i.e city 5
'''

### Solution - 1
## Time - O(n^2)| Space - O(1)

def validStartCity(cities,fuel, mileage):

    fuel = [val * mileage for val in fuel]
    for i in range(len(cities)):
        tank = 0
        tour = True
        newcities = cities[i:] + cities[:i]
        fuelRange = fuel[i:] + fuel [:i]
        for j in range(len(newcities)) :
            tank += fuelRange[j]
            if tank < newcities[j] :
                tour = False
                break
            tank -= newcities[j]
        if tour:
            return i    
    return -1


distance = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mileage = 10

print(validStartCity(distance,fuel,mileage))


        









