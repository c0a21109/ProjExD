import random
import datetime


def shutudai(qa_list):
    qa = random.choice(qa_list)
    print("問題：" + qa["q"])
    return qa["a"]

def kaitou(ans_list):
    st = datetime.datetime.now()
    ans = input("解答：")
    end = datetime.datetime.now()
    if ans in ans_list:
        print("正解")
        print(F"解答時間{(end-st).seconds}秒")
    else:
        print("不正解")
    
if __name__ == "__main__":
    qa_list = [
        {"q":"サザエの旦那の名前は", "a":["ますお", "マスオ"]},
        {"q":"カツオの妹の名前は？", "a":["わかめ", "ワカメ"]},
        {"q":"タラオはカツオから見てどんな関係？", "a":["甥", "甥っ子", "おい", "おいっこ"]}
    ]

    ans_list = shutudai(qa_list)
    kaitou(ans_list)