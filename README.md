# Flix App 🎥

Um sistema modular para gerenciamento de dados relacionado a filmes, gêneros, atores, avaliações e autenticação de usuários. O projeto utiliza Python, com uma arquitetura limpa e organizada para cada funcionalidade.

## Tecnologias Utilizadas 🛠️

- **Python**: Linguagem principal utilizada no projeto.
- **Flake8**: Ferramenta para garantia da qualidade do código.
- **HTML/CSS**: Para estruturação e estilização das páginas (ainda em desenvolvimento).
- **Virtualenv**: Para isolação do ambiente de dependências.

## Estrutura do Projeto 🗂️

A estrutura do projeto está organizada da seguinte forma:

```
flix_app/
├── actors/
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
├── api/
│   ├── __init__.py
│   └── service.py
├── genres/
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
├── home/
│   ├── __init__.py
│   ├── page.py
├── login/
│   ├── __init__.py
│   ├── page.py
│   └── service.py
├── movies/
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
├── reviews/
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
├── venv/
├── .flake8
├── .gitignore
├── app.py
├── config.toml
├── requirements_dev.txt
└── requirements.txt
```

### Principais Pastas e Arquivos

- **actors/**, **genres/**, **movies/**, **reviews/**: Cada módulo é responsável por uma área específica do sistema, contendo lógica de serviços, repositórios e interfaces de página.
- **login/**: Gerenciamento de autenticação e sessões de usuários.
- **api/**: Contém serviços para exposição ou consumo de APIs.
- **home/**: Módulo inicial para renderização da página principal.
- **config.toml**: Configurações do projeto.
- **requirements.txt**: Dependências necessárias para execução.
- **venv/**: Ambiente virtual para dependências.

## Funcionalidades 🚀

- CRUD (Create, Read, Update, Delete) completo para:
  - Atores
  - Filmes
  - Gêneros
  - Avaliações
- Autenticação e gerenciamento de sessões.
- Arquitetura modular para maior manutenção e escalabilidade.

## Como Executar o Projeto 🔧

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/flix-app.git
   ```
2. **Entre no diretório do projeto:**
   ```bash
   cd flix-app
   ```
3. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Unix ou MacOS
   source venv/bin/activate
   ```
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure o arquivo config.toml se necessário.**

6. **Execute o projeto:**
   ```bash
   python app.py
   ```
7. **Acesse o projeto no navegador:**
   Abra o navegador e acesse `http://127.0.0.1:5000/`.

## Contribuindo 🤝

Contribuições são bem-vindas! Se você tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Contato 💬

Caso tenha dúvidas ou sugestões, entre em contato:

- **Nome**: Leandro Fernandes
- **Email**: leandrofernandes1600@gmail.com
- **GitHub**: https://github.com/LeandroFernandess

---

*Documentação atualizada em: `11/01/2025`.* 🚀

