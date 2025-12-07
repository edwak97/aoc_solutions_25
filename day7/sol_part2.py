if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        lines = [list(line.strip()) for line in file.readlines()]
    existing_beams = {lines[0].index('S'):1}
    timeline_count = 1
    for i in range(1, len(lines)):
        beams_to_remove, beams_to_write = [], dict()
        for k in existing_beams:
            if lines[i][k] == '^':
                beams_to_remove.append(k)
                if (k-1) in beams_to_write:
                    beams_to_write[k-1] += existing_beams[k]
                else:
                    beams_to_write[k-1] = existing_beams[k]
                if (k+1) in beams_to_write:
                    beams_to_write[k+1] += existing_beams[k]
                else:
                    beams_to_write[k+1] = existing_beams[k]
                timeline_count += existing_beams[k]
        for k in beams_to_remove:
            del existing_beams[k]
        for k in beams_to_write:
            if k in existing_beams:
                existing_beams[k] += beams_to_write[k]
            else:
                existing_beams[k] = beams_to_write[k]
    print(timeline_count)
