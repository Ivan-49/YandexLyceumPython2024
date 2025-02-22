def quarter(xcoord, ycoord):
    chetv = [1, 2, 3, 4]
    if xcoord > 0 and ycoord > 0:
        print(f"{'I' * chetv[0]} четверть")
    elif xcoord < 0 and ycoord > 0:
        print(f"{'I' * chetv[1]} четверть")
    elif xcoord < 0 and ycoord < 0:
        print(f"{'I' * chetv[2]} четверть")
    elif xcoord > 0 and ycoord < 0:
        print(f"{'IV'} четверть")
