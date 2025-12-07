if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        lines = [list(line.strip()) for line in file.readlines()]
    existing_beams = {lines[0].index('S')}
    split_count = 0
    for i in range(1, len(lines)):
        beams_to_remove, beams_to_write_next = [], []
        for beam in existing_beams:
            if lines[i][beam] == '^':
                split_count += 1
                beams_to_remove.append(beam)
                if (beam+1) < len(lines[0]):
                    beams_to_write_next.append(beam+1)
                if (beam-1) > -1:
                    beams_to_write_next.append(beam-1)
        for beam in beams_to_remove:
            existing_beams.remove(beam)
        for beam in beams_to_write_next:
            existing_beams.add(beam)
    print(split_count)
