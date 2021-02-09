# I/P: {[AT, NY], [LV, CH], [SF, LV], [CH, AT]}
# O/P: {[SF, LV], [LV, CH], [CH, AT], [AT, NY]}

input_list = [['AT', 'NY'], ['LV', 'CH'], ['SF', 'LV'], ['CH', 'AT']]
itinerary = []
source = []
destination = []
for flight in input_list:
    source.append(flight[0])
    destination.append(flight[1])

for i in range(0, len(source)-1):
    if source[i] not in destination:
        start_flight = input_list[i]
        break

print(f'starting flight is {start_flight}')
itinerary.append(start_flight)


while len(input_list) > len(itinerary):
    connecting_flight_source = itinerary[-1][1]
    connecting_flight_index = source.index(connecting_flight_source)
    next_flight = input_list[connecting_flight_index]
    itinerary.append(next_flight)
print(f'Dear passenger, your itinerary is {itinerary}')