

import unittest
class TestCountPrimes(unittest.TestCase):
    def test(self):
        case = "junyiacademy"
        expect = "ymedacaiynuj"
        result = inv_str(case)
        self.assertEqual(result, expect)

    def test2(self):
        case = "flipped class room is important"
        expect = "deppilf ssalc moor si tnatropmi"
        result = inv_word(case)
        self.assertEqual(result, expect)

    def test3(self):
        case = 15
        expect = 9
        result = removeNums(case)
        self.assertEqual(result, expect)
    

def inv_str(s):
    return s[::-1]

def inv_word(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = inv_str(words[i])
    return " ".join(words)

def removeNums(n):
    rm_cnt = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            continue
        if i%3 == 0 or i%5 == 0:
            rm_cnt += 1

    return n-rm_cnt


unittest.main()


'''
房間裡有三個袋子，一個只裝鉛筆，一個只裝原子筆，第三個有鉛筆也有原子筆。
袋子是不透明的，單從袋子的外表上看不出任何差異，你不知道哪個袋子裝什麼。
除了袋子上各貼了一個標示（"鉛筆"、"原子筆"、"混和"），且標示都是錯的
（e.g. 標示鉛筆的袋子可能是混和的或是只裝原子筆）。
你只能選一個袋子，拿出裡面一支筆，看是鉛筆還是原子筆，然後你要推論出這三
個袋子分別的情況。請列出你的作法，以及解釋為什麼這樣可以找到答案。

假設標示為
0<鉛筆> 1<原子筆> 2<混和>

因為標示都是錯的
鉛筆可能在   0<> 1<鉛筆> 2<鉛筆>
原子筆可能在 0<原子筆> 1<> 2<原子筆>
混和可能在   0<混和> 1<混和> 2<>

鉛筆在1
    原子筆在0
        混和只能在2，但不能在2，失敗
    原子筆在3
        混和在0，OK
鉛筆在2
    原子筆在0
        混和在1，OK

可能的組合
0<混和> 1<鉛筆> 2<原子筆>
0<原子筆> 1<混和> 2<鉛筆>

因為兩種組合同一個編號的袋子都裝不同東西
若隨便挑一個袋子確認內容物，即可知道是哪一個組合
'''


'''
有三個人一起到迪士尼遊玩，中午肚子餓了，去餐廳點了一份現在最夯的冰雪奇緣
雙人組，要價 900 元，付錢後，服務生發現今天套餐大特價，只要 750 元，因此
服務生應該退還 150 元給這三個人，但是這位服務生一時鬼迷心竅，決定暗槓 60
元，只退了 90 元給這三個遊客。
那麼：三人各出 300 元 - 服務生還給他們一人 30 元 = 三人各出 270 元。270
元 × 3 人+ 服務生私吞的 60 元 = 810 + 60 = 870 !? 怎麼不是 900 元呢？還
有 30 元去哪了呢？請用敘述的方式，儘量清楚解釋問題出在哪裡。

(900-750)-60=90

(300-30)*3 = 900-90 = 750+60
810 是三個人總共付出的金額，包括商品750與服務生暗槓的60
810再加上60，是沒有意義的
'''