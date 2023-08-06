import requests
import pandapower as pp
import pandas as pd
import numpy as np
from pathlib import Path
import os
import json
from fastapi.encoders import jsonable_encoder

class PandaHubClient:
    def __init__(self):
        config = os.path.join(Path.home(), "pandahub.config")
        try:
            with open(config, "r") as f:
                d = json.load(f)
        except FileNotFoundError:
            raise UserWarning("No pandahub configuration file found - log in first")
        self.url = d["url"]
        self.token = d["token"]
        self.cert = None
        if d.get("client_cert_path") and d.get("client_key_path"):
            self.cert = (d["client_cert_path"], d["client_key_path"])
        self.project_id = None

    def set_active_project(self, project_name):
        r = self._post("/projects/set_active_project", json=locals())
        if r.ok:
            self.project_id = r.json()
        else:
            self.project_id = None
        return r

    ### PROJECT HANDLING

    def create_project(self, name):
        return self._post("/projects/create_project", json=locals())

    def delete_project(self, i_know_this_action_is_final=False,
                             error_on_missing_project=True):
        return self._post("/projects/delete_project", json=locals())

    def project_exists(self, name):
        return self._post("/projects/project_exists", json=locals()).json()

    def get_projects(self):
        return self._post("/projects/get_projects").json()

    ### NET HANDLING

    def write_network_to_db(self, net, name, overwrite=True):
        json = locals()
        json["net"] = pp.to_json(net)
        return self._post("/net/write_network_to_db", json=json)

    def get_net_from_db(self, name, include_results=True, only_tables=None):
        r = self._post("/net/get_net_from_db", json=locals())
        return pp.from_json_string(r.json())


    ### TIMESERIES

    def multi_get_timeseries_from_db(self, filter_document={}, timestamp_range=None,
                                    exclude_timestamp_range=None,
                                    global_database=False):
        ts = self._post("/timeseries/multi_get_timeseries_from_db", json=locals()).json()
        for i, data in enumerate(ts):
            ts[i]["timeseries_data"] = pd.Series(json.loads(data["timeseries_data"]))
        return ts

    def get_timeseries_from_db(self, filter_document={}, timestamp_range=None,
                                    exclude_timestamp_range=None,
                                    global_database=False):
        r = self._post("/timeseries/get_timeseries_from_db", json=locals())
        return pd.Series(json.loads(r.json()))

    def write_timeseries_to_db(self, timeseries, data_type, element_type=None,
                               netname=None, element_index=None, name=None,
                               global_database=False, collection_name="timeseries"):
        json = locals()
        json["timeseries"] = json["timeseries"].to_json(date_format="iso")
        return self._post("/timeseries/write_timeseries_to_db", json=json)

    ### INTERNAL

    def _post(self, path, json=None, authorize=True):
        headers = {'Authorization': 'Bearer {}'.format(self.token)} if authorize else None
        path = self.url + path
        if json is None:
            json = {}
        if json is not None and "self" in json:
            del json['self']
        json = jsonable_encoder(json)
        json["project_id"] = self.project_id
        return requests.post(path, headers=headers, json=json, cert=self.cert)
