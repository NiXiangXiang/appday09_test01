import allure,pytest

class TestReport:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step("这是一个测试方法描述")
    def test_001(self):
        print("s")
        allure.attach("txt文件标题","txt文件的写入具体描述内容") # 添加描述信息
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("这是一个测试方法描述步骤")
    def test_002(self):
        print("s")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step("这是一个测试方法描述步骤3")
    def test_003(self):
        print("s")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step("这是一个测试方法描述步骤4")
    def test_004(self):
        print("s")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step("这是一个测试方法描述步骤5")
    def test_005(self):
        print("s")
        assert True