#LIST-ALGO :  THE SMALLEST NUMBER IN THE LIST
distance_driver_km =[1.5,     2.2,    0.4,       0.9,  4.3]
driver_names =      ["John", "Doe", "dariste", "jean","paul"]
#index_min 
distance_min =distance_driver_km[0]
for distance in distance_driver_km:
    if distance < distance_min:
        distance_min = distance
        index_min = distance_driver_km.index(distance_min)
        
print("the smallest distance is: " +str(distance_min))
print("the driver is: " +driver_names[index_min])
