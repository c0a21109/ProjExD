# 第6回
## うんこうかとん（名前は未定）（ex06/kihon.py）
### ゲーム概要
* 開始すると２つのstuffが動かせるようになる。
* 左のプレイヤーはWASDで移動，eキーで弾を設置する。
* 右のプレイヤーは十字キーで移動，SPACEで弾を設置する。
* 弾の設置フェイズと，弾の発射フェイズがある。
* 設置フェイズでのみ弾の設置が可能で，発射フェイズに切り替わった瞬間に弾が動き出す。
* 一定時間後に弾が動き出すのでそれを避ける。当たった方は負け。
### 追加機能
* フェイズが切り替わるまでの時間を示すタイマーを設置
### class
* クラスscreen   :スクリーンの描画クラス
* クラスPlayer   :Player1, Player2の弾，座標などのクラス
* クラスBullets  :弾の挙動とかのクラス
### 参考
* https://goodlucknetlife.com/python-shooting-title-gameclear/
* https://neutralx0.net/tools/dot3/
* https://runebook.dev/ja/docs/pygame/ref/time
* 
* 