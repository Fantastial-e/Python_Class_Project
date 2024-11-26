import turtle

# 设置画布
wn = turtle.Screen()
wn.bgcolor("white")

# 创建海龟
star_turtle = turtle.Turtle()
star_turtle.color("red")

# 绘制五角星
for _ in range(5):
    star_turtle.forward(100)
    star_turtle.right(144)

# 绑定退出函数到键盘事件
def exit_on_key():
    print("Exiting...")
    wn.bye()  # 关闭窗口

wn.onkey(exit_on_key, "space")  # 可以绑定到空格键或其他键
wn.listen()  # 开始监听键盘事件

# 保持窗口打开直到用户按下键
wn.mainloop()
