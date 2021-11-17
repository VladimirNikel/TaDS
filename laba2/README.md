# 2 лабораторная работа - System Tests
> Необходимо реализовать системное тестирование в виде проверки категорий товаров на сайте www.avito.ru.
> 
> Для этого:
> 1. Формируем дата-сет
> 2. Заходим на Авито
> 3. Ищем по ключевому слову товар
> 4. Проверяем, что в выдаче есть нужный товар
> 
> Должно получиться:
> 1. Data driven test
> 2. С ожидаемыми результатами
> 3. Сложный **asserting** по 5 и более элементам
> 
> Найти отличия и чем схожи:
> - XPATH
> - CSS
> - Браузер - что это?
> - DOM - что это?
> - Rendering - это откуда и зачем?
> 


## Ход работы:

Чтобы запустить выполнение приложения, необходимо выполнить команду ```python3 silenium_test.py```

Чтобы запустить тестирование сервиса, необходимо выполнить команду ```python3 -m pytest -rA silenium_test.py```


## Результаты выполнения тестирования

Полученные результаты тестирования сведены в файл `result_test.md`



## Инструменты:
- **GIT** (устанавливается командой `sudo apt install git -y`)
- **Python** (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов **Python PIP3** (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные **модули**:
    + **pytest** `sudo pip3 install pytest`
    + **selenium** - `sudo pip3 install selenium`
- chromedriver_96 - https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/
- ```bash
  sudo apt-get install libxss1 libappindicator1 libindicator7
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

  sudo dpkg -i google-chrome*.deb
  sudo apt-get install -f```