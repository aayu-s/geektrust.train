from station import Station

class Route:
    route_dict = {}
    @staticmethod
    def create_stations(stations):
        route = {}
        for elem in stations:
            route[elem[2]] = Station(elem[0], elem[1], elem[2], elem[3])
        return route

    @staticmethod
    def get_route():
        print("No route found!")

    @staticmethod
    def register_routes():
        Route_for_A.create_route()
        Route_for_B.create_route()


class Route_for_A(Route):
    route_A = {}
    @staticmethod
    def create_route():
        stations = list()
        source = 'CHN'
        stations.append([0, 'CHENNAI', 'CHN', source])
        stations.append([350, 'SALEM', 'SLM', source])
        stations.append([550, 'BANGALORE', 'BLR', source])
        stations.append([900, 'KURNOOL', 'KRN', source])
        stations.append([1200, 'HYDERABAD', 'HYB', source])
        stations.append([1600, 'NAGPUR', 'NGP', source])
        stations.append([1900, 'ITARSI', 'ITJ', source])
        stations.append([2000, 'BHOPAL', 'BPL', source])
        stations.append([2500, 'AGRA', 'AGA', source])
        stations.append([2700, 'NEW DELHI', 'NDL', source])
        Route_for_A.route_A = Route.create_stations(stations)

    @staticmethod
    def get_route():
        return Route_for_A.route_A


class Route_for_B(Route):
    route_B = {}
    @staticmethod
    def create_route():
        stations = list()
        source = 'TVC'
        stations.append([0, 'TRIVANDRUM', 'TVC', source])
        stations.append([300, 'SHORANUR', 'SRR', source])
        stations.append([600, 'MANGALORE', 'MAQ', source])
        stations.append([1000, 'MADGAON', 'MAO', source])
        stations.append([1400, 'PUNE', 'PNE', source])
        stations.append([2000, 'HYDERABAD', 'HYB', source])
        stations.append([2400, 'NAGPUR', 'NGP', source])
        stations.append([2700, 'ITARSI', 'ITJ', source])
        stations.append([2800, 'BHOPAL', 'BPL', source])
        stations.append([3800, 'PATNA', 'PTA', source])
        stations.append([4200, 'NEW JALPAIGURI', 'NJP', source])
        stations.append([4700, 'GUWAHATI', 'GHY', source])
        Route_for_B.route_B = Route.create_stations(stations)

    @staticmethod
    def get_route():
        return Route_for_B.route_B
