
# 🧠 smart-text — бібліотека для обробки природної мови

`smart-text` — це легка бібліотека Python для попередньої обробки текстів, лематизації, видалення стоп-слів і аналізу частоти слів.

## 🔧 Встановлення

```bash
pip install smart-text
````

## 💡 Використання

```python
from smart_text import TextProcessor

tp = TextProcessor("Я люблю програмувати на Python!")
print(tp.tokens)
print(tp.lemmatized())
```

## 🧰 Можливості

* Токенізація речень і слів
* Лематизація української та англійської мов
* Видалення пунктуації й стоп-слів
* Підрахунок частоти лексем

## 📦 Залежності

* `nltk`
* `pymorphy3`
* `re`

## 🧪 Тести

```bash
pytest tests/
```

## 🔗 Посилання

* [Документація](https://smart-text.readthedocs.io)
* [PyPI сторінка](https://pypi.org/project/smart-text/)
