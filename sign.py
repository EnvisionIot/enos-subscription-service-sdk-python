import hashlib


def main():
    m = hashlib.sha256()
    m.update(b'access_key')
    m.update(b'123')
    m.update(b'access_secret')
    m.update(b'456')
    m.update(b'sub_id')
    m.update(b'789')
    print(m.hexdigest())


if __name__ == "__main__":
    main()
