from time import sleep


class InstagramException(Exception):
    pass


class InternetException(InstagramException):
    def __init__(self, exception):
        super().__init__("Error by connection with Instagram to '%s' with response code '%s'" % (
            exception.request.url,
            exception.response.status_code,
        ))

        self.request = exception.request
        self.response = exception.response


class AuthException(InstagramException):
    def __init__(self, login):
        super().__init__("Cannot auth user with username '%s'" % login)


class UnexpectedResponse(InstagramException):
    def __init__(self, exception, url, data=None):
        super().__init__("Get unexpected response from '%s' with data: %s\nError: %s" % (
            url,
            str(data),
            str(exception),
        ))


class NotUpdatedElement(InstagramException):
    def __init__(self, element, argument):
        super().__init__("Element '%s' haven't argument %s. Please, update this element" % (
            element.__repr__(),
            argument,
        ))


class ExceptionManager:
    def __init__(self, repeats=1):
        self._tree = {
            "action": lambda exception, *args, **kwargs: (args, kwargs),
            "branch": {},
        }
        self.repeats = repeats


    def __getitem__(self, key):
        if not issubclass(key, Exception):
            raise TypeError("Key must be Exception type")

        return self._search(key)[0]["action"]


    def _search(self, exception):
        if not issubclass(exception, Exception):
            raise TypeError("'exception' must be Exception type")

        current = self._tree
        while True:
            for key, value in current["branch"].items():
                if key == exception:
                    return value, True
                elif issubclass(exception, key):
                    current = value
                    break
            else:
                return current, False
            continue


    def __setitem__(self, key, value):
        if not issubclass(key, Exception):
            raise TypeError("Key must be Exception type")
        if not callable(value):
            raise TypeError("Value must be function")

        item, exists = self._search(key)
        if exists:
            item["action"] = value
        else:
            item["branch"][key] = {"branch": {}, "action": value}


    def decorator(self, func):
        def wrapper(obj, *args, **kwargs):
            for _ in range(self.repeats):
                try:
                    return func(obj, *args, **kwargs)
                except Exception as e:
                    exception = e
                    args, kwargs = self[exception.__class__](exception, *args, **kwargs)
            else:
                raise exception

        return wrapper


def http_response_handler(exception, *args, **kwargs):
    if exception.response.status_code == 429:
        sleep(600)
        return (args, kwargs)
    if exception.response.status_code == 400:
        sleep(60)

    raise exception
