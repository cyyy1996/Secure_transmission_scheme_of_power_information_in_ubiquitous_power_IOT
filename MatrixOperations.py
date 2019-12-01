import math

import Entity2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    cy = []
    jh = []
    for i in range(90):
        cy0 = []
        jh0 = []
        E2 = Entity2.Entity2(n=1, size=10)
        E2.DataRefresh()
        E2.DataPack()
        E2.TransferData()
        E2.TransferData(inc=2)
        E2.TransferData(types=1)
        E2.TransferData(types=1)
        E2.TransferData(types=1)
        # E2.PrintAll()
        for j in range(90):
            a, b = E2.Statistics(j)
            cy0.append(a)
            if b > 200:
                jh0.append(200)
            else:
                jh0.append(b)
        cy.append(cy0.copy())
        jh.append(jh0.copy())
    # print(cy)
    plt.matshow(jh)
    plt.savefig("jh1.png")
    plt.matshow(cy)
    plt.savefig("cy1.png")
    plt.show()

    sum0 = 0
    for i in range(100):
        for j in range(100):
            sum0 += math.pow((cy[i][j] - jh[i][j]), 2)
    print("++++++++++++++++++++++")
    print(math.sqrt(sum0))
    # file_handle = open('cy.txt', mode='a')
    # file_handle.write(cy)
    # file_handle.close()
