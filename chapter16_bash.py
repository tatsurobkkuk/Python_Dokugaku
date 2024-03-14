### Chapter 16: Bash
# Ex 1. Bash でself-taught と出力しよう。
> echo Self-taught

# Ex 2. ホームディレクトリ以外のパスから、ホームディレクトリに現在の作業ディレクトリを移動しよう。
# パスは絶対パスと相対パスの両方で実行しよう。
# 絶対パス
cd /Users/tatsurotanioka/iCloud/Learning/Python_Dokugaku /Users/tatsurotanioka/
# 相対パス
cd Users/tatsurotanioka/iCloud/Learning/Python_Dokugaku /Users/tatsurotanioka/

# Ex 3. 環境変数$python_projectsを作って、あなたがPythonのファイルを置いているディレクトリの
# 絶対パスを設定しよう。環境変数を.profile ファイルに保存して、cd $python_projects コマンドで
# そのディレクトリに移動しよう。
echo python_projects="/Users/tatsurotanioka/iCloud/Learning/Python_Dokugaku" > .zprofile
cd $python_projects