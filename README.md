VideoCapture()で得た映像をトーンカーブ,色調変換,フィルターを使い,(Trackbarの値に応じて)変化させる処理を実装した.

使い方:trackbarを左右に動かして明るさ調節,色調調節,ぼかし,などの処理を行う.

実行:pythonの使える環境で実行

参考にしたサイトのリンク

http://optie.hatenablog.com/entry/2018/03/03/141427

: S字トーンカーブの数式を引用

http://opencv.jp/opencv-2.1/cpp/image_filtering.html
: cv::blurの項目を参考

トーンカーブでの処理動画  :  https://youtu.be/kEMSa6eO21Q
フィルターでの処理動画  :  https://youtu.be/8JdUMhQb_mU
色調変化の処理動画   :  https://youtu.be/V9yP8kroKRA
