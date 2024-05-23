*pt / en*

## Desafio de Código - Sistema de Banco em Python - Parte 2
<b>Objetivos: </b>
- Modularizar, separando as funções existentes de saque, depósito e extrato em funções; 
- Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária vinculada ao usuário;
- Opcional: novas funcionalidades, como função de listar contas.
<b>Requisitos:</b>
- <b>Saldo:</b> deve receber os argumentos apenas por nome (keyword only); 
    - Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
    - Sugestão de retorno: saldo e extrato;
- <b>Depósito:</b> deve receber os argumentos apenas por posição (positional only). 
    - Sugestão de argumentos: saldo, valor, extrato;
    - Sugestão de retorno: saldo e extrato.
- <b>Extrato:</b> deve receber os argumentos por posição e nome (positional only e keyword only). 
    - Argumentos posicionais: saldo;
    - Argumentos nomeados: extrato.
- <b>Criar usuário:</b>
    - Devem ser armazenados em uma lista;
    - Cada usuário é composto por nome, data de nascimento, cpf e endereço;
    - O endereço é uma string com o formato: logradouro, nº - bairro - cidade/sigla do estado;
    - Deve ser armazenado somente os números do CPF;
    - Não deve ser possível cadastrar 2 usuários com o mesmo CPF.
- <b>Criar conta corrente:</b>
    - Devem ser armazenados em uma lista;
    - Uma conta é composta por: agência, número da conta e usuário;
    - O número da conta é sequencial, iniciando em 1;
    - O número da agência é fixo: “0001”;
    - O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.
Dica: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

## Code Challenge - Bank System in Python - Part 2
<b>Objectives:</b>
- Modularize, separating existing functions for withdrawal, deposit, and statement into functions;
- Create two new functions: register user (client) and register bank account linked to the user;
- Optional: new functionalities, such as listing accounts.
<b>Requirements:</b>
- <b>Balance:</b> must receive arguments only by name (keyword only);
    - Argument suggestions: balance, value, statement, limit, number_withdrawals, withdrawal_limit.
    - Return suggestions: balance and statement;
- <b>Deposit:</b> must receive arguments only by position (positional only).
    - Argument suggestions: balance, value, statement;
    - Return suggestions: balance and statement.
- <b>Statement:</b> must receive arguments by position and name (positional only and keyword only).
    - Positional arguments: balance;
    - Named arguments: statement.
- <b>Create user:</b>
    - Must be stored in a list;
    - Each user consists of name, date of birth, cpf, and address;
    - The address is a string with the format: street, number - neighborhood - city/state abbreviation;
    - Only the numbers of the CPF must be stored;
    - It must not be possible to register 2 users with the same CPF.
- <b>Create checking account:</b>
    - Must be stored in a list;
    - An account consists of: branch, account number, and user;
    - The account number is sequential, starting at 1;
    - The branch number is fixed: "0001";
    - A user can have more than one account, but an account belongs only to one user.
Tip: to link a user to an account, filter the list of users by searching for the CPF number provided for each user in the list.