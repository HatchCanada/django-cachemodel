from hashlib import md5

from django.utils.encoding import smart_str


def generate_cache_key(prefix, *args, **kwargs):
    arg_str = ":".join(smart_str(a) for a in args)
    kwarg_str = ":".join("{}={}".format(smart_str(k), smart_str(v)) for k, v in list(kwargs.items()))
    key_str = "{}::{}".format(arg_str, kwarg_str)
    argkwarg_str = md5(smart_str(key_str).encode('utf-8')).hexdigest()
    if not isinstance(prefix, str):
        prefix = "_".join(str(a) for a in prefix)
    return "{}__{}".format(prefix, argkwarg_str)
