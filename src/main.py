import analysis.LoadDeflection as LoadDeflection

if __name__ == "__main__":

    # クライアントからの入力受付
    values = input("\n❯ ")
    try:
        a, b, E = map(float, values.split(","))
    except ValueError:
        print("\n\033[31mカンマ区切りで3つの数値を入力してください。（左から a, b, E）\033[0m\n")
        exit(1)
    
    # 荷重・たわみ関係のプロット
    LoadDeflection.plot(a, b, E)