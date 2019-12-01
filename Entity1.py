import math
import random


class Entity1:
    """
    第一实体（智能电表）
        OutputData 实体产出数据
        Entity1ID 实体身份编号
        DataLog 实体数据日志
        DataBase 实体数据仓库
        EntityType 实体类型
    """

    def __init__(self, x, y, n, types):
        self.Entity1_OutputData = -1
        self.Entity1_DataBase = DataBase_Entity1()
        self.Entity1_DataLog = DataLog_Entity1()
        self.Entity1_ID = x * n + y
        self.Entity1_Position = [x, y]
        self.Entity1_EntityType = types

    def DataPack(self, size=3):
        if size == 3:
            multiplier = [-1, -2, -5, -10]
            data = [-1, -1, -1]
            data[0] = random.choice(multiplier)
            data0 = self.Entity1_OutputData / (data[0] * -1)
            data[1] = random.randint(0, data0 // 1)
            data[2] = data0 - data[1]
            for i in range(3):
                data_pack = DataPack(round(data[i], 2), self.Entity1_ID)
                self.Entity1_DataBase.DataBase_Entity1_DataList.append(data_pack)
                self.Entity1_DataLog.DataLog_Entity1_DataList.append(data_pack)
            self.Entity1_OutputData = -1
        else:
            multiplier = [-1, -2, -5, -10]
            data = [-1] * size
            data[0] = random.choice(multiplier)
            data0 = self.Entity1_OutputData / (data[0] * -1)
            for i in range(1, size-1):
                data[i] = random.randint(0, data0 // 1)
                data0 = data0 - data[i]
            data[size-1] = data0 - data[size-2]
            for i in range(size):
                data_pack = DataPack(round(data[i], 4), self.Entity1_ID)
                self.Entity1_DataBase.DataBase_Entity1_DataList.append(data_pack)
                self.Entity1_DataLog.DataLog_Entity1_DataList.append(data_pack)
            self.Entity1_OutputData = -1

    def DataRefresh(self):
        if self.Entity1_EntityType == 0:
            self.Entity1_OutputData = random.randint(1, 1000)
        elif self.Entity1_EntityType == 1:
            self.Entity1_OutputData = random.randint(1001, 2000)
        else:
            self.Entity1_OutputData = random.randint(2001, 3000)

    def TransferData(self, entity, types=0):
        if types == 0:
            self.Entity1_DataBase.DataBase_Entity1_DataList[0].DataPack_path.append(entity.Entity1_ID)
            entity.Entity1_DataLog.DataLog_Entity1_DataList.append(
                self.Entity1_DataBase.DataBase_Entity1_DataList[0])
            entity.Entity1_DataBase.DataBase_Entity1_DataList.append(
                self.Entity1_DataBase.DataBase_Entity1_DataList.pop(0))
        elif types == 1:
            self.Entity1_DataBase.DataBase_Entity1_DataList[0].DataPack_path.append(entity.Entity2_ID * (-1))
            entity.Entity2_DataLog.append(self.Entity1_DataBase.DataBase_Entity1_DataList[0])
            entity.Entity2_DataBase.append(self.Entity1_DataBase.DataBase_Entity1_DataList.pop(0))


class DataBase_Entity1:
    """
    第一实体存储的数据
    """

    def __init__(self):
        self.DataBase_Entity1_DataList = []


class DataLog_Entity1:
    """
    第一实体数据日志
    """

    def __init__(self):
        self.DataLog_Entity1_DataList = []


class DataPack:
    """
    数据包：数据产生后，封装成数据包传输，存储
    data: 数据
    source: 数据来源
    status: 数据状态
    time： 数据时间戳
    """

    def __init__(self, data, source):
        self.DataPack_data = data
        self.DataPack_source = source
        self.DataPack_status = 0
        self.DataPack_time = 0
        self.DataPack_path = [source]
