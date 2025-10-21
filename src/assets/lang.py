import matplotlib.font_manager as fm

def find_japanese_font(candidates=None):
    # システム内のフォントから日本語フォント候補名を探す
    if candidates is None:
        candidates = [
            'IPAPGothic', 'IPAexGothic', 'Noto Sans CJK JP',
            'TakaoGothic', 'Yu Gothic', 'Meiryo', 'Hiragino Kaku Gothic ProN'
        ]
    for font_path in fm.findSystemFonts(fontext='ttf'):
        try:
            name = fm.FontProperties(fname=font_path).get_name()
        except Exception:
            continue
        for cand in candidates:
            if cand.lower() in name.lower():
                return name
    return None

def set_font(font_name):
    # matplotlibのフォントを設定
    if font_name:
        import matplotlib.pyplot as plt
        plt.rcParams['font.family'] = 'sans-serif'
        current = list(plt.rcParams.get('font.sans-serif', []))
        if font_name not in current:
            plt.rcParams['font.sans-serif'] = [font_name] + current