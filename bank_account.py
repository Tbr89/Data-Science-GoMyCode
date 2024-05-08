{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ba82f63d-6340-4f07-bb67-57a0c3e7c318",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "500\n",
      "500\n",
      "600\n",
      "Sorry not enough balance in your account.\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "class Account :\n",
    "    def __init__(self,number,balance,holder):\n",
    "        self.number = number\n",
    "        self.balance= balance\n",
    "        self.holder= holder\n",
    "    def deposit(self,amount):\n",
    "        self.balance = self.balance + amount\n",
    "        return self.balance\n",
    "    def withdraw(self,amount):\n",
    "        if self.balance > amount :\n",
    "            self.balance = self.balance - amount\n",
    "            return self.balance\n",
    "        else :\n",
    "            print(\"Sorry not enough balance in your account.\")\n",
    "    def check_balance(self):\n",
    "        return self.balance\n",
    "    \n",
    "my_account = Account(1,1000,\"Tarek\")\n",
    "print (my_account.number)\n",
    "print(my_account.withdraw(500))\n",
    "print(my_account.check_balance())\n",
    "print (my_account.deposit(100))\n",
    "print(my_account.withdraw(1500))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6ae0294-489f-4fc7-9a7b-b212dc570181",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
