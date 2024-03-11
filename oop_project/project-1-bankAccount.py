'''
Project-1
We need to design an dimplement a class that will be used to represent bank accounts.

We want the following functionality and characteristics:
- accounts are uniquely identified by an **account number** (assume it will just be passed in the initializer)
- account holders have a **first** and **last** name
- accounts have an associated **preferred time zone offset** (e.g. -7 for MST)
- **balances** need to be zero or higher, and should not be directly settable.
- but, **deposits** and **withdrawals** can be made (given sufficient funds)
    - if a withdrawal is attempted that would result in nagative funds, the transaction should be declined.
- a **monthly interest rate** exists and is applicable to all accounts **uniformly**. There should be a method that can be called to calculate the interest on the current balance using the current interest rate, and **add it** to the balance.
- each deposit and withdrawal must generate a **confirmation number** composed of:
    - the transaction type: `D` for deposit, and `W` for withdrawal, `I` for interest deposit, and `X` for declined (in which case the balance remains unaffected)
    - the account number
    - the time the transaction was made, using UTC
    - an incrementing number (that increments across all accounts and transactions)
    - for (extreme!) simplicity assume that the transaction id starts at zero (or whatever number you choose) whenever the program starts
    - the confirmation number should be returned from any of the transaction methods (deposit, withdraw, etc)
- create a **method** that, given a confirmation number, returns:
    - the account number, transaction code (D, W, etc), datetime (UTC format), date time (in whatever timezone is specified in te argument, but more human readable), the transaction ID
    - make it so it is a nicely structured object (so can use dotted notation to access these three attributes)
    - I purposefully made it so the desired timezone is passed as an argument. Can you figure out why? (hint: does this method require any information from any instance?)


For example, we may have an account with:
- account number `140568` 
- preferred time zone offset of -7 (MST) 
- an existing balance of `100.00`

Suppose the last transaction ID in the system was `123`, and a deposit is made for `50.00` on `2019-03-15T14:59:00` (UTC) on that account (or `2019-03-15T07:59:00` in account's preferred time zone offset)

The new balance should reflect `150.00` and the confirmation number returned should look something like this:

```D-140568-20190315145900-124```

We also want a method that given the confirmation number returns an object with attributes:
- `result.account_number` --> `140568`
- `result.transaction_code` --> `D`
- `result.transaction_id` --> `124`
- `result.time` --> `2019-03-15 07:59:00 (MST)`
- `result.time_utc` --> `2019-03-15T14:59:00`

Furthermore, if current interest rate is `0.5%`, and the account's balance is `1000.00`, then the result of calling the `deposit_interest` (or whatever name you choose) method, should result in a new transaction and a new balance of `1050.00`. Calling this method should also return a confirmation number.

For simplicty, just use floats, but be aware that for these types of situations you'll probably want to use `Decimal` objects instead of floats.

There are going to be many ways to design something like this, especially since I have not nailed down all the specific requirements, so you'll have to fill the gaps yourself and decide what other things you may want to implement (like is the account number going to be a mutable property, or "read-only" and so on).

See how many different ideas you can use from what we covered in the last section. 

My approach will end up creating two classes: a `TimeZone` class used to store the time zone name and offset definition (in hours and minutes), and a main class called `Account` that will have the following "public" interface:
- initializer with account number, first name, last name, optional preferred time zone, starting balance (defaults to 0)
- a first name property (read/write)
- a last name property (read/write)
- a full name property (computed, read-only)
- a balance property (read-only)
- an interest rate property (class level property)
- deposit, withdraw, pay_interest methods
- parse confirmation code

Class will have additional state and methods, but those will be used for implementation.

You should also remember to test your code! In the solutions I will introduce you to Python's `unittest` package. Even if you skip this project, at least review that video and/or notebook if you are unfamiliar with `unittest`.
'''
import numbers
from datetime import timedelta


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')
            
        self._name = str(name).strip()
        
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')
        
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer.')
            
        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')
            
        # for time delta sign of minutes will be set to sign of hours
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')
            
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset
        
    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other):
        return (isinstance(other, TimeZone) and 
                self.name == other.name and 
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)
    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")

tz1 = TimeZone('ABC', -2, -15)
tz1.name
from datetime import datetime

dt = datetime.utcnow()
print(dt)
print(dt + tz1.offset)