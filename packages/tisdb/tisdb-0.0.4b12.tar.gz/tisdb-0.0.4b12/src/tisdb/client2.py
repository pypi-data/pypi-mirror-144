# -*- coding: utf-8

from __future__ import annotations
from collections import defaultdict
from typing import Dict, List
from tisdb.api import MetricdbApi
from tisdb.client import TsdbClient
import pandas as pd
from pandas import DataFrame
import simplejson as json
from tisdb.config import TsdbConfig
from tisdb.model.metricdb import MetricdbData
from tisdb.model.tsdb import SaveResult, TsdbFields, TsdbTags
from tisdb.types import OpType, StoreType
from dateutil import parser as dt_parser


class MetricdbClient(TsdbClient):
    def __init__(self, store_type: StoreType = StoreType.PORM, conn_conf: TsdbConfig = TsdbConfig()):
        super().__init__(store_type=store_type, conn_conf=conn_conf)
        self.store_type = store_type
        self.config = conn_conf
        self.api = MetricdbApi(self.store_type, self.config)
        self.mydb = self._create_mydb(conn_conf=self.config)

    def create_metricdf_mydb(
        self, sql: str, param: dict = None, conn_conf: dict = None
    ) -> DataFrame:
        """create a dataframe of result from the given sql with params and connection configuration

        Args:
            sql (str): the given sql template
            param (dict, optional): sql param from the sql
            conn_conf (dict, optional): connection configs

        Returns:
            DataFrame: result in DataFrame Object
        """
        if (conn_conf is None):
            return pd.read_sql(sql=sql, params=param, con=self.mydb.connection())
        else:
            mydb = self._create_mydb(conn_conf=conn_conf)
            return pd.read_sql(sql=sql, params=param, con=mydb.connection())

    def dfpmetrics(self, df: DataFrame) -> List[MetricdbData]:
        return [MetricdbData.from_dict(_d) for _d in df.to_dict('records')]

    def metrics2icuser(self, metrics: List[MetricdbData]) -> List[Dict]:
        rets = defaultdict(list)
        for _m in metrics:
            rows = rets[json.dumps(_m.get_data_key())]
            _v = _m.get_data_value()
            _v['tags'] = _v.pop('tag')
            _v['fields'] = _v.pop('field')
            rows.append(_v)
        ret = []
        for _k, _v in rets.items():
            _r = json.loads(_k)
            _r['rows'] = _v
            ret.append(_r)
        return ret

    def parse(self, value: Dict[str, object]) -> MetricdbData:
        return MetricdbData(
            metric=value.get('metric'),
            ts=dt_parser.parse(value.get('ts', '1970-01-01')),
            tags=TsdbTags(**value.get("tag", {})),
            fields=TsdbFields(**value.get("field", {})),
        )

    def parsefdf(self, value: Dict[str, object]) -> MetricdbData:
        return MetricdbData.from_dict(value)

    def save(self, value: MetricdbData, op_type: OpType = OpType.UPSERT) -> SaveResult:
        """Save metricdb data

        Args:
            value (MetricdbData): Metricdb value to save
            op_type (OpType, optional): Saving operation type. Defaults to OpType.INSERT_IGNORE.

        Returns:
            SaveResult: Result of this save
        """
        return self.save_batch([value])

    def save_batch(self, value: List[MetricdbData], op_type: OpType = OpType.UPSERT) -> SaveResult:
        """Save metricdb data

        Args:
            value (MetricdbData): Metricdb value to save
            op_type (OpType, optional): Saving operation type. Defaults to OpType.INSERT_IGNORE.

        Returns:
            SaveResult: Result of this save
        """
        ret = self.api.upsert_batch(value)
        return SaveResult(data=ret)
