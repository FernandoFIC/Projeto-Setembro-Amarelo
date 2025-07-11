# Projeto Setembro Amarelo

![Setembro Amarelo](https://img.shields.io/badge/Campanha-Setembro%20Amarelo-ffe600?style=for-the-badge&logoSize=auto)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.2.2-black?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?style=for-the-badge&logo=sqlite)

Este projeto é destinado ao desenvolvimento de uma aplicação web completa com o objetivo de divulgar e apoiar a campanha **Setembro Amarelo**, o mês da prevenção ao suicídio. O objetivo da plataforma é servir como um canal de informações não oficial e reunir recursos destinados a ajudarem pessoas que possam estar passando por momentos difíceis. **Se precisar, peça ajuda!**

## 📜 Sobre a Campanha

O Setembro Amarelo® é a maior campanha anti estigma do mundo, dedicada à prevenção do suicídio e à conscientização sobre a importância da saúde mental. Lançada no Brasil em 2013 e promovida anualmente desde 2014 pela Associação Brasileira de Psiquiatria (ABP) em parceria com o Conselho Federal de Medicina (CFM).

## ✨ Funcionalidades

O projeto conta com as seguintes funcionalidades:

* **Página Informativa:** Uma página inicial que apresenta a campanha, divulga estatísticas relevantes e destaca os canais oficiais da causa.
* **Mural de Apoio:** Uma seção dinâmica onde são exibidas todas as mensagens de apoio enviadas pelos usuários, ordenadas da mais recente para a mais antiga.
* **Formulário de Envio:** Um formulário simples e seguro para que qualquer pessoa possa enviar sua mensagem, com a opção de se identificar ou permanecer anônima.

## 💻 Tecnologias Utilizadas

A aplicação foi construída utilizando um conjunto de tecnologias modernas, separando as responsabilidades entre o front-end, o back-end e o banco de dados.

* **Front-end (Interface do Usuário):**
    * `HTML5`: Para a estruturação semântica do conteúdo.
    * `CSS3`: Para a estilização, layout e design responsivo, seguindo a identidade visual do Setembro Amarelo.
    * `Bootstrap`: Para elementos avançados de estilização, padronizando elementos visuais.
    * `JavaScript`: Para a interatividade e o carregamento dinâmico das mensagens no mural, consumindo a API do back-end.

* **Back-end (Lógica do Servidor):**
    * `Python 3`: Linguagem principal para toda a lógica da aplicação.
    * `Flask`: Um micro-framework leve e poderoso para criar o servidor web, gerenciar as rotas e a API.
    * `Django`:...

* **Banco de Dados:**
    * `SQLite 3`: Um banco de dados relacional baseado em arquivo, ideal para projetos de pequeno e médio porte pela sua simplicidade e por não necessitar de um servidor dedicado.

## 🚀 Como Executar o Projeto Localmente

Para rodar esta aplicação em seu ambiente de desenvolvimento, siga os passos detalhados abaixo.

### Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes softwares instalados em sua máquina:

* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/) (para clonar o repositório)

### Passo a Passo para a Instalação

1.  **Clone o repositório:**
    Abra seu terminal e execute o seguinte comando para criar uma cópia local do projeto.
    ```bash
    git clone [https://github.com/FernandoFIC/Projeto-Setembro-Amarelo.git](https://github.com/FernandoFIC/Projeto-Setembro-Amarelo.git)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd projeto-setembro-amarelo
    ```

3.  **Crie e ative um ambiente virtual:**
    O uso de um ambiente virtual (venv) é uma boa prática para isolar as dependências do projeto.
    ```bash
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    O arquivo `requirements.txt` contém as bibliotecas Python necessárias. Instale-as com um único comando.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Inicialize o Banco de Dados:**
    Este comando executa o script `database.py` para criar o arquivo `mensagens.db` e a tabela correspondente. **Execute este passo apenas uma vez.**
    ```bash
    python database.py
    ```

6.  **Inicie o servidor Flask:**
    Agora, sua aplicação está pronta para ser executada!
    ```bash
    python app.py
    ```

7.  **Acesse a aplicação:**
    Abra seu navegador de internet e acesse a seguinte URL:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

Pronto! A aplicação estará rodando em sua máquina local.

## 📂 Estrutura de Pastas

```
setembro-amarelo/
|-- app.py             # Arquivo principal do Flask (Back-end)
|-- database.py        # Script para criar o banco de dados
|-- static/            # Pasta para arquivos estáticos
|   |-- css/
|   |   `-- style.css  # Folha de estilos
|   `-- js/
|       `-- script.js  # Código JavaScript
|-- templates/         # Pasta para os templates HTML
|   |-- index.html     # Página inicial com o formulário
|   `-- mural.html     # Página para exibir as mensagens
|-- .gitignore         # Arquivo para ignorar arquivos no Git
|-- requirements.txt   # Dependências do Python
`-- README.md          # Este arquivo de documentação
```

---
💛Se precisar, peça ajuda!💛

**Desenvolvedores:**

[![Fernando](https://img.shields.io/badge/Fernando_F%C3%A1bio_Inoc%C3%AAncio_Cavalcante-ffe600?style=for-the-badge&logo=github&logoColor=black&link=https%3A%2F%2Fgithub.com%2FFernandoFIC)](https://github.com/FernandoFIC)

[![Davi](https://img.shields.io/badge/Davi_Rocha_Fortes_Bezerra-ffe600?style=for-the-badge&logo=github&logoColor=black&link=https%3A%2F%2Fgithub.com%2Fdavirfb)](https://github.com/davirfb)

[![Lucas](https://img.shields.io/badge/Lucas_Henrique_Ferreira_Alves-ffe600?style=for-the-badge&logo=github&logoColor=black&link=https%3A%2F%2Fgithub.com%2Flucashf04)](
https://github.com/lucashf04)

[![Christopher](https://img.shields.io/badge/Christopher_da_Silva_Nascimento-ffe600?style=for-the-badge&logo=github&logoColor=black&link=https%3A%2F%2Fgithub.com%2FChristopher-Nascimento)](
https://github.com/Christopher-Nascimento)
