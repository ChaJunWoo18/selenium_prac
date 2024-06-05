def get_matching_color_coordinates(image, color1, color2):
    width, height = image.size
    # 이미지를 로드하고 픽셀 데이터를 가져옴
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            current_color = pixels[x, y]
            if current_color == color1 or current_color == color2:
                # 조건을 만족하는 픽셀을 발견하면 해당 좌표를 반환하고 함수를 종료

                return (x,y)

    return None