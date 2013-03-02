import time
def Main():
    filename = "100_PANA_0.ply"
    fin = open(filename, "r")
    fout = open("new_mesh.ply", "w")
    header_count = 10
    header = []
    points_x = []
    points_y = []
    points_z = []
    points_r = []
    points_g = []
    points_b = []
    points = []
    new_points = []
    count = 0 
    time1 = time.time()
    for line in fin:
        if header_count > 0:
            line = line[:-1]
            header.append(line)
            header_count -= 1
            continue
        values = line.split()
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        r = int(values[3])
        g = int(values[4])
        b = int(values[5])
        points.append([x,y,z,r,g,b])
        points.sort()
        points_x.append(points[0][0])
        points_y.append(points[0][1])
        points_z.append(points[0][2])
        points_r.append(points[0][3])
        points_g.append(points[0][4])
        points_b.append(points[0][5])
        count += 1
        if count == 5000:
            print "5,000"
            time2 = time.time()
            print time2 - time1
            print
        if count == 10000:
            print "10,000"
            time3 = time.time()
            print time3 - time2
            print
        if count == 15000:
            print "15,000"
            time4 = time.time()
            print time4 - time3
            print
        if count == 20000:
            print "20,000"
            time5 = time.time()
            print time5 - time4
            print
        if count == 25000:
            print "25,000"
            time6 = time.time()
            print time6 - time5
            print
        if count == 30000:
            print "30,000"
            time7 = time.time()
            print time7 - time6
            print
        if count == 100000:
            print "100,000"
            time8 = time.time()
            print time8 - time7
            print
        if count == 150000:
            print "150,000"
            time9 = time.time()
            print time9 - time8
            print
        if count == 180000:
            print "180,000, almost done"
            time10 = time.time()
            print time10 - time9
            print
        
    print "done with first part"
    time11 = time.time()
    print time11 - time10
    print "Total time: ", (time11 - time1)
    for i in range(len(points_x)-2):
        if i == (len(points_x)-1):
            break
        if points_x[i] == points_x[i+1]:
            if points_y[i] == points_y[i+1]:
                if points_z[i] <  points_z[i+1]:
                        new_r = (points_r[i] + points_r[i+1]) / 2
                        new_g = (points_g[i] + points_g[i+1]) / 2
                        new_b = (points_b[i] + points_b[i+1]) / 2
                        new_z = (points_z[i+1] + points_z[i]) / 2
                        new_points.append([points_x[i], points_y[i], new_z, new_r, new_g, new_b])
                        continue
                if points_z[i] > points_z[i+1]:
                        new_r = (points_r[i] + points_r[i+1]) / 2
                        new_g = (points_g[i] + points_g[i+1]) / 2
                        new_b = (points_b[i] + points_b[i+1]) / 2
                        new_z = (points_z[i] + points[i+1]) / 2
                        new_points.append([points_x[i], points_y[i], new_z, new_r, new_g, new_b])
                        continue
            if points_z[i] ==  points_z[i+1]:
                if points_y[i] <  points_y[i+1]:
                        new_r = (points_r[i] + points_r[i+1]) / 2
                        new_g = (points_g[i] + points_g[i+1]) / 2
                        new_b = (points_b[i] + points_b[i+1]) / 2
                        new_y = (points_y[i+1] + points_y[i]) / 2
                        new_points.append([points_x[i], new_y, points_z[i], new_r, new_g, new_b])
                        continue
                if points_y[i] >  points_y[i+1]:
                        new_r = (points_r[i] + points_r[i+1]) / 2
                        new_g = (points_g[i] + points_g[i+1]) / 2
                        new_b = (points_b[i] + points_b[i+1]) / 2
                        new_y = (points_y[i] + points_y[i+1]) / 2
                        new_points.append([points_x[i], new_y, points_z[i], new_r, new_g, new_b])
                        continue
        if points_y[i] == points[i+1]:
            if points_z[i] == points[i+1]:
                if points_x[i] <  points_x[i+1]:
                        new_r = (points_r[i] + points_r[i+1]) / 2
                        new_g = (points_g[i] + points_g[i+1]) / 2
                        new_b = (points_b[i] + points_b[i+1]) / 2
                        new_x = (points_x[i+1] + points_x[i]) / 2
                        new_points.append([new_x, points_y[i], points_z[i], new_r, new_g, new_b])
                        continue
                if points_x[i] >  points_x[i+1]:
                        new_r = (points_r[i] + points_r[i+1]) / 2
                        new_g = (points_g[i] + points_g[i+1]) / 2
                        new_b = (points_b[i] + points_b[i+1]) / 2
                        new_x = (points_x[i] + points_x[i+1]) / 2
                        new_points.append([new_x, points_y[i], points_z[i], new_r, new_g, new_b])
                        continue
    for h in header:
        print >>fout, h
    for p in range(len(points)-1):
        print >>fout, points[p][0], points[p][1], points[p][2], points[p][3], points[p][4], points[p][5]
    for n in range(len(new_points)-1):
        print >>fout, new_points[n][0], new_points[n][1], new_points[n][2], new_points[n][3], new_points[n][4], new_points[n][5]
        fin.close()
        fout.close()


Main()
