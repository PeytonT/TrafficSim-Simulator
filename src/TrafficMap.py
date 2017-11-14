import random
from src.drivers.DriverTemplate import *
from src.vehicles.VehicleTemplate import *

class TrafficMap:
    """
    :type roadlist: list(Road)
    """
    def __init__(self):

        self.roadlist = []
        self.intersectionlist = []

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
            if self.roadlist[i].chance_spawn >= random.random():
                if random.random() > .5:
                    if random.randint(0, 1):
                        self.roadlist[i].spawn(VehicleTemplate(),DriverTemplate(),'outbound')
                    else:
                        self.roadlist[i].spawn(VehicleTemplate(),DriverTemplate(),'inbound')
                else:
                    if random.randint(0, 1):
                        self.roadlist[i].spawn(VehicleTemplate(), SlowDriver(),'outbound')
                    else:
                        self.roadlist[i].spawn(VehicleTemplate(), SlowDriver(), 'inbound')

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