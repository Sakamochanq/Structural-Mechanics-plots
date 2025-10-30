import analysis.LoadDeflection as LoadDeflection
import assets.cls as cls

# コンソールをクリアするかのフラグ
IS_CLEAR = True

if __name__ == "__main__":

    while True:
        cls.clear_console(IS_CLEAR)
        
        # クライアントからの入力受付
        print("\n\033[36mカンマ区切りで3つの数値を入力してください。（左から a, b, E）\033[0m")
        print("\033[37m※ ?exit で終了します。\033[0m")
        
        values = input("\n❯ ")
        try:
            if values.strip() == "?exit":
                cls.clear_console(IS_CLEAR)
                break
            
            a, b, E = map(float, values.split(","))
        except ValueError:
            print("\n\033[31mError::Invalidinput\033[0m\n")
            continue

        # 荷重・たわみ関係のプロット
        LoadDeflection.plot(a, b, E)