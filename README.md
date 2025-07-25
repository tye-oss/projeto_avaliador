# 🧃 PyOnERP — Sistema de Estoque e Vendas com Interface Gráfica

**PyOnERP** é um sistema modular de controle de estoque e fluxo de vendas desenvolvido em Python com integração ao banco de dados MySQL. Com interface gráfica intuitiva, é ideal para pequenos comércios que desejam gerenciar produtos de forma prática e segura.

---

## 🚀 Funcionalidades

- ✅ Cadastro, listagem e remoção de produtos
- 🧾 Interface gráfica com Tkinter (modo visual)
- 💳 Caixa para processamento de compras e cálculo de troco
- 🔐 Integração com banco de dados MySQL via `.env`
- 📋 Modo offline com backend simulado (sem conexão)
- 🛠 Arquitetura extensível e testável
- 🗃️ Separação clara entre interface, lógica de negócio e dados

---

## 🗂 Estrutura do Projeto

pyonerp/ ├── main.py # Ponto de entrada ├── interface_gui.py # Interface gráfica de estoque ├── caixa_gui.py # Interface separada do caixa ├── backend_mysql.py # Conexão com MySQL via .env ├── backend_simulado.py # Simulador para modo offline ├── .env # Credenciais do banco (não versionar) ├── README.md # Documentação do projeto


---

## ⚙️ Pré-requisitos

- Python 3.9+
- MySQL Server instalado e configurado
- Instalação de dependências:

```bash
pip install mysql-connector-python python-dotenv
🔐 Arquivo .env
Crie um .env com as credenciais do banco:

env
DB_HOST=localhost
DB_USER=usuario
DB_PASSWORD=senha
DB_NAME=your_bank
🛢️ Estrutura da Tabela no MySQL
Execute no MySQL:

sql
CREATE TABLE produtos (
  nome VARCHAR(255) PRIMARY KEY,
  quantidade INT NOT NULL,
  preco FLOAT NOT NULL
);
▶️ Como executar
bash
python main.py
💡 Para testar sem banco, troque o backend para FakeBackend dentro do interface_gui.py.

🧪 Modo Debug
Dentro do código, você pode alternar o backend:

python
modo_debug = True

if modo_debug:
    self.db = FakeBackend()
else:
    self.db = Backend()  # com conexão MySQL
📌 Contribuições
Sinta-se à vontade para abrir issues ou pull requests com melhorias de interface, suporte a múltiplos usuários, relatórios ou persistência em arquivos!

👨‍💻 Autor
Desenvolvido com ❤️ por Jonnathan 📍 Curitiba, Brasil

📝 Licença
Este projeto é livre para uso e modificação. Licença MIT opcional.
