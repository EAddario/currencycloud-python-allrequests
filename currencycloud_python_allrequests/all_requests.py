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


def logout(session):
    try:
        session.auth.close_session()
        print("Session closed")
    except ApiError as err:
        print("Logoff encountered an error: {0} (HTTP code {1})".format(err.code, err.status_code))
