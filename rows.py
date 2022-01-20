

def img2rows(a, w, h):
    inLine = False
    start = 0
    mark_boxes = []

    for i in range(0, len(a)):
        if inLine == False and a[i] > 10:
            inLine = True
            start = i
        elif i-start > 5 and a[i] < 10 and inLine:
            inLine = False
            if i-start > 10:
                top = max(start-1, 0)
                bottom = min(h, i+1)
                box = [0, top, w, bottom]
                mark_boxes.append(box)

    return mark_boxes

