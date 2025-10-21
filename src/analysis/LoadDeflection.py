import matplotlib.pyplot as plt
import assets.lang as lang
import numpy as np

def plot(x, y):

    # フォント設定
    lang.set_font(font_name=None or lang.find_japanese_font())

    # データの生成（仮）
    load = np.linspace(0, x, 100)
    deflection = (load / y) ** 2

    # プロットの作成
    plt.figure(figsize=(8, 6))
    plt.plot(deflection, load, color='gray')
    plt.title('図1  荷重・たわみの関係')
    plt.xlabel('たわみδ（mm）')
    plt.ylabel('荷重（N）')
    plt.grid(True)
    plt.tight_layout()
    plt.show()