"""
Copyright start
Copyright (C) 2008 - 2022 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end
"""
from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations, _check_health

logger = get_logger('hikvision')


class hikvision(Connector):
    def execute(self, config, operation, operation_params, **kwargs):
        try:
            operation = operations.get(operation)
            return operation(config, operation_params)
        except Exception as err:
            logger.error('{0}'.format(err))
            raise ConnectorError('{0}'.format(err))

    def check_health(self, config):
        try:
            _check_health(config)
        except Exception as e:
            raise ConnectorError(e)
