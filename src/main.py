import analysis.LoadDeflection as LoadDeflection

if __name__ == "__main__":

    # クライアントからの入力受付
    values = input("\n(a, b, E) > ")
    a, b, E = map(float, values.split(","))
    
    # a = 8.95376
    # b = 0.30596
    # E = 6.28782

    # 荷重・たわみ関係のプロット
    LoadDeflection.plot(a, b, E)