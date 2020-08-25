import random
import uuid
import sys

from colorama import init

import currencycloud
import currencycloud_allrequests.api as api
from currencycloud_allrequests.util import output, random_string, add_working_days

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

find_conversions = api.find_conversions(client, per_page=3, order_asc_desc="desc")
for elmt in find_conversions:
    output("find_conversions - Conversion {0} Buy: {1} Sell: {2}, Type: {3} Amount: {4})".format(
        elmt.id,
        elmt.buy_currency,
        elmt.sell_currency,
        elmt.fixed_side,
        elmt.client_buy_amount if elmt.fixed_side == "buy" else elmt.client_sell_amount))

find_conversions = api.find_conversions(client, per_page=3, order_asc_desc="desc")
for elmt in find_conversions:
    output("get_conversion - Conversion {0} Amount: {1} Currency: {2} Request Id: {3}".format(
        elmt.id,
        elmt.buy_currency,
        elmt.client_buy_amount,
        elmt.unique_request_id))

create_conversion = api.create_conversion(
    client,
    buy_currency="EUR",
    sell_currency="GBP",
    amount=str(round(random.uniform(6543.21, 12345.67), 2)),
    fixed_side="buy",
    reason="Invoice Payment",
    term_agreement="true",
    unique_request_id=uuid.uuid4())
output("create_conversion - Conversion {0} Amount: {1} Currency: {2} Request Id: {3}".format(
    create_conversion.id,
    create_conversion.buy_currency,
    create_conversion.client_buy_amount,
    create_conversion.unique_request_id))

get_conversion = api.get_conversion(client, resource_id=create_conversion.id)
output("get_conversion - Conversion {0} Amount: {1} Currency: {2} Request Id: {3}".format(
    get_conversion.id,
    get_conversion.buy_currency,
    get_conversion.client_buy_amount,
    get_conversion.unique_request_id))

date_change_quote = api.date_change_quote(
    client,
    resource_id=create_conversion.id,
    new_settlement_date=add_working_days(create_conversion.settlement_date, 7))
output("date_change_quote - Conversion {0} Amount: {1} Old Date: {2} New Date: {3}".format(
    date_change_quote.conversion_id,
    date_change_quote.amount,
    date_change_quote.old_settlement_date,
    date_change_quote.new_settlement_date))

date_change = api.date_change(
    client,
    resource_id=create_conversion.id,
    new_settlement_date=add_working_days(create_conversion.settlement_date, 7))
output("date_change - Conversion {0} Amount: {1} Old Date: {2} New Date: {3}".format(
    date_change.conversion_id,
    date_change.amount,
    date_change.old_settlement_date,
    date_change.new_settlement_date))

split_preview = api.split_preview(
    client,
    resource_id=create_conversion.id,
    amount=round((float(create_conversion.client_buy_amount) * 0.5), 2))
output("split_preview - Parent: {0} Amount: {1} Child: {2} Amount: {3}".format(
    split_preview.parent_conversion.get("id"),
    split_preview.parent_conversion.get("buy_amount"),
    split_preview.child_conversion.get("id"),
    split_preview.child_conversion.get("buy_amount")))

split = api.split(
    client,
    resource_id=create_conversion.id,
    amount=round((float(create_conversion.client_buy_amount) * 0.5), 2))
output("split - Parent: {0} Amount: {1} Child: {2} Amount: {3}".format(
    split.parent_conversion.get("id"),
    split.parent_conversion.get("buy_amount"),
    split.child_conversion.get("id"),
    split.child_conversion.get("buy_amount")))

split_history = api.split_history(
    client,
    resource_id=create_conversion.id)
output("split_history - Parent: {0} Origin: {1} Child: {2} Amount: {3}".format(
    split_history.parent_conversion,
    split_history.origin_conversion,
    split_history.child_conversions[0]["id"],
    split_history.child_conversions[0]["buy_amount"]))

parent_cancellation_quote = api.cancellation_quote(client, resource_id=split.parent_conversion.get("id"))
output("cancellation_quote - Parent Amount: {0} Currency: {1} Time: {2}".format(
    parent_cancellation_quote.amount,
    parent_cancellation_quote.currency,
    parent_cancellation_quote.event_date_time))

child_cancellation_quote = api.cancellation_quote(client, resource_id=split.child_conversion.get("id"))
output("cancellation_quote - Child Amount: {0} Currency: {1} Time: {2}".format(
    child_cancellation_quote.amount,
    child_cancellation_quote.currency,
    child_cancellation_quote.event_date_time))

cancel_parent_conversion = api.cancel_conversion(client, resource_id=split.parent_conversion.get("id"))
output("cancel_conversion - Conversion {0} Amount: {1} Type: {2}".format(
    cancel_parent_conversion.conversion_id,
    cancel_parent_conversion.amount,
    cancel_parent_conversion.event_type))

cancel_child_conversion = api.cancel_conversion(client, resource_id=split.child_conversion.get("id"))
output("cancel_conversion - Conversion {0} Amount: {1} Type: {2}".format(
    cancel_child_conversion.conversion_id,
    cancel_child_conversion.amount,
    cancel_child_conversion.event_type))

profit_and_loss = api.profit_and_loss(client, currency="EUR")
for elmt in profit_and_loss:
    output("profit_and_loss - Conversion {0} Amount: {1} Type: {2}".format(
        elmt.conversion_id,
        elmt.amount,
        elmt.event_type))

api.logout(client)
