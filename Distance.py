import csv
import datetime

distance_data_list = []


def load_distance_data(file_name):
    with open(file_name) as distance_list:
        distance_data = list(csv.reader(distance_list, delimiter=','))
    with open(file_name) as distance_list_2:
        distance_data_2 = list(csv.reader(distance_list_2, delimiter=','))

        def get_address():
            return distance_data_2

        def get_distance(row, col, total):
            distance = distance_data[row][col]
            if distance == '':
                distance = distance_data[col][row]
            return total + float(distance)

        def get_distance_from_location(row, col):
            location_distance = distance_data[row][col]
            if location_distance == '':
                location_distance = distance_data[col][row]
            return float(location_distance)

        def get_time(distance, truck_list):
            new_time = distance / 18
            minute_distance = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
            end_time = minute_distance + ':00'
            truck_list.append(end_time)
            total = datetime.timedelta()
            for i in truck_list:
                (hours, minutes, seconds) = i.split(':')
                total += datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
            return total

        print(distance_data)
        print(distance_data_2)


load_distance_data('Data/WGUPS_Distance_Table.csv')
