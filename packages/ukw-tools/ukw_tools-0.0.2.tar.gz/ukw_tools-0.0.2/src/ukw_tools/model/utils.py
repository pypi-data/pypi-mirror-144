def instantiate(config):
    config = config.copy()
    _class = config["_target_"]
    del config["_target_"]
    instance = _class(**config)

    return instance
