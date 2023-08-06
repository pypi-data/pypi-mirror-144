|License| |Contact|

Добавление PLAYER_ID игроков к данным play-by-play
=================

Play-by-play данные, которые предоставляет НБА на своём сайте, не
содержат информации о том, кто из игроков находится на площадке.

Пакет **player_on_court** по play-by-play данным заполняет эти
данные.

**Важно: данный пакет не получает данные play-by-play с сайта НБА.
Их нужно получить заранее, например с помощью пакета nba_api
<https://github.com/swar/nba_api>**

Пример использования
----------------
.. code:: python

    >>> import player_on_court as poc
    >>> print(df.shape[1])
    34
    >>> df1 = poc.adding_player_on_court(df)
    >>> print(df1.shape[1])
    44

.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target:  https://opensource.org/licenses/MIT
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
    :target:  https://t.me/nbaatlantic
