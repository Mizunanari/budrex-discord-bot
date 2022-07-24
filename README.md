# ふいうちbot

ポケモンの技をチャンネルに投稿すると、投稿された技が攻撃技でない場合と技の優先度が条件を満たさない場合に「しかしうまくきまらなかった」と投稿される。そうでない場合は、「（ユーザー名）はたおおれた」と投稿するbot。

ポケモンの技データは[PokéAPI](https://pokeapi.co/)から取得している。

```text
.
├── README.md
├── discord_bot
│   ├── env.py
│   ├── get_move.py     # PokeAPIから、技データを取得するスクリプト
│   ├── main.py
│   └── moves.py        # 技の判定を行う
├── doc
├── poetry.lock
├── pyproject.toml
└── res.json            # ./discord_bot/get_move.pyにて取得した技データ
```

## 実行コマンド

プロジェクトルートで実行すること。

```bash
python discord_bot/main.py
```

APIデータ取得コマンド

```bash
python discord_bot/get_move.py
```

## poetryについて

poetryを使用している。サーバーなどで環境を構築する際はこちら。

```bash
poetry install
poetry shell
```