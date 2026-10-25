# cp-library

競技プログラミング用のライブラリとテンプレート。

| ディレクトリ | 中身 |
| --- | --- |
| `python/` | Python (PyPy) 用ライブラリ |
| `cpp/` | C++ 用テンプレート |
| `snippets/` | VSCode 用の入力スニペット |

AtCoder の生成AI対策ルールに従い、生成AIを使って書いたコードもここで事前に公開し、
提出時にはこのリポジトリの URL を記載している。

ac-library-python と機能が重なるもののうち、PyPy で計測して速かったもの
（SCC、2-SAT、Z algorithm、floor_sum）だけを残している。CRT と suffix array は
`atcoder.math.crt` と `atcoder.string.suffix_array` を使う。
