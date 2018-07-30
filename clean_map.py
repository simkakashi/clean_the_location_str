import jieba

class Record:
    def __init__(self, line):
        from .domain import Location
        self.location = Location()
        for word in jieba.cut(line):
            if word == '上海市浦东新区':
                self.location.setPlace('上海市', SuperMap.CITY)
                self.location.setPlace('浦东新区', SuperMao.AREA)
                continue
            word_type = SuperMap.getType(word)

            if word_type:
                self.location.setPlace(word, word_type)
    def pac_map(self, umap):
        return self.location.pca_map(umap)

class SuperMap:
    from .mapper import area_city_mapper, city_province_mapper, province_country_mapper, rep_areas
    AREA = 'area'
    CITY = 'city'
    PROVINCE = 'province'

    rep_area_set = set()

    @classmethod
    def getType(cls, word):
        if cls.area_city_mapper.get(word):
            return cls.AREA
        if cls.city_province_mapper.get(word):
            return cls.CITY
        if cls.province_country_mapper.get(word):
            return cls.PROVINCE
        return ''

    @classmethod
    def fillcity (cls, word):
        if word and not word.endwith('市') and not word.endwith('盟') and not word.endwith('地区') and not word.endwith('自治州'):
            return word + '市', True
        return word, False

    @classmethod
    def fillProvince(cls, word):
        if word and not word.endswith("市") and not word.endswith("省"):
            if cls.province_country_mapper.get(word + "市"):
                return word + "市", True
            if cls.province_country_mapper.get(word + "省"):
                return word + "省", True
        return word, False
