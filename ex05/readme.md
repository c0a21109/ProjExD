# 第5回
## 逃げろこうかとん（ex04/dodge_bomb.py）
### 使い方
* 開始するとこうかとんが動かせるようになり，爆弾１つが動き出す。
* こうかとんは最初，真ん中にいる
* 爆弾も，こうかとんも画面外に出ることはできない
* 十字キー工科とんが移動する。
* 工科とんがダメージを受けるとソウルオーブ（黒紫色の玉）を残す。
* ソウルオーブがあるときにEキーを押すとディスミス状態になり，無敵になる。ソウルオーブは消える。
### 追加機能
* wasdでも工科とんが移動する。
* 爆弾に当たると♡（画面右上）が減る。
* 爆弾に当たると一定期間（500フレーム）無敵になる。
### 追加class
* heartクラス   :♡の描画を担当している。残りライフを受け取って描画する
* dismissクラス :無敵時間中のこうかとんを描画するクラス
* soulorbクラス :ソウルオーブ（無敵アイテムのようなもの）を描画するクラス
### やりたかったけれどできなかったもの
* こうかとんに攻撃できる機能をつけたかった。
* クラスを使ってLIFEを増やしたかったが，できなかった。
### ( ..)φメモメモ
* blit以外はwhileの外に書いた方がいい。
