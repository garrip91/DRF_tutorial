<br/>
<p align="center">
  <a href="https://github.com/garrip91/password_generator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Веб-проект (сервис) "Генератор паролей"</h3>

  <p align="center">
    Readme веб-проекта (сервиса) "Генератор паролей"
    <br/>
    <br/>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/Garrip91/password_generator?color=dark-green) ![Issues](https://img.shields.io/github/issues/Garrip91/password_generator) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](images/screenshot.png)

Этот проект является сервисом по генерации случайных паролей по 3-м критериям:


* Длина пароля (от 6-и до 14-и символов)
* Будут встречаться латинские буквы в верхнем регистре
* Будут встречаться числа
* Будут встречаться специальные символы

## Built With

Веб-проект (сервис) создан с помощью Python, Django

## Getting Started

Шаги для начала работы:

### Prerequisites

Перед установкой проекта требуется установить

* python

```
https://www.python.org/
```

### Installation

1. Clone the repo

```sh
git clone https://github.com/garrip91/password_generator
```


2. Install python virtual environment

```sh
python -m venv venv
source venv/bin/activate
```

3. Install python packages

```sh
pip install -r requirements.txt
```

4. Migrate base

```sh
python manage.py migrate
```

4. Run server

```sh
python manage.py runserver
```

## Usage

Данный веб-проект (сервис) Вы можете использовать для генерации рандомных паролей длиной от 6-и до 14-и символов, а также содержащих латинские буквы в верхнем регистре, числа и специальные символы

## Contributing



### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/newFeature`)
3. Commit your Changes (`git commit -m 'Add some newFeature'`)
4. Push to the Branch (`git push origin feature/newFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/Garrip91/password_generator/blob/main/LICENSE.md) for more information.

## Authors

* **Garrip91** - *Backend developer* - [Garrip91](https://github.com/garrip91) - *Создал сайт*

## Acknowledgements

* [Garrip91](https://github.com/garrip91)
* [password_generator](https://github.com/garrip91/password_generator)
* [Python](https://www.python.org/)
