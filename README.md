*pt / en*

## Sistema de Banco em Python
### Desafio de código proposto no bootcamp Python AI Backend Developer da DIO
<b>Objetivo:</b> <br>Criar um sistema bancário com as operações sacar, depositar e visualizar extrato;
A v1 do projeto trabalha apenas com um usuário, não sendo necessário se preocupar em identificar número da agência e conta bancária;
- <b>Depósito:</b>
    - Deve ser possível depositar apenas valores positivos;
    - Todos os depósitos devem ser armazenados em uma variável (os quais serão exibidos na operação de extrato);
- <b>Saque:</b>
    - O sistema deve permitir realizar 3 saques diários com limite de R$500 por saque;
    - Caso o usuário não possua saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo;
    - Todos os saques devem ser armazenados em uma variável (os quais serão exibidos na operação de extrato);
- <b>Extrato:</b> 
    - Essa operação deve listar todos os depósitos e saques realizados;
    - No fim da listagem deve ser exibido o saldo atual da conta;
    - Se o extrato estiver em branco exibir a mensagem: Não foram realizadas movimentações.
    - Os valores devem ser exibidos utilizando o formato R$xxx.xx;

<hr>

### Melhorias implementadas
- Utilização dos blocos try e except para lidar com exceções;
- Utilização da biblioteca datetime para registrar data e hora das transações realizadas pelo usuário;


<hr>

## Python Bank System
### Code challenge proposed in the Python AI Backend Developer bootcamp by DIO
<b>Objective:</b> <br>Create a banking system with operations to withdraw, deposit, and view statement;
The project's v1 works with only one user, so there's no need to worry about identifying agency and bank account numbers;

- <b>Deposit:</b>
    - It should only be possible to deposit positive values;
    - All deposits must be stored in a variable (which will be displayed in the statement operation);
- <b>Withdrawal:</b>
    - The system should allow up to 3 withdrawals per day with a limit of $500 per withdrawal;
    - If the user doesn't have enough balance, the system should display a message indicating that it's not possible to withdraw due to insufficient funds;
All withdrawals must be stored in a variable (which will be displayed in the statement operation);
- <b>Statement:</b>
    -  This operation should list all deposits and withdrawals made;
    - At the end of the list, the current account balance should be displayed;
    - If the statement is empty, display the message: No transactions have been made.
    - Values should be displayed using the format $xxx.xx;
<hr>

### Implemented Improvements
- Usage of try and except blocks to handle exceptions;
- Usage of the datetime library to record the date and time of user transactions.