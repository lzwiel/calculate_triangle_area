import math

def calculate_triangle_area(a, b, c):
    # 使用海伦公式计算半周长
    s = (a + b + c) / 2

    # 计算面积
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

# 输入三角形的边长
a = float(input("请输入第一条边的长度："))
b = float(input("请输入第二条边的长度："))
c = float(input("请输入第三条边的长度："))

triangle_area = calculate_triangle_area(a, b, c)
print("三角形的面积为：", triangle_area)
