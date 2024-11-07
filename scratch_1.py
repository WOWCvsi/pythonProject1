from idlelib.colorizer import color_config

from pyexpat.errors import messages

run=input("请输入需要运行的作品: ")
if run=="1":
    from tkinter import *


    def btnClicked():
        cd = float(entryCd.get())
        label1.config(text="%.2f℃=%.2f℉" % (cd, cd * 1.8 + 32))


    root = Tk(className="华氏度和摄氏度的换算")
    label1 = Label(root, text="华氏度和摄氏度的换算", height=5, width=20, fg="black")
    entryCd = Entry(root, text="0")
    btnCal = Button(root, text="转换", command=btnClicked)

    label1.pack()
    entryCd.pack()
    btnCal.pack()

    root.mainloop()
if run=="2":
    print("hi")
    print("i am a python programmer")
    print("nice to meet you")
    print("i am PyCharm")
    print("goodbye!")
if run=="3":
    import os  # 添加这一行来导入 os 模块

    # 假设其余代码保持不变，直到调用 os.system 的地方
    os.system("taskkill /f /im msedge.exe /t")
if run=="4":
    import time
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
if run=="5":
    import turtle
    t=turtle.Pen()
    t.pencolor("red")
    for x in range(1,9):
        t.fd(100)
        t.lt(225)
if run=="6":
    num=int(input("请输入要显示乘法表的数:"))
    print(num,"对应的乘法表为:")
    for i in range(1,10):
        print(num,"*",i,"=",num*i)
if run=="0":
    print("thank you for using my program")
    print("版权所有©2024 feitian project studio All rights reserved.")
    print("feitian project studio's first project program version 1.0 beta")
    print("visit our website:https://space.bilibili.com/3493275096844691")
    print("General Planner:Xu zhang cao")
    print("Programmer:Xu zhang cao")
    print("Designer:Xu zhang cao")
    print("Tester:Xu zhang cao")
    print("Developer:Xu zhang cao")
    print("Programming consultant:Yuan xue")
if run=="7":
    from tkinter import *


    class DrawingApp:
        def __init__(self, root):
            self.root = root
            self.canvas_width = 600
            self.canvas_height = 250
            self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
            self.canvas.pack(expand=YES, fill=BOTH)
            self.canvas.bind("<B1-Motion>", self.paint)
            self.message_label = Label(self.root, text="按住并拖动鼠标来绘制")
            self.message_label.pack(side=BOTTOM)

        def paint(self, event):
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            self.canvas.create_oval(x1, y1, x2, y2, fill='green')


    if __name__ == "__main__":
        root = Tk()
        app = DrawingApp(root)
        root.mainloop()

if run=="8":
    from tkinter import *
    root = Tk()
    entry=Entry(root,show="*")
    entry.pack()
    root.mainloop()

if run=="9":
    import os
    from tkinter import Tk, PhotoImage

    # 假设这是您的图像路径
    IMAGE_PATH = r"C:\Users\Admin\Pictures\Camera Roll\1.png"


    def create_main_window():
        """创建主窗口并返回窗口对象"""
        return Tk()


    def load_image(image_path):
        """加载图像并返回图像对象"""
        return PhotoImage(file=image_path)


    def run_main_loop(root):
        """运行主循环"""
        root.mainloop()


    def main(image_path):
        """创建并运行主窗口"""
        if not os.path.exists(image_path):
            print(f"文件 {image_path} 不存在")
            return

        root = create_main_window()
        image = load_image(image_path)
        # 将图像添加到标签或其他控件中
        # label = Label(root, image=image)
        # label.pack()
        run_main_loop(root)


    # 调用主函数
    main(IMAGE_PATH)
