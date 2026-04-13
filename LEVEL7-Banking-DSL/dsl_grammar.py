#!/usr/bin/env python3
"""
Banking DSL Grammar Specification
Defines the formal grammar for the Banking Domain Specific Language
APT1030-A Fundamentals of Programming Languages
"""

"""
================================================================================
BANKING DSL GRAMMAR (EBNF - Extended Backus-Naur Form)
================================================================================

COMMAND         ::= CREATE_CMD | DEPOSIT_CMD | WITHDRAW_CMD | TRANSFER_CMD | 
                     BALANCE_CMD | HISTORY_CMD | LIST_CMD

CREATE_CMD      ::= "CREATE" "ACCOUNT" ACCOUNT_ID ["WITH" AMOUNT]
DEPOSIT_CMD     ::= "DEPOSIT" AMOUNT "TO" ACCOUNT_ID
WITHDRAW_CMD    ::= "WITHDRAW" AMOUNT "FROM" ACCOUNT_ID
TRANSFER_CMD    ::= "TRANSFER" AMOUNT "FROM" ACCOUNT_ID "TO" ACCOUNT_ID [CONDITION]
BALANCE_CMD     ::= "BALANCE" ACCOUNT_ID
HISTORY_CMD     ::= "HISTORY" ACCOUNT_ID
LIST_CMD        ::= "LIST"

CONDITION       ::= "IF" "BALANCE" ">" AMOUNT

ACCOUNT_ID      ::= LETTER (LETTER | DIGIT | "_")*
AMOUNT          ::= DIGIT+ ["." DIGIT+]

LETTER          ::= "A" | "B" | ... | "Z" | "a" | "b" | ... | "z"
DIGIT           ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

================================================================================
TOKEN SPECIFICATION
================================================================================

Token          | Pattern                          | Example
---------------|----------------------------------|------------------
CREATE         | CREATE                           | CREATE
ACCOUNT        | ACCOUNT                          | ACCOUNT
DEPOSIT        | DEPOSIT                          | DEPOSIT
WITHDRAW       | WITHDRAW                         | WITHDRAW
TRANSFER       | TRANSFER                         | TRANSFER
FROM           | FROM                             | FROM
TO             | TO                               | TO
BALANCE        | BALANCE                          | BALANCE
IF             | IF                               | IF
WITH           | WITH                             | WITH
HISTORY        | HISTORY                          | HISTORY
LIST           | LIST                             | LIST
IDENTIFIER     | [A-Za-z][A-Za-z0-9_]*            | SAVINGS, CHECKING_001
NUMBER         | [0-9]+(\.[0-9]+)?                | 1000, 500.50
WHITESPACE     | [ \t\n\r]+                       | (ignored)

================================================================================
EXAMPLE COMMANDS WITH PARSE TREES
================================================================================

Example 1: CREATE ACCOUNT SAVINGS WITH 5000
--------------------------------------------------------------------------------
Parse Tree:
COMMAND
├── CREATE_CMD
    ├── "CREATE"
    ├── "ACCOUNT"
    ├── ACCOUNT_ID: "SAVINGS"
    ├── "WITH"
    └── AMOUNT: 5000

Example 2: TRANSFER 1000 FROM CHECKING TO SAVINGS IF BALANCE > 500
--------------------------------------------------------------------------------
Parse Tree:
COMMAND
└── TRANSFER_CMD
    ├── "TRANSFER"
    ├── AMOUNT: 1000
    ├── "FROM"
    ├── ACCOUNT_ID: "CHECKING"
    ├── "TO"
    ├── ACCOUNT_ID: "SAVINGS"
    └── CONDITION
        ├── "IF"
        ├── "BALANCE"
        ├── ">"
        └── AMOUNT: 500

Example 3: BALANCE SAVINGS
--------------------------------------------------------------------------------
Parse Tree:
COMMAND
└── BALANCE_CMD
    ├── "BALANCE"
    └── ACCOUNT_ID: "SAVINGS"

================================================================================
LEXICAL SPECIFICATION (Regex Patterns)
================================================================================
"""

import re
from enum import Enum
from typing import List, Tuple, Optional

class TokenType(Enum):
    """Token types for the DSL lexer"""
    # Keywords
    CREATE = r'CREATE'
    ACCOUNT = r'ACCOUNT'
    DEPOSIT = r'DEPOSIT'
    WITHDRAW = r'WITHDRAW'
    TRANSFER = r'TRANSFER'
    FROM = r'FROM'
    TO = r'TO'
    BALANCE = r'BALANCE'
    IF = r'IF'
    WITH = r'WITH'
    HISTORY = r'HISTORY'
    LIST = r'LIST'
    
    # Operators
    GT = r'>'
    
    # Literals
    IDENTIFIER = r'[A-Za-z][A-Za-z0-9_]*'
    NUMBER = r'\d+(?:\.\d+)?'
    
    # Other
    WHITESPACE = r'[ \t\n\r]+'
    UNKNOWN = r'.'

class Token:
    """Represents a token from the lexer"""
    def __init__(self, type: TokenType, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}', {self.line}:{self.column})"

class Lexer:
    """Lexical analyzer for Banking DSL"""
    
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.position = 0
        self.line = 1
        self.column = 1
    
    def tokenize(self) -> List[Token]:
        """Convert source string to list of tokens"""
        self.tokens = []
        self.position = 0
        self.line = 1
        self.column = 1
        
        while self.position < len(self.source):
            token = self._next_token()
            if token.type != TokenType.WHITESPACE:
                self.tokens.append(token)
        
        return self.tokens
    
    def _next_token(self) -> Token:
        """Get the next token from the source"""
        if self.position >= len(self.source):
            return Token(TokenType.UNKNOWN, '', self.line, self.column)
        
        # Try to match each token type
        for token_type in TokenType:
            pattern = token_type.value
            regex = re.compile(pattern)
            match = regex.match(self.source, self.position)
            
            if match:
                value = match.group(0)
                token = Token(token_type, value, self.line, self.column)
                
                # Update position
                self.position += len(value)
                
                # Update line/column for newlines
                if '\n' in value:
                    self.line += value.count('\n')
                    last_newline = value.rfind('\n')
                    self.column = len(value) - last_newline
                else:
                    self.column += len(value)
                
                return token
        
        # Unknown token
        return Token(TokenType.UNKNOWN, self.source[self.position], self.line, self.column)

class ASTNode:
    """Abstract Syntax Tree Node"""
    def __init__(self, type: str, value=None):
        self.type = type
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def __repr__(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.type}"
        if self.value:
            result += f": {self.value}"
        result += "\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result

class Parser:
    """Parser for Banking DSL - converts tokens to AST"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
    
    def parse(self) -> ASTNode:
        """Parse tokens into AST"""
        if not self.tokens:
            raise SyntaxError("Empty command")
        
        return self._parse_command()
    
    def _current_token(self) -> Token:
        """Get current token"""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None
    
    def _advance(self):
        """Move to next token"""
        self.position += 1
    
    def _match(self, expected_type: TokenType) -> bool:
        """Check if current token matches expected type"""
        token = self._current_token()
        return token and token.type == expected_type
    
    def _expect(self, expected_type: TokenType) -> Token:
        """Expect a specific token type, raise error if not found"""
        token = self._current_token()
        if not token or token.type != expected_type:
            raise SyntaxError(f"Expected {expected_type.name}, got {token.type.name if token else 'EOF'}")
        self._advance()
        return token
    
    def _parse_command(self) -> ASTNode:
        """Parse a command"""
        token = self._current_token()
        
        if token.type == TokenType.CREATE:
            return self._parse_create()
        elif token.type == TokenType.DEPOSIT:
            return self._parse_deposit()
        elif token.type == TokenType.WITHDRAW:
            return self._parse_withdraw()
        elif token.type == TokenType.TRANSFER:
            return self._parse_transfer()
        elif token.type == TokenType.BALANCE:
            return self._parse_balance()
        elif token.type == TokenType.HISTORY:
            return self._parse_history()
        elif token.type == TokenType.LIST:
            return self._parse_list()
        else:
            raise SyntaxError(f"Unknown command: {token.value}")
    
    def _parse_create(self) -> ASTNode:
        """Parse CREATE ACCOUNT <id> [WITH <amount>]"""
        node = ASTNode("CREATE")
        
        self._expect(TokenType.CREATE)
        self._expect(TokenType.ACCOUNT)
        
        id_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("ACCOUNT_ID", id_token.value))
        
        if self._match(TokenType.WITH):
            self._advance()
            amount_token = self._expect(TokenType.NUMBER)
            node.add_child(ASTNode("AMOUNT", float(amount_token.value)))
        
        return node
    
    def _parse_deposit(self) -> ASTNode:
        """Parse DEPOSIT <amount> TO <id>"""
        node = ASTNode("DEPOSIT")
        
        self._expect(TokenType.DEPOSIT)
        
        amount_token = self._expect(TokenType.NUMBER)
        node.add_child(ASTNode("AMOUNT", float(amount_token.value)))
        
        self._expect(TokenType.TO)
        
        id_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("ACCOUNT_ID", id_token.value))
        
        return node
    
    def _parse_withdraw(self) -> ASTNode:
        """Parse WITHDRAW <amount> FROM <id>"""
        node = ASTNode("WITHDRAW")
        
        self._expect(TokenType.WITHDRAW)
        
        amount_token = self._expect(TokenType.NUMBER)
        node.add_child(ASTNode("AMOUNT", float(amount_token.value)))
        
        self._expect(TokenType.FROM)
        
        id_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("ACCOUNT_ID", id_token.value))
        
        return node
    
    def _parse_transfer(self) -> ASTNode:
        """Parse TRANSFER <amount> FROM <id> TO <id> [IF BALANCE > <amount>]"""
        node = ASTNode("TRANSFER")
        
        self._expect(TokenType.TRANSFER)
        
        amount_token = self._expect(TokenType.NUMBER)
        node.add_child(ASTNode("AMOUNT", float(amount_token.value)))
        
        self._expect(TokenType.FROM)
        
        from_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("FROM_ACCOUNT", from_token.value))
        
        self._expect(TokenType.TO)
        
        to_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("TO_ACCOUNT", to_token.value))
        
        # Check for condition
        if self._match(TokenType.IF):
            node.add_child(self._parse_condition())
        
        return node
    
    def _parse_condition(self) -> ASTNode:
        """Parse IF BALANCE > <amount>"""
        node = ASTNode("CONDITION")
        
        self._expect(TokenType.IF)
        self._expect(TokenType.BALANCE)
        self._expect(TokenType.GT)
        
        amount_token = self._expect(TokenType.NUMBER)
        node.add_child(ASTNode("MIN_BALANCE", float(amount_token.value)))
        
        return node
    
    def _parse_balance(self) -> ASTNode:
        """Parse BALANCE <id>"""
        node = ASTNode("BALANCE")
        
        self._expect(TokenType.BALANCE)
        
        id_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("ACCOUNT_ID", id_token.value))
        
        return node
    
    def _parse_history(self) -> ASTNode:
        """Parse HISTORY <id>"""
        node = ASTNode("HISTORY")
        
        self._expect(TokenType.HISTORY)
        
        id_token = self._expect(TokenType.IDENTIFIER)
        node.add_child(ASTNode("ACCOUNT_ID", id_token.value))
        
        return node
    
    def _parse_list(self) -> ASTNode:
        """Parse LIST"""
        node = ASTNode("LIST")
        self._expect(TokenType.LIST)
        return node

# ============================================================================
# GRAMMAR VALIDATION AND TESTING
# ============================================================================

def validate_command(command: str) -> Tuple[bool, Optional[str], Optional[ASTNode]]:
    """
    Validate a command against the grammar
    Returns: (is_valid, error_message, ast)
    """
    try:
        lexer = Lexer(command)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        return True, None, ast
    except SyntaxError as e:
        return False, str(e), None
    except Exception as e:
        return False, f"Unexpected error: {e}", None

def demo_grammar():
    """Demonstrate the grammar with examples"""
    print("=" * 60)
    print("   BANKING DSL GRAMMAR DEMONSTRATION")
    print("=" * 60)
    
    test_commands = [
        "CREATE ACCOUNT SAVINGS WITH 5000",
        "CREATE ACCOUNT CHECKING",
        "DEPOSIT 1000 TO SAVINGS",
        "WITHDRAW 500 FROM CHECKING",
        "TRANSFER 2000 FROM SAVINGS TO CHECKING",
        "TRANSFER 500 FROM SAVINGS TO CHECKING IF BALANCE > 1000",
        "BALANCE SAVINGS",
        "HISTORY CHECKING",
        "LIST",
        "INVALID COMMAND"  # This should fail
    ]
    
    for command in test_commands:
        print(f"\n{'='*60}")
        print(f"Input: {command}")
        print("-" * 40)
        
        is_valid, error, ast = validate_command(command)
        
        if is_valid:
            print("✅ Valid command")
            print("\nAST:")
            print(ast)
        else:
            print(f"❌ Invalid: {error}")

if __name__ == "__main__":
    demo_grammar()