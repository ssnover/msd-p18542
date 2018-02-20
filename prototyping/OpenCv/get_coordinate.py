def get_coordinate(px):
    x = px[0]
    y = px[1]

    if x < 299:
        if x < 159:
            if  x < 88:
                x = 1
            elif x > 88:
                x = 2
        elif x >159:
            if x < 229:
                x = 3
            elif x > 229:
                x = 4
    elif x > 299:
        if x < 440:
            if x < 370:
                x = 5
            elif x > 370:
                x = 6
        elif x > 440:
            if x < 511:
                x = 7
            elif x > 511:
                x = 8
    if y < 250:
        if y < 130:
            if y < 70:
                y = 1
            elif y > 70:
                y = 2
        elif y >170:
            if y < 190:
                y = 3
            elif y > 190:
                y = 4
    elif y > 250:
        if y < 370:
            if y < 310:
                y = 5
            elif y > 310:
                y = 6
        elif y > 370:
            if y < 430:
                y = 7
            elif y > 430:
                y = 8
    coordinate = [x, y]

    return coordinate