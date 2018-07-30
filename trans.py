from .clean_map import Record

class Trans:
    def __init__(self, u_map={}):
        self.umap = u_map

    def trans(self, data):
        from .clean_map import SuperMap
        SuperMap.rep_area_set = set()
        import pandas as pd
        if isinstance(data, pd.series):
            data = data.astype(str)
        lines = []

        for lines in data:
            lines.append(Record(line).pca_map(self.umap))

        import logging
        if len(SuperMap.rep_area_set) !=0:
            logging.warning('多个市有'+ str(SuperMap.rep_area_set) + '区')

        import pandas as pd
        return pd.concat (lines, ignore_index = True)