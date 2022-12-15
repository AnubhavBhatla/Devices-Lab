import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    Rfb = 8.2 # 8.2k
    Cfb = 390 # 390 pF
    f = 10e6  # 1 MHz

    vdut = np.array([32, 60, 40, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24])
    vout = np.array([40, 48, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32])

    assert vdut.shape == vout.shape
    cdut = (vout / vdut) * (Cfb * 10 ** -12) * np.sqrt(1 + 1/(2 * np.pi * (f * 10 ** 6) * (Rfb * 10 ** 3) * (Cfb * 10 ** -12)) ** 2)
    print(cdut)
    vdc = np.array([0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    plt.title(r'$C_{dut}$ vs $V_{dc}$')
    plt.xlabel(r'$V_{dc}$ (V)')
    plt.ylabel(r'$C_{dut}$ $(pF)$')
    plt.plot(vdc, cdut * 10 ** 9)
    plt.show()

    plt.title(r'$1/C_{dut}^{2}$ vs $V_{dc}$')
    plt.xlabel(r'$V_{dc}$ (V)')
    plt.ylabel(r'$\frac{1}{C_{dut}^{2}}$ $(pF^{-2})$')
    plt.plot(vdc, 1 / (cdut * 10 ** 9) ** 2)
    plt.show()
