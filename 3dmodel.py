import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection

class model:

    def __init__(self):
        # 空间划分：固定 √
        self.Xspace = 100; self.Yspace = 100; self.Zspace = 100  # 模型在三个方向的"总大小"！
        self.a = 10; self.b = 10; self.c = 10  # 单个方块的3边长
        self.block_total = int((self.Xspace / self.a) * (self.Yspace / self.b) * (self.Zspace / self.c))  # 总网格块体数(转int)： self.block_total

        # 每个立方体的坐标：固定 √  一层一层生成：先x后y，最后是z！
        self.x0 = [xtmp1 for xtmp1 in np.arange(self.a / 2, self.Xspace, self.a) for xtmp2 in np.arange(0, self.b * self.c)]
        self.y0 = [ytmp1 for ytmp1 in np.arange(self.b / 2, self.Yspace, self.b) for ytmp2 in np.arange(0, self.c)] * self.a
        self.z0 = [ztmp1 for ztmp1 in np.arange(self.c / 2, self.Zspace, self.c)] * (self.a * self.b)
        self.Pointxyz = [(self.x0[xyz], self.y0[xyz], self.z0[xyz]) for xyz in np.arange(0, self.block_total)]

        # 观测点分布：固定 √
        self.Xmin = 5; self.dx = 10; self.Nx = 10  # x向10个观测点，起点5，间距10
        self.Ymin = 5; self.dy = 10; self.Ny = 10  # y向同上
        self.Zplane = 90                           # 观测点所在的平面
        self.ober_total = self.Nx * self.Ny        # 总观测点数：10x10 = 100

        self.oberx0 = [ xtmp1 for xtmp1 in range(self.Xmin, self.Xspace, self.Nx) ] * 10
        self.obery0 = [ ytmp1 for ytmp1 in range(self.Ymin, self.Yspace, self.Ny) for ytmp2 in range(10) ]
        self.oberz0 = [self.Zplane]*100

    # 1. 画所有"上面"
    def surface_up(self, ax, kappa_position):
        for num in range(self.block_total):
            # 块体中心点：
            center = self.Pointxyz[num]
            # "上面"的4个顶点：
            point1 = (center[0] - self.a / 2, center[1] - self.b / 2, center[2] - self.c / 2)
            point2 = (center[0] - self.a / 2, center[1] + self.b / 2, center[2] - self.c / 2)
            point3 = (center[0] + self.a / 2, center[1] + self.b / 2, center[2] - self.c / 2)
            point4 = (center[0] + self.a / 2, center[1] - self.b / 2, center[2] - self.c / 2)
            # 顶点汇总：
            verts = [point1, point2, point3, point4]
            poly3d = [verts]

            # 画顶点(同时限定空间范围)：必须有！
            x = (point1[0], point2[0], point3[0], point4[0])
            y = (point1[1], point2[1], point3[1], point4[1])
            z = (point1[2], point2[2], point3[2], point4[2])
            ax.scatter(x, y, z, c='k', marker='None')

            if num in kappa_position:
                # 画"下面"：
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='y', linewidths=2, alpha=1))
                continue

            # 画"下面"：
            ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.05))

    # 2. 画所有"下面"
    def surface_down(self, ax, kappa_position):
        for num in range(self.block_total):
            # 块体中心点：
            center = self.Pointxyz[num]
            # "上面"的4个顶点：
            point5 = (center[0] - self.a / 2, center[1] - self.b / 2, center[2] + self.c / 2)
            point6 = (center[0] - self.a / 2, center[1] + self.b / 2, center[2] + self.c / 2)
            point7 = (center[0] + self.a / 2, center[1] + self.b / 2, center[2] + self.c / 2)
            point8 = (center[0] + self.a / 2, center[1] - self.b / 2, center[2] + self.c / 2)
            # 顶点汇总：
            verts = [point5, point6, point7, point8]
            poly3d = [verts]

            # 画顶点(同时限定空间范围)：必须有！
            x = (point5[0], point6[0], point7[0], point8[0])
            y = (point5[1], point6[1], point7[1], point8[1])
            z = (point5[2], point6[2], point7[2], point8[2])
            ax.scatter(x, y, z, c='k', marker='None')

            if num in kappa_position:
                # 画"下面"：
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='y', linewidths=2, alpha=1))
                continue

            # 画"下面"：
            ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.05))

    # 3. 画所有"前面"
    def surface_forward(self, ax, kappa_position):
        for num in range(self.block_total):
            # 块体中心点：
            center = self.Pointxyz[num]
            # "前面"的4个顶点：
            point2 = (center[0] - self.a / 2, center[1] + self.b / 2, center[2] - self.c / 2)
            point3 = (center[0] + self.a / 2, center[1] + self.b / 2, center[2] - self.c / 2)
            point7 = (center[0] + self.a / 2, center[1] + self.b / 2, center[2] + self.c / 2)
            point6 = (center[0] - self.a / 2, center[1] + self.b / 2, center[2] + self.c / 2)
            # 顶点汇总：
            verts = [point2, point3, point7, point6]
            poly3d = [verts]

            # 画顶点(同时限定空间范围)：必须有！
            x = (point2[0], point3[0], point7[0], point6[0])
            y = (point2[1], point3[1], point7[1], point6[1])
            z = (point2[2], point3[2], point7[2], point6[2])
            ax.scatter(x, y, z, c='k', marker='None')

            if num in kappa_position:
                # 画"下面"：
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='y', linewidths=2, alpha=1))
                continue

            # 画"下面"：
            ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.05))

    # 4. 画所有的"后面"
    def surface_back(self, ax, kappa_position):
        for num in range(self.block_total):
            # 块体中心点：
            center = self.Pointxyz[num]
            # "后面"的4个顶点：
            point1 = (center[0] - self.a / 2, center[1] - self.b / 2, center[2] - self.c / 2)
            point4 = (center[0] + self.a / 2, center[1] - self.b / 2, center[2] - self.c / 2)
            point8 = (center[0] + self.a / 2, center[1] - self.b / 2, center[2] + self.c / 2)
            point5 = (center[0] - self.a / 2, center[1] - self.b / 2, center[2] + self.c / 2)
            # 顶点汇总：
            verts = [point1, point4, point8, point5]
            poly3d = [verts]

            # 画顶点(同时限定空间范围)：必须有！
            x = (point1[0], point4[0], point8[0], point5[0])
            y = (point1[1], point4[1], point8[1], point5[1])
            z = (point1[2], point4[2], point8[2], point5[2])
            ax.scatter(x, y, z, c='k', marker='None')

            if num in kappa_position:
                # 画"下面"：
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='y', linewidths=2, alpha=1))
                continue

            # 画"下面"：
            ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.05))

    # 5. 画所有的"左面"
    def surface_left(self, ax, kappa_position):
        for num in range(self.block_total):
            # 块体中心点：
            center = self.Pointxyz[num]
            # "左面"的4个顶点：
            point1 = (center[0] - self.a / 2, center[1] - self.b / 2, center[2] - self.c / 2)
            point2 = (center[0] - self.a / 2, center[1] + self.b / 2, center[2] - self.c / 2)
            point6 = (center[0] - self.a / 2, center[1] + self.b / 2, center[2] + self.c / 2)
            point5 = (center[0] - self.a / 2, center[1] - self.b / 2, center[2] + self.c / 2)
            # 顶点汇总：
            verts = [point1, point2, point6, point5]
            poly3d = [verts]

            # 画顶点(同时限定空间范围)：必须有！
            x = (point1[0], point2[0], point6[0], point5[0])
            y = (point1[1], point2[1], point6[1], point5[1])
            z = (point1[2], point2[2], point6[2], point5[2])
            ax.scatter(x, y, z, c='k', marker='None')

            if num in kappa_position:
                # 画"下面"：
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='y', linewidths=2, alpha=1))
                continue

            # 画"下面"：
            ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.05))

    # 6. 画所有的"右面"
    def surface_right(self, ax, kappa_position):
        for num in range(self.block_total):
            # 块体中心点：
            center = self.Pointxyz[num]
            # "右面"的4个顶点：
            point4 = (center[0] + self.a / 2, center[1] - self.b / 2, center[2] - self.c / 2)
            point3 = (center[0] + self.a / 2, center[1] + self.b / 2, center[2] - self.c / 2)
            point7 = (center[0] + self.a / 2, center[1] + self.b / 2, center[2] + self.c / 2)
            point8 = (center[0] + self.a / 2, center[1] - self.b / 2, center[2] + self.c / 2)
            # 顶点汇总：
            verts = [point4, point3, point7, point8]
            poly3d = [verts]

            # 画顶点(同时限定空间范围)：必须有！
            x = (point4[0], point3[0], point7[0], point8[0])
            y = (point4[1], point3[1], point7[1], point8[1])
            z = (point4[2], point3[2], point7[2], point8[2])
            ax.scatter(x, y, z, c='k', marker='None')

            if num in kappa_position:
                # 画"下面"：
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='y', linewidths=2, alpha=1))
                continue

            # 画"下面"：
            ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.05))

    # 7. 画观测面：
    def surface_ober(self, ax):
        # 观测点：
        ax.scatter(self.oberx0, self.obery0, self.oberz0, c = 'r', marker='*')
        # 观测面：
        for numy in range(1,10):
            for numx in range(1,10):
                point1 = ( self.Xmin + self.dx*(numx-1), self.Ymin + self.dy*(numy-1), self.Zplane )
                point2 = ( self.Xmin + self.dx*(numx), self.Ymin + self.dy*(numy-1), self.Zplane )
                point3 = ( self.Xmin + self.dx*(numx), self.Ymin + self.dy*(numy), self.Zplane  )
                point4 = ( self.Xmin + self.dx*(numx-1), self.Ymin + self.dy*(numy), self.Zplane )

                verts = [point1, point2, point3, point4]
                poly3d = [verts]
                ax.add_collection3d(Poly3DCollection(poly3d, facecolors='m', linewidths=2, alpha=1))


if __name__ == '__main__':

    mymodel = model()
    kappa_position = input('输入观测点位置(空格间隔，回车结束):')
    kappa_position = list( map(int, kappa_position.split(' ')) )

    # 创建图：
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # 分别、一次性画完所有块体的6个面
    mymodel.surface_up(ax, kappa_position)
    mymodel.surface_down(ax, kappa_position)
    mymodel.surface_forward(ax, kappa_position)
    mymodel.surface_back(ax, kappa_position)
    mymodel.surface_left(ax, kappa_position)
    mymodel.surface_right(ax, kappa_position)
    # 画观测面 + 观测点：
    mymodel.surface_ober(ax)
    # 关闭网格
    plt.axis('off')

    from matplotlib.pyplot import savefig
    savefig("quan3.pdf")
