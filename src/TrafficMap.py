import random
from src.drivers.DriverTemplate import *
from src.vehicles.VehicleTemplate import *
from src.Reporter import Reporter

class TrafficMap:
    """
    :type roadlist: list(Road)
    """
    def __init__(self):

        self.roadlist = []
        self.intersectionlist = []
        self.reporter = Reporter()

    def add_road(self, road):
        road.set_name(len(self.roadlist))
        road.set_reporter(self.reporter)
        self.reporter.create_road_entry(len(self.roadlist))
        print(self.reporter.road_report_table.keys())
        self.roadlist.append(road)
        return

    def add_intersection(self, intersection):
        intersection.set_name(len(self.intersectionlist))
        intersection.set_reporter(self.reporter)
        self.reporter.create_intersection_entry(len(self.intersectionlist))
        print(self.reporter.intersection_report_table.keys())
        self.intersectionlist.append(intersection)

    def get_roads(self):
        """
        :return: a list of all roads in the map
        :rtype: list(Road)
        """
        return self.roadlist

    def get_intersections(self):
        """
        :return: list of all intersections in the map
        :rtype: list(Road)
        """
        return self.intersectionlist

    def tick(self, ticktime_ms):
        """
        :type ticktime_ms: float
        :return: None
        """
        for i in range(len(self.roadlist)):
            self.roadlist[i].tick(ticktime_ms)

        for i in range(len(self.intersectionlist)):
            self.intersectionlist[i].tick(ticktime_ms)

    def tock(self, ticktime_ms):
        """
        :type ticktime_ms: float
        :return:
        """
        for i in range(len(self.roadlist)):
            self.roadlist[i].tock_positions()

        for i in range(len(self.intersectionlist)):
            self.intersectionlist[i].tock_positions()

        for i in range(len(self.roadlist)):
            self.roadlist[i].tock_crashes()

        for i in range(len(self.intersectionlist)):
            self.intersectionlist[i].tock_crashes()

    def report(self, compact = True, output_file = None):
        if compact:
            self.reporter.generate_compact_report(output_file)
        else:
            self.reporter.generate_complete_report(output_file)