import os

from zetemple import reader


def test_create_file(tmpdir):
    path = tmpdir.join("config.csv")

    contents = "host1, prefix1:\n" \
               "host2, prefix2:\n" \
               "#comment,comment\n" \
               "comment\n" \
               "host3, prefix3:"
    path.write(contents)

    expected_hosts = [
                      {"name": "host1", "prefix": "prefix1:"},
                      {"name": "host2", "prefix": "prefix2:"},
                      {"name": "host3", "prefix": "prefix3:"},
                     ]
    hosts = reader.read_config(str(path))

    assert hosts == expected_hosts
