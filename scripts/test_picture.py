import allure,os

class TestAddPicture:
    def test_add_picture(self):
        with open(os.getcwd()+os.sep+"微信图片_20190520105434.png","rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)