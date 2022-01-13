import cv2


def convert(png_path: str, txt_path: str):
    img = cv2.imread(png_path)
    h, w, c = img.shape
    with open(txt_path, 'wt') as f:
        for y in range(h):
            for x in range(w):
                b, g, r = img[y, x]
                print(f'{r:02x}{g:02x}{b:02x}', file=f, end='')
            print(file=f)


if __name__ == '__main__':
    convert('olympics.png', 'olympics.txt')
