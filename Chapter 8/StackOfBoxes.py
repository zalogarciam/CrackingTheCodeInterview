
class Box:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def can_stack(self, top_box):
        return (
                self.width > top_box.width and
                self.height > top_box.height and
                self.length > top_box.length
        )


def get_stackable_boxes(box, boxes):
    for i, top_box in enumerate(boxes):
        if box.can_stack(top_box):
            return boxes[i:]
    return None


def stack_of_boxes_util(boxes):
    if len(boxes) == 1:
        return boxes[0].height

    current_box = boxes[0]
    stackable_boxes = get_stackable_boxes(current_box, boxes[1:])

    if stackable_boxes:
        current_height = current_box.height + stack_of_boxes_util(stackable_boxes)
    else:
        current_height = current_box.height
    return max(current_height, stack_of_boxes_util(boxes[1:]))


def stack_of_boxes(boxes):
    boxes.sort(key=lambda x: x.height, reverse=True)
    return stack_of_boxes_util(boxes)

stack_of_boxes([Box(4, 4, 6), Box(7, 8, 1), Box(5, 5, 7)])
