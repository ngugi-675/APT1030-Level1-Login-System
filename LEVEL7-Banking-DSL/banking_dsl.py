#!/usr/bin/env python3
"""
Banking Domain Specific Language (DSL) - Interpreter
Parses and executes banking transaction commands
APT1030-A Fundamentals of Programming Languages
"""

import re
from typing import Dict, Tuple, Optional, List
from datetime import datetime
from enum import Enum

# ============================================
# DATA STRUCTURES
# ============================================

class TransactionType(Enum):
    """Types of transactions"""
    TRANSFER = "TRANSFER"
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    BALANCE = "BALANCE"

class Account:
    """Bank account representation"""
    def __init__(self, account_id: str, initial_balance: float = 0):
        self.account_id = account_id
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount: float) -> bool:
        self.balance += amount
        self.transaction_history.append({
            'type': 'DEPOSIT',
            'amount': amount,
            'balance': self.balance,
            'timestamp': datetime.now()
        })
        return True
    
    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append({
                'type': 'WITHDRAW',
                'amount': amount,
                'balance': self.balance,
                'timestamp': datetime.now()
            })
            return True
        return False
    
    def transfer(self, amount: float, to_account) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            
            self.transaction_history.append({
                'type': 'TRANSFER_OUT',
                'amount': amount,
                'to': to_account.account_id,
                'balance': self.balance,
                'timestamp': datetime.now()
            })
            to_account.transaction_history.append({
                'type': 'TRANSFER_IN',
                'amount': amount,
                'from': self.account_id,
                'balance': to_account.balance,
                'timestamp': datetime.now()
            })
            return True
        return False
    
    def __str__(self):
        return f"Account({self.account_id}, Balance: KES {self.balance:,.2f})"

# ============================================
# DSL PARSER
# ============================================

class BankingDSLParser:
    """Parses banking DSL commands into structured data"""
    
    # Command patterns using regex
    PATTERNS = {
        'TRANSFER': re.compile(
            r'TRANSFER\s+(\d+(?:\.\d+)?)\s+FROM\s+(\w+)\s+TO\s+(\w+)(?:\s+IF\s+BALANCE\s*>\s*(\d+(?:\.\d+)?))?',
            re.IGNORECASE
        ),
        'DEPOSIT': re.compile(
            r'DEPOSIT\s+(\d+(?:\.\d+)?)\s+TO\s+(\w+)',
            re.IGNORECASE
        ),
        'WITHDRAW': re.compile(
            r'WITHDRAW\s+(\d+(?:\.\d+)?)\s+FROM\s+(\w+)',
            re.IGNORECASE
        ),
        'BALANCE': re.compile(
            r'BALANCE\s+(\w+)',
            re.IGNORECASE
        ),
        'CREATE': re.compile(
            r'CREATE\s+ACCOUNT\s+(\w+)(?:\s+WITH\s+(\d+(?:\.\d+)?))?',
            re.IGNORECASE
        ),
        'HISTORY': re.compile(
            r'HISTORY\s+(\w+)',
            re.IGNORECASE
        )
    }
    
    @classmethod
    def parse(cls, command: str) -> Tuple[Optional[str], Optional[dict]]:
        """
        Parse a DSL command
        Returns: (command_type, parsed_data)
        """
        command = command.strip()
        
        for cmd_type, pattern in cls.PATTERNS.items():
            match = pattern.match(command)
            if match:
                return cmd_type, cls._extract_data(cmd_type, match)
        
        return None, None
    
    @classmethod
    def _extract_data(cls, cmd_type: str, match) -> dict:
        """Extract data from regex match based on command type"""
        data = {}
        
        if cmd_type == 'TRANSFER':
            groups = match.groups()
            data['amount'] = float(groups[0])
            data['from_account'] = groups[1].upper()
            data['to_account'] = groups[2].upper()
            if groups[3] is not None:
                data['condition_balance'] = float(groups[3])
        
        elif cmd_type == 'DEPOSIT':
            data['amount'] = float(match.group(1))
            data['to_account'] = match.group(2).upper()
        
        elif cmd_type == 'WITHDRAW':
            data['amount'] = float(match.group(1))
            data['from_account'] = match.group(2).upper()
        
        elif cmd_type == 'BALANCE':
            data['account'] = match.group(1).upper()
        
        elif cmd_type == 'CREATE':
            data['account'] = match.group(1).upper()
            if match.group(2):
                data['initial_balance'] = float(match.group(2))
            else:
                data['initial_balance'] = 0
        
        elif cmd_type == 'HISTORY':
            data['account'] = match.group(1).upper()
        
        return data

# ============================================
# DSL INTERPRETER
# ============================================

class BankingDSLInterpreter:
    """Executes parsed DSL commands"""
    
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.transaction_log = []
    
    def execute(self, command: str) -> Tuple[bool, str]:
        """
        Execute a DSL command
        Returns: (success, message)
        """
        # Parse the command
        cmd_type, data = BankingDSLParser.parse(command)
        
        if cmd_type is None:
            return False, f"Syntax Error: Invalid command format\n    Valid commands:\n    TRANSFER amount FROM A TO B [IF BALANCE > X]\n    DEPOSIT amount TO A\n    WITHDRAW amount FROM A\n    BALANCE A\n    CREATE ACCOUNT A [WITH amount]"
        
        # Execute based on command type
        if cmd_type == 'CREATE':
            return self._execute_create(data)
        elif cmd_type == 'DEPOSIT':
            return self._execute_deposit(data)
        elif cmd_type == 'WITHDRAW':
            return self._execute_withdraw(data)
        elif cmd_type == 'TRANSFER':
            return self._execute_transfer(data)
        elif cmd_type == 'BALANCE':
            return self._execute_balance(data)
        elif cmd_type == 'HISTORY':
            return self._execute_history(data)
        
        return False, "Unknown command type"
    
    def _execute_create(self, data: dict) -> Tuple[bool, str]:
        """CREATE ACCOUNT command"""
        account_id = data['account']
        
        if account_id in self.accounts:
            return False, f"Error: Account {account_id} already exists"
        
        initial_balance = data.get('initial_balance', 0)
        self.accounts[account_id] = Account(account_id, initial_balance)
        
        self._log_transaction('CREATE', f"Created account {account_id} with KES {initial_balance:,.2f}")
        
        return True, f"✅ Account {account_id} created with balance KES {initial_balance:,.2f}"
    
    def _execute_deposit(self, data: dict) -> Tuple[bool, str]:
        """DEPOSIT command"""
        account_id = data['to_account']
        amount = data['amount']
        
        if account_id not in self.accounts:
            return False, f"Error: Account {account_id} does not exist"
        
        if amount <= 0:
            return False, "Error: Amount must be positive"
        
        self.accounts[account_id].deposit(amount)
        self._log_transaction('DEPOSIT', f"Deposited KES {amount:,.2f} to {account_id}")
        
        return True, f"✅ Deposited KES {amount:,.2f} to {account_id}. New balance: KES {self.accounts[account_id].balance:,.2f}"
    
    def _execute_withdraw(self, data: dict) -> Tuple[bool, str]:
        """WITHDRAW command"""
        account_id = data['from_account']
        amount = data['amount']
        
        if account_id not in self.accounts:
            return False, f"Error: Account {account_id} does not exist"
        
        if amount <= 0:
            return False, "Error: Amount must be positive"
        
        if self.accounts[account_id].withdraw(amount):
            self._log_transaction('WITHDRAW', f"Withdrew KES {amount:,.2f} from {account_id}")
            return True, f"✅ Withdrew KES {amount:,.2f} from {account_id}. New balance: KES {self.accounts[account_id].balance:,.2f}"
        else:
            return False, f"❌ Insufficient funds in {account_id}. Balance: KES {self.accounts[account_id].balance:,.2f}"
    
    def _execute_transfer(self, data: dict) -> Tuple[bool, str]:
        """TRANSFER command with optional condition"""
        amount = data['amount']
        from_id = data['from_account']
        to_id = data['to_account']
        
        # Validate accounts exist
        if from_id not in self.accounts:
            return False, f"Error: Account {from_id} does not exist"
        if to_id not in self.accounts:
            return False, f"Error: Account {to_id} does not exist"
        
        if amount <= 0:
            return False, "Error: Amount must be positive"
        
        # Check condition if specified
        if 'condition_balance' in data:
            required_balance = data['condition_balance']
            if self.accounts[from_id].balance <= required_balance:
                return False, f"❌ Condition failed: Balance in {from_id} (KES {self.accounts[from_id].balance:,.2f}) must be > KES {required_balance:,.2f}"
        
        # Execute transfer
        if self.accounts[from_id].transfer(amount, self.accounts[to_id]):
            self._log_transaction('TRANSFER', f"Transferred KES {amount:,.2f} from {from_id} to {to_id}")
            return True, f"✅ Transferred KES {amount:,.2f} from {from_id} to {to_id}\n   {from_id} balance: KES {self.accounts[from_id].balance:,.2f}\n   {to_id} balance: KES {self.accounts[to_id].balance:,.2f}"
        else:
            return False, f"❌ Transfer failed: Insufficient funds in {from_id}. Balance: KES {self.accounts[from_id].balance:,.2f}"
    
    def _execute_balance(self, data: dict) -> Tuple[bool, str]:
        """BALANCE command"""
        account_id = data['account']
        
        if account_id not in self.accounts:
            return False, f"Error: Account {account_id} does not exist"
        
        balance = self.accounts[account_id].balance
        return True, f"💰 Account {account_id} balance: KES {balance:,.2f}"
    
    def _execute_history(self, data: dict) -> Tuple[bool, str]:
        """HISTORY command - show transaction history"""
        account_id = data['account']
        
        if account_id not in self.accounts:
            return False, f"Error: Account {account_id} does not exist"
        
        account = self.accounts[account_id]
        
        if not account.transaction_history:
            return True, f"📝 No transactions for account {account_id}"
        
        result = f"\n📝 TRANSACTION HISTORY for {account_id}\n"
        result += "=" * 50 + "\n"
        
        for i, tx in enumerate(account.transaction_history[-10:], 1):  # Show last 10
            timestamp = tx['timestamp'].strftime("%H:%M:%S")
            result += f"{i:2}. [{timestamp}] {tx['type']:12} KES {tx['amount']:>10,.2f} → Balance: KES {tx['balance']:>10,.2f}\n"
        
        result += "=" * 50
        return True, result
    
    def _log_transaction(self, cmd_type: str, details: str):
        """Log all transactions for audit"""
        self.transaction_log.append({
            'timestamp': datetime.now(),
            'type': cmd_type,
            'details': details
        })
    
    def display_all_accounts(self) -> str:
        """Display all accounts and balances"""
        if not self.accounts:
            return "No accounts created"
        
        result = "\n📊 ALL ACCOUNTS\n"
        result += "=" * 40 + "\n"
        for acc_id, account in self.accounts.items():
            result += f"  {acc_id}: KES {account.balance:>12,.2f}\n"
        result += "=" * 40
        return result

# ============================================
# INTERACTIVE SHELL
# ============================================

def interactive_shell():
    """Interactive DSL interpreter shell"""
    interpreter = BankingDSLInterpreter()
    
    print("=" * 60)
    print("   BANKING DSL INTERPRETER")
    print("=" * 60)
    print("\nCommands:")
    print("  CREATE ACCOUNT A [WITH amount]")
    print("  DEPOSIT amount TO A")
    print("  WITHDRAW amount FROM A")
    print("  TRANSFER amount FROM A TO B [IF BALANCE > X]")
    print("  BALANCE A")
    print("  HISTORY A")
    print("  LIST")
    print("  HELP")
    print("  EXIT")
    
    print("\nExamples:")
    print("  CREATE ACCOUNT SAVINGS WITH 5000")
    print("  CREATE ACCOUNT CHECKING")
    print("  DEPOSIT 1000 TO SAVINGS")
    print("  TRANSFER 500 FROM SAVINGS TO CHECKING IF BALANCE > 1000")
    print("  BALANCE SAVINGS")
    
    while True:
        try:
            command = input("\nDSL> ").strip()
            
            if not command:
                continue
            
            if command.upper() == 'EXIT':
                print("Goodbye!")
                break
            
            if command.upper() == 'HELP':
                print("\nAvailable Commands:")
                print("  CREATE ACCOUNT <id> [WITH <amount>] - Create new account")
                print("  DEPOSIT <amount> TO <id> - Deposit money")
                print("  WITHDRAW <amount> FROM <id> - Withdraw money")
                print("  TRANSFER <amount> FROM <id1> TO <id2> [IF BALANCE > X] - Transfer")
                print("  BALANCE <id> - Check balance")
                print("  HISTORY <id> - View transaction history")
                print("  LIST - Show all accounts")
                print("  HELP - Show this help")
                print("  EXIT - Exit interpreter")
                continue
            
            if command.upper() == 'LIST':
                print(interpreter.display_all_accounts())
                continue
            
            success, message = interpreter.execute(command)
            
            if success:
                print(f"\n{message}")
            else:
                print(f"\n{message}")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

def run_demo():
    """Run a demonstration of the DSL"""
    print("=" * 60)
    print("   BANKING DSL DEMONSTRATION")
    print("=" * 60)
    
    interpreter = BankingDSLInterpreter()
    
    # Demo commands
    demo_commands = [
        "CREATE ACCOUNT SAVINGS WITH 10000",
        "CREATE ACCOUNT CHECKING WITH 5000",
        "CREATE ACCOUNT INVESTMENT",
        "BALANCE SAVINGS",
        "DEPOSIT 2000 TO SAVINGS",
        "WITHDRAW 500 FROM CHECKING",
        "TRANSFER 3000 FROM SAVINGS TO INVESTMENT",
        "TRANSFER 2000 FROM SAVINGS TO CHECKING IF BALANCE > 5000",
        "BALANCE INVESTMENT",
        "HISTORY SAVINGS",
        "LIST"
    ]
    
    for cmd in demo_commands:
        print(f"\n{'='*60}")
        print(f">>> {cmd}")
        print('-' * 40)
        success, result = interpreter.execute(cmd)
        print(result)
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'demo':
        run_demo()
    else:
        interactive_shell()