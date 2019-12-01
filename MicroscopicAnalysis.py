import math

import Entity2

if __name__ == '__main__':
    for k in range(3, 11):
        cyy = 0
        for i in range(100):
            cy = 0
            jh = 0
            E2 = Entity2.Entity2(n=1, size=10)
            E2.DataRefresh()
            E2.DataPack(size=k)
            for l in range(1, k):
                E2.TransferData(inc=l)
            for l in range(k):
                E2.TransferData(types=1)

        #     # E2.PrintAll()
            for j in range(100):
                d1, d0 = E2.Statistics(index=j)
                if d1 != 0:
                    cy += math.fabs(d0 / d1)
                    jh += 1
            cyy += cy / jh
        jhh = cyy / 100
        file_handle = open('cy.txt', mode='a')
        file_handle.write(str(jhh) + ",")
        file_handle.close()
