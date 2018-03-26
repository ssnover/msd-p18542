def get_coordinate(px):
    x = px[0]
    y = px[1]

    if y < 299:
        if y < 150:
            if y < 80:
                y = 1
            elif y > 80:
                y = 2
        elif y > 150:
            if y < 220:
                y = 3
            elif y > 220:
                y = 4
    elif y > 299:
        if y < 440:
            if y < 370:
                y = 5
            elif y > 370:
                y = 6
        elif y > 440:
            if y < 511:
                y = 7
            elif y > 511:
                y = 8
    if x < 250:
        if x < 130:
            if x < 70:
                x = 1
            elif x > 70:
                x = 2
        elif x > 130:
            if x < 190:
                x = 3
            elif x > 190:
                x = 4
    elif x > 250:
        if x < 370:
            if x < 310:
                x = 5
            elif x > 310:
                x = 6
        elif x > 370:
            if x < 430:
                x = 7
            elif x > 430:
                x = 8
    coordinate = [x, y]

    return coordinate