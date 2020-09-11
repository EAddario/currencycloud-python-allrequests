from currencycloud.errors import ApiError


def current_account(session):
    try:
        return session.accounts.current()
    except ApiError as err:
        print("Current Account encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def create_account(session, **kwargs):
    try:
        return session.accounts.create(**kwargs)
    except ApiError as err:
        print("Create Account encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_account(session, **kwargs):
    try:
        return session.accounts.retrieve(**kwargs)
    except ApiError as err:
        print("Get Account encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_accounts(session, **kwargs):
    try:
        return session.accounts.find(**kwargs)
    except ApiError as err:
        print("Find Accounts encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def update_account(session, **kwargs):
    try:
        return session.accounts.update(**kwargs)
    except ApiError as err:
        print("Update Account encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_payment_charges(session, **kwargs):
    try:
        return session.accounts.retrieve_payment_charges_settings(**kwargs)
    except ApiError as err:
        print("Get Payment Charges encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def update_payment_charges(session, **kwargs):
    try:
        return session.accounts.payment_charges_settings(**kwargs)
    except ApiError as err:
        print("Update Payment Charges encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_balance(session, **kwargs):
    try:
        return session.balances.for_currency(**kwargs)
    except ApiError as err:
        print("Check Balance encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_balances(session, **kwargs):
    try:
        return session.balances.find(**kwargs)
    except ApiError as err:
        print("Check Balances encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def topup_margin(session, **kwargs):
    try:
        return session.balances.top_up_margin(**kwargs)
    except ApiError as err:
        print("Top-up Margin Balance encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_beneficiaries(session, **kwargs):
    try:
        return session.beneficiaries.find(**kwargs)
    except ApiError as err:
        print("Find Beneficiaries encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def validate_beneficiary(session, **kwargs):
    try:
        return session.beneficiaries.validate(**kwargs)
    except ApiError as err:
        print("Validate Beneficiary encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def create_beneficiary(session, **kwargs):
    try:
        return session.beneficiaries.create(**kwargs)
    except ApiError as err:
        print("Create Beneficiary encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_beneficiary(session, **kwargs):
    try:
        return session.beneficiaries.retrieve(**kwargs)
    except ApiError as err:
        print("Get Beneficiary encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def update_beneficiary(session, **kwargs):
    try:
        return session.beneficiaries.update(**kwargs)
    except ApiError as err:
        print("Update Beneficiary encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def delete_beneficiary(session, **kwargs):
    try:
        return session.beneficiaries.delete(**kwargs)
    except ApiError as err:
        print("Delete Beneficiary encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def current_contact(session):
    try:
        return session.contacts.current()
    except ApiError as err:
        print("Current Contact encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def create_contact(session, **kwargs):
    try:
        return session.contacts.create(**kwargs)
    except ApiError as err:
        print("Create Contact encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_contact(session, **kwargs):
    try:
        return session.contacts.retrieve(**kwargs)
    except ApiError as err:
        print("Get Contact encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_contacts(session, **kwargs):
    try:
        return session.contacts.find(**kwargs)
    except ApiError as err:
        print("Find Contacts encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def update_contact(session, **kwargs):
    try:
        return session.contacts.update(**kwargs)
    except ApiError as err:
        print("Update Contact encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_conversions(session, **kwargs):
    try:
        return session.conversions.find(**kwargs)
    except ApiError as err:
        print("Find Conversions encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_conversion(session, **kwargs):
    try:
        return session.conversions.retrieve(**kwargs)
    except ApiError as err:
        print("Get Conversion encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def create_conversion(session, **kwargs):
    try:
        return session.conversions.create(**kwargs)
    except ApiError as err:
        print("Create Conversion encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def cancellation_quote(session, **kwargs):
    try:
        return session.conversions.cancellation_quote(**kwargs)
    except ApiError as err:
        print("Conversion Cancellation Quote encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def cancel_conversion(session, **kwargs):
    try:
        return session.conversions.cancel(**kwargs)
    except ApiError as err:
        print("Cancel Conversion encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def date_change_quote(session, **kwargs):
    try:
        return session.conversions.date_change_quote(**kwargs)
    except ApiError as err:
        print("Conversion Date Change Quote encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def date_change(session, **kwargs):
    try:
        return session.conversions.date_change(**kwargs)
    except ApiError as err:
        print("Conversion Date Change encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def split_preview(session, **kwargs):
    try:
        return session.conversions.split_preview(**kwargs)
    except ApiError as err:
        print("Conversion Split Preview encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def split(session, **kwargs):
    try:
        return session.conversions.split(**kwargs)
    except ApiError as err:
        print("Conversion Split encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def split_history(session, **kwargs):
    try:
        return session.conversions.split_history(**kwargs)
    except ApiError as err:
        print("Conversion Split History encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def profit_and_loss(session, **kwargs):
    try:
        return session.conversions.profit_and_loss(**kwargs)
    except ApiError as err:
        print("Conversion Profit & Loss encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_funding_accounts(session, **kwargs):
    try:
        return session.funding.find_funding_accounts(**kwargs)
    except ApiError as err:
        print("Find Funding Accounts encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_ibans(session, **kwargs):
    try:
        return session.ibans.find(**kwargs)
    except ApiError as err:
        print("Find IBANs encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_payments(session, **kwargs):
    try:
        return session.payments.find(**kwargs)
    except ApiError as err:
        print("Find Payments encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def create_payment(session, **kwargs):
    try:
        return session.payments.create(**kwargs)
    except ApiError as err:
        print("Create Payment encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def delete_payment(session, **kwargs):
    try:
        return session.payments.delete(**kwargs)
    except ApiError as err:
        print("Delete Payment encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_payment(session, **kwargs):
    try:
        return session.payments.retrieve(**kwargs)
    except ApiError as err:
        print("Retrieve Payment encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def update_payment(session, **kwargs):
    try:
        return session.payments.update(**kwargs)
    except ApiError as err:
        print("Update Payment encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def authorise_payment(session, **kwargs):
    try:
        return session.payments.authorise(**kwargs)
    except ApiError as err:
        print("Authorise Payment encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payment_delivery_date(session, **kwargs):
    try:
        return session.payments.payment_delivery_date(**kwargs)
    except ApiError as err:
        print("Payment Delivery Date encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def quote_payment_fee(session, **kwargs):
    try:
        return session.payments.quote_payment_fee(**kwargs)
    except ApiError as err:
        print("Quote Payment Fee encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payment_confirmation(session, **kwargs):
    try:
        return session.payments.payment_confirmation(**kwargs)
    except ApiError as err:
        print("Payment Confirmation encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payment_submission(session, **kwargs):
    try:
        return session.payments.retrieve_submission(**kwargs)
    except ApiError as err:
        print("Payment Submission encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_payer(session, **kwargs):
    try:
        return session.payers.retrieve(**kwargs)
    except ApiError as err:
        print("Retrieve Payers encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def find_rates(session, **kwargs):
    try:
        return session.rates.find(**kwargs)
    except ApiError as err:
        print("Find Rates encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def get_rate(session, **kwargs):
    try:
        return session.rates.detailed(**kwargs)
    except ApiError as err:
        print("Get Rate encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def beneficiary_required_details(session, **kwargs):
    try:
        return session.reference.beneficiary_required_details(**kwargs)
    except ApiError as err:
        print("Beneficiary Required Details encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def conversion_dates(session, **kwargs):
    try:
        return session.reference.conversion_dates(**kwargs)
    except ApiError as err:
        print("Conversion Dates encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def currencies(session, **kwargs):
    try:
        return session.reference.currencies(**kwargs)
    except ApiError as err:
        print("Currencies encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payment_dates(session, **kwargs):
    try:
        return session.reference.payment_dates(**kwargs)
    except ApiError as err:
        print("Payment Dates encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def settlement_accounts(session, **kwargs):
    try:
        return session.reference.settlement_accounts(**kwargs)
    except ApiError as err:
        print("Settlement Accounts encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payer_required_details(session, **kwargs):
    try:
        return session.reference.payer_required_details(**kwargs)
    except ApiError as err:
        print("Payer Required Details encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payment_purpose_codes(session, **kwargs):
    try:
        return session.reference.payment_purpose_codes(**kwargs)
    except ApiError as err:
        print("Payment Purpose Codes encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def bank_details(session, **kwargs):
    try:
        return session.reference.bank_details(**kwargs)
    except ApiError as err:
        print("Bank Details encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def payment_fee_rules(session, **kwargs):
    try:
        return session.reference.payment_fee_rules(**kwargs)
    except ApiError as err:
        print("Payment Fee Rules encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))


def logout(session):
    try:
        session.auth.close_session()
        print("Session closed")
    except ApiError as err:
        print("Logoff encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))
