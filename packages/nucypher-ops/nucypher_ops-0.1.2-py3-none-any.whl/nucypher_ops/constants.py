import os
from appdirs import AppDirs
from pathlib import Path

APP_DIR = AppDirs("nucypher-ops")
DEFAULT_CONFIG_ROOT = Path(os.getenv('NUCYPHER_OPS_CONFIG_ROOT', default=APP_DIR.user_data_dir))

MAINNET = 1
ROPSTEN = 3
RINKEBY = 4
GOERLI = 5

POLYGON_MAINNET = 137
POLYGON_MUMBAI = 80001


CHAIN_NAMES = {
    MAINNET: "Mainnet",
    ROPSTEN: "Ropsten",
    RINKEBY: "Rinkeby",
    GOERLI: "Goerli",
    POLYGON_MAINNET: "Polygon/Mainnet",
    POLYGON_MUMBAI: "Polygon/Mumbai"
}

REVERSE_LOOKUP_CHAIN_NAMES = {v: k for k, v in CHAIN_NAMES.items()}


NETWORKS = { 
    'mainnet': {'policy': MAINNET, 'payment': POLYGON_MAINNET},
    'ibex': {'policy': RINKEBY, 'payment': POLYGON_MUMBAI},
    'lynx': {'policy': GOERLI, 'payment': POLYGON_MUMBAI}
}

PAYMENT_NETWORK_CHOICES = {k:k for k in ('polygon', 'mumbai')}

PLAYBOOKS = 'nucypher_ops/playbooks'
TEMPLATES = 'nucypher_ops/templates'


# Environment variable names
NUCYPHER_ENVVAR_KEYSTORE_PASSWORD = "NUCYPHER_KEYSTORE_PASSWORD"
NUCYPHER_ENVVAR_OPERATOR_ADDRESS = "NUCYPHER_OPERATOR_ADDRESS"
NUCYPHER_ENVVAR_OPERATOR_ETH_PASSWORD = "NUCYPHER_OPERATOR_ETH_PASSWORD"
NUCYPHER_ENVVAR_PROVIDER_URI = "NUCYPHER_PROVIDER_URI"

DEFAULT_NAMESPACE=os.getenv('NUCYPHER_OPS_DEFAULT_NAMESPACE', 'nucypher')
DEFAULT_NETWORK=os.getenv('NUCYPHER_OPS_DEFAULT_NETWORK', 'mainnet')