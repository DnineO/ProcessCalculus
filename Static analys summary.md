# Статические анализаторы кода

## Статический анализ кода с Mypy

Python — динамически типизированный язык. Это значит, что переменная связывается с типом данных не в момент объявления, а в момент присваивания ей значения. То есть одна и та же переменная может быть и строкой, и целым числом, и каким-либо другим типом в зависимости от последнего присвоенного ей значения.

```python
# Например, вот одна и та же переменная с разными типами данных.
# Python определяет тип данных динамически:

# string
var_name = "string here"

# integer
var_name = 1234
```

А вот примеры языков со статической типизацией, где для каждой переменной задан один конкретный тип данных, и в логике кода нужно придерживаться именно его:

```clike
# Для многих языков обязательно предварительное объявление типа.

# string
str str_var_name = "string here"

# integer
int int_var_name = 1234
```

### Плюсы и минусы динамической типизации

Главное преимущество динамической типизации в том, что вам может быть лень постоянно прописывать типы, и такой язык, как Python, в этом поможет.

А вот недостатков больше:

- как правило, вы сталкиваетесь с ошибками на более поздних этапах разработки;
- код работает медленнее, ведь Python постоянно вычисляет типы;
- код становится менее безопасным, так как на входе и выходе функции у одной и той же переменной могут быть разные типы данных;
- читать ваш код становится сложнее, поскольку другой человек не может быть уверен в том, что уже объявленная переменная не изменит свой тип в дальнейшем.

### Статическая типизация в Python

В Python нет статической типизации как таковой, но есть аннотации типов, которые проверяются статическими анализаторами с целью контроля типов переменных.

Обратите внимание на Mypy. Это статический анализатор типов для Python, который позволяет находить ошибки несоответствия типов в коде. Mypy выводит ошибку, если при работе с аннотациями типов значение переменной не соответствует присвоенному ей типу.

```python
from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

fib(10)
fib("10")
```

В результате запуска статического анализатора Mypy в приведённом выше коде вы получите следующую ошибку: `main.py:10: error: Argument 1 to "fib" has incompatible type "str"; expected "int"`. Таким образом Mypy предупреждает, что мы пытаемся присвоить строковое значение переменной с целочисленным типом данных. Это лишь один из примеров использования Mypy.

Если ваш код работает на проде, и вам важна его устойчивость к ошибкам, связанным с типизацией, используйте инструмент [Mypy](https://mypy.readthedocs.io/en/stable/getting_started.html).



## Быстрый поиск ошибок и чистый код с SonarLint

Сейчас почти во всех IDE есть линтер — статический анализатор возможных ошибок. Другими словами, он предугадывает ещё до запуска кода, что может пойти не так, и выделяет предполагаемые ошибки.

В свою очередь, *динамический* анализ не предугадывает, а действительно запускает/компилирует части кода, чтобы определить, работает ли он, но делает это автоматически в фоновом режиме. То есть он на самом деле знает, что пойдёт не так в процессе выполнения программы.

SonarLint — это тот самый динамический анализатор кода, который поможет решить следующие проблемы.

### Лишний код

Допустим, вы не удалили закомментированные части кода, оставили неиспользуемые функции и прочие рудименты. SonarLint предупредит об этом, и вы сможете своевременно очистить код от всего лишнего.

### Уязвимости

Большая обновляемая база данных с перечнем уязвимостей позволяет плагину вовремя предупреждать о любых известных уязвимостях, которые встречаются в вашем коде.

### Когнитивная сложность

Если говорить кратко, разработчики плагина создали математическую формулу, которая может оценить, насколько читабелен ваш код.

Это не только полезно, но и просто. Каждый раз, когда SonarLint предупреждает вас о чрезмерной сложности, это сопровождается объяснением правила, которое вы нарушили. Например, «слишком большая вложенность операторов if», более известная как спагетти-код. Удобно, правда?

Плагин SonarLint позволяет использовать лучшие практики и писать понятный чистый код.



## ИИ автодополнение и быстрый доступ к документации с Kite

У современных IDE есть встроенное автозаполнение.

Встроенный инструмент обычно использует документацию для определения имён и типов возможных функций и параметров. Но что если редактор получит доступ к коду из всех публичных репозиториев GitHub и начнёт подтягивать не просто имена, а целые строки кода? И это реализовано в Kite.

Разберём подробнее особенности Kite — инструмента для Python с функциями умного автодополнения и быстрого доступа к документации.

### Умные подсказки

Плагин Kite смотрит в комплексе ваш код, переменные, часто используемые имена параметров, документацию.

### Copilot для документации

Прежде чем беспокоить более опытного коллегу или мчаться за ответами на Stack Overflow, почитайте документацию.

[Kite Copilot](https://kite.com/copilot/) упрощает поиск по документации. Он работает параллельно с IDE и показывает информацию о любых объектах или функциях, на которые наведён курсор.

### Работает локально, приватно

Вдобавок ко всему, плагин создан для локальной работы, так что вы получаете быстрые советы, работа происходит в автономном режиме, и ваш код никогда не будет отправлен в облако.

Это крайне важно для людей с плохим интернет-соединением и тех, кто работает с закрытым исходным кодом.

Всё, что нужно сделать, это загрузить и установить плагин Kite для вашего редактора: есть бесплатная версия и Free Beta на Pro план с умным автозаполнением.



##### Источники: https://tproger.ru/translations/3-tools-for-python/ - tproger.ru