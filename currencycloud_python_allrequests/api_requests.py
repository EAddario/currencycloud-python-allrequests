import sys
from colorama import init
from colorama import Fore, Style

import currencycloud
import currencycloud_python_allrequests.all_requests as api

colors = ["WHITE", "YELLOW", "GREEN", "CYAN", "BLUE", "MAGENTA"]
idx = 0


def output(msg):
    global idx
    print(Style.BRIGHT + getattr(Fore, colors[idx % len(colors)]) + msg)
    idx += 1


login_id = sys.argv[1]
api_key = sys.argv[2]
environment = currencycloud.Config.ENV_DEMO
client = currencycloud.Client(login_id, api_key, environment)
init(autoreset=True)

current_account = api.current_account(client)
output("current_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(current_account.account_name,
                                                                                 current_account.id,
                                                                                 current_account.street,
                                                                                 current_account.city,
                                                                                 current_account.postal_code,
                                                                                 current_account.country))

find_accounts = api.find_accounts(client, per_page=3)
for elmt in find_accounts:
    output("find_accounts - Account {0} ({1})".format(current_account.account_name, current_account.id))

create_account = api.create_account(client, account_name="Wirecard Development",
                                    legal_entity_type="individual",
                                    street="12 Steward St",
                                    city="london",
                                    postal_code="E1 6FQ",
                                    country="GB",
                                    api_trading=True,
                                    online_trading=True,
                                    phone_trading=True)
output("create_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(create_account.account_name,
                                                                                create_account.id,
                                                                                create_account.street,
                                                                                create_account.city,
                                                                                create_account.postal_code,
                                                                                create_account.country))

update_account = api.update_account(client, resource_id=create_account.id, city="London")
output("update_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(update_account.account_name,
                                                                                update_account.id,
                                                                                update_account.street,
                                                                                update_account.city,
                                                                                update_account.postal_code,
                                                                                update_account.country))

get_account = api.get_account(client, resource_id=update_account.id)
output("get_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(get_account.account_name,
                                                                             get_account.id,
                                                                             get_account.street,
                                                                             get_account.city,
                                                                             get_account.postal_code,
                                                                             get_account.country))

get_payment_charges = api.get_payment_charges(client, resource_id=get_account.id)
output("get_payment_charges - Charge Id: {0}, Account Id: {1}, Charge Type: {2}, Enabled? {3}, Default? {4}".format(get_payment_charges[0].charge_settings_id,
                                                                                                                    get_payment_charges[0].account_id,
                                                                                                                    get_payment_charges[0].charge_type,
                                                                                                                    get_payment_charges[0].enabled,
                                                                                                                    get_payment_charges[0].default))

update_payment_charges = api.update_payment_charges(client, account_id=get_payment_charges[0].account_id, resource_id=get_payment_charges[0].charge_settings_id)
output("update_payment_charges - Charge Id: {0}, Account Id: {1}, Charge Type: {2}, Enabled? {3}, Default? {4}".format(update_payment_charges.charge_settings_id,
                                                                                                                       update_payment_charges.account_id,
                                                                                                                       update_payment_charges.charge_type,
                                                                                                                       update_payment_charges.enabled,
                                                                                                                       update_payment_charges.default))

balance = api.get_balance(client, currency='USD')
output("Your {0} balance is {1}".format(balance.currency, balance.amount))

balances = api.find_balances(client, order='currency', per_page=5)
for elmt in balances:
    output("Your {0} balance is {1}".format(elmt.currency, elmt.amount))

for elmt in balances:
    topup_margin = api.topup_margin(client, currency=elmt.currency, amount=(float(elmt.amount) + 1234.56))
    output("Your new {0} balance is {1}".format(topup_margin.currency, topup_margin.amount))

api.logout(client)
