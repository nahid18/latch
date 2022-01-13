"""
login
~~~~~
Performs authorization flow with the latch platform.
"""

from latch.auth import PKCE, CSRFState, OAuth2
from latch.config import Config
from latch.constants import OAuth2Constants


def login():
    """Retrieves + persists an access token to a user's latch resources."""

    with PKCE() as pkce:
        with CSRFState() as csrf_state:

            oauth2_flow = OAuth2(pkce, csrf_state, OAuth2Constants)
            auth_code = oauth2_flow.authorization_request()
            token = oauth2_flow.access_token_request(auth_code)

            config = Config()
            if config.token_exists():
                config.update_token(token)