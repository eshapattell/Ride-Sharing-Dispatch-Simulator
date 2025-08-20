from simulator import Driver, Rider, RideRequest, RideDispatchSystem

# Initialize system
system = RideDispatchSystem()

# Register drivers
system.register_driver(Driver(driver_id="D1", location=(0, 0), rating=4.7))
system.register_driver(Driver(driver_id="D2", location=(5, 5), rating=4.8))
system.register_driver(Driver(driver_id="D3", location=(2, 3), rating=4.9))

# Register riders
r1 = Rider(rider_id="R1", location=(3, 4))
r2 = Rider(rider_id="R2", location=(7, 1))
system.register_rider(r1)
system.register_rider(r2)

# Enqueue ride requests
system.enqueue_request(RideRequest(rider=r1, drop_location=(8, 2)))
system.enqueue_request(RideRequest(rider=r2, drop_location=(6, 9)))

# Dispatch rides
ride1 = system.dispatch()
ride2 = system.dispatch()

# Complete first ride
if ride1:
    system.complete_ride(ride1.ride_id)

# Show history
system.show_history()
