__author__ = "Karun Sandhu"

import paramiko
from paramiko import SSHClient
from getpass import getpass


def key_based_connect(host: str, passphrase: str | None = None) -> SSHClient:
    username = "karun"
    keyfile = "/home/karun/.ssh/id_ed25519"
    if not passphrase:
        passphrase = getpass(f"Enter passphrase for key: {keyfile}")
    pkey = paramiko.Ed25519Key.from_private_key_file(
        keyfile, password=passphrase
    )
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(
        host,
        username=username,
        pkey=pkey,
    )
    return client


def read_remote_journal() -> None:
    host = input("Enter the IP for the host: ")
    minutes = input("Of how many minutes do you want to see the logs? ")
    client = key_based_connect(host)
    _, stdout, _ = client.exec_command(f"journalctl --since '{minutes}m ago'")
    print("".join(stdout.readlines()))
    client.close()


if __name__ == "__main__":
    read_remote_journal()
