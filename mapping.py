
my_umap = {'南关区': '长春市',
           '南山区': '深圳市',
           '宝山区': '上海市',
           '市辖区': '东莞市',
           '普陀区': '上海市',
           '朝阳区': '北京市',
           '河东区': '天津市',
           '白云区': '广州市',
           '西湖区': '杭州市',
           '铁西区': '沈阳市'}


def transform(location_strs, umap=my_umap):
    from .Trans import trans
    temp = trans(umap)
    return temp.transform(location_strs)