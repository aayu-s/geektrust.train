import heapq
from station import Station
from train import Train
from route import Route_for_A, Route_for_B


class Services:
    @staticmethod
    def get_train_and_bogies(text):
        split_text = text.split()
        train_name = split_text[0]
        bogies = list()
        for elem in split_text[1:]:
            bogies.append(elem)
        return train_name, bogies

    @staticmethod
    def read_file(input_file):
        trains = list()
        # parse the file data
        train_id = 1
        with open(input_file) as fp:
            lines = fp.readlines()
            for line in lines:
                train_name, bogies = Services.get_train_and_bogies(line)
                if train_id == 1:
                    source, destination = 'CHN', 'NDL'
                elif train_id == 2:
                    source, destination = 'TVC', 'GHY'

                train = Train(train_id, train_name, bogies, source, destination)
                trains.append(train)
                train_id += 1
        return trains
    @staticmethod
    def print_path_till_hyb(trains):
        new_stations = list()
        for train in trains:
            at_hyb = get_bogie_at('PPP', train)
            if at_hyb == 'E01':
                return 'Invalid Station'
            print('ARRIVAL', train.name, *at_hyb, sep=' ')
            new_stations.append(at_hyb)

        return new_stations

    @staticmethod
    def get_merged_bogies(trains):
        train1 = trains[0]
        train2 = trains[1]
        route1 = Route_for_A.get_route()
        route2 = Route_for_B.get_route()
        dist1 = route1['HYB'].dist_frm_source
        dist2 = route2['HYB'].dist_frm_source
        temp = list()
        heapq.heapify(temp)

        for elem in train1:
            if elem=='ENGINE':
                heapq.heappush(temp, [-10**6, elem])
            if elem in route1:
                heapq.heappush(temp, [-1*abs(dist1-route1[elem].dist_frm_source), elem])
            elif elem in route2:
                heapq.heappush(temp, [-1*abs(dist2-route2[elem].dist_frm_source), elem])

        for elem in train2:
            if elem=='ENGINE':
                heapq.heappush(temp, [-10**6, elem])
            if elem in route2:
                heapq.heappush(temp, [-1*abs(dist2-route2[elem].dist_frm_source), elem])
            elif elem in route1:
                heapq.heappush(temp, [-1*abs(dist1-route1[elem].dist_frm_source), elem])

        ans=list()

        while len(temp)>0:
            n=heapq.heappop(temp)
            ans.append(n[1])

        return ans

    @staticmethod
    def get_bogie_at(at_station, train):
        if train.train_id == 1:
            route_list = Route_for_A.get_route()
        elif train.train_id == 2:
            route_list = Route_for_B.get_route()

        if at_station in route_list:
            dist = route_list[at_station].dist_frm_source
        else:
            return 'E01'

        values = list()
        for i in range(len(train.bogies)):
            if train.bogies[i] in route_list and route_list[train.bogies[i]].dist_frm_source <= dist:
                continue
            else:
                values.append(train.bogies[i])

        return values

    @staticmethod
    def check_valid_file(input_file):
        file_size = os.path.getsize(input_file)
        if file_size == 0:
            return False
        return True


















