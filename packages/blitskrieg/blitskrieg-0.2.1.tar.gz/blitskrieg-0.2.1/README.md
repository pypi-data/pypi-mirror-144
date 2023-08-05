# BLITSkrieg: Bitcoin Lightning Integration Test Service

BLITSkrieg is a gRPC server in Python that aims to provide a set of utilities
to test Bitcoin and Lightning Network services.

It uses [boltlight](https://gitlab.com/hashbeam/boltlight) in order to hide
the differences between the different LN node implementations.

Currently the available services are:
* `bitcoind` <sup>[1]</sup>
* `boltlight` <sup>[2]</sup>
* `c-lightning`
* `eclair`
* `electrs` <sup>[3]</sup>
* `electrum`
* `lnd`

#### Notes

1. docker image always necessary
2. docker image necessary to call LN-related commands
3. docker image necessary to run `electrum`

## System dependencies

- Linux or macOS (_Windows may work, but is not supported_)
- Python 3.9+
- poetry
- docker

## Build

In order to build the docker image for BLITSkrieg, run:
```bash
# production mode
$ ./unix_helper build

# development mode
$ ./unix_helper build-dev
```

Production mode does not include the package dev dependencies.

Pre-built (production mode) images for the latest versions can be downloaded
from GitLab's [container
registry](https://gitlab.com/hashbeam/blitskrieg/container_registry).

## Run

In order to launch the docker image of BLITSkrieg, run:
```bash
# production mode
$ ./unix_helper run

# development mode
$ ./unix_helper run-dev
```

## CLI

BLITSkrieg features a Command Line Interface, named `bli`. It can be installed
and called from the project directory.

In order to install the project, run:
```bash
$ poetry install
```

In order to run `bli`, call it via poetry:
```bash
$ poetry run bli
```

`bli` supports shell completion for bash and zsh (the shell needs to have
completion support enabled). It can be enabled sourcing the appropriate file
for the running shell, from the project directory:
```bash
$ . ./blitskrieg/share/complete-bli.bash
$ . ./blitskrieg/share/complete-bli.zsh
```

## Use

In order to run a command on BLITSkrieg, you can directly call it by making
a gRPC call to it, or you can use its CLI.

To get a list of available CLI commands, run:
```bash
$ poetry run bli --help
```

In order to perform any action in BLITSkrieg, you first need to create a LN
stack. To do so, call:
```bash
$ poetry run bli createstack [--<implementation>=<number_of_nodes>]
```

If you do not specify any LN node, this will run a single `bitcoind` instance
and only Bitcoin-related commands will be available.

Visit our [docker repository](https://gitlab.com/hashbeam/docker) in
order to build the required services.
Otherwise, if the needed docker images are not available, they will be pulled
from hashbeam's GitLab container registry.
