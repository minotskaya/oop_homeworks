# Moodle breaker
_Make your Moodle life easier_

## Запуск
```bash
git clone https://github.com/alekseik1/moodle-breaker
cd moodle-breaker
pip install -r requirements.txt
```

Откройте `settings.py` и запишите туда логин/пароль от мудла,
а также ссылки на задания.

`HOMEWORK_URLS` - это задания с наивысшей оценкой.

`MEAN_URLS` - это задания со средней оценкой.

Ссылки надо писать в кавычках, ссылки должны быть вида:
`'http://moodle.phystech.edu/mod/quiz/view.php?id=28639'`

**ВНИМАНИЕ: обязательно прочитайте предупреждение в `settings.py`**

Чтобы запустить взлом, вбейте
```bash
python run.py
```

## Что работает
- [x] Задания со свободным ответом (ввод с клавиатуры)
- [x] Задания с _Radio button_ (клик по кружочку)
- [ ] Задания с чекбоксами ([пример](http://moodle.phystech.edu/mod/quiz/view.php?id=42800))
- [x] Задания с `picker` (один вариант из выпадающего списка)
- [ ] Задания на несколько страниц ([пример](http://moodle.phystech.edu/mod/quiz/view.php?id=42797))

Также скрипт умеет искать ваши лучшие попытки и тырить ответы с них.

**НИЧЕГО не работает, если мудл не показывает в конце ответы!**

Мог что-то упустить, пишите в ВК (alekseik1) или ТГ (@alekseik1), если что-то упустил.

## Contribution
Вы здорово поможете проекту, если сообщите о пропущенных типах задач.
