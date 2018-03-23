# -*- coding: utf-8 -*-

from promotion.utils.fields import Base64ImageField
from promotion.properties.models import AssetsImg
from promotion.properties.models import Assets
from promotion.accounts.models import User


class Ssql(object):
    def __init__(self, keys):
        self.sql = 'select * from properties_assets where '
        self.conver = self.unicode_to_ascii
        self.task_list = []
        # self.keys = keys
        for attr in keys:
            if isinstance(attr.get('val')[1], tuple):
                tmp = self.fuzzy_match(attr['val'], attr['key'])
                self.task_list.append(tmp)
                continue
            if attr.get('val'):
                tmp = self.exact_fit(attr['val'], attr['key'])
                self.task_list.append(tmp)
        self.sql += ' and '.join(self.task_list)
        self.sql = self.sql.decode('utf-8')

    # 范围搜索(模糊搜索)
    def fuzzy_match(self, arg, t):
        json_k, json_v = arg
        if json_v:
            tp_sql = '''{0[0]}->'$.{0[1]}'>={0[2]} and {0[0]}->'$.{0[1]}'<={0[3]}'''
            format_val = [t, json_k, json_v[0], json_v[1]]
            return tp_sql.format(self.conver(format_val))

    # 精确匹配
    def exact_fit(self, arg, t):
        json_k, json_v = arg
        format_val = [t, json_k, json_v]
        return '''{0[0]}->'$.{0[1]}'={0[2]}'''.format(self.conver(format_val))

    def _format(self, ele):
        if isinstance(ele, unicode):
            if ele == u'parms' or ele == u'instruction':
                ele = ele.encode('utf-8')
            else:
                ele = '"' + ele.encode('utf-8') + '"'
        return ele

    def unicode_to_ascii(self, ul):
        if isinstance(ul, list):
            res = map(self._format, ul)
            return res


class AssetsImgHandler:
    def __init__(self, assets_id, assets_imgs=''):
        self.id = assets_id
        self.imgs = assets_imgs
        self.incubator = Base64ImageField()
        self.imgModel = AssetsImg
        self.imgsId = []

    def execute(self, option):
        if option == 'update':
            assetsImgs = self.imgModel.objects.filter(assets_id=self.id)
            self.imgsId = [int(img.id) for img in assetsImgs]

        if option != 'destroy':
            for size, imgs in self.imgs.items():
                for img in imgs:
                    if option == 'update':
                        try:
                            self.imgsId.remove(img['id'])
                        except Exception,e:
                            pass
                    if img['src'] and 'base64,' in img['src']:
                        rawImg = self.incubator.to_internal_value(img['src'])
                        if img.get('id'):
                            self.update(img['id'], rawImg)
                        else:
                            self.create(rawImg, size)
            if len(self.imgsId):
                for imgId in self.imgsId:
                    self.destroy(imgId)

        else:
            self.destroy(imgId=False)

    def create(self, rawImg, sizeImg):
        assetsImg = self.imgModel(assets_img=rawImg, assets_id=self.id, img_type=sizeImg)
        assetsImg.save()

    def update(self, imgId, rawImg):
        assetsImg = self.imgModel.objects.get(id=imgId)
        if self._cleanFromDisk(assetsImg.assets_img):
            assetsImg.assets_img = rawImg
            assetsImg.save()

    def destroy(self, imgId=False):
        if imgId != False:
            img = self.imgModel.objects.get(id=imgId)
            if self._cleanFromDisk(img.assets_img):
                img.delete()
            return

        AssetsImgs = self.imgModel.objects.filter(assets_id=self.id)
        for img in AssetsImgs:
            if self._cleanFromDisk(img.assets_img):
                img.delete()

    def _cleanFromDisk(self, imgFieldFile):
        img_path = imgFieldFile.path
        storage = imgFieldFile.storage
        storage.delete(img_path)
        return True


class QSHandler(Ssql):
    def __init__(self, t, user_id='', region_id='', keys=''):
        self.requestType = t
        self.user_id = user_id
        self.region_id = region_id
        self.isuper = False
        self.keys = keys
        self.queryset = getattr(self, t)

    def _isSuperUser(self):
        user = User.objects.get(id=self.user_id)
        self.isuper = user.is_superuser

    @property
    def backend(self):
        self._isSuperUser()
        if not self.isuper:
            return Assets.objects.filter(region_id=self.region_id)
        return Assets.objects.all()

    @property
    def frontend(self):
        if self.keys:
            super(QSHandler, self).__init__(self.keys)
            return Assets.objects.raw(self.sql.encode('utf-8'))
        return Assets.objects.all()
















