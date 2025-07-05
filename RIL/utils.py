from yarl import URL


def docs(path: str = "") -> URL:
    return URL("https://ril.celsiusnarhwal.dev").with_path(path, encoded=True)
