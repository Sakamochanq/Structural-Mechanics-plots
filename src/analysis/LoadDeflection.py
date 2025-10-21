import matplotlib.pyplot as plt
import assets.lang as lang
import numpy as np

def plot(a, b, E):

    # フォント設定
    lang.set_font(font_name=None or lang.find_japanese_font())
 
    # x軸の範囲
    RANGE = 5

    x_line = np.linspace(0, RANGE, 100)
    x_dot  = np.arange(1, RANGE)

    # 5つの式（線用）
    y1_line = a*x_line + b
    y2_line = a*x_line
    y3_line = E*x_line
    y4_line = (E*1.05)*x_line
    y5_line = (E*0.95)*x_line

    # 5つの式（点用）
    y1_dot = a*x_dot + b
    y2_dot = a*x_dot
    y3_dot = E*x_dot
    y4_dot = (E*1.05)*x_dot
    y5_dot = (E*0.95)*x_dot

    # 計算結果をConsoleに出力
    print(f'\ny = {a}x + {b}')
    print(f'y = {a}x')
    print(f'E = {E}')
    print(f'E +5% = {E*1.05}')
    print(f'E -5% = {E*0.95}')

    # プロット作成
    plt.figure(figsize=(8, 6))

    # 線の描画
    plt.plot(x_line, y1_line, color='gray')
    plt.plot(x_line, y2_line, color='blue')
    plt.plot(x_line, y3_line, color='red')
    plt.plot(x_line, y4_line, color='red')
    plt.plot(x_line, y5_line, color='red')

    # 点の描画
    plt.scatter(x_dot, y1_dot, color='gray')
    plt.scatter(x_dot, y2_dot, color='blue')
    plt.scatter(x_dot, y3_dot, color='red')
    plt.scatter(x_dot, y4_dot, color='red')
    plt.scatter(x_dot, y5_dot, color='red')

    # テキスト描画
    plt.text(5, y1_line[-1], '  y = ax + b', color='gray', va='center')
    plt.text(5, y2_line[-1], '  y = ax',     color='blue', va='center')
    plt.text(5, y3_line[-1], '  E',          color='red', va='center')
    plt.text(5, y4_line[-1], '  +5%',        color='red', va='center')
    plt.text(5, y5_line[-1], '  -5%',        color='red', va='center')

    # 軸ラベル
    plt.title('図1  荷重・たわみの関係')
    plt.xlabel('たわみ δ (mm)')
    plt.ylabel('荷重 (N)')
    plt.grid(True)
    plt.tight_layout()

    # 補助目盛り
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

    # 表示
    try:
        print("\n全てのプロットを正常に描画しました。\n")
        plt.show()
    except Exception as e:
        print(f"{e}")  