# Automação de Testes: Urban Routes

Este projeto consiste na automação de testes de ponta a ponta (E2E) para o serviço de transporte **Urban Routes**. O foco é validar o fluxo completo do usuário, desde a definição de rotas até a solicitação de um táxi com preferências específicas, garantindo confiabilidade e eficiência na experiência do usuário.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework de Testes:** Pytest
- **Automação de Browser:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM) para garantir modularidade e manutenção

## Casos de Teste Automatizados

O projeto cobre os seguintes cenários críticos de negócio:

- **Definição de Rota:** Validação da inserção correta dos endereços de origem e destino.
- **Seleção de Plano:** Verificação da escolha do plano "Comfort".
- **Fluxo de Usuário:**
    - Cadastro de número de telefone com validação de código via SMS.
    - Adição de cartão de crédito.
    - Inclusão de comentários para o motorista.
    - Adição de itens extras (cobertor, lenços e sorvetes).
- **Finalização:** Validação do surgimento da janela modal de busca de motorista após a confirmação do pedido.

## Estrutura do Projeto

- `pages/`: Contém as classes que mapeiam os elementos da interface (Page Objects).
- `data/`: Arquivo de configuração com dados de teste (endereços, números, cartões).
- `helpers/`: Funções auxiliares para operações como recuperação de código SMS.
- `test_urban_routes.py`: Conjunto de testes automatizados executados pelo Pytest.

## Como Executar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
