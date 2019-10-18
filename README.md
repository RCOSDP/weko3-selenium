# WEKO3 selenium test code repository (experimental)

WEKO3(https://github.com/RCOSDP/weko)のためにSeleniumテストコードリポジトリです。
Selenum IDE(https://www.seleniumhq.org/selenium-ide/)を利用して作成したコードをベースにしています。

## 動かし方

1. seleniumパッケージをインストールします。

```bash
pip install selenium
```

1. ウェブブラウザドライバを https://www.seleniumhq.org/download/　からダウンロードします。現時点では chromeとfirefox用のコードを用意しています。

2. ダウンロードしたドライバをPATHに含めます。

3. WEKO3のホストアドレスを環境変数に設定します。

```
export WEKO3_HOST="https://localhost"
```

4. テストコードを実行します。


```
$ pytest chrome/test_login.py 
============================= test session starts ==============================
platform darwin -- Python 3.6.7, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
rootdir: 
plugins: pep8-1.0.6, cov-2.7.1
collected 1 item                                                               

chrome/test_login.py .                                                   [100%]

============================== 1 passed in 4.40s ===============================
```




