5th percentileの計算
=
*研究データ処理用*

* 研究で使う多量の機械学習モデルのトレーニング結果を解析するプログラム
* 結果はフォルダー毎に保存されていて、一つのフォルダーが一回のトレーニングに対応する

##ファイル説明
***
***excel_recal.py***  
トレーニング結果の5th percentileをフォルダー毎に計算し、Excelファイルに出力する。  
line 10 ```path```で directory入力

***excel_NORM95_30_sum.py***  
5th percentileの結果を一つのExcelファイルにまとめる。  
line 10 ```path```で directory入力

***excel_NORM95_30_sum_par_for_sort.py***  
結果を並び替えるため、フォルダー名に基づいてトレーニングのハイパーパラメーターと5th percentileをExcelに入力する。  
line 5 ```path```で directory入力
