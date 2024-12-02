def check_collision(obj1, obj2):
    # 두 객체의 충돌 박스를 가져와 충돌 여부 확인
    left1, bottom1, right1, top1 = obj1.get_bb()
    left2, bottom2, right2, top2 = obj2.get_bb()

    if left1 > right2 or right1 < left2 or top1 < bottom2 or bottom1 > top2:
        return False
    return True

# 충돌 처리 함수
def handle_collisions(objects):
    for obj1 in objects:
        for obj2 in objects:
            if obj1 != obj2 and check_collision(obj1, obj2):
                obj1.handle_collision('pikachu:monster_ball', obj2)
                obj2.handle_collision('pikachu:monster_ball', obj1)
