
# SET Covering Problem
# figure out the smallest set of stations you can play to cover all states? you need to pay to play a station

# can ideally be solved by taking the combinations of all stations, figure out the minimum combo of stations that covers
# maximum states but this end up running in O(2 ^ n) which is exponential. Greedy algorithms can provide a pretty good
# approximations and can be best fit as an approximation algorithm. Also its easy to implement and took O(n ^ 2) time which is quadratic.


# Approximation Algorithm (Greedy solution)

stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"]),
}
states_needed = set(["id", "nv", "ut", "wa", "mt", "or", "ca", "az"])

final_stations = set()
while states_needed:
    states_covered = set()
    best_station = None
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
