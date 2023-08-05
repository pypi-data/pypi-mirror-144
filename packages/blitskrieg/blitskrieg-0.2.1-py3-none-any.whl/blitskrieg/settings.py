# BLITSkrieg - a Bitcoin Lightning Integration Test Service
#
# Copyright (C) 2022 hashbeam contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# For a full list of contributors, please see the AUTHORS.md file.
"""Settings module for BLITSkrieg.

WARNING: only Python's core module imports here, to avoid breaking build system
         and import loops
"""

from decimal import Decimal
from os import environ as env
from os import path
from pathlib import Path

# Package settings
PKG_NAME = 'blitskrieg'
PIP_NAME = PKG_NAME

# Server settings
HOST = '0.0.0.0'
PORT = '6969'
GRPC_WORKERS = 10
GRPC_GRACE_TIME = 40
ONE_DAY_IN_SECONDS = 60 * 60 * 24
RUNTIME_SERVER = None
THREADS = []
HOST_WORKDIR = env.get('HOST_WORKDIR', '')
DATA = path.join(str(Path.home()), '.' + PKG_NAME)
CONFIG = path.join(DATA, 'config')
CONFIG_MAIN_OPTS = ['PORT', 'LOGS_DIR', 'LOGS_LEVEL']
EXIT_WAIT = 30
STACK_CREATING = 0
STACK_REMOVING = 0
STACK_RUNNING = 0

# CLI settings
CLI_RPCSERVER = 'localhost:6969'
CLI_BASE_GRPC_CODE = 64
CONFIG_CLI_OPTS = ['RPCSERVER']

# Services settings
USER = 'blits'
PASSWORD = 'default_password'
SERVICES = [
    'bitcoind',
    'boltlight',
    'clightning',
    'eclair',
    'electrs',
    'electrum',
    'lnd',
]
BITCOIND_REF = '22.0'
BOLTLIGHT_REF = '2.1.0'
CLIGHTNING_REF = '0.10.1'
ECLAIR_REF = '0.6.2'
ELECTRS_REF = '0.9.6'
ELECTRUM_REF = '4.1.5'
LND_REF = '0.13.4-beta'

# Compose settings
COMPOSE_FILE = 'compose.yml'
COMPOSE_PRJ_NAME = 'krieg'
COMPOSE_BASE_CMD = (f'docker-compose -f {COMPOSE_FILE} -p {COMPOSE_PRJ_NAME} '
                    '--ansi=never'.split())

# RPC settings
RPCSERVER = 'localhost:6969'
RPC_URL = ''
RPC_TRIES = 10
RPC_SLEEP = 1
RPC_CONN_TIMEOUT = 3.1
RPC_READ_TIMEOUT = 30

# Bitcoin settings
CMD_BASE_BITCOIND = ['bitcoin-cli']
BITCOIND_RPC_URL = f'http://user:{PASSWORD}@bitcoind:18443'
BITCOIND_DIR = '.bitcoin'
MINER_WLT = 'miner'
GENTXS_MAX_INPUTS = 3
GENTXS_MAX_OUTPUTS = 3
MAX_ADDR_PER_WALLET = 200000
MAX_REWARD = 50
HALVING_INTERVAL = 150
BITCOIN_PRECISION = Decimal('.00000001')
DUST_AMT = Decimal('0.000006')
MIN_RELAY_FEE = Decimal('0.000015')

# Lightning settings
CURRENT_BOLTLIGHT_NODES = []
BOLTLIGHT_PORT = 1708
BL_ADDR = '{}:' + str(BOLTLIGHT_PORT)
BOLTLIGHT_DATA = 'data'
INIT_SH = 'init_{}.sh'

# Logging settings
LOGS_DIR = './logs'
LOGS_BLITSKRIEG = PKG_NAME + '.log'
LOG_TIMEFMT = '%Y-%m-%d %H:%M:%S %z'
LOG_TIMEFMT_SIMPLE = '%d %b %H:%M:%S'
LOGS_LEVEL = 'INFO'
LOG_LEVEL_FILE = 'DEBUG'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            "[%(asctime)s] %(levelname).3s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': LOG_TIMEFMT
        },
        'simple': {
            'format': '%(asctime)s %(levelname).3s: %(message)s',
            'datefmt': LOG_TIMEFMT_SIMPLE
        },
    },
    'handlers': {
        'console': {
            'level': LOGS_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    }
}
LOGGING_FILE = {
    'file': {
        'level': LOG_LEVEL_FILE,
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': path.join(LOGS_DIR, LOGS_BLITSKRIEG),
        'maxBytes': 1048576,
        'backupCount': 7,
        'formatter': 'verbose'
    }
}
