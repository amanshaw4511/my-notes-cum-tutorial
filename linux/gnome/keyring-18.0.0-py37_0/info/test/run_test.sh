

set -ex



py.test -v keyring/tests
keyring --help
exit 0
