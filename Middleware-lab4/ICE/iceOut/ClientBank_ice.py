# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.2
#
# <auto-generated>
#
# Generated from file `ClientBank.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module ClientBank
_M_ClientBank = Ice.openModule('ClientBank')
__name__ = 'ClientBank'

if 'UnauthorizedErr' not in _M_ClientBank.__dict__:
    _M_ClientBank.UnauthorizedErr = Ice.createTempClass()
    class UnauthorizedErr(Ice.UserException):
        def __init__(self, msg=''):
            self.msg = msg

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::ClientBank::UnauthorizedErr'

    _M_ClientBank._t_UnauthorizedErr = IcePy.defineException('::ClientBank::UnauthorizedErr', UnauthorizedErr, (), False, None, (('msg', (), IcePy._t_string, False, 0),))
    UnauthorizedErr._ice_type = _M_ClientBank._t_UnauthorizedErr

    _M_ClientBank.UnauthorizedErr = UnauthorizedErr
    del UnauthorizedErr

if 'RegistrationErr' not in _M_ClientBank.__dict__:
    _M_ClientBank.RegistrationErr = Ice.createTempClass()
    class RegistrationErr(Ice.UserException):
        def __init__(self, msg=''):
            self.msg = msg

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::ClientBank::RegistrationErr'

    _M_ClientBank._t_RegistrationErr = IcePy.defineException('::ClientBank::RegistrationErr', RegistrationErr, (), False, None, (('msg', (), IcePy._t_string, False, 0),))
    RegistrationErr._ice_type = _M_ClientBank._t_RegistrationErr

    _M_ClientBank.RegistrationErr = RegistrationErr
    del RegistrationErr

if 'LoanRefusalErr' not in _M_ClientBank.__dict__:
    _M_ClientBank.LoanRefusalErr = Ice.createTempClass()
    class LoanRefusalErr(Ice.UserException):
        def __init__(self, msg=''):
            self.msg = msg

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::ClientBank::LoanRefusalErr'

    _M_ClientBank._t_LoanRefusalErr = IcePy.defineException('::ClientBank::LoanRefusalErr', LoanRefusalErr, (), False, None, (('msg', (), IcePy._t_string, False, 0),))
    LoanRefusalErr._ice_type = _M_ClientBank._t_LoanRefusalErr

    _M_ClientBank.LoanRefusalErr = LoanRefusalErr
    del LoanRefusalErr

if 'Type' not in _M_ClientBank.__dict__:
    _M_ClientBank.Type = Ice.createTempClass()
    class Type(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Type.STANDARD = Type("STANDARD", 1)
    Type.PREMIUM = Type("PREMIUM", 2)
    Type._enumerators = { 1:Type.STANDARD, 2:Type.PREMIUM }

    _M_ClientBank._t_Type = IcePy.defineEnum('::ClientBank::Type', Type, (), Type._enumerators)

    _M_ClientBank.Type = Type
    del Type

if 'Currency' not in _M_ClientBank.__dict__:
    _M_ClientBank.Currency = Ice.createTempClass()
    class Currency(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Currency.EUR = Currency("EUR", 1)
    Currency.USD = Currency("USD", 2)
    Currency.CHF = Currency("CHF", 3)
    Currency.GBP = Currency("GBP", 4)
    Currency.PLN = Currency("PLN", 5)
    Currency._enumerators = { 1:Currency.EUR, 2:Currency.USD, 3:Currency.CHF, 4:Currency.GBP, 5:Currency.PLN }

    _M_ClientBank._t_Currency = IcePy.defineEnum('::ClientBank::Currency', Currency, (), Currency._enumerators)

    _M_ClientBank.Currency = Currency
    del Currency

if 'LoanResponse' not in _M_ClientBank.__dict__:
    _M_ClientBank.LoanResponse = Ice.createTempClass()
    class LoanResponse(object):
        def __init__(self, valuePLN=0.0, currencyValue=0.0, currency=_M_ClientBank.Currency.EUR, exchange=0.0):
            self.valuePLN = valuePLN
            self.currencyValue = currencyValue
            self.currency = currency
            self.exchange = exchange

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_ClientBank.LoanResponse):
                return NotImplemented
            else:
                if self.valuePLN != other.valuePLN:
                    return False
                if self.currencyValue != other.currencyValue:
                    return False
                if self.currency != other.currency:
                    return False
                if self.exchange != other.exchange:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_LoanResponse)

        __repr__ = __str__

    _M_ClientBank._t_LoanResponse = IcePy.defineStruct('::ClientBank::LoanResponse', LoanResponse, (), (
        ('valuePLN', (), IcePy._t_float),
        ('currencyValue', (), IcePy._t_float),
        ('currency', (), _M_ClientBank._t_Currency),
        ('exchange', (), IcePy._t_float)
    ))

    _M_ClientBank.LoanResponse = LoanResponse
    del LoanResponse

if 'AccountKey' not in _M_ClientBank.__dict__:
    _M_ClientBank.AccountKey = Ice.createTempClass()
    class AccountKey(object):
        def __init__(self, pesel='', type=_M_ClientBank.Type.STANDARD):
            self.pesel = pesel
            self.type = type

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.pesel)
            _h = 5 * _h + Ice.getHash(self.type)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_ClientBank.AccountKey):
                return NotImplemented
            else:
                if self.pesel is None or other.pesel is None:
                    if self.pesel != other.pesel:
                        return (-1 if self.pesel is None else 1)
                else:
                    if self.pesel < other.pesel:
                        return -1
                    elif self.pesel > other.pesel:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_AccountKey)

        __repr__ = __str__

    _M_ClientBank._t_AccountKey = IcePy.defineStruct('::ClientBank::AccountKey', AccountKey, (), (
        ('pesel', (), IcePy._t_string),
        ('type', (), _M_ClientBank._t_Type)
    ))

    _M_ClientBank.AccountKey = AccountKey
    del AccountKey

if 'AccountUser' not in _M_ClientBank.__dict__:
    _M_ClientBank.AccountUser = Ice.createTempClass()
    class AccountUser(object):
        def __init__(self, name='', surname='', pesel='', type=_M_ClientBank.Type.STANDARD, password=''):
            self.name = name
            self.surname = surname
            self.pesel = pesel
            self.type = type
            self.password = password

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.surname)
            _h = 5 * _h + Ice.getHash(self.pesel)
            _h = 5 * _h + Ice.getHash(self.type)
            _h = 5 * _h + Ice.getHash(self.password)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_ClientBank.AccountUser):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.surname is None or other.surname is None:
                    if self.surname != other.surname:
                        return (-1 if self.surname is None else 1)
                else:
                    if self.surname < other.surname:
                        return -1
                    elif self.surname > other.surname:
                        return 1
                if self.pesel is None or other.pesel is None:
                    if self.pesel != other.pesel:
                        return (-1 if self.pesel is None else 1)
                else:
                    if self.pesel < other.pesel:
                        return -1
                    elif self.pesel > other.pesel:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                if self.password is None or other.password is None:
                    if self.password != other.password:
                        return (-1 if self.password is None else 1)
                else:
                    if self.password < other.password:
                        return -1
                    elif self.password > other.password:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_AccountUser)

        __repr__ = __str__

    _M_ClientBank._t_AccountUser = IcePy.defineStruct('::ClientBank::AccountUser', AccountUser, (), (
        ('name', (), IcePy._t_string),
        ('surname', (), IcePy._t_string),
        ('pesel', (), IcePy._t_string),
        ('type', (), _M_ClientBank._t_Type),
        ('password', (), IcePy._t_string)
    ))

    _M_ClientBank.AccountUser = AccountUser
    del AccountUser

if 'AccountBank' not in _M_ClientBank.__dict__:
    _M_ClientBank.AccountBank = Ice.createTempClass()
    class AccountBank(object):
        def __init__(self, accountUser=Ice._struct_marker, value=0.0):
            if accountUser is Ice._struct_marker:
                self.accountUser = _M_ClientBank.AccountUser()
            else:
                self.accountUser = accountUser
            self.value = value

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_ClientBank.AccountBank):
                return NotImplemented
            else:
                if self.accountUser != other.accountUser:
                    return False
                if self.value != other.value:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_AccountBank)

        __repr__ = __str__

    _M_ClientBank._t_AccountBank = IcePy.defineStruct('::ClientBank::AccountBank', AccountBank, (), (
        ('accountUser', (), _M_ClientBank._t_AccountUser),
        ('value', (), IcePy._t_float)
    ))

    _M_ClientBank.AccountBank = AccountBank
    del AccountBank

if 'Date' not in _M_ClientBank.__dict__:
    _M_ClientBank.Date = Ice.createTempClass()
    class Date(object):
        def __init__(self, year=0, month=0, day=0):
            self.year = year
            self.month = month
            self.day = day

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.year)
            _h = 5 * _h + Ice.getHash(self.month)
            _h = 5 * _h + Ice.getHash(self.day)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_ClientBank.Date):
                return NotImplemented
            else:
                if self.year is None or other.year is None:
                    if self.year != other.year:
                        return (-1 if self.year is None else 1)
                else:
                    if self.year < other.year:
                        return -1
                    elif self.year > other.year:
                        return 1
                if self.month is None or other.month is None:
                    if self.month != other.month:
                        return (-1 if self.month is None else 1)
                else:
                    if self.month < other.month:
                        return -1
                    elif self.month > other.month:
                        return 1
                if self.day is None or other.day is None:
                    if self.day != other.day:
                        return (-1 if self.day is None else 1)
                else:
                    if self.day < other.day:
                        return -1
                    elif self.day > other.day:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_Date)

        __repr__ = __str__

    _M_ClientBank._t_Date = IcePy.defineStruct('::ClientBank::Date', Date, (), (
        ('year', (), IcePy._t_int),
        ('month', (), IcePy._t_int),
        ('day', (), IcePy._t_int)
    ))

    _M_ClientBank.Date = Date
    del Date

if 'RegistrationResponse' not in _M_ClientBank.__dict__:
    _M_ClientBank.RegistrationResponse = Ice.createTempClass()
    class RegistrationResponse(object):
        def __init__(self, password='', type=_M_ClientBank.Type.STANDARD):
            self.password = password
            self.type = type

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.password)
            _h = 5 * _h + Ice.getHash(self.type)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_ClientBank.RegistrationResponse):
                return NotImplemented
            else:
                if self.password is None or other.password is None:
                    if self.password != other.password:
                        return (-1 if self.password is None else 1)
                else:
                    if self.password < other.password:
                        return -1
                    elif self.password > other.password:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_RegistrationResponse)

        __repr__ = __str__

    _M_ClientBank._t_RegistrationResponse = IcePy.defineStruct('::ClientBank::RegistrationResponse', RegistrationResponse, (), (
        ('password', (), IcePy._t_string),
        ('type', (), _M_ClientBank._t_Type)
    ))

    _M_ClientBank.RegistrationResponse = RegistrationResponse
    del RegistrationResponse

_M_ClientBank._t_StandardAccount = IcePy.defineValue('::ClientBank::StandardAccount', Ice.Value, -1, (), False, True, None, ())

if 'StandardAccountPrx' not in _M_ClientBank.__dict__:
    _M_ClientBank.StandardAccountPrx = Ice.createTempClass()
    class StandardAccountPrx(Ice.ObjectPrx):

        def getAccountBalance(self, context=None):
            return _M_ClientBank.StandardAccount._op_getAccountBalance.invoke(self, ((), context))

        def getAccountBalanceAsync(self, context=None):
            return _M_ClientBank.StandardAccount._op_getAccountBalance.invokeAsync(self, ((), context))

        def begin_getAccountBalance(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_ClientBank.StandardAccount._op_getAccountBalance.begin(self, ((), _response, _ex, _sent, context))

        def end_getAccountBalance(self, _r):
            return _M_ClientBank.StandardAccount._op_getAccountBalance.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ClientBank.StandardAccountPrx.ice_checkedCast(proxy, '::ClientBank::StandardAccount', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ClientBank.StandardAccountPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ClientBank::StandardAccount'
    _M_ClientBank._t_StandardAccountPrx = IcePy.defineProxy('::ClientBank::StandardAccount', StandardAccountPrx)

    _M_ClientBank.StandardAccountPrx = StandardAccountPrx
    del StandardAccountPrx

    _M_ClientBank.StandardAccount = Ice.createTempClass()
    class StandardAccount(Ice.Object):

        def ice_ids(self, current=None):
            return ('::ClientBank::StandardAccount', '::Ice::Object')

        def ice_id(self, current=None):
            return '::ClientBank::StandardAccount'

        @staticmethod
        def ice_staticId():
            return '::ClientBank::StandardAccount'

        def getAccountBalance(self, current=None):
            raise NotImplementedError("servant method 'getAccountBalance' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_StandardAccountDisp)

        __repr__ = __str__

    _M_ClientBank._t_StandardAccountDisp = IcePy.defineClass('::ClientBank::StandardAccount', StandardAccount, (), None, ())
    StandardAccount._ice_type = _M_ClientBank._t_StandardAccountDisp

    StandardAccount._op_getAccountBalance = IcePy.Operation('getAccountBalance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_float, False, 0), ())

    _M_ClientBank.StandardAccount = StandardAccount
    del StandardAccount

_M_ClientBank._t_PremiumAccount = IcePy.defineValue('::ClientBank::PremiumAccount', Ice.Value, -1, (), False, True, None, ())

if 'PremiumAccountPrx' not in _M_ClientBank.__dict__:
    _M_ClientBank.PremiumAccountPrx = Ice.createTempClass()
    class PremiumAccountPrx(_M_ClientBank.StandardAccountPrx):

        def getLoan(self, value, currency, date, context=None):
            return _M_ClientBank.PremiumAccount._op_getLoan.invoke(self, ((value, currency, date), context))

        def getLoanAsync(self, value, currency, date, context=None):
            return _M_ClientBank.PremiumAccount._op_getLoan.invokeAsync(self, ((value, currency, date), context))

        def begin_getLoan(self, value, currency, date, _response=None, _ex=None, _sent=None, context=None):
            return _M_ClientBank.PremiumAccount._op_getLoan.begin(self, ((value, currency, date), _response, _ex, _sent, context))

        def end_getLoan(self, _r):
            return _M_ClientBank.PremiumAccount._op_getLoan.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ClientBank.PremiumAccountPrx.ice_checkedCast(proxy, '::ClientBank::PremiumAccount', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ClientBank.PremiumAccountPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ClientBank::PremiumAccount'
    _M_ClientBank._t_PremiumAccountPrx = IcePy.defineProxy('::ClientBank::PremiumAccount', PremiumAccountPrx)

    _M_ClientBank.PremiumAccountPrx = PremiumAccountPrx
    del PremiumAccountPrx

    _M_ClientBank.PremiumAccount = Ice.createTempClass()
    class PremiumAccount(_M_ClientBank.StandardAccount):

        def ice_ids(self, current=None):
            return ('::ClientBank::PremiumAccount', '::ClientBank::StandardAccount', '::Ice::Object')

        def ice_id(self, current=None):
            return '::ClientBank::PremiumAccount'

        @staticmethod
        def ice_staticId():
            return '::ClientBank::PremiumAccount'

        def getLoan(self, value, currency, date, current=None):
            raise NotImplementedError("servant method 'getLoan' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_PremiumAccountDisp)

        __repr__ = __str__

    _M_ClientBank._t_PremiumAccountDisp = IcePy.defineClass('::ClientBank::PremiumAccount', PremiumAccount, (), None, (_M_ClientBank._t_StandardAccountDisp,))
    PremiumAccount._ice_type = _M_ClientBank._t_PremiumAccountDisp

    PremiumAccount._op_getLoan = IcePy.Operation('getLoan', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_float, False, 0), ((), _M_ClientBank._t_Currency, False, 0), ((), _M_ClientBank._t_Date, False, 0)), (), ((), _M_ClientBank._t_LoanResponse, False, 0), (_M_ClientBank._t_LoanRefusalErr,))

    _M_ClientBank.PremiumAccount = PremiumAccount
    del PremiumAccount

if 'LoginResponse' not in _M_ClientBank.__dict__:
    _M_ClientBank.LoginResponse = Ice.createTempClass()
    class LoginResponse(object):
        def __init__(self, type=_M_ClientBank.Type.STANDARD, accountAdministrator=None):
            self.type = type
            self.accountAdministrator = accountAdministrator

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_ClientBank.LoginResponse):
                return NotImplemented
            else:
                if self.type != other.type:
                    return False
                if self.accountAdministrator != other.accountAdministrator:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_LoginResponse)

        __repr__ = __str__

    _M_ClientBank._t_LoginResponse = IcePy.defineStruct('::ClientBank::LoginResponse', LoginResponse, (), (
        ('type', (), _M_ClientBank._t_Type),
        ('accountAdministrator', (), _M_ClientBank._t_StandardAccountPrx)
    ))

    _M_ClientBank.LoginResponse = LoginResponse
    del LoginResponse

_M_ClientBank._t_UsersRegistration = IcePy.defineValue('::ClientBank::UsersRegistration', Ice.Value, -1, (), False, True, None, ())

if 'UsersRegistrationPrx' not in _M_ClientBank.__dict__:
    _M_ClientBank.UsersRegistrationPrx = Ice.createTempClass()
    class UsersRegistrationPrx(Ice.ObjectPrx):

        def register(self, name, surname, pesel, income, context=None):
            return _M_ClientBank.UsersRegistration._op_register.invoke(self, ((name, surname, pesel, income), context))

        def registerAsync(self, name, surname, pesel, income, context=None):
            return _M_ClientBank.UsersRegistration._op_register.invokeAsync(self, ((name, surname, pesel, income), context))

        def begin_register(self, name, surname, pesel, income, _response=None, _ex=None, _sent=None, context=None):
            return _M_ClientBank.UsersRegistration._op_register.begin(self, ((name, surname, pesel, income), _response, _ex, _sent, context))

        def end_register(self, _r):
            return _M_ClientBank.UsersRegistration._op_register.end(self, _r)

        def login(self, pesel, password, context=None):
            return _M_ClientBank.UsersRegistration._op_login.invoke(self, ((pesel, password), context))

        def loginAsync(self, pesel, password, context=None):
            return _M_ClientBank.UsersRegistration._op_login.invokeAsync(self, ((pesel, password), context))

        def begin_login(self, pesel, password, _response=None, _ex=None, _sent=None, context=None):
            return _M_ClientBank.UsersRegistration._op_login.begin(self, ((pesel, password), _response, _ex, _sent, context))

        def end_login(self, _r):
            return _M_ClientBank.UsersRegistration._op_login.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ClientBank.UsersRegistrationPrx.ice_checkedCast(proxy, '::ClientBank::UsersRegistration', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ClientBank.UsersRegistrationPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ClientBank::UsersRegistration'
    _M_ClientBank._t_UsersRegistrationPrx = IcePy.defineProxy('::ClientBank::UsersRegistration', UsersRegistrationPrx)

    _M_ClientBank.UsersRegistrationPrx = UsersRegistrationPrx
    del UsersRegistrationPrx

    _M_ClientBank.UsersRegistration = Ice.createTempClass()
    class UsersRegistration(Ice.Object):

        def ice_ids(self, current=None):
            return ('::ClientBank::UsersRegistration', '::Ice::Object')

        def ice_id(self, current=None):
            return '::ClientBank::UsersRegistration'

        @staticmethod
        def ice_staticId():
            return '::ClientBank::UsersRegistration'

        def register(self, name, surname, pesel, income, current=None):
            raise NotImplementedError("servant method 'register' not implemented")

        def login(self, pesel, password, current=None):
            raise NotImplementedError("servant method 'login' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ClientBank._t_UsersRegistrationDisp)

        __repr__ = __str__

    _M_ClientBank._t_UsersRegistrationDisp = IcePy.defineClass('::ClientBank::UsersRegistration', UsersRegistration, (), None, ())
    UsersRegistration._ice_type = _M_ClientBank._t_UsersRegistrationDisp

    UsersRegistration._op_register = IcePy.Operation('register', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_float, False, 0)), (), ((), _M_ClientBank._t_RegistrationResponse, False, 0), (_M_ClientBank._t_RegistrationErr,))
    UsersRegistration._op_login = IcePy.Operation('login', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_ClientBank._t_LoginResponse, False, 0), (_M_ClientBank._t_UnauthorizedErr,))

    _M_ClientBank.UsersRegistration = UsersRegistration
    del UsersRegistration

# End of module ClientBank
