#!/usr/bin/env python3
"""
Unit Tests for Banking DSL
Tests parser, interpreter, and edge cases
"""

import unittest
from banking_dsl import BankingDSLParser, BankingDSLInterpreter, Account

class TestDSLParser(unittest.TestCase):
    """Test the DSL parser"""
    
    def test_parse_create_account(self):
        cmd_type, data = BankingDSLParser.parse("CREATE ACCOUNT A WITH 1000")
        self.assertEqual(cmd_type, 'CREATE')
        self.assertEqual(data['account'], 'A')
        self.assertEqual(data['initial_balance'], 1000)
    
    def test_parse_create_account_no_balance(self):
        cmd_type, data = BankingDSLParser.parse("CREATE ACCOUNT B")
        self.assertEqual(cmd_type, 'CREATE')
        self.assertEqual(data['account'], 'B')
        self.assertEqual(data['initial_balance'], 0)
    
    def test_parse_deposit(self):
        cmd_type, data = BankingDSLParser.parse("DEPOSIT 500 TO A")
        self.assertEqual(cmd_type, 'DEPOSIT')
        self.assertEqual(data['amount'], 500)
        self.assertEqual(data['to_account'], 'A')
    
    def test_parse_withdraw(self):
        cmd_type, data = BankingDSLParser.parse("WITHDRAW 300 FROM B")
        self.assertEqual(cmd_type, 'WITHDRAW')
        self.assertEqual(data['amount'], 300)
        self.assertEqual(data['from_account'], 'B')
    
    def test_parse_transfer(self):
        cmd_type, data = BankingDSLParser.parse("TRANSFER 1000 FROM A TO B")
        self.assertEqual(cmd_type, 'TRANSFER')
        self.assertEqual(data['amount'], 1000)
        self.assertEqual(data['from_account'], 'A')
        self.assertEqual(data['to_account'], 'B')
    
    def test_parse_transfer_with_condition(self):
        cmd_type, data = BankingDSLParser.parse("TRANSFER 500 FROM A TO B IF BALANCE > 1000")
        self.assertEqual(cmd_type, 'TRANSFER')
        self.assertEqual(data['amount'], 500)
        self.assertEqual(data['condition_balance'], 1000)
    
    def test_parse_balance(self):
        cmd_type, data = BankingDSLParser.parse("BALANCE A")
        self.assertEqual(cmd_type, 'BALANCE')
        self.assertEqual(data['account'], 'A')
    
    def test_parse_invalid_command(self):
        cmd_type, data = BankingDSLParser.parse("INVALID COMMAND")
        self.assertIsNone(cmd_type)
    
    def test_case_insensitive(self):
        cmd_type, data = BankingDSLParser.parse("create account test with 100")
        self.assertEqual(cmd_type, 'CREATE')
        self.assertEqual(data['account'], 'TEST')

class TestDSLInterpreter(unittest.TestCase):
    """Test the DSL interpreter"""
    
    def setUp(self):
        """Set up test environment"""
        self.interpreter = BankingDSLInterpreter()
    
    def test_create_account(self):
        success, msg = self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        self.assertTrue(success)
        self.assertIn("Account A created", msg)
        self.assertIn("A", self.interpreter.accounts)
        self.assertEqual(self.interpreter.accounts['A'].balance, 1000)
    
    def test_create_duplicate_account(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        success, msg = self.interpreter.execute("CREATE ACCOUNT A WITH 2000")
        self.assertFalse(success)
        self.assertIn("already exists", msg)
    
    def test_deposit(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        success, msg = self.interpreter.execute("DEPOSIT 500 TO A")
        self.assertTrue(success)
        self.assertEqual(self.interpreter.accounts['A'].balance, 1500)
    
    def test_deposit_nonexistent_account(self):
        success, msg = self.interpreter.execute("DEPOSIT 500 TO X")
        self.assertFalse(success)
        self.assertIn("does not exist", msg)
    
    def test_withdraw(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        success, msg = self.interpreter.execute("WITHDRAW 300 FROM A")
        self.assertTrue(success)
        self.assertEqual(self.interpreter.accounts['A'].balance, 700)
    
    def test_withdraw_insufficient_funds(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 100")
        success, msg = self.interpreter.execute("WITHDRAW 500 FROM A")
        self.assertFalse(success)
        self.assertIn("Insufficient funds", msg)
    
    def test_transfer(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        self.interpreter.execute("CREATE ACCOUNT B WITH 500")
        success, msg = self.interpreter.execute("TRANSFER 300 FROM A TO B")
        self.assertTrue(success)
        self.assertEqual(self.interpreter.accounts['A'].balance, 700)
        self.assertEqual(self.interpreter.accounts['B'].balance, 800)
    
    def test_transfer_with_condition_success(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 2000")
        self.interpreter.execute("CREATE ACCOUNT B WITH 100")
        success, msg = self.interpreter.execute("TRANSFER 500 FROM A TO B IF BALANCE > 1000")
        self.assertTrue(success)
    
    def test_transfer_with_condition_fail(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 800")
        self.interpreter.execute("CREATE ACCOUNT B WITH 100")
        success, msg = self.interpreter.execute("TRANSFER 500 FROM A TO B IF BALANCE > 1000")
        self.assertFalse(success)
        self.assertIn("Condition failed", msg)
    
    def test_balance(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        success, msg = self.interpreter.execute("BALANCE A")
        self.assertTrue(success)
        self.assertIn("KES 1,000", msg)
    
    def test_list_accounts(self):
        self.interpreter.execute("CREATE ACCOUNT A WITH 1000")
        self.interpreter.execute("CREATE ACCOUNT B WITH 2000")
        result = self.interpreter.display_all_accounts()
        self.assertIn("A", result)
        self.assertIn("B", result)
        self.assertIn("1,000", result)
        self.assertIn("2,000", result)

class TestAccount(unittest.TestCase):
    """Test Account class"""
    
    def test_deposit(self):
        acc = Account("TEST", 1000)
        acc.deposit(500)
        self.assertEqual(acc.balance, 1500)
    
    def test_withdraw_success(self):
        acc = Account("TEST", 1000)
        result = acc.withdraw(300)
        self.assertTrue(result)
        self.assertEqual(acc.balance, 700)
    
    def test_withdraw_fail(self):
        acc = Account("TEST", 100)
        result = acc.withdraw(500)
        self.assertFalse(result)
        self.assertEqual(acc.balance, 100)
    
    def test_transfer(self):
        from_acc = Account("A", 1000)
        to_acc = Account("B", 500)
        result = from_acc.transfer(300, to_acc)
        self.assertTrue(result)
        self.assertEqual(from_acc.balance, 700)
        self.assertEqual(to_acc.balance, 800)
    
    def test_transaction_history(self):
        acc = Account("TEST", 1000)
        acc.deposit(500)
        acc.withdraw(200)
        self.assertEqual(len(acc.transaction_history), 2)
        self.assertEqual(acc.transaction_history[0]['type'], 'DEPOSIT')
        self.assertEqual(acc.transaction_history[1]['type'], 'WITHDRAW')

if __name__ == '__main__':
    print("=" * 60)
    print("   RUNNING DSL UNIT TESTS")
    print("=" * 60)
    unittest.main()