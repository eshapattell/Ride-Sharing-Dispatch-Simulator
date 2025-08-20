from dataclasses import dataclass, field
from collections import deque
import heapq
import time
import math


@dataclass
class Driver:
    driver_id: str
    location: tuple  # (x, y)
    rating: float
    available: bool = True
    join_time: float = field(default_factory=time.time)  # tie-breaker


@dataclass
class Rider:
    rider_id: str
    location: tuple  # (x, y)


@dataclass
class RideRequest:
    rider: Rider
    drop_location: tuple  # (x, y)
    request_time: float = field(default_factory=time.time)


@dataclass
class RideHistory:
    ride_id: int
    rider_id: str
    driver_id: str
    pickup: tuple
    drop: tuple
    distance: float
    fare: float
    timestamp: float = field(default_factory=time.time)


class RideDispatchSystem:
    def _init_(self):
        self.drivers = {}
        self.riders = {}
        self.requests = deque()  # queue for ride requests
        self.ride_history = []
        self.ride_counter = 0

    def register_driver(self, driver: Driver):
        self.drivers[driver.driver_id] = driver
        print(f"Driver registered: {driver}")

    def register_rider(self, rider: Rider):
        self.riders[rider.rider_id] = rider
        print(f"Rider registered: {rider}")

    def enqueue_request(self, request: RideRequest):
        self.requests.append(request)
        print(f"Enqueued Request: {request.rider.rider_id} -> {request.drop_location}")

    def _calculate_distance(self, loc1, loc2):
        return math.sqrt((loc1[0] - loc2[0])*2 + (loc1[1] - loc2[1])*2)

    def dispatch(self):
        if not self.requests:
            print("No ride requests in queue.")
            return None

        request = self.requests.popleft()
        available_drivers = [
            d for d in self.drivers.values() if d.available
        ]

        if not available_drivers:
            print("No available drivers right now.")
            return None

        # Build a heap with priority: distance, -rating, join_time
        heap = []
        for d in available_drivers:
            distance = self._calculate_distance(request.rider.location, d.location)
            heapq.heappush(heap, (distance, -d.rating, d.join_time, d))

        # Best driver
        _, _, _, chosen_driver = heapq.heappop(heap)
        chosen_driver.available = False

        # Calculate fare
        trip_distance = self._calculate_distance(request.rider.location, request.drop_location)
        fare = round(trip_distance * 8.5, 2)

        self.ride_counter += 1
        ride = RideHistory(
            ride_id=self.ride_counter,
            rider_id=request.rider.rider_id,
            driver_id=chosen_driver.driver_id,
            pickup=request.rider.location,
            drop=request.drop_location,
            distance=trip_distance,
            fare=fare
        )
        self.ride_history.append(ride)

        print(f"Assigned: Rider {request.rider.rider_id} -> Driver {chosen_driver.driver_id} (dist={trip_distance:.2f}, rating={chosen_driver.rating})")
        return ride

    def complete_ride(self, ride_id):
        for ride in self.ride_history:
            if ride.ride_id == ride_id:
                driver = self.drivers[ride.driver_id]
                driver.available = True
                driver.location = ride.drop
                print(f"Ride completed: {ride}")
                return ride
        print("Ride not found.")
        return None

    def show_history(self):
        print("\nRide History:")
        for ride in self.ride_history:
            print(f"Ride {ride.ride_id}: Rider={ride.rider_id}, Driver={ride.driver_id}, Distance={ride.distance:.2f}, Fare=₹{ride.fare}")
