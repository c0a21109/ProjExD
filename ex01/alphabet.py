import random 
import datetime
import string

taishoumozisuu = 10
kessonkosuu = 2
kaitousuu = 3

def shutudai():
    alphabets = list(string.ascii_uppercase)
    mondai = random.sample(alphabets, taishoumozisuu)
    print("対象文字", end = " ")
    for i in mondai:
        print(i, end = " ")
    print()
    kessonmozi = random.sample(mondai,kessonkosuu)
    for i in kessonmozi:
        mondai.remove(i)
    print("表示文字", end = " ")
    random.shuffle(mondai)
    for i in mondai:
        print(i, end = " ")
    print()

    return kessonmozi

def kaitou(kessonmozi):
    ans = int(input("欠損文字はいくつあるでしょうか？"))

    if  ans == len(kessonmozi):
        print("正解です。それでは，具体的な欠損文字を入力してください")
        kesson1 = kessonmozi
        print(kessonmozi)

        for i in range(len(kessonmozi)):

            a = str(input(F"{i + 1}個めの文字を入力してください"))
            if a in kessonmozi:
                kesson1.remove(a)

            else:
                print("不正解です。またチャレンジしてください")
                print("-----------------------------------")
                break
            
            if len(kesson1) == 0:
                return "Finish"
                break

    else:
        print("不正解です。またチャレンジしてください")




if __name__ == "__main__":

    for _ in range(kaitousuu):
        aaa = shutudai()
        hoge = kaitou(aaa)
        if hoge == "Finish":
            print("おめでとうございます")
            break