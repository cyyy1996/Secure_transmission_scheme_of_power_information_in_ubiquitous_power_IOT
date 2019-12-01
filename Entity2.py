import math

import Entity1
import matplotlib.pyplot as plt
import numpy as np


class Entity2:
    """
    第二实体（集中器）
    P :与之链接的第一实体矩阵
    Entity2_ID: 第二实体D
    """

    def __init__(self, n, size):
        self.Entity2_ID = n
        self.Entity2_Size = size
        self.Entity2_Matrix = [[0 for i in range(self.Entity2_Size)] for i in range(self.Entity2_Size)]
        self.Entity2_DataBase = []
        self.Entity2_DataLog = []
        for i in range(self.Entity2_Size):
            for j in range(self.Entity2_Size):
                entity1 = Entity1.Entity1(x=i, y=j, n=self.Entity2_Size, types=i % 3)
                self.Entity2_Matrix[i][j] = entity1

    def PrintAll(self):
        for i in range(self.Entity2_Size):
            for j in range(self.Entity2_Size):
                print("ID:", self.Entity2_Matrix[i][j].Entity1_ID, end=" ", sep="")
                print("DATA:", self.Entity2_Matrix[i][j].Entity1_OutputData, end=" ", sep="")
                print("TYPE:", self.Entity2_Matrix[i][j].Entity1_EntityType, end=" ", sep="")
                print("Position:", self.Entity2_Matrix[i][j].Entity1_Position, sep="")
                for k in self.Entity2_Matrix[i][j].Entity1_DataLog.DataLog_Entity1_DataList:
                    print(k.DataPack_path, k.DataPack_data)
                print("*******************")
                for k in self.Entity2_Matrix[i][j].Entity1_DataBase.DataBase_Entity1_DataList:
                    print(k.DataPack_path, k.DataPack_data)
                # print("LOG", self.Entity2_Matrix[i][j].Entity1_DataLog.DataLog_Entity1_DataList)

    def DataRefresh(self):
        for i in range(self.Entity2_Size):
            for j in range(self.Entity2_Size):
                self.Entity2_Matrix[i][j].DataRefresh()

    def DataPack(self, size=3):
        for i in range(self.Entity2_Size):
            for j in range(self.Entity2_Size):
                self.Entity2_Matrix[i][j].DataPack(size=size)

    def TransferData(self, types=0, inc=1):
        if types == 0:
            for i in range(self.Entity2_Size):
                for j in range(self.Entity2_Size):
                    self.Entity2_Matrix[i][j].TransferData(self.Entity2_Matrix[(i + inc) % self.Entity2_Size][j])
        elif types == 1:
            for i in range(self.Entity2_Size):
                for j in range(self.Entity2_Size):
                    self.Entity2_Matrix[i][j].TransferData(entity=self, types=1)

    def Statistics(self, index):
        data0 = []
        data1 = []
        for k in self.Entity2_DataBase:
            # print(k.DataPack_path, k.DataPack_data)
            # print(k.DataPack_path[0])
            if k.DataPack_path[0] == index:
                data1.append(k.DataPack_data)
            if k.DataPack_path[-2] == index:
                data0.append(k.DataPack_data)
        data0.sort()
        data1.sort()
        # print(data0)
        sum0 = 0
        sum1 = 1
        for i in range(1, len(data0)):
            sum0 += data0[i]
            sum1 += data1[i]
        d0 = -1 * data0[0] * sum0
        d1 = -1 * data1[0] * sum1
        print("真实数据:", d1)
        print("传递数据:", d0)
        return d1, d0


class Monitor:
    """
    监听者（通信过程监控）
    """

# if __name__ == '__main__':
#     for i in range(100):
#         cy = ""
#         E2 = Entity2(n=1, size=10)
#         E2.DataRefresh()
#         E2.DataPack()
#         E2.TransferData()
#         E2.TransferData(inc=2)
#         E2.TransferData(inc=3)
#         E2.TransferData(inc=4)
#         E2.TransferData(inc=5)
#         E2.TransferData(types=1)
#         E2.TransferData(types=1)
#         E2.TransferData(types=1)
#         E2.TransferData(types=1)
#         E2.TransferData(types=1)
#         E2.TransferData(types=1)
#         # E2.PrintAll()
#         for j in range(100):
#             d1, d0 = E2.Statistics(index=j)
#             if d1 != 0:
#                 cy += str(math.fabs(d0 / d1)) + ","
#             else:
#                 cy += "NULL" + ","
#         cy += "\n"
#         file_handle = open('cy.txt', mode='a')
#         file_handle.write(cy)
#         file_handle.close()
