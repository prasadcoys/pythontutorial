# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

speedOfLightInMetersPerSecond = 299792458
centimeters = 100
nanosecond = 1.0/1000000000
speedOfLightInCentimetersPerNanoSecond = speedOfLightInMetersPerSecond * centimeters * nanosecond
print speedOfLightInCentimetersPerNanoSecond

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion
nanodistance = speed_of_light/nano_per_sec
print nanodistance