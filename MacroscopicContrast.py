import Entity2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ccc = 0
    for cc in range(1):
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
                if a <= 1000:
                    a = 0
                elif a <= 2000:
                    a = 100
                else:
                    a = 200
                if b <= 1000:
                    b = 0
                elif b <= 2000:
                    b = 100
                else:
                    b = 200
                cy0.append(a)
                jh0.append(b)
            cy.append(cy0.copy())
            jh.append(jh0.copy())
        # print(cy)
        print(cy)
        plt.matshow(jh)
        plt.savefig("jh1.png")
        plt.matshow(cy)
        plt.savefig("cy1.png")
        plt.show()
        # sum0 = 0
        # for i in range(100):
        #     for j in range(100):
        #         if cy[i][j] == jh[i][j]:
        #             sum0 += 1
        # print(sum0/10000)
        # ccc += sum0/10000
    # file_handle = open('cy.txt', mode='a')
    # file_handle.write(cy)
    # file_handle.close()
    print(ccc/100)
