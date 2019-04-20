def sort(intervals):
    map = {}
    for interval in intervals:
        map[interval[1]] = interval

    intervals.clear()
    intervals.extend([map[key] for key in sorted(map.keys())])


def max_intervals(intervals):
    sort(intervals)

    set = [intervals[0]]
    i = 0
    for j in range(len(intervals)):
        if intervals[j][0] >= set[i][1]:
            set.append(intervals[j])
            i += 1
    return set


if __name__ == '__main__':
    intervals = [(1,2),(0,6),(3,4),(5,9),(5,7),(8,9)]
    print(max_intervals(intervals))
