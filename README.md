# Netflix Catalog Manager

Um gerenciador de catálogos para a Netflix, desenvolvido utilizando **Azure Functions** e um banco de dados baseado na nuvem (**Azure Cosmos DB** ou **Azure SQL Database**). Este projeto suporta operações CRUD (Criar, Ler, Atualizar e Excluir) para gerenciar o catálogo de títulos.

## 🎯 Funcionalidades
- Adicionar novos títulos ao catálogo.
- Listar todos os títulos disponíveis.
- Atualizar informações de títulos existentes.
- Remover títulos do catálogo.

## 🚀 Tecnologias Utilizadas
- **Azure Functions**: Para criar uma arquitetura de microsserviços escalável.
- **Azure Cosmos DB** ou **Azure SQL Database**: Como banco de dados para armazenar os títulos.
- **Python**: Linguagem de programação principal.
- **Azure CLI**: Para configurar e gerenciar recursos no Azure.

## 🛠️ Configuração e Instalação

### Pré-requisitos
- Conta no [Microsoft Azure](https://azure.microsoft.com/).
- Ferramentas instaladas:
  - [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local).
  - [Python 3.8+](https://www.python.org/downloads/).
  - [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

### Passos para Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/mario-evangelista/gerenciador-catalogo-streaming-azure-functions-bd.git
   cd gerenciador-catalogo-streaming-azure-functions-bd
   ```

2. Configure o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate # (Linux/Mac)
   .venv\Scripts\activate    # (Windows)
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure os recursos no Azure:
   - Crie um **Cosmos DB** ou **Azure SQL Database**.
   - Configure as variáveis de ambiente para conexão ao banco no arquivo `local.settings.json`:
     ```json
     {
       "IsEncrypted": false,
       "Values": {
         "AzureWebJobsStorage": "<Sua-Conexão-Azure>",
         "COSMOS_DB_URI": "<URI-do-Cosmos-DB>",
         "COSMOS_DB_KEY": "<Chave-do-Cosmos-DB>",
         "SQL_DB_CONNECTION": "<String-de-Conexão-SQL>"
       }
     }
     ```

5. Inicie o projeto localmente:
   ```bash
   func start
   ```

6. Teste os endpoints utilizando ferramentas como **Postman** ou **curl**.

### Publicação no Azure
1. Faça login no Azure CLI:
   ```bash
   az login
   ```

2. Publique o aplicativo:
   ```bash
   func azure functionapp publish <APP_NAME>
   ```

## 📚 Endpoints Disponíveis
- **GET /api/CatalogManager**: Lista todos os títulos.
- **POST /api/CatalogManager**: Adiciona um novo título. Envie um corpo JSON com:
  ```json
  {
    "id": "1",
    "name": "Breaking Bad",
    "description": "Um professor de química vira produtor de metanfetamina.",
    "year": 2008,
    "genre": "Drama",
    "rating": 9.5
  }
  ```
- **PUT /api/CatalogManager**: Atualiza um título existente. Corpo JSON semelhante ao `POST`.
- **DELETE /api/CatalogManager?id=<ID>`**: Remove um título pelo ID.

## 🧑‍💻 Contribuindo
Contribuições são bem-vindas! Siga os passos abaixo:
1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Adiciona minha nova feature"
   ```
4. Envie para sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### 🌟 Agradecimentos
Obrigado por explorar este projeto! Se gostou, não esqueça de deixar uma ⭐ no repositório. 😊
