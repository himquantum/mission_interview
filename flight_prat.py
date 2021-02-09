ll = [['AT', 'NY'], ['LV', 'CH'], ['SF', 'LV'], ['CH', 'AT']]

xx = [each for ele in ll for each in ele]
print(xx)
temp_d = {}
for ele in xx:
    if ele not in temp_d:
        temp_d[ele] = 1
    else:
        temp_d[ele] += 1
end_points = [k for k, v in temp_d.items() if v==1]
print("end_points -", end_points)

for city in end_points:
    for x in ll:
        if city in x and x.index(city) == 0:
            source = x
        if city in x and x.index(city) == 1:
            destination = x
print("source, destination - {}, {}".format(source, destination))

flight = source
new_itinerary = [flight]
for x in ll:
    if flight[1] == x[0]:
        flight = x
        new_itinerary.append(flight)
new_itinerary.append(destination)
print(new_itinerary)