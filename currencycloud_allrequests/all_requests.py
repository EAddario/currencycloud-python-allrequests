import random
import sys

from colorama import init

import currencycloud
import currencycloud_allrequests.api as api
from currencycloud_allrequests.util import output, random_string

login_id = sys.argv[1]
api_key = sys.argv[2]
environment = currencycloud.Config.ENV_DEMO
client = currencycloud.Client(login_id, api_key, environment)
init(autoreset=True)

current_account = api.current_account(client)
output("current_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(
    current_account.account_name,
    current_account.id,
    current_account.street,
    current_account.city,
    current_account.postal_code,
    current_account.country))

find_accounts = api.find_accounts(client, per_page=3)
for elmt in find_accounts:
    output("find_accounts - Account {0} ({1})".format(elmt.account_name, elmt.id))

create_account = api.create_account(
    client,
    account_name="Wirecard Development",
    legal_entity_type="individual",
    street="12 Steward St",
    city="london",
    postal_code="E1 6FQ",
    country="GB",
    api_trading=True,
    online_trading=True,
    phone_trading=True)
output("create_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(
    create_account.account_name,
    create_account.id,
    create_account.street,
    create_account.city,
    create_account.postal_code,
    create_account.country))

update_account = api.update_account(client, resource_id=create_account.id, city="London")
output("update_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(
    update_account.account_name,
    update_account.id,
    update_account.street,
    update_account.city,
    update_account.postal_code,
    update_account.country))

get_account = api.get_account(client, resource_id=update_account.id)
output("get_account - Account {0} ({1}), Address: {2}, {3}, {4}, {5}".format(
    get_account.account_name,
    get_account.id,
    get_account.street,
    get_account.city,
    get_account.postal_code,
    get_account.country))

get_payment_charges = api.get_payment_charges(client, resource_id=get_account.id)
output("get_payment_charges - Charge Id: {0}, Account Id: {1}, Charge Type: {2}, Enabled? {3}, Default? {4}".format(
    get_payment_charges[0].charge_settings_id,
    get_payment_charges[0].account_id,
    get_payment_charges[0].charge_type,
    get_payment_charges[0].enabled,
    get_payment_charges[0].default))

update_payment_charges = api.update_payment_charges(
    client,
    account_id=get_payment_charges[0].account_id,
    resource_id=get_payment_charges[0].charge_settings_id)
output("update_payment_charges - Charge Id: {0}, Account Id: {1}, Charge Type: {2}, Enabled? {3}, Default? {4}".format(
    update_payment_charges.charge_settings_id,
    update_payment_charges.account_id,
    update_payment_charges.charge_type,
    update_payment_charges.enabled,
    update_payment_charges.default))

get_balance = api.get_balance(client, currency='USD')
output("get_balance - Your {0} balance is {1}".format(get_balance.currency, get_balance.amount))

find_balances = api.find_balances(client, order='currency', per_page=5)
for elmt in find_balances:
    output("find_balances - Your {0} balance is {1}".format(elmt.currency, elmt.amount))

for elmt in find_balances:
    topup_margin = api.topup_margin(client, currency=elmt.currency, amount=(float(elmt.amount) + 1234.56))
    output("topup_margin - Your new {0} balance is {1}".format(topup_margin.currency, topup_margin.amount))

find_beneficiaries = api.find_beneficiaries(client, per_page=5)
for elmt in find_beneficiaries:
    output("find_beneficiaries - Name: {0}, Account Holder Name: {1}, Bank Country: {2}, Currency {3}".format(
        elmt.name,
        elmt.bank_account_holder_name,
        elmt.bank_country,
        elmt.currency))

validate_beneficiary = api.validate_beneficiary(
    client,
    bank_country="IT",
    currency="EUR",
    beneficiary_country="IT",
    iban="IT1200012030200359100100",
    bic_swift="IBSPITNA020",
    bank_name="Banca Monte dei Paschi di Siena",
    bank_address="n° 3 Piazza Salimbeni, Siena SI, 53100",
    bank_account_type="checking",
    beneficiary_entity_type="individual",
    beneficiary_first_name="Dame Tamara",
    beneficiary_last_name="Carlton",
    beneficiary_address="Piazza Museo n° 19, Napoli, 80135",
    beneficiary_city="Napoli",
    beneficiary_postcode="80135",
    beneficiary_state_or_province="Provincia di Napoli",
    payment_types=["priority", "regular"])
output("validate_beneficiary - Name: {0}, Last Name: {1}, Bank Name: {2}, Bank Address {3}".format(
    validate_beneficiary.beneficiary_first_name,
    validate_beneficiary.beneficiary_last_name,
    validate_beneficiary.bank_name,
    validate_beneficiary.bank_address))

create_beneficiary = api.create_beneficiary(
    client,
    bank_country="IT",
    currency="EUR",
    beneficiary_country="IT",
    iban="IT1200012030200359100100",
    bic_swift="IBSPITNA020",
    bank_name="Banca Monte dei Paschi di Siena",
    bank_address="n° 3 Piazza Salimbeni, Siena SI, 53100",
    bank_account_type="checking",
    beneficiary_entity_type="individual",
    beneficiary_first_name="Dame Tamara",
    beneficiary_last_name="Carlton",
    beneficiary_address="Piazza Museo n° 19, Napoli, 80135",
    beneficiary_city="Napoli",
    beneficiary_postcode="80135",
    beneficiary_state_or_province="Provincia di Napoli",
    payment_types=["priority", "regular"],
    bank_account_holder_name="Dame Tamara Carlton",
    name="Fulcrum Fund")
output("create_beneficiary - Id: {0} Name: {1}, Account Holder: {2}, Bank Country: {3}, Currency: {4}".format(
    create_beneficiary.id,
    create_beneficiary.name,
    create_beneficiary.bank_account_holder_name,
    create_beneficiary.bank_country,
    create_beneficiary.currency))

get_beneficiary = api.get_beneficiary(client, resource_id=create_beneficiary.id)
output("get_beneficiary - Id: {0} Name: {1}, Account Holder: {2}, Bank Country: {3}, Currency: {4}".format(
    get_beneficiary.id,
    get_beneficiary.name,
    get_beneficiary.bank_account_holder_name,
    get_beneficiary.bank_country,
    get_beneficiary.currency))

update_beneficiary = api.update_beneficiary(
    client,
    resource_id=get_beneficiary.id,
    account_number=random.randint(100000000, 999999999),
    beneficiary_date_of_birth="1968-03-23",
    beneficiary_identification_type="passport",
    beneficiary_identification_value=random.randint(100000000, 999999999),
    beneficiary_external_reference="BEN-REF-" + str(random.randint(1000, 9999)),
    email="tamara.carlton@fulcrum-fund.org")
output("update_beneficiary - Id: {0} Name: {1}, Account Number: {2}, Date of birth: {3}, Email: {4}".format(
    update_beneficiary.id,
    update_beneficiary.name,
    update_beneficiary.account_number,
    update_beneficiary.beneficiary_date_of_birth,
    update_beneficiary.email))

delete_beneficiary = api.delete_beneficiary(client, resource_id=update_beneficiary.id)
output("delete_beneficiary - Id: {0} Name: {1}, Account Holder: {2}, Bank Country: {3}, Currency: {4}".format(
    delete_beneficiary.id,
    delete_beneficiary.name,
    delete_beneficiary.bank_account_holder_name,
    delete_beneficiary.bank_country,
    delete_beneficiary.currency))

current_contact = api.current_contact(client)
output("current_contact - Login Id {0} ({1}), Name: {2}, Last Name: {3}, Account: {4}, Id: {5}".format(
    current_contact.login_id,
    current_contact.id,
    current_contact.first_name,
    current_contact.last_name,
    current_contact.account_name,
    current_contact.account_id))

find_contacts = api.find_contacts(client, per_page=3)
for elmt in find_contacts:
    output("find_contacts - Account {0} ({1})".format(elmt.login_id, elmt.id))

create_contact = api.create_contact(
    client,
    account_id=create_account.id,
    first_name="Wirecard",
    last_name="Development",
    email_address="development." + random_string(6) + "@wirecard.com",
    phone_number="+44 20 3326 8173",
    date_of_birth="1968-03-23")
output("create_contact - Login Id {0} ({1}), Name: {2}, Last Name: {3}, Account: {4}, Id: {5}".format(
    create_contact.login_id,
    create_contact.id,
    create_contact.first_name,
    create_contact.last_name,
    create_contact.account_name,
    create_contact.account_id))

update_contact = api.update_contact(
    client,
    resource_id=create_contact.id,
    your_reference="CTCT-REF-" + str(random.randint(1000, 9999)),
    status="enabled",
    locale="en-GB")
output("update_contact - Login Id {0} ({1}), Name: {2}, Last Name: {3}, Reference: {4}, Status: {5}".format(
    update_contact.login_id,
    update_contact.id,
    update_contact.first_name,
    update_contact.last_name,
    update_contact.your_reference,
    update_contact.status))

get_contact = api.get_contact(client, resource_id=update_contact.id)
output("get_contact - Login Id {0} ({1}), Name: {2}, Last Name: {3}, Account: {4}, Id: {5}".format(
    get_contact.login_id,
    get_contact.id,
    get_contact.first_name,
    get_contact.last_name,
    get_contact.account_name,
    get_contact.account_id))

api.logout(client)
