import matplotlib.pyplot as plt
import assets.lang as lang
import numpy as np

def plot(a, b, E):

    # フォント設定
    lang.set_font(font_name=None or lang.find_japanese_font())
 
    # x 軸の範囲（0〜10）
    x = np.linspace(0, 5)

    # 5つの式
    y1 = a*x + b
    y2 = a*x
    y3 = E*x
    y4 = (E*1.05)*x
    y5 = (E*0.95)*x

    # グラフ作成
    plt.figure(figsize=(8, 6))

    plt.plot(x, y1, color='gray', label='y = ax + b')
    plt.plot(x, y2, color='blue', label='y = ax')
    plt.plot(x, y3, color='red', label='y = Ex')
    plt.plot(x, y4, color='red', label='y = 1.05Ex')
    plt.plot(x, y5, color='red', label='y = 0.95Ex')

    # テキストの生成
    plt.text(x[-1], y1[-1], '  y = ax + b', color='gray', va='center')
    plt.text(x[-1], y2[-1], '  y = ax',     color='blue', va='center')
    plt.text(x[-1], y3[-1], '  E',     color='red', va='center')
    plt.text(x[-1], y4[-1], '  +5%', color='red', va='center')
    plt.text(x[-1], y5[-1], '  -5%', color='red', va='center')

    # タイトル・軸
    plt.title('図1  荷重・たわみの関係')
    plt.xlabel('たわみ δ (mm)')
    plt.ylabel('荷重 (N)')
    plt.grid(True)
    # plt.legend()
    plt.tight_layout()
    plt.show()